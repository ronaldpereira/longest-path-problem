import argparse

def parser():
    parser = argparse.ArgumentParser(description='Longest Path Problem heuristic solution using Ant Colony Optimization (ACO).')

    # Required arguments
    parser.add_argument('input', type=str, help='Input file path')

    # Optional arguments
    parser.add_argument('-a', '--ants', type=int, default=20, help='Number of ants in each iteration (default: 20)')
    parser.add_argument('-e', '--evaporation_rate', type=float, default=0.05, help='Evaporation rate in each iteration (default: 0.05)')
    parser.add_argument('-i', '--iterations', type=int, default=100, help='Number of iterations to be executed (default: 100)')

    args = parser.parse_args()

    return args
