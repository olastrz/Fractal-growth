'''
# Simulation parameters
GRID_SIZE = 500
NUM_PARTICLES = 3000
SEED_POSITION = (250, 250)  # Center

# Walker parameters
RELEASE_RADIUS_OFFSET = 5  # Spawn walkers this far from aggregate
KILL_RADIUS_OFFSET = 50     # Respawn if walker goes too far
STICKING_PROBABILITY = 1.0  # Probability to stick on contact

# Visualization
PLOT_INTERVAL = 100  # Update plot every N particles
SAVE_IMAGES = True
OUTPUT_DIR = "results"
'''