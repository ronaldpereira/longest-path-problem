import math

import numpy as np


class AntColonyOptimization:
    def __init__(self, g):
        self.g = g
        self.graph = g.graph

    def build_solution(self, ant, originVertice, targetVertice):
        actualVertice = originVertice

        while actualVertice != targetVertice and ant.validPath:
            nextVertice = self.probabilistic_transition(actualVertice, ant)

            if nextVertice > 0:
                ant.walk(nextVertice, self.g.get_edge_weight(actualVertice, nextVertice))
                actualVertice = nextVertice

            # If there's no valid path from that actual vertice
            else:
                ant.validPath = False
            
    def probabilistic_transition(self, originVertice, ant):
        pathDistribution = []
        for edge in self.graph[originVertice]:
            if edge['target'] not in ant.path:
                pathDistribution.extend([edge['target']]*math.ceil(edge['weight']*edge['pheromone']))
        
        if len(pathDistribution) > 0:
            targetVertice = pathDistribution[np.random.randint(len(pathDistribution))]
            return targetVertice
        else:
            return 0
