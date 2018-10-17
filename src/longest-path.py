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

ants = ANT.ant_colony_creator(args.ants)

aco = ACO.AntColonyOptimization(args.evaporation_rate, g)

print(len(ants))
print(g.nVertices)
print(g.nEdges)

for iteration in range(args.iterations):
    for antIndex in range(len(ants)):
        pass
