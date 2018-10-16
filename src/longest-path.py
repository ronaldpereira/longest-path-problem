import sys

try:
    input_path = sys.argv[1]
except:
    raise Exception('Not all required arguments were given. Execute \'make help\' for more detailed instructions.')

graph = {}
with open(input_path, 'r') as inputFile:
    for line in inputFile:
        originVertice, targetVertice, edgeWeight = list(map(lambda x: int(x), line.split()))

        try:
            graph[originVertice].append((targetVertice, edgeWeight))
        except KeyError:
            graph[originVertice] = [(targetVertice, edgeWeight)]

    print(graph)
