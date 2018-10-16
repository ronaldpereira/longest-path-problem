import sys
import libs.graph as graphLib

try:
    inputPath = sys.argv[1]
except:
    raise Exception('Not all required arguments were given. Execute \'make help\' for more detailed instructions.')

graph = graphLib.Graph(inputPath)
print(graph.graph)
