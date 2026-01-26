'''
import numpy as np
from scipy.stats import linregress

def calculate_fractal_dimension(aggregate, method='sandbox'):
    """
    Sandbox method:
    - For increasing radii r from center
    - Count mass M(r) = number of particles within radius r
    - Plot log(M) vs log(r)
    - Fractal dimension D_f = slope of linear fit
    
    Algorithm:
    radii = [10, 20, 30, ..., max_radius]
    masses = []
    for r in radii:
        mass = count particles with distance < r from center
        masses.append(mass)
    
    # Linear fit in log-log space
    slope, intercept = linregress(log(radii), log(masses))
    D_f = slope
    """
    
def plot_fractal_analysis(aggregate):
    """
    Create log-log plot of M(r) vs r
    Show fitted line and calculated dimension
    """
'''