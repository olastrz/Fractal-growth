import random
import config 

class Aggregate:
    """Represents an aggregate of particles in a fractal growth simulation."""
    
    def __init__(self, seed_position):
        self.seed = seed_position
        self.particles = {seed_position}
        self.attachment_sites = set()
        self._initialize_attachment_sites()
    
    def _get_neighbors(self, position):
        """Return 8 neighbors"""
        x, y = position
        
        neighbors = [
            (x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)
        ]
        if config.USE_DIAGONALS:
            neighbors.extend([
                (x+1, y+1), (x+1, y-1), 
                (x-1, y+1), (x-1, y-1)
            ])
        
        random.shuffle(neighbors)
        return neighbors
    
    def _initialize_attachment_sites(self):
        """Add neighbors of seed to attachment sites"""
        for neighbor in self._get_neighbors(self.seed):
            if neighbor not in self.particles:
                self.attachment_sites.add(neighbor)
    
    def add_particle(self, position):
        """Add particle and update attachment sites"""
        self.particles.add(position)
        self.attachment_sites.discard(position)
        
        for neighbor in self._get_neighbors(position):
            if neighbor not in self.particles:
                self.attachment_sites.add(neighbor)
    
    def is_attachment_site(self, position):
        """Check if position is available for attachment"""
        return position in self.attachment_sites
    
    def get_radius(self):
        """Max distance from seed"""
        if not self.particles:
            return 0
        distances = [((x - self.seed[0])**2 + (y - self.seed[1])**2)**0.5 
                     for x, y in self.particles]
        return max(distances)