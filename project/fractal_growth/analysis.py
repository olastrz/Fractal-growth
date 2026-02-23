import numpy as np
from scipy.stats import linregress

def calculate_fractal_dimension(aggregate, num_points=20):
    """
    Calculate fractal dimension using sandbox method
    
    Args:
        aggregate: Aggregate object to analyze
        num_points: Number of radii to sample
    
    Returns:
        float: Fractal dimension D_f
    """
    max_radius = aggregate.get_radius()
    
    # Create logarithmically spaced radii
    radii = np.logspace(np.log10(2), np.log10(max_radius), num_points)
    masses = []
    
    # Count particles within each radius
    for r in radii:
        mass = 0
        for particle in aggregate.particles:
            distance = np.sqrt((particle[0] - aggregate.seed[0])**2 + 
                             (particle[1] - aggregate.seed[1])**2)
            if distance <= r:
                mass += 1
        masses.append(mass)
    
    # Filter out zeros and take log
    valid_indices = [i for i, m in enumerate(masses) if m > 0]
    log_radii = np.log10([radii[i] for i in valid_indices])
    log_masses = np.log10([masses[i] for i in valid_indices])
    
    # Linear fit in log-log space: log(M) = D_f * log(r) + const
    slope, intercept, r_value, p_value, std_err = linregress(log_radii, log_masses)
    
    return slope

def print_fractal_dimension(aggregate):
    """
    Calculate and print fractal dimension
    
    Args:
        aggregate: Aggregate to analyze
    """
    D_f = calculate_fractal_dimension(aggregate)
    
    print("\n" + "="*60)
    print(f"Fractal Dimension: {D_f:.3f}")
    print(f"Expected for 2D DLA: ~1.71")
    print("="*60 + "\n")
    
    return D_f