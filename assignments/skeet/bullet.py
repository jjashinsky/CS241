import arcade
import math
from point import Point
from globals import *
from flyingObject import FlyingObject

"""
This is the bullet class, to be fired from the rifle.
Inherited most attibutes and methods from FlyingObject
"""
class Bullet(FlyingObject):
    
    def __init__(self, angle):
        super().__init__()
        self.angle = angle # receives angle (to be used for speed)

    def advance(self):
        # using angle to proper change in x and y for desired speed
        self.center.x += math.cos(math.radians(self.angle)) * BULLET_SPEED
        self.center.y += math.sin(math.radians(self.angle)) * BULLET_SPEED
        