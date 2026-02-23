GRID_SIZE = 500
NUM_PARTICLES = 1000
SEED_POSITION = (250, 250)  # Center of grid

RELEASE_RADIUS_OFFSET = 5   # Spawn walkers this far from aggregate edge
KILL_RADIUS_OFFSET = 50      # Respawn if walker goes this far beyond aggregate

STICKING_PROBABILITY = 1.0   # Probability to stick on contact (1.0 = always stick)

PLOT_EVERY_N_PARTICLES = 1   # Update plot every N particles (1 = smooth, every particle)
PRINT_EVERY_N_PARTICLES = 50 # Print progress every N particles
SAVE_IMAGE_EVERY_N = 200     # Save image every N particles
SAVE_IMAGES = True
OUTPUT_DIR = "results"

# Random seed (for reproducibility)
RANDOM_SEED = None           # Set to integer for reproducible results, None for random