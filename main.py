import sys
from cities import Graph

def firstMenu():
    print("Please enter:\n"
          "\t1. To go to the drivers' menu\n"
          "\t2. To go to the cities' menu\n"
          "\t3. To exit the system")
    
def driversMenu():
    print("Enter:\n"
          "\t1. To view all the drivers\n"
          "\t2. To add a driver\n"
          "\t3. To go back to main menu")
    
def citiesMenu():
    print("Enter:\n"
          "\t1. To show cities\n"
          "\t2. To print neighboring cities\n"
          "\t3. To print drivers delivering to city")
    
# Function to import drivers from the text file into the list as a form of list of dictionaries
# Inspired from https://www.youtube.com/watch?v=hUyopAoOpG4
def importDriversFile(path):
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

def viewAllDrivers(driversList):   
    for driver in driversList:
        print(driver['driverID'] + ", " + driver['driverName'] + ", " + driver['city'])

def setupGraph(g):
    g.addCity("Beirut")
    g.addCity("Jbeil")
    g.addCity("Akkar")
    
    g.addCity("Saida")
    g.addCity("Zahle")
    
    g.addPath("Beirut", "Jbeil")
    g.addPath("Beirut", "Akkar")
    g.addPath("Jbeil", "Akkar")
    
    g.addPath("Saida", "Zahle")

def saveDriversFile(driversList, path):
    try:
        with open(path, 'w') as file:
            for driver in driversList:
                file.write(driver['driverID'] + ", " + driver['driverName'] + ", " + driver['city'] + "\n")
        print("Driver saved to " + path + " successfully.")
    except Exception as e:
        print("Error saving drivers to file '" + path + "': " + str(e))

def addDriver(driversList, g):
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
    driverID = "ID" + str(nextID).zfill(3)

    # Add driver to the list
    driversList.append({
        'driverID': driverID,
        'driverName': name,
        'city': startCity
    })

    # Save updated list to drivers.txt
    saveDriversFile(driversList, 'drivers.txt')

    print("Driver [" + name + "] added with ID " + driverID + " starting from [" + startCity + "].")
    
# Function to exit the program
def exitProgram():
    print("Thank you for using our program :)")
    # Exit the program using sys module
    # reference: https://www.scaler.com/topics/exit-in-python/
    sys.exit(0)
    

def main():
    # First we import the drivers (in the form of list of dictionaries) from the text file and assign it to drivers variable
    drivers = importDriversFile('drivers.txt')
    cities = Graph()
    setupGraph(cities)
    
    while True:
        firstMenu()
        option = input("Choose an option: ")
        
        if option == '1':
            driversMenu()
            option = input("Choose an option: ")
            if option == '1':
                viewAllDrivers(drivers)
            elif option == '2':
                addDriver(drivers, cities)
            elif option == '3':
                continue # Go back to the main menu
            else:
                print("Invalid option. Please try again.")
        
        elif option == '2':
            citiesMenu()
            option = input("Choose an option: ")
            if option == '1':
                cities.showAllCities()
            elif option == '2':
                city = input("Enter a city name to print all neighbors: ")
                cities.neighboringCities(city)
        elif option == '3':
            exitProgram()
            break
        
        else:
            print("Invalid option. Please try again.")

        
        
    


# To ensure the run of the proram main function as a script (A good habit)       
if __name__ == "__main__":
    main()