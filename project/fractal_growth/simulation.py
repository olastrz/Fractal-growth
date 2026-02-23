import random
import math
from aggregate import Aggregate
from walker import Walker
import config

class Simulation:
    def __init__(self):
        """Initialize DLA simulation"""
        # Set random seed if specified
        if config.RANDOM_SEED is not None:
            random.seed(config.RANDOM_SEED)
        
        # Create aggregate with seed particle
        self.aggregate = Aggregate(config.SEED_POSITION)
        self.seed = config.SEED_POSITION
        
        # Statistics
        self.particle_count = 1  # Start with seed
        self.step_counts = []    # Track how many steps each walker took
    
    def spawn_walker(self):
        """
        Spawn walker on circle around aggregate
        
        Returns:
            Walker: New walker at release radius
        """
        # Calculate spawn radius
        radius = self.aggregate.get_radius() + config.RELEASE_RADIUS_OFFSET
        
        # Random angle
        angle = random.uniform(0, 2 * math.pi)
        
        # Convert polar to cartesian coordinates
        x = self.seed[0] + int(radius * math.cos(angle))
        y = self.seed[1] + int(radius * math.sin(angle))
        
        return Walker((x, y))
    
    def run(self, visualizer=None):
    
        # Grow until we reach target number of particles
        while self.particle_count < config.NUM_PARTICLES:
            # Spawn new walker
            walker = self.spawn_walker()
            steps = 0
            
            # Random walk until attachment
            while True:
                walker.step()
                steps += 1
                pos = walker.get_position()
                
                # Check if walker went too far (kill radius)
                distance_from_seed = walker.distance_from(self.seed)
                kill_radius = self.aggregate.get_radius() + config.KILL_RADIUS_OFFSET
                
                if distance_from_seed > kill_radius:
                    # Walker escaped - respawn
                    walker = self.spawn_walker()
                    steps = 0
                    continue
                
                # Check if walker hit an attachment site
                if self.aggregate.is_attachment_site(pos):
                    # Sticking probability
                    if random.random() < config.STICKING_PROBABILITY:
                        # Attach particle
                        self.aggregate.add_particle(pos)
                        self.particle_count += 1
                        self.step_counts.append(steps)
                        break
            
            # Update visualization (every N particles for smooth growth)
            if visualizer and self.particle_count % config.PLOT_EVERY_N_PARTICLES == 0:
                visualizer.plot_aggregate(self.aggregate, self.particle_count)
            
            # Console progress reporting (less frequent to avoid spam)
            if self.particle_count % config.PRINT_EVERY_N_PARTICLES == 0:
                avg_steps = sum(self.step_counts[-config.PRINT_EVERY_N_PARTICLES:]) / config.PRINT_EVERY_N_PARTICLES
                radius = self.aggregate.get_radius()
                
        return self.aggregate