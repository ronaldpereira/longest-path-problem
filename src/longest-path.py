import sys
import libs.graph as GRAPH
import libs.argParserConfig as APC
import libs.ant as ANT
import libs.antColonyOptimization as ACO

args = APC.parser()

g = GRAPH.Graph(args.input)
# print(g.graph)
# print(g.graph[g.minVertice])
# print(g.graph[g.maxVertice])

ants = ANT.ant_colony_creator(args.ants, g.minVertice)

aco = ACO.AntColonyOptimization(args.evaporation_rate, g)

print('n_ants:', len(ants))
print('n_vertices:', g.nVertices)
print('n_edges:', g.nEdges)

aco.build_solution(ants[0], g.minVertice, g.maxVertice)
# for iteration in range(args.iterations):
    # for antIndex in range(len(ants)):
    #     aco.build_solution(ants[antIndex], g.minVertice, g.maxVertice)
