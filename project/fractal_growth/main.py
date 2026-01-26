'''
from simulation import Simulation
from visualization import Visualizer
from analysis import calculate_fractal_dimension, plot_fractal_analysis
import config

def main():
    # Create simulation
    sim = Simulation()
    viz = Visualizer()
    
    # Run DLA growth
    print("Starting DLA simulation...")
    sim.run(visualizer=viz)
    
    # Final visualization
    viz.save_final(sim.aggregate, f"{config.OUTPUT_DIR}/final_aggregate.png")
    
    # Fractal analysis
    D_f = calculate_fractal_dimension(sim.aggregate)
    print(f"Fractal dimension: {D_f:.3f}")
    
    plot_fractal_analysis(sim.aggregate)
    plt.show()

if __name__ == "__main__":
    main()
'''