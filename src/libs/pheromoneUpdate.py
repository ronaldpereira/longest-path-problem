import math


class PheromoneUpdate:
    def __init__(self, evaporationRate, k):
        self.evaporationRate = evaporationRate
        self.k = k
    
    def update(self, graph, ants):
        for originVertice in graph.keys():
            for index in range(len(graph[originVertice])):
                graph[originVertice][index]['pheromone'] = graph[originVertice][index]['pheromone'] * (1-self.evaporationRate)

        if self.k == 0:
            self.k = len(ants)

        sortedAnts = sorted(ants, key=lambda ant: ant.pathWeight, reverse=True)

        for antIndex in range(self.k):
            sortedAnts[antIndex].deposite_pheromone(graph)
