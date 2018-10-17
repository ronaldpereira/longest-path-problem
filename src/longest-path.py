import sys

import libs.ant as ANT
import libs.antColonyOptimization as ACO
import libs.argParserConfig as APC
import libs.graph as GRAPH
import libs.pheromoneUpdate as PU

args = APC.parser()

g = GRAPH.Graph(args.input)

# print(g.graph)
# print(g.graph[g.minVertice])
# print(g.graph[g.maxVertice])

aco = ACO.AntColonyOptimization(g)
pheromoneUpdate = PU.PheromoneUpdate(args.evaporation_rate, args.k_ants)

# print('n_ants:', len(ants))
# print('n_vertices:', g.nVertices)
# print('n_edges:', g.nEdges)

bestSolution = ANT.BestSolution()

for iteration in range(args.iterations):
    ants = ANT.ant_colony_creator(args.ants, g.minVertice)
    for antIndex in range(len(ants)):
        aco.build_solution(ants[antIndex], g.minVertice, g.maxVertice)
        # print(ants[antIndex].path)
        # print(ants[antIndex].pathWeight)
        # print(ants[antIndex].validPath)
        pheromoneUpdate.update(g.graph, ants)

    bestSolution.set_best_solution(ants)

print(bestSolution.path)
print(bestSolution.pathWeight)
