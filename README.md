# Longest Path Problem

Longest Path Problem heuristic solution using Ant Colony Optimization (ACO).

## How to 'Help Menu'

```sh
python3 longest-path.py -h
```

## Usage

```text
usage: longest-path.py [-h] [-a ANTS] [-e EVAPORATION_RATE] [-i ITERATIONS]
                       [-k K_ANTS]
                       input

Longest Path Problem heuristic solution using Ant Colony Optimization (ACO).

positional arguments:
  input                 Input file path

optional arguments:
  -h, --help            show this help message and exit
  -a ANTS, --ants ANTS  Number of ants in each iteration (default: 50)
  -e EVAPORATION_RATE, --evaporation_rate EVAPORATION_RATE
                        Evaporation rate in each iteration between 0 and 1
                        (default: 0.1)
  -i ITERATIONS, --iterations ITERATIONS
                        Number of iterations to be executed (default: 50)
  -k K_ANTS, --k_ants K_ANTS
                        Number of k best ants that will deposite pheromone on
                        path. If k=0, then all ants will deposit pheromone
                        (default: 1)
```
