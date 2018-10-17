class Graph:
    def __init__(self, inputPath, pheromoneInitialValue=1):
        self.graph = {}
        self.nVertices = 0
        self.nEdges = 0

        with open(inputPath, 'r') as inputFile:
            for line in inputFile:
                originVertice, targetVertice, edgeWeight = list(map(lambda x: int(x), line.split()))

                dictData = {'origin': originVertice,
                            'target': targetVertice,
                            'weight': edgeWeight,
                            'pheromone': pheromoneInitialValue}

                try:
                    self.graph[originVertice].append(dictData)

                # If the origin vertice is not in the graph
                except KeyError:
                    self.graph[originVertice] = [dictData]

                self.nEdges += 1

        if len(self.graph) > 0:
            self.nVertices = len(self.graph.keys())
            self.minVertice = min(self.graph.keys())
            self.maxVertice = max(self.graph.keys())

    def get_edge_weight(self, originVertice, targetVertice):
        if originVertice in self.graph.keys():
            for edge in self.graph[originVertice]:
                if edge['target'] == targetVertice:
                    return edge['weight']
        
        return 0

