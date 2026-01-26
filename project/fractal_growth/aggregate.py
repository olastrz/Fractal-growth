'''class Aggregate:
    def __init__(self, seed_position):
        """
        - self.particles: set of (x, y) tuples
        - self.perimeter: set of neighboring empty sites
        - self.radius: current max distance from seed
        """
    
    def add_particle(self, position):
        """
        - Add position to particles set
        - Update perimeter (add new neighbors, remove filled site)
        - Update radius
        """
    
    def is_occupied(self, position):
        """Check if position is in aggregate"""
    
    def get_neighbors(self, position):
        """Return 4 or 8 neighbors (lattice sites)"""
    
    def update_perimeter(self, position):
        """
        - Remove position from perimeter
        - Add unoccupied neighbors to perimeter
        """
    
    def get_radius(self):
        """Return max distance from seed to any particle"""
    
    def get_center_of_mass(self):
        """For fractal dimension calculation"""
'''