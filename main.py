def firstMenu():
    print("Hello! Please enter:\n"
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