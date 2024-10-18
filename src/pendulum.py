from p5 import Vector, circle, line, stroke,radians, no_stroke, fill
import numpy as np
class Pendulum:
    def __init__(self, v_angle,mass: float , l:float, angle:float, buffer, center, color,pendulum:'Pendulum' = None) -> None:
        self.mass = mass
        self.color = color
        self.buffer = buffer
        self.long = l
        self.angle = angle
        self.a_angle = 0
        self.v_angle = v_angle
        self.center = center
        self.pendulum = pendulum 
        self.position = Vector(np.cos(angle)*self.long, np.sin(angle)*(-self.long)) 
        self.drawPos = self.position + self.center
        self.posBefore = None
    
    def draw(self):
        # self.v_angle += self.a_angle
        self.position.rotate(radians(self.v_angle))
        self.drawPos = self.position + self.center
        line(self.center, self.drawPos)


    def drawMass(self):
        no_stroke()
        fill(self.color[0],self.color[1],self.color[2])
        circle(self.drawPos.x,self.drawPos.y,self.mass)
        if self.pendulum != None:
            if self.posBefore != None:
                self.buffer.line(self.posBefore,self.drawPos)
            self.posBefore = self.drawPos
        stroke(0)
  
