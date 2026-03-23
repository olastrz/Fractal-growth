from simulation import Simulation
from visualization import Visualizer
from analysis import print_fractal_dimension
import config

def main():
    print("="*60)
    print("DLA FRACTAL GROWTH SIMULATION")
    print("="*60)
    print(f"Grid size: {config.GRID_SIZE}x{config.GRID_SIZE}")
    print(f"Target particles: {config.NUM_PARTICLES}")
    print(f"Seed position: {config.SEED_POSITION}")
    print(f"Directions: {'8 (with diagonals)' if config.USE_DIAGONALS else '4 (cardinal only)'}")
    print(f"Release offset: {config.RELEASE_RADIUS_OFFSET}")
    print(f"Kill offset: {config.KILL_RADIUS_OFFSET}")
    print(f"Visualization: {'ENABLED' if config.ENABLE_VISUALIZATION else 'DISABLED (fast mode)'}")
    print("="*60 + "\n")
    
    viz = None
    if config.ENABLE_VISUALIZATION:
        viz = Visualizer()
        print("Live visualization enabled - this will be slower\n")
    else:
        print("Running in fast mode (no live visualization)\n")

    if config.ENABLE_CSV_LOGGING:
        from logger import SimulationLogger
        logger = SimulationLogger()


    sim = Simulation()
    aggregate = sim.run(visualizer=viz, logger = logger)
    
    if viz:
        viz.close()
    
    print_fractal_dimension(aggregate)
    
    print("\n✓ Simulation complete!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

