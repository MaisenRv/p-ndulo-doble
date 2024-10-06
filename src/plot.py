from .pendulum import Pendulum 
from numpy import pi

class Plot: 
    def __init__(self,buffer, bufferW) -> None:
        self.buffer = buffer
        self.bufferW = bufferW
        self.start = 0
        self.buffer.stroke_weight(2)
        self.beforePos = None
        self.beforePos2 = None
    
    def draw(self, data:list[Pendulum]):
        color1 = data[0].color
        color2 = data[1].color

        posY1 = self.format_angle(data[0].position.angle)
        posY2 = self.format_angle(data[1].position.angle)
        if self.beforePos != None:
            if not ((data[0].position.angle < 0 and self.beAngle1 > 0) or (data[0].position.angle > 0 and self.beAngle1 < 0)) : 
                self.buffer.stroke(color1[0],color1[1],color1[2],100)
                # self.buffer.circle(self.start,posY1,2)
                self.buffer.line(self.beforePos, [self.start,posY1])

        if self.beforePos2 != None:
            if not ((data[1].position.angle < 0 and self.beAngle2 > 0) or (data[1].position.angle > 0 and self.beAngle2 < 0) ): 
                self.buffer.stroke(color2[0],color2[1],color2[2],100)
                # self.buffer.circle(self.start,posY2,2)
                self.buffer.line(self.beforePos2,[self.start,posY2])


        self.beforePos = [self.start, posY1]
        self.beforePos2 = [self.start, posY2]

        self.beAngle1 = data[0].position.angle
        self.beAngle2 = data[1].position.angle

        self.start+=0.5
        if(self.start > self.bufferW):
            self.start = 0 
            self.buffer.clear()
            self.beforePos = None
            self.beforePos2 = None
    
    def format_angle(self,angle):
        return angle * 30 + 100