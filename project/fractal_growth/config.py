GRID_SIZE = 500
NUM_PARTICLES = 2000
SEED_POSITION = (250, 250)  # Center of grid

RELEASE_RADIUS_OFFSET = 5   # Spawn walkers this far from aggregate edge
KILL_RADIUS_OFFSET = 50      # Respawn if walker goes this far beyond aggregate

STICKING_PROBABILITY = 1.0   # Probability to stick on contact (1.0 = always stick)
USE_DIAGONALS = False         # Allow sticking on diagonal neighbors (8-connectivity) if True, otherwise only orthogonal (4-connectivity)

ENABLE_VISUALIZATION = False # Set to True to see visualization
PLOT_EVERY_N_PARTICLES = 1   # Update plot every N particles (1 = smooth, every particle)
PRINT_EVERY_N_PARTICLES = 50 # Print progress every N particles
SAVE_IMAGE_EVERY_N = 200     # Save image every N particles
SAVE_IMAGES = True
OUTPUT_DIR = "results"

RANDOM_SEED = None           # Set to integer for reproducible results, None for random

ENABLE_CSV_LOGGING = True
LOG_EVERY_N_PARTICLES = 100
