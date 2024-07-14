class Graph:
    def __init__(self):
        self.graph = {}

    def addCity(self, city):
        if city not in self.graph:
            self.graph[city] = []
            
    def addPath(self, city1, city2):
        if city1 in self.graph and city2 in self.graph:
            self.graph[city1].append(city2)
            self.graph[city2].append(city1)
        else:
            print("One or both cities", city1, city2, "are not in the graph.") 
            
    def cityExists(self, city):
        if city in self.graph:
            return True
        else:
            return False
        
    def showAllCities(self):
        for city in self.graph:
            print("- " + city)
            
    def neighboringCities(self, city):
        if city in self.graph:
            print("The cities that can be reached from " + city + " : " + ", ".join(self.graph[city]))
        else:
            print(city, "is not in the graph.")