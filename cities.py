class Graph:
    
    # initializer (Default instructor)
    def __init__(self):
        self.graph = {}

    # Function to add city to the graph
    def addCity(self, city):
        if city.lower() not in self.graph:
            self.graph[city.lower()] = []
    
    # Function to add a path between two cities        
    def addPath(self, city1, city2):
        if city1.lower() in self.graph and city2.lower() in self.graph:
            self.graph[city1.lower()].append(city2.lower())
            self.graph[city2.lower()].append(city1.lower())
        else:
            print("One or both cities", city1, city2, "are not in the graph.") 
    
    # Function to check if a city exists in the graph        
    def cityExists(self, city):
        if city.lower() in self.graph:
            return True
        else:
            return False
    
    # Function to display all cities in the graph    
    def showAllCities(self):
        for city in self.graph:
            print("- " + city.capitalize())
    
    # Function to print the cities that have a path between them (neighbors)        
    def neighboringCities(self, city):
        if city.lower() in self.graph:
            neighbors = self.graph[city.lower()]
            print("The cities that can be reached from " + city.capitalize() + " : " + ", ".join(neighbor.capitalize() for neighbor in neighbors))
        else:
            print(city.capitalize(), "is not in the graph.")
    
    # Function to check if a city can be reached from a given city        
    def canReachCities(self, startCity):
        visited = set()
        queue = [startCity.lower()]
        
        while queue:
            city = queue.pop(0)
            
            if city not in visited:
                visited.add(city)
                for neighbor in self.graph.get(city, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        
        return visited