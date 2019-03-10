import random

class Velocity:
    
    def __init__(self):
        # randomly selects a speed for the ball
        self.dx = random.uniform(6,8)
        self.dy = random.uniform(6,8) * random.choice([-1,1])
        # randomly choicing -1 or 1 so that dy will wither up or down     