# Import sys module to use it to exit the program
import sys

# Import the cities graph
from cities import Graph

# Function to display the first menu
def firstMenu(): # O(1)
    print("Please enter:\n"
          "\t1. To go to the drivers' menu\n"
          "\t2. To go to the cities' menu\n"
          "\t3. To exit the system")
    
# Function to display the drivers menu   
def driversMenu(): # O(1)
    print("Enter:\n"
          "\t1. To view all the drivers\n"
          "\t2. To add a driver\n"
          "\t3. To go back to main menu")

# Function to display the cities menu  
def citiesMenu(): # O(1)
    print("Enter:\n"
          "\t1. To show cities\n"
          "\t2. To print neighboring cities\n"
          "\t3. To print drivers delivering to city\n"
          "\t4. To go back to main menu")
    
# Function to import drivers from the text file into the list as a form of list of dictionaries
# Inspired from https://www.youtube.com/watch?v=hUyopAoOpG4
def importDriversFile(path): # O(n)
    driversList = []
    
    with open(path, 'r') as file:
        for line in file:
            item = line.strip().split(', ')
            
            driver = {
                'driverID': item[0],
                'driverName': item[1],
                'city': item[2]
            }

            driversList.append(driver)

    return driversList

# Function to view all the drivers
def viewAllDrivers(driversList): # O(n)
    for driver in driversList:
        print(driver['driverID'] + ", " + driver['driverName'] + ", " + driver['city'])

# Function to add the cities and the paths between them
def setupGraph(g): # O(1)
    g.addCity("Beirut")
    g.addCity("Jbeil")
    g.addCity("Akkar")
    
    g.addCity("Saida")
    g.addCity("Zahle")
    
    g.addPath("Beirut", "Jbeil")
    g.addPath("Beirut", "Akkar")
    g.addPath("Jbeil", "Akkar")
    
    g.addPath("Saida", "Zahle")

# reference: https://www.pythontutorial.net/python-basics/python-write-text-file/
def saveDriversFile(driversList, path): # O(n)
    try:
        with open(path, 'w') as file:
            for driver in driversList:
                file.write(driver['driverID'] + ", " + driver['driverName'] + ", " + driver['city'] + "\n")
        print("Driver saved to " + path + " successfully.")
    except Exception as e:
        print("Error saving drivers to file '" + path + "': " + str(e))

# Function to add a driver
def addDriver(driversList, g): # O(n)
    name = input("Enter the name of the driver: ").strip()
    startCity = input("Enter the start city of the driver: ").strip()

    # Check if the city exists in the graph
    if g.cityExists(startCity) == False:
        choice = input("The city [" + startCity + "] is not available in the current cities database. Do you want to add it to the database? (yes/no): ").strip().lower()
        if choice == 'yes':
            g.addCity(startCity)
            print("City [" + startCity + "] added to the cities database.")

    # Generate next driver ID
    nextID = len(driversList) + 1
    driverID = "ID" + str(nextID).zfill(3) # ID auto increament

    # Add driver to the list
    driversList.append({
        'driverID': driverID,
        'driverName': name,
        'city': startCity
    })

    # Save updated list to drivers.txt
    saveDriversFile(driversList, 'drivers.txt')

    print("Driver [" + name + "] added with ID " + driverID + " starting from [" + startCity + "].")

# Function to print neighboring cities
def printNeighboringCities(g): # O(V)
    city = input("Enter a city name to print all neighbors: ")
    g.neighboringCities(city)

# Function to print drivers delivering to city
def driversDeliveringToCity(driversList, g): # O(V + E)
    city = input("Enter the city name: ").strip().lower()
    if g.cityExists(city) == False:
        print(city + " is not in the graph!")
        return

    canReach = g.canReachCities(city)
    
    cities = []
    for c in canReach:
        capCity = c.capitalize()
        cities.append(capCity)

    print("Reachable cities from " + city.capitalize() + " : " + ', '.join(cities))
    driversDelivering = []

    for driver in driversList:
        if driver['city'].lower() in canReach:
            driversDelivering.append(driver)

    if not driversDelivering:
        print("No drivers are delivering to " + city.capitalize())
    else:
        print("Drivers delivering to " + city.capitalize() + ": ")
        for driver in driversDelivering:
            print(driver['driverID'] + ", " + driver['driverName'] + ", " + driver['city'].capitalize())

# Function to exit the program
def exitProgram(): # O(1)
    print("Thank you for using our program :)")
    # Exit the program using sys module
    # reference: https://www.scaler.com/topics/exit-in-python/
    sys.exit(0)
    

def main():
    drivers = importDriversFile('drivers.txt')
    cities = Graph()
    setupGraph(cities)
    
    while True:
        firstMenu()
        option = input("Choose an option: ")
        
        if option == '1':
            while True:
                driversMenu()
                option = input("Choose an option: ")
                if option == '1':
                    viewAllDrivers(drivers)
                elif option == '2':
                    addDriver(drivers, cities)
                elif option == '3':
                    break  # Go back to the main menu
                else:
                    print("Invalid option. Please try again.")
        
        elif option == '2':
            while True:
                citiesMenu()
                option = input("Choose an option: ")
                if option == '1':
                    cities.showAllCities()
                elif option == '2':
                    printNeighboringCities(cities)
                elif option == '3':
                    driversDeliveringToCity(drivers, cities)
                elif option == '4':
                    break  # Go back to the main menu
                else:
                    print("Invalid option. Please try again.")
                
        elif option == '3':
            exitProgram()
            break
        
        else:
            print("Invalid option. Please try again.")


# To ensure the run of the proram main function as a script (A good habit)       
if __name__ == "__main__":
    main()