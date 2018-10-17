import sys
import libs.graph as graph

try:
    inputPath = sys.argv[1]
except:
    raise Exception('Not all required arguments were given. Execute \'make help\' for more detailed instructions.')

g = graph.Graph(inputPath)
print(g.graph[g.minVertice])
print(g.graph[g.maxVertice])
