import random

class Velocity:
    
    def __init__(self):
        # randomly selects a speed for the flying object. 
        self.dx = random.uniform(3,5)
        self.dy = random.uniform(.2,3) * -1     