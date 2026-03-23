import csv
import os
from datetime import datetime
import config

class SimulationLogger:
    def __init__(self):
        """Initialize CSV logger"""
        # Create results directory
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filename = os.path.join(config.OUTPUT_DIR, f"fractal_dimension_log_{timestamp}.csv")
        
        # Create CSV file and write header
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Particle_Count', 'Fractal_Dimension'])
        
        print(f"✓ Logging fractal dimensions to: {self.filename}\n")
    
    def log_fractal_dimension(self, particle_count, aggregate):
        """
        Calculate and log fractal dimension
        
        Args:
            particle_count: Current number of particles
            aggregate: Current aggregate state
        """
        from analysis import calculate_fractal_dimension
        
        D_f = calculate_fractal_dimension(aggregate)
        
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([particle_count, f"{D_f:.4f}"])
        
        print(f"  → Logged D_f = {D_f:.4f} at {particle_count} particles")