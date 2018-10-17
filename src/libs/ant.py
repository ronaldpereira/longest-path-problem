class Ant:
    def __init__(self, originVertice):
        self.path = [originVertice]
        self.pathWeight = 0
        self.validPath = True

    def walk(self, targetVertice, edgeWeight):
        self.path.append(targetVertice)
        self.pathWeight += edgeWeight
                
def ant_colony_creator(n_ants, originVertice):
    colony = []
    for _ in range(n_ants):
        colony.append(Ant(originVertice))
        
    return colony
