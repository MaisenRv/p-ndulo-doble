from .pendulum import Pendulum 

class Plot: 
    def __init__(self,buffer, bufferW) -> None:
        self.buffer = buffer
        self.bufferW = bufferW
        self.start = 0
        
    
    def draw(self, data:list[Pendulum]):
        color1 = data[0].color
        color2 = data[1].color

        angle1 = self.format_angle(data[0].position.angle)
        angle2 = self.format_angle(data[1].position.angle)
      
        self.buffer.stroke(color1[0],color1[1],color1[2])
        self.buffer.circle(self.start,angle1,1)
        self.buffer.stroke(color2[0],color2[1],color2[2])
        self.buffer.circle(self.start,angle2,1)
    
        self.start+=0.2
        if(self.start > self.bufferW):
            self.start = 0 
            self.buffer.clear()
    
    def format_angle(self,angle):
        return angle * 27 + 100