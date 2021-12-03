#Mihai Lache
#10_1 assignment
# This assignment demonstrates my knowledge of OOP and setting up real world objects/classes

class Motorcycle:

    num_wheels = 2  #class variable

    def __init__(self, year_made, brand, tanksize, license_plate):
        self.__license_plate = license_plate    #This is a private data variable that can be accessed using self in the class. 
        self.__year = year_made #This is a private data variable that can be accessed using self in the class. 
        self.__brand = brand    #This is a private data variable that can be accessed using self in the class. 
        self.__tanksize = tanksize  #This is a private data variable that can be accessed using self in the class. 
        self.__fuel_level = 0   #This is a private data variable that can be accessed using self in the class. 
        self.__speed = 0    #This is a private data variable that can be accessed using self in the class. 

    def get_motorcycle_details(self):   # This method does not return anything, but it does print out the details of the motorcycle in a formatted fashion.

        print(f'Year made: {self.__year}\nBrand: {self.__brand}\nGas Tank Size: {self.__tanksize} gallons\nNumber of Wheels: {self.num_wheels}\nLicense Plate: {self.__license_plate}')
        
    def fully_fuel_up(self):    #Essentially, this method is adding gas to the full tank capacity of the motorcycle object. After this, it will print out “Gas tank is now full.” and return nothing.

        self.__fuel_level = self.__tanksize
        print(f'Gas tank is now full.')

    def set_speed_up(self,mph): #This method does not return anything but it will print out how much faster the motorcycle is going. 

        self.__speed += mph 
        print(f"Successfully sped up {mph} miles per hour.")

    def set_speed_down(self,mph):   # This method will print out how much the motorcycle has slowed down or it will print an error message.
        if self.__speed - mph >=0:
            self.__speed -= mph
            print(f"Succesfully slowed down {mph} miles per hour.")
        else:
            print(f"Can not slow down more than {self.__speed} miles per hour")


    def get_speed(self):    # Inside of the method, all it is doing is printing out the speed of the motorcycle.

        print(f"The current speed of the motorcycle is {self.__speed} miles per hour")

    

    def set_add_gas(self, amount):  #If the gas is too much, an error message is printed and nothing is added to the tank, if the gas is respecting the tank size, it will be added to the tank and printed out a message.
        if (self.__fuel_level + amount <= self.__tanksize):
            self.__fuel_level += amount
            print(f'Added {amount} gallons')
        else:
            print('The amount of gas you wanted to add exceeded the motorcycles tank size.')

    def set_remove_gas(self, amount):   #If the gas is too much, an error message is printed and nothing is removed from the tank. If the gas wanting to be removed is respecting the tank size, it will be removed from the tank and printed out a message.

        if (self.__fuel_level - amount >= 0):
            self.__fuel_level -= amount
            print(f'Removed {amount} gallons')
        else:
            print('The amount of gas you wanted to remove is exceeded the amount of gas in the tank.')

    def get_gas(self):  #The method will print out the amount of gas in the tank / the tank size.
        print(f'{self.__fuel_level}/{self.__tanksize} gallons')

    def get_num_wheels(self):   #prints out amount of wheels
        print(f'There are {self.num_wheels} wheels on the motorcycle.')
    
    def get_license_plate(self):        #prints license plate of object
        print(f'The license plate is : {self.__license_plate}')

    def get_year_made(self):        #prints out year made of object
        print(f"The motorcycle is from {self.__year}")

    def get_brand(self):        #prints out brand of object
        print(f"The brand is: {self.__brand}")

    def get_tank_size(self):    #prints out tank size of object
        print(f"The tank size is: {self.__tanksize}")


def main(): 
    
    mybike = Motorcycle(1977,"Harley Davinson",20,"F4G7C790")        #makes a motorcycle class object with the respective information inputed
    
    mybike.get_motorcycle_details()      #calls the bike object made #will print out the motorcycles details formatted

    print("-----------")        #this is a divider for the printed output to be more understandable
    
    mybike.get_gas()               #prints out the amount of gas in the tank

    print("-----------")       #divider

    mybike.set_add_gas(4)        #this adds 4 gallons to the motorcycles tank
    mybike.get_gas()               #prints out the amount of gas in the tank after adding 4 gallons

    print("-----------")        #divider

    mybike.set_remove_gas(2)        #this removes 2 gallons from the motorcycles tank
    mybike.get_gas()               #prints out the amount of gas in the tank after removing 2 gallons
  
    print("-----------")        #divider

    mybike.fully_fuel_up()      #this will fully fill up the bikes gas tank
    mybike.get_gas()            # This will print the gas in the bike after fully filling it

    print("-----------")        #divider

    mybike.get_speed()        #calls the bike object made      #This will print out the current speed of the bike (currently 0 as it starts in place.)

    print("-----------")        #divider

    mybike.set_speed_up(35)     #this line will add 35mph to the bikes current speed (which is 0 as shown above)
    mybike.get_speed()       #prints out the speed of object mybike after adding 35 to current speed

    print("-----------")        #divider

    mybike.set_speed_down(15)     #this line will remove 15mph from the bikes current speed (which is 35 as shown above)
    mybike.get_speed()       #prints out the speed of object mybike after removing 15mph from current speed


    print("-----------")        #divider


    mybike.get_brand()      #this will print the motorcycles brand
    mybike.get_license_plate()      #this will print out the motorcycles license plate
    mybike.get_num_wheels()     #this will print out the class variable which holds the amount of wheels on a motorcycle
    mybike.get_tank_size()      #this will print out the motorcycles tank size
    mybike.get_year_made()      #this will print out the year the motorcycle was made


    print("-----------")        #divider



    
    
    
    
    

    
    


if __name__ == "__main__":      #calls the main function
    main()
 
 
 
 
 

 
 
 
 
 
 
