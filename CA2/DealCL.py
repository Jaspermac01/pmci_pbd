#---------------------
# Define a dealership class
#---------------------
#imports
from CarCL import Car, PetrolCar, DieselCar, ElectricCar, HybridCar

# The dealer class

class Dealership(object): 
    def __init__(self): 
        # record cars
        self.petrol_cars = [] 
        self.diesel_cars = [] 
        self.electric_cars = [] 
        self.hybrid_cars = []         
        self.cars_count = []  
        
        # record rental cars
        self.petrol_rental = [] 
        self.diesel_rental = [] 
        self.electric_rental = [] 
        self.hybrid_rental = []         
        self.cars_rental = []     
         
    #------------------------------------------
    # Inventory Management - create
    #------------------------------------------   
    # Create petrol inventory    
    def add_petrol_stock(self, num): 
        for i in range(int(num)): 
            print 'i', i
            print 'num', num           
            self.petrol_cars.append(PetrolCar()) 
            
    # Create diesel inventory 
    def add_diesel_stock(self, num):     
        for i in range(int(num)): 
            print 'i', i
            print 'num', num  
            self.diesel_cars.append(DieselCar()) 
        
    # Create electric inventory     
    def add_electric_stock(self, num): 
        for i in range(int(num)): 
            print 'i', i
            print 'num', num   
            self.electric_cars.append(ElectricCar())
            
    # Create hybrid inventory 
    def add_hybrid_stock(self, num):     
        for i in range(int(num)): 
            print 'i', i
            print 'num', num  
            self.hybrid_cars.append(HybridCar()) 

    #------------------------------------------
    # Inventory Management - reduce
    #------------------------------------------
    def reduce_petrol_stock(self, num): 
        for i in range(int(num)): 
            self.petrol_cars.pop() 
            
    # reduce diesel inventory 
    def reduce_diesel_stock(self, num):     
        for i in range(int(num)): 
            self.diesel_cars.pop() 
        
    # reduce elecric inventory     
    def reduce_electric_stock(self, num): 
        for i in range(int(num)): 
            self.electric_cars.pop()
            
    # reduce hybrid inventory 
    def reduce_hybrid_stock(self, num):     
        for i in range(int(num)): 
            self.hybrid_cars.pop() 
            
    #------------------------------------------
    # Inventory Management - Reporting
    #------------------------------------------        
    # get petrol inventory    
    def count_petrol_stock(self): 
        count = int(len(self.petrol_cars))
        return count
            
    # get diesel inventory 
    def count_diesel_stock(self):     
        count = int(len(self.diesel_cars))
        return count
        
    # get electric inventory     
    def count_electric_stock(self): 
        count = int(len(self.electric_cars))
        return count
            
    # get hybrid inventory
    def count_hybrid_stock(self):     
        count = int(len(self.hybrid_cars))
        return count

    # Print Stock detail ------------------------           
    def stock_count(self): 
        print '----------------------------------------------------------------------'
        print '         Petrol cars in stock   ' + str(len(self.petrol_cars))
        print '         Diesel cars in stock   ' + str(len(self.diesel_cars)) 
        print '         Electric cars in stock ' + str(len(self.electric_cars)) 
        print '         Hybrid cars in stock   ' + str(len(self.hybrid_cars)) 
        print '         -----------------------'  


    #------------------------------------------
    # Rental Management - create
    #------------------------------------------        
    # Create petrol inventory   
    def add_petrol_rental(self, num): 
        for i in range(int(num)): 
            self.petrol_rental.append(PetrolCar()) 
            
    # Create diesel inventory 
    def add_diesel_rental(self, num):     
        for i in range(int(num)): 
            self.diesel_rental.append(DieselCar()) 
        
    # Create electric inventory     
    def add_electric_rental(self, num): 
        for i in range(int(num)): 
            self.electric_rental.append(ElectricCar())
            
    # Create hybrid inventory 
    def add_hybrid_rental(self, num):     
        for i in range(int(num)): 
            self.hybrid_rental.append(HybridCar())     
    #------------------------------------------
    # Rental Management - reduce
    #------------------------------------------        
    # Create petrol inventory   
    def reduce_petrol_rental(self, num): 
        for i in range(int(num)): 
            self.petrol_rental.pop(PetrolCar()) 
            
    # Create diesel inventory 
    def reduce_diesel_rental(self, num):     
        for i in range(int(num)): 
            self.diesel_rental.pop(DieselCar()) 
        
    # Create electric inventory     
    def reduce_electric_rental(self, num): 
        for i in range(int(num)): 
            self.electric_rental.pop(ElectricCar())
            
    # Create hybrid inventory 
    def reduce_hybrid_rental(self, num):     
        for i in range(int(num)): 
            self.hybrid_renal.pop(HybridCar())                 
            
    #------------------------------------------
    # Rental Management - Reporting
    #------------------------------------------        
    # get petrol inventory    
    def count_petrol_rental(self): 
        count = int(len(self.petrol_cars))
        return count
            
    # get diesel inventory 
    def count_diesel_rental(self):     
        count = int(len(self.diesel_cars))
        return count
        
    # get electric inventory     
    def count_electric_rental(self): 
        count = int(len(self.electric_cars))
        return count
            
    # get hybrid inventory
    def count_hybrid_rental(self):     
        count = int(len(self.hybrid_cars))
        return count

    # Print rental detail ------------------------           
    def rental_count(self): 
        print '         Petrol cars in rental   ' + str(len(self.petrol_rental)) 
        print '         Diesel cars in rental   ' + str(len(self.diesel_rental)) 
        print '         Electric cars in rental ' + str(len(self.electric_rental)) 
        print '         Hybrid cars in rental   ' + str(len(self.hybrid_rental)) 
        print '----------------------------------------------------------------------'  
