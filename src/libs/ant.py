import copy


class Ant:
    def __init__(self, originVertice):
        self.path = [originVertice]
        self.pathWeight = 0
        self.validPath = True

    def walk(self, targetVertice, edgeWeight):
        self.path.append(targetVertice)
        self.pathWeight += edgeWeight

    def deposite_pheromone(self, graph):
        if self.validPath:
            for nodeIndex in range(len(self.path)-1):
                for index in range(len(graph[self.path[nodeIndex]])):
                    if graph[self.path[nodeIndex]][index]['target'] == self.path[nodeIndex+1]:
                        graph[self.path[nodeIndex]][index]['pheromone'] += 1-(1/self.pathWeight)
                        break


class BestSolution:
    def __init__(self):
        self.path = []
        self.pathWeight = 0

    def set_best_solution(self, ants):
        validAnts = list(filter(lambda ant: ant.validPath == True, ants))

        if len(validAnts) > 0:
            bestAnt = copy.deepcopy(max(validAnts, key=lambda ant: ant.pathWeight))

            if self.pathWeight < bestAnt.pathWeight:
                self.path = bestAnt.path
                self.pathWeight = bestAnt.pathWeight


def ant_colony_creator(n_ants, originVertice):
    colony = []
    for _ in range(n_ants):
        colony.append(Ant(originVertice))
        
    return colony
