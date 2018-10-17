import numpy as np

class AntColonyOptimization:
    def __init__(self, evaporationRate, g):
        self.evaporationRate = evaporationRate
        self.g = g
        self.graph = g.graph

    def build_solution(self, ant, originVertice, targetVertice):
        actualVertice = originVertice

        while actualVertice != targetVertice and ant.validPath:
            nextVertice = self.probabilistic_transition(actualVertice)

            ant.walk(nextVertice, self.g.get_edge_weight(actualVertice, nextVertice))

            actualVertice = nextVertice

        print(ant.path)
        print(ant.pathWeight)
            
    def probabilistic_transition(self, originVertice):
        pathDistribution = []
        totalPheromone = 0
        for edge in self.graph[originVertice]:
            totalPheromone += edge['pheromone']
            pathDistribution.extend([edge['target']]*edge['pheromone'])
        
        targetVertice = pathDistribution[np.random.randint(totalPheromone)]

        return targetVertice
