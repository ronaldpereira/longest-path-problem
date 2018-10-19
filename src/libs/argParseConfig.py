import argparse


def parser():
    parser = argparse.ArgumentParser(description='Longest Path Problem heuristic solution using Ant Colony Optimization (ACO).')

    # Required arguments
    parser.add_argument('input', type=str, help='Input file path')

    # Optional arguments
    parser.add_argument('-a', '--ants', type=int, default=500, help='Number of ants in each iteration (default: 500)')
    parser.add_argument('-e', '--evaporation_rate', type=float, default=0.1, help='Evaporation rate in each iteration between 0 and 1 (default: 0.1)')
    parser.add_argument('-i', '--iterations', type=int, default=100, help='Number of iterations to be executed (default: 100)')
    parser.add_argument('-k', '--k_ants', type=int, default=1, help='Number of k best ants that will deposite pheromone on path. If k=0, then all ants will deposit pheromone (default: 1)')

    args = parser.parse_args()

    return args
