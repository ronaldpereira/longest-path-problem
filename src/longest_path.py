import libs.ant as ANT
import libs.ant_colony_optimization as ACO
import libs.arg_parse_config as APC
import libs.graph as GRAPH
import libs.pheromone_update as PU

args = APC.parser()

g = GRAPH.Graph(args.input)

aco = ACO.AntColonyOptimization(g)
pheromoneUpdate = PU.PheromoneUpdate(args.evaporation_rate, args.k_ants)

bestSolution = ANT.BestSolution()

for iteration in range(args.iterations):
    ants = ANT.ant_colony_creator(args.ants, g.minVertice)
    for antIndex in range(len(ants)):
        aco.build_solution(ants[antIndex], g.minVertice, g.maxVertice)
        
    pheromoneUpdate.update(g.graph, ants)
    bestSolution.set_best_solution(ants)
    print(iteration, bestSolution.pathWeight)

print(bestSolution.path)
print(bestSolution.pathWeight)
