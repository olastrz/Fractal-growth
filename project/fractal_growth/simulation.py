import random
import math
from aggregate import Aggregate
from walker import Walker
import config

class Simulation:
    def __init__(self):
        """Initialize DLA simulation"""
        if config.RANDOM_SEED is not None:
            random.seed(config.RANDOM_SEED)
        
        self.aggregate = Aggregate(config.SEED_POSITION)
        self.seed = config.SEED_POSITION
        self.particle_count = 1
        self.step_counts = []
    
    def spawn_walker(self):
        """Spawn walker on circle around aggregate"""
        radius = self.aggregate.get_radius() + config.RELEASE_RADIUS_OFFSET
        angle = random.uniform(0, 2 * math.pi)
        x = self.seed[0] + int(radius * math.cos(angle))
        y = self.seed[1] + int(radius * math.sin(angle))
        return Walker((x, y))
    
    def run(self, visualizer=None, logger=None):
        """Main DLA growth loop"""
        print(f"Starting DLA simulation...")
        print(f"Target: {config.NUM_PARTICLES} particles")
        print(f"Seed at: {self.seed}\n")
        
        while self.particle_count < config.NUM_PARTICLES:
            walker = self.spawn_walker()
            steps = 0
            
            while True:
                walker.step()
                steps += 1
                pos = walker.get_position()
                
                distance_from_seed = walker.distance_from(self.seed)
                kill_radius = self.aggregate.get_radius() + config.KILL_RADIUS_OFFSET
                
                if distance_from_seed > kill_radius:
                    walker = self.spawn_walker()
                    steps = 0
                    continue
                
                if self.aggregate.is_attachment_site(pos):
                    if random.random() < config.STICKING_PROBABILITY:
                        self.aggregate.add_particle(pos)
                        self.particle_count += 1
                        self.step_counts.append(steps)
                        break
            
            if self.particle_count % config.PRINT_EVERY_N_PARTICLES == 0:
                avg_steps = sum(self.step_counts[-config.PRINT_EVERY_N_PARTICLES:]) / config.PRINT_EVERY_N_PARTICLES
                radius = self.aggregate.get_radius()
                print(f"Particles: {self.particle_count}/{config.NUM_PARTICLES} | "
                      f"Radius: {radius:.1f} | "
                      f"Avg steps: {avg_steps:.0f}")
                
                if visualizer:
                    visualizer.plot_aggregate(self.aggregate, self.particle_count)
            
            if logger and self.particle_count % config.LOG_EVERY_N_PARTICLES == 0:
                logger.log_fractal_dimension(self.particle_count, self.aggregate)
        
        print(f"\n✓ Simulation complete!")
        print(f"Final particle count: {self.particle_count}")
        print(f"Final radius: {self.aggregate.get_radius():.2f}")
        
        return self.aggregate