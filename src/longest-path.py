import sys
import libs.graph as graph
import libs.argParserConfig as APC

args = APC.parser()

g = graph.Graph(args.input)
print(g.graph)
# print(g.graph[g.minVertice])
# print(g.graph[g.maxVertice])
