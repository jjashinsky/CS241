import random
import arcade
from globals import *
from flyingObject import FlyingObject
from abc import abstractmethod
from abc import ABC

class Target(FlyingObject, ABC):
    
    """
    This is the target base class.
    Inherited most attibutes and methods from FlyingObject
    """
    
    def __init__(self):
        super().__init__()
        self.center.x = random.uniform(0,100) # slight random start from top of screen
        self.center.y = random.uniform(SCREEN_HEIGHT -100, SCREEN_HEIGHT - 11) # slight random start from top left side of screen
        self.alive = True # start out being alive
        self.radius = TARGET_RADIUS
        self.color = TARGET_COLOR
        
    @abstractmethod
    def hit(self):
        pass
        
class regularTarget(Target):
    
    # only needs to inherit and redefine self.hit()
    
    def __init__(self):
        super().__init__()
        
    def hit(self):
        self.alive = False
        return 1 # gives a point for hitting
    
class strongTarget(regularTarget):
    
    def __init__(self):
        super().__init__()
        self.health = random.randint(3,5) # random health 3-5
        self.velocity.dx = random.uniform(1.5,2) # slower speed
        self.velocity.dy = random.uniform(.2,.3) * -1 # more likely to stay at top of screen
        # random color
        self.color = (random.randint(0,225), random.randint(0,225), random.randint(0,225))
        self.hit_count = 0 # used for hit function
        
    def draw(self):
        # not filled in circle with health displayed in middle
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, self.color)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.health), text_x, text_y, self.color, font_size=20)
        
    def hit(self):
        self.health -= 1
        if self.hit_count < self.health:
            return 1 # one point for each hit
        else:
            self.alive = False
            return 5 # bonus for finishing off the target

class safeTarget(regularTarget):
    
    def __init__(self):
        super().__init__()
        self.color = TARGET_SAFE_COLOR # new color
        
    def draw(self):
        # changing to a square
        arcade.draw_rectangle_filled(self.center.x, self.center.y, TARGET_SAFE_WIDTH, TARGET_SAFE_WIDTH, self.color)
    
    def hit(self):
        self.alive = False
        return -10 # very bad 