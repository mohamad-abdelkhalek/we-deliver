class Graph:
    def __init__(self):
        self.graph = {}

    def addCity(self, city):
        if city.lower() not in self.graph:
            self.graph[city.lower()] = []
            
    def addPath(self, city1, city2):
        if city1.lower() in self.graph and city2.lower() in self.graph:
            self.graph[city1.lower()].append(city2.lower())
            self.graph[city2.lower()].append(city1.lower())
        else:
            print("One or both cities", city1, city2, "are not in the graph.") 
            
    def cityExists(self, city):
        if city.lower() in self.graph:
            return True
        else:
            return False
        
    def showAllCities(self):
        for city in self.graph:
            print("- " + city.capitalize())
            
    def neighboringCities(self, city):
        if city.lower() in self.graph:
            neighbors = self.graph[city.lower()]
            print("The cities that can be reached from " + city.capitalize() + " : " + ", ".join(neighbor.capitalize() for neighbor in neighbors))
        else:
            print(city.capitalize(), "is not in the graph.")