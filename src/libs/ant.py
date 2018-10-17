class Ant:
    def __init__(self):
        self.path = []
        self.pathLength = 0
        self.validPath = 1

    def walk(self, originVertice, targetVertice, pathLength):
        if len(self.path) == 0:
            self.path = [originVertice, targetVertice]

        else:
            if self.path[-1] == originVertice:
                self.path.append(originVertice)
                self.pathLength += pathLength
                
            else:
                self.validPath = 0
                
