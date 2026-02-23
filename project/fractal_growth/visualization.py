import matplotlib.pyplot as plt
import numpy as np
import os
import config

class Visualizer:
    def __init__(self):
        if config.SAVE_IMAGES:
            os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(10, 10))

    def plot_aggregate(self, aggregate, step):
        self.ax.clear()
        
        if len(aggregate.particles) > 0:
            x_coords = [p[0] for p in aggregate.particles]
            y_coords = [p[1] for p in aggregate.particles]
            
            distances = [
                np.sqrt((x - aggregate.seed[0])**2 + (y - aggregate.seed[1])**2)
                for x, y in aggregate.particles
            ]
            
            scatter = self.ax.scatter(
                x_coords, y_coords, 
                c=distances, 
                cmap='viridis',
                s=10,
                marker='s',
                edgecolors='none'
            )
            
        self.ax.set_aspect('equal')
        self.ax.set_title(
            f'DLA Fractal Growth - {step} particles | Radius: {aggregate.get_radius():.1f}',
            color='black',
            fontsize=14,
            pad=20
        )
        self.ax.set_xlabel('X', color='black')
        self.ax.set_ylabel('Y', color='black')
        self.ax.tick_params(colors='black')
        
        self.ax.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
        
        # Set limits based on aggregate size
        margin = 20
        radius = aggregate.get_radius()
        center_x, center_y = aggregate.seed
        self.ax.set_xlim(center_x - radius - margin, center_x + radius + margin)
        self.ax.set_ylim(center_y - radius - margin, center_y + radius + margin)
        plt.pause(0.001)
        

    def plot_aggregate_3d_view(self, aggregate, step):
        """Plot 2D aggregate as 3D surface (height = distance)"""
        from mpl_toolkits.mplot3d import Axes3D
        
        if not hasattr(self, 'fig_3d'):
            self.fig_3d = plt.figure(figsize=(12, 10))
            self.ax_3d = self.fig_3d.add_subplot(111, projection='3d')
            self.angle_3d = 0
        
        self.ax_3d.clear()
        
        if len(aggregate.particles) > 0:
            x_coords = [p[0] for p in aggregate.particles]
            y_coords = [p[1] for p in aggregate.particles]
            
            # Height = distance from seed
            z_coords = [
                np.sqrt((x - aggregate.seed[0])**2 + (y - aggregate.seed[1])**2)
                for x, y in aggregate.particles
            ]
            
            scatter = self.ax_3d.scatter(
                x_coords, y_coords, z_coords,
                c=z_coords,
                cmap='plasma',
                s=20,
                marker='o',
                alpha=0.8
            )
        
        self.ax_3d.set_xlabel('X')
        self.ax_3d.set_ylabel('Y')
        self.ax_3d.set_zlabel('Distance')
        self.ax_3d.set_title(f'2.5D View - {step} particles')
        
        # Rotate
        self.angle_3d = (self.angle_3d + 1) % 360
        self.ax_3d.view_init(elev=30, azim=self.angle_3d)