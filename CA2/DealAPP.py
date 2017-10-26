# --------------------------------
# Dealership
# Author : Pat McIvor
# ID : 10190740
# --------------------------------

# Import Car Classes & Dealing Classes
from CarCL import Car, PetrolCar, DieselCar, ElectricCar, HybridCar
from DealCL import Dealership
 
#-------------
# initialise stock
#-------------

Found = False
count = 0
petrol_stock = 0
diesel_stock = 0
electric_stock = 0
hybrid_stock = 0
petrol_rental = 0
diesel_rental = 0
electric_rental = 0
hybrid_rental = 0


lines = open('dealership_file.csv', 'r')

for line in lines:
    detail_line=line.rsplit(',')
    print 'detail_line', detail_line
    
    #line type
    LineType = detail_line[0]
                
    # set available stock
    if LineType == 'stock':
        petrol_stock = int(detail_line[1])
        diesel_stock = int(detail_line[2])
        electric_stock = int(detail_line[3])
        hybrid_stock = int(detail_line[4])
        
    # set rental stock
    if LineType == 'rental':
        petrol_rental = int(detail_line[1])
        diesel_rental = int(detail_line[2])
        electric_rental = int(detail_line[3])
        hybrid_rental = int(detail_line[4])
lines.close()

print 'petrol_stock', petrol_stock
print 'diesel_stock', diesel_stock
print 'electric_stock', electric_stock
print 'hybrid_stock', hybrid_stock
print 'petrol_rental', petrol_rental
print 'diesel_rental', diesel_rental
print 'electric_rental', electric_rental
print 'hybrid_rental', hybrid_rental

pats_dealership = Dealership()
pats_dealership.add_petrol_stock(petrol_stock) 
pats_dealership.add_diesel_stock(diesel_stock)     
pats_dealership.add_electric_stock(electric_stock) 
pats_dealership.add_hybrid_stock(hybrid_stock)

pats_dealership.add_petrol_stock(petrol_rental) 
pats_dealership.add_diesel_stock(diesel_rental)     
pats_dealership.add_electric_stock(electric_rental) 
pats_dealership.add_hybrid_stock(hybrid_rental)

pats_dealership.stock_count()
pats_dealership.rental_count()


#-------------
# initialise variables
#-------------
EXITpgm = False
pet_s = 0
die_s = 0
ele_s = 0
hyb_s = 0
pet_r = 0
die_r = 0
ele_r = 0
hyb_r = 0


