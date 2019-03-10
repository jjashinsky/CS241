import arcade
import random
from point import Point

class Paddle:
    
    def __init__(self):
        self.center = Point()
        self.center.x = 395 # locked at x = 390
        
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, 10, 50, (0, random.randint(0,225), random.randint(0,225))) 
        # constant changing the color
    def move_up(self):
        # this will stop the paddle when it hits ceiling
        if self.center.y < 275: #275 so that it stops at the edge of the paddle - not the center
            self.center.y  += 5 # speed is 5
        
    def move_down(self):
        # this will stop the paddle when it hits the floor
        if self.center.y > 25: # 25 so that it stops at the edge of the paddle - not the center
            self.center.y -= 5 # speed is 5