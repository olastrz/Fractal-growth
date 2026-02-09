import random

class Walker:
    def __init__(self, position):
        self.x, self.y = position
    
    def step(self):
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]
        
        dx, dy = random.choice(directions)
        self.x += dx
        self.y += dy
    
    def get_position(self):
        return (self.x, self.y)
    
    def distance_from(self, position):
        dx = self.x - position[0]
        dy = self.y - position[1]
        return (dx**2 + dy**2)**0.5