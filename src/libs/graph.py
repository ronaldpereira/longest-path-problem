class Graph:
    def __init__(self, inputPath, pheromoneInitialValue=1):
        self.graph = {}

        with open(inputPath, 'r') as inputFile:
            for line in inputFile:
                originVertice, targetVertice, edgeWeight = list(map(lambda x: int(x), line.split()))

                dictData = {'origin': originVertice,
                            'target': targetVertice,
                            'weight': edgeWeight,
                            'pheromone': pheromoneInitialValue}

                try:
                    self.graph[originVertice].append(dictData)
                except KeyError:
                    self.graph[originVertice] = [dictData]

        if len(self.graph) > 0:
            self.minVertice = min(self.graph.keys())
            self.maxVertice = max(self.graph.keys())

    def get_edge_weight(self, originVertice, targetVertice):
        if originVertice in self.graph.keys():
            for edge in self.graph[originVertice]:
                if edge['target'] == targetVertice:
                    return edge['weight']
        
        return 0

