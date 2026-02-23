from simulation import Simulation
from visualization import Visualizer
from analysis import print_fractal_dimension

def main():
    viz = Visualizer()

    sim = Simulation()
    aggregate = sim.run(visualizer=viz)
    
    print_fractal_dimension(aggregate)

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()