#-------------
# start process outer loop 
#-------------
while EXITpgm == False:

    # set inner loop variables
    Selected_Opt = False
    Selected_type = False
    Selected_amt = False
    Leave2 = False
    Leave3 = False
    
    options = ['RENT','RETURN']   
    types = ['PETROL','DIESEL','ELECTRIC','HYBRID']   

    #------------------------------------------------
    # start inner loop 1 - RENT or RETURN selection
    #------------------------------------------------
    while Selected_Opt == False and EXITpgm == False: 
        
        # initialise inner loop 1 variables
        entry1 = ''
        value1 = ''
        funct1 = ''

        # print menu
        print ' '
        print '      Do you wish to RENT a car OR RETURN a car ? '
        print '         Enter "rent"     to rent a car'
        print '         Enter "return"   to return a car ' 
        print '         Enter "exit"     to leave dealership app '
        print ' '

        # read values from keyboard
        entry1 = raw_input('> ')   
        try:
            # is a number entered ?
            value1=float(entry1)
            print '1 Enter a valid selection OR enter "exit" '
        except:
            # check if user wants to exit 
            # or 
            # has selected a valid function name 
            funct1 = entry1.upper()  
            if funct1 == 'EXIT':
                EXITpgm = True
            elif funct1 in options:
                Selected_Opt = True
            else:
                print '2 Enter a valid selection OR enter "exit" '

    # ------------------------------
    # Next loop - TYPE of car to rent or return  
    # ------------------------------
    while Selected_type == False and Leave2 == False and Selected_Opt == True and EXITpgm == False: 

        #-------------
        # initialise inner loop 1 variables
        #-------------
        entry2 = ''
        value2 = ''
        funct2 = ''

            
        # print initial menu
        print '----------------------------------------------------------------------'
        print '      What type of car do you want to ' , entry1
        print '         Enter "petrol"    '
        print '      or Enter "diesel"    '
        print '      or Enter "electric"  '
        print '      or Enter "hybrid"    '
        print ' '
        print '      or Enter "exit"      to go back to the main nenu'
        print ' '

        # read values from keyboard
        entry2 = raw_input('> ')   
        try:
            # is a number entered ?
            value2=float(entry2)
            print '3 Enter a valid selection OR enter "exit" '
        except:
            # check if user wants to exit 
            # or 
            # has entered a valid function name 
            funct2 = entry2.upper()  
            if funct2 == 'EXIT':
                Leave2 = True
            elif funct2 in types:
                Selected_type = True
            else:
                print '4 Enter a valid selection OR enter "exit" '
   
    # ------------------------------
    # Next loop - How MANY to rent or return  
    # ------------------------------            
    while Selected_amt == False and Leave3 == False and Selected_type == True and Selected_Opt == True and EXITpgm == False: 
        
        # print menu
        print '----------------------------------------------------------------------'
        print '      How many do you want to rent ? '
        print ' '
        print '      or Enter "exit"      to go back to the main nenu'
        print ' '
        
        # read values from keyboard
        entry3 = raw_input('> ')   
        try:
            # is a number entered ?
            value3=float(entry3)
            Selected_amt = True
        except:
            funct3 = entry3.upper()  
            if funct3 == 'EXIT':
               Leave3 = True
            else:            
                print '5 Enter a valid selection OR enter "exit" '


    # ------------------------------
    # Next loop - Process request  
    # ------------------------------            
    if Selected_amt == True and Selected_type == True and Selected_Opt == True and EXITpgm == False:                         
    
        # Get values
        pet_s = pats_dealership.count_petrol_stock()
        die_s = pats_dealership.count_diesel_stock()
        ele_s = pats_dealership.count_electric_stock()
        hyb_s = pats_dealership.count_hybrid_stock()
        
        pet_r = pats_dealership.count_petrol_rental()
        die_r = pats_dealership.count_diesel_rental()
        ele_r = pats_dealership.count_electric_rental()
        hyb_r = pats_dealership.count_hybrid_rental()

        # RENTAL CALCs
        if  funct1 == 'RENT':
            if funct2 == 'PETROL':
                if value3 > pet_s :
                    print ''
                    print '      Petrol Rental amount requested', value3 ,' greater than', pet_s, 'available. Try again'
                    print ''
                elif value3 <= 0:
                    print ''
                    print '      Petrol Rental amount requested', value3 ,'invalid. Try again'
                    print ''
                else:
                    pats_dealership.reduce_petrol_stock(1)
                    pats_dealership.add_petrol_rental(1)
                    print ''
                    print '      Petrol Rental requested for', value3 ,' completed. Thanks'
                    print ''
            elif funct2 == 'DIESEL':
                if value3 > die_s :
                    print ''
                    print '      Diesel Rental amount requested', value3 ,' greater than', die_s, 'available. Try again'
                    print ''
                elif value3 <= 0:
                    print ''
                    print '      Diesel Rental amount requested', value3 ,'invalid. Try again'
                    print ''
                else:
                    pats_dealership.reduce_diesel_stock(1)
                    pats_dealership.add_diesel_rental(1)
                    print ''
                    print '      Diesel Rental request for', value3 ,' completed. Thanks'
                    print ''         
            elif funct2 == 'ELECTRIC':
                if value3 > ele_s :
                    print ''
                    print '      Electric Rental amount requested', value3 ,' greater than', ele_s, 'available. Try again'
                    print ''
                elif value3 <= 0:
                    print ''
                    print '      Electric Rental amount requested', value3 ,'invalid. Try again'
                    print ''
                else:
                    pats_dealership.reduce_electric_stock(1)
                    pats_dealership.add_electric_rental(1)
                    print ''
                    print '      Electric Rental request for', value3 ,' completed. Thanks'
                    print ''         
            elif funct2 == 'HYBRID':
                if value3 > hyb_s :
                    print ''
                    print '      Hybrid Rental amount requested', value3 ,' greater than', hyb_s, 'available. Try again'
                    print ''
                elif value3 <= 0:
                    print ''
                    print '      Hybrid Rental amount requested', value3 ,'invalid. Try again'
                    print ''
                else:
                    pats_dealership.reduce_hybrid_stock(1)
                    pats_dealership.add_hybrid_rental(1)
                    print ''
                    print '      Hybrid Rental request for', value3 ,' completed. Thanks'
                    print ''        
        # RETURN CALCs
        else :        
            if funct2 == 'PETROL':
                if value3 > pet_r :
                    print ''
                    print '      Petrol Return amount requested', value3 ,' greater than', pet_r, 'rented. Try again'
                    print ''
                elif value3 <= 0:
                    print ''
                    print '      Petrol Return amount requested', value3 ,'invalid. Try again'
                    print ''
                else:
                    pats_dealership.reduce_petrol_rental(1)
                    pats_dealership.add_petrol_stock(1)
                    print ''
                    print '      Petrol Return request for', value3 ,' completed. Thanks'
                    print ''   
            elif funct2 == 'DIESEL':
                if value3 > die_r :
                    print ''
                    print '      Diesel Return amount requested', value3 ,' greater than', die_r, 'rented. Try again'
                    print ''
                elif value3 <= 0:
                    print ''
                    print '      Diesel Return amount requested', value3 ,'invalid. Try again'
                    print ''
                else:
                    pats_dealership.reduce_diesel_rental(1)
                    pats_dealership.add_diesel_stock(1)
                    print ''
                    print '      Diesel Return request for', value3 ,' completed. Thanks'
                    print ''          
            elif funct2 == 'ELECTRIC':
                if value3 > ele_r :
                    print ''
                    print '      Electric Return amount requested', value3 ,' greater than', ele_r, 'rented. Try again'
                    print ''
                elif value3 <= 0:
                    print ''
                    print '      Electric Return amount requested', value3 ,'invalid. Try again'
                    print ''
                else:
                    pats_dealership.reduce_electric_rental(1)
                    pats_dealership.add_electric_stock(1)
                    print ''
                    print '      Electric Return request for', value3 ,' completed. Thanks'
                    print ''      
            elif funct2 == 'HYBRID':
                if value3 > hyb_r :
                    print ''
                    print '      Hybrid Return amount for', value3 ,' completed. Thanks'
                    print ''
                elif value3 <= 0:
                    print ''
                    print '      Hybrid Return amount requested', value3 ,'invalid. Try again'
                    print ''
                else:
                    pats_dealership.reduce_hybrid_rental(1)
                    pats_dealership.add_hybrid_stock(1)
                    print ''
                    print '      Hybrid Return request for', value3 ,' completed. Thanks'
                    print ''               
                        
        pats_dealership.stock_count()
        pats_dealership.rental_count()
        
        line1 = 'stock' + ',' + str(len(pats_dealership.petrol_cars)) + ',' + str(len(pats_dealership.diesel_cars)) + ',' + str(len(pats_dealership.electric_cars)) + ',' + str(len(pats_dealership.hybrid_cars)) + '\n'
        line2 = 'rental' + ',' + str(len(pats_dealership.petrol_rental)) + ',' + str(len(pats_dealership.diesel_rental)) + ',' + str(len(pats_dealership.electric_rental)) + ',' + str(len(pats_dealership.hybrid_rental))
        
        lines = open('dealership_file.csv', 'w')
        lines.write(line1)
        lines.write(line2)        
        lines.close()
        
