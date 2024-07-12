class Graph:
    def __init__(self):
        self.graph = {}

    def AddCity(self, city):
        if city not in self.graph:
            self.graph[city] = []