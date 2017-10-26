#---------------------
# Define a class for car
#---------------------

class Car(object):
   
    def __init__(self):
        # set the initial car values.   
        self.__make = ''
        self.__mileage = 1
        self.__seats = 5  
        self.__colour = ''

    # Set Values----------------
    def setMake(self, make):
        #set make 
        self.__make = make

    def setMileage(self, mileage):
        #set mileage 
        self.__mileage = mileage

    def move(self, distance):
        #set change in mileage 
        self.__mileage = self.__mileage + distance
        return self.__mileage

    def setSeats(self, seats):
        # set number of seats 
        self.__seats = seats

    def paint(self, colour):
        # Set new clour and return it   
        self.__colour = colour
        return self.__colour
       
    # Retrieve Values-----------        
    def getMake(self):
        #retrieve make 
        return self.__make

    def getMileage(self):
        # retrieve mileage 
        return self.__mileage
        
    def getSeats(self): 
        # retrieve number of seats     
        return self.__seats
        
    def getColour(self):
        # retrieve colour   
        return self.__colour

        
class PetrolCar(Car): 
    def __init__(self): 
        Car.__init__(self) 
        self.__numberCylinders = 1 
        self.__engineSize = 0
        
    # Set Values----------------        
    def setNumberCylinders(self, numberCylinders): 
        self.__numberCylinders = numberCylinders    

    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize
              
    # Retrieve Values-----------     
    def getNumberCylinders(self): 
        return self.__numberCylinders 

    def getEngineSize(self):
        return self.__engineSize
        
        
class DieselCar(Car): 
    def __init__(self): 
        Car.__init__(self) 
        self.__numberCylinders = 1 
        self.__engineSize = 0
        
    # Set Values----------------    
    def setNumberCylinders(self, numberCylinders): 
        self.__numberCylinders = numberCylinders    

    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize
              
    # Retrieve Values-----------     
    def getNumberCylinders(self): 
        return self.__numberCylinders 

    def getEngineSize(self):
        return self.__engineSize 
        
       
class ElectricCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        
    # Set Values----------------    
    def setNumberFuelCells (self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

    # Retrieve Values-----------  
    def getNumberFuelCells(self):
        return self.__numberFuelCells
 
       
class HybridCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1 
        self.__engineSize = 0
        self.__numberFuelCells = 1       
        
    # Set Values----------------   
    def setNumberCylinders(self, numberCylinders): 
        self.__numberCylinders = numberCylinders    

    def setEngineSize(self, engineSize):
        self.__engineSize =  engineSize  
        
    def setNumberFuelCells (self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells
              
    # Retrieve Values-----------  
    def getNumberCylinders(self): 
        return self.__numberCylinders 

    def getEngineSize(self):
        return self.__engineSize 
 
    def getNumberFuelCells(self):
        return self.__numberFuelCells       
         
