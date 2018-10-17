class Graph:
    def __init__(self, inputPath):
        self.graph = {}

        with open(inputPath, 'r') as inputFile:
            for line in inputFile:
                originVertice, targetVertice, edgeWeight = list(map(lambda x: int(x), line.split()))

                try:
                    self.graph[originVertice].append((targetVertice, edgeWeight))
                except KeyError:
                    self.graph[originVertice] = [(targetVertice, edgeWeight)]

        if len(self.graph) > 0:
            self.minVertice = min(self.graph.keys())
            self.maxVertice = max(self.graph.keys())
