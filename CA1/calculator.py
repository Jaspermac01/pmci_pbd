# --------------------------------
# Calculator
# Author : Pat McIvor
# ID : 10190740
# --------------------------------

#-------------
# imports
#-------------
# Import Maths 
import math

# --------------------------------
# Calculator Class
# --------------------------------
class Calculator(object): 

# function 1
    def add(self, x, y): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types) and isinstance(y, number_types): 
            return x + y 
        else: 
            raise ValueError 

# function 2
    def subtract(self, x, y): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types) and isinstance(y, number_types): 
            return x - y 
        else: 
            raise ValueError 

# function 3
    def multiply(self, x, y): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types) and isinstance(y, number_types): 
            return x * y 
        else: 
            raise ValueError 

# function 4
    def divide(self, x, y): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types) and isinstance(y, number_types): 
            return x / y 
        else: 
            raise ValueError 

# function 5
    def exponent(self, x, y): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types) and isinstance(y, number_types): 
            return x ** y 
        else: 
            raise ValueError 

# function 6
    def square(self, x): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types): 
            return x ** 2 
        else: 
            raise ValueError 

# function 7
    def cube(self, x): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types): 
            return x ** 3 
        else: 
            raise ValueError 

# function 8
    def sin(self, x): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types): 
            return math.sin(x)
        else: 
            raise ValueError 

# function 9
    def cos(self, x): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types): 
            return math.cos(x)
        else: 
            raise ValueError 

# function 10
    def tan(self, x): 
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types): 
            return math.tan(x)
        else: 
            raise ValueError      




#----------------------
# Screen entry that receives 
# (a) function selection
# (b) value(s) to used in calculation
# (c) completes the calulation
#----------------------    

# set variables
functions = ['ADD','SUBTRACT','MULTIPLY','DIVIDE','EXPONENT','SQUARE','CUBE','SIN','COS','TAN']
functions1 = ['ADD','SUBTRACT','MULTIPLY','DIVIDE','EXPONENT']
functions2 = ['SQUARE','CUBE','SIN','COS','TAN']
counter = 0 
entry = ''
status = '' 
value = 0.0 
EXITpgm = False

funct = ''  
calculation = ''


# start loop 
while EXITpgm == False:

    # set variables
    STOPcalc = False
    FUNCset = False
    
    
    # start loop 
    while FUNCset == False and EXITpgm == False: 

        # print initial request
        print '----------------------------------------------------------------------'
        print '      Enter the function you want to use from the following list '
        print '                     OR "exit" to leave calculator'
        print '----------------------------------------------------------------------'
        print '  -->', 'add   ','--', 'subtract','--', 'multiply','--', 'divide','--', 'exponent'
        print '  -->', 'square','--', 'cube    ','--', 'sin     ','--', 'cos   ','--', 'tan'

        # read values from keyboard
        entry = raw_input('> ')   
        try:
            value=float(entry)
        except:
            # check if user wants to exit 
            # or 
            # has entered a valid function name 
            funct = entry.upper()  
            if funct == 'EXIT':
                EXITpgm = True
            elif funct in functions:
                FUNCset = True
            else:
                print 'Enter valid function name OR the word "exit" '
        
            
            
    # start calculation loop 
    while STOPcalc == False and EXITpgm == False: 

        # set variables           
        entry1 = ''
        entry2 = '' 
        value = ''
        value1 = ''
        value2 = ''
        result = 0
        two_entry = False
        STOPcalc = False

     
        # print request for 1st value
        print '----------------------------------------------------------------------'
        print ''
        if funct in functions1:
            print '              Enter the first Value for the', funct, 'calculation'
            two_entry = True    
        else:
            print '                 Enter the Value for the calculation'

           
        print '                 OR "stop" to return to the menu'
        print '                 OR "exit" to exit the calculator'
        print '----------------------------------------------------------------------'

        # start loop   
        while entry1 != 'done':
            # read values from keyboard
            value = raw_input('> ')    
            # check if number was entered
            try:
                value1=float(value)
                entry1 = 'done'
            except:
                preference = ''
                preference = value.upper() 
                if preference == 'STOP':
                    entry1 = 'done'
                    STOPcalc = True
                elif preference == 'EXIT':
                    entry1 = 'done'
                    STOPcalc = True
                    EXITpgm = True
                else:
                    print 'Only enter numbers please or the word "stop" or the word "exit"'
                        
                        
      
        
        if two_entry == True and STOPcalc == False:
            # set variables
            value = ''
            STOP=''
             
            # print request for value 2nd value (if required)
            print '----------------------------------------------------------------------'
            print '              Enter the second value for the' , funct, 'calculation'
            print '                 OR "stop" to stop THIS calculation'
            print '----------------------------------------------------------------------'

            # start loop 
            while entry2 != 'done':
                # read values from keyboard
                value = raw_input('> ')    
                # check if number was entered
                try:
                    value2=float(value)
                    entry2 = 'done'
                except:
                    STOP = value2.upper() 
                    if STOPcalc == True:
                        entry2 = 'done'
                    else:
                        print 'Only enter numbers please or the word "stop"'

        # ------------------
        # Complete the calculation
        # ------------------
        
        if STOPcalc == False:
        
            # set variables
            result = 0
            
            if funct == 'ADD' :               
                result = float(Calculator().add(value1, value2))
            if funct == 'SUBTRACT' :               
                result = float(Calculator().subtract(value1, value2))
            if funct == 'MULTIPLY' :               
                result = float(Calculator().multiply(value1, value2))
            if funct == 'DIVIDE' :               
                result = float(Calculator().divide(value1, value2))
            if funct == 'EXPONENT' :               
                result = float(Calculator().exponent(value1, value2))
            if funct == 'SQUARE' :               
                result = float(Calculator().square(value1))
            if funct == 'CUBE' :               
                result = float(Calculator().cube(value1))
            if funct == 'SIN' :               
                result = float(Calculator().sin(value1))
            if funct == 'COS' :               
                result = float(Calculator().cos(value1))
            if funct == 'TAN' :               
                result = float(Calculator().tan(value1))
            
            # ------------------
            # Display the results
            # ------------------
            
            
            print '----------------------------------------------------------------------'
            print ' '
            print '              The result for your' , funct, 'calculation is: ', result
            print ' '
            print '----------------------------------------------------------------------' 