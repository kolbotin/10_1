# 10_1

Part 1

Class Description:

	The class that I decided to create demonstrating a real world object was “Motorcycle”. In order to make an object of the motorcycle class, 4 values must be passed as parameters into the class. In other words, with this motorcycle class, you can make an object which is unique in terms of the motorcycle's year made, brand, tank size, and license plate. In addition, you can fill up or remove gas from the motorcycle, and you can control the way the motorcycle speeds up or slows down.

Class and data variable description:

Num_wheels: This is a class variable in the motorcycle class. It is a class variable because every object made out of the motorcycle class must have 2 wheels.

__license_plate : This is a private data variable that can be accessed using self in the class. The value this variable holds is a string of the motorcycle's license plate, passed in through the init method.

__year : This is a private data variable that can be accessed using self in the class. The value this variable holds is a number representing the year the motorcycle was made, passed in through the init method.

__brand: This is a private data variable that can be accessed using self in the class. The value this variable holds is a string representing the motorcycles brand, passed in through the init method.

__tanksize : This is a private data variable that can be accessed using self in the class. The value this variable holds is a number representing the tank size of the motorcycle object, passed in through the init method.

__fuel_level:	This is a private data variable that can be accessed using self in the class. The value this variable holds is initially 0 which represents the motorcycle's current fuel level, because the motorcycle will be initially empty of gas.

__speed:	This is a private data variable that can be accessed using self in the class. The value this variable holds is initially 0, because the motorcycle will be initially stationary.






Method description:

def get_motorcycle_details(self): This method does not require any input arguments as it will be calling variables with self. This method does not return anything, but it does print out the details of the motorcycle in a formatted fashion.

def fully_fuel_up(self): This method does not require any input arguments as it will be altering the private data variables using self. Essentially, this method is adding gas to the full tank capacity of the motorcycle object. After this, it will print out “Gas tank is now full.” and return nothing.

def set_speed_up(self,mph): This method does require one input argument which will be how much faster in mph you want the motorcycle to go. The method then adds the input argument mph to the current speed of the bike. This method does not return anything but it will print out how much faster the motorcycle is going. 

def set_speed_down(self,mph): This method is very similar to the set_speed_up method as they are both taking in one argument of “mph” but this method includes an extra step. The extra step is checking if the amount of speed the method is asking to slow down is more than the speed of the bike (Basically doesn't allow the motorcycle to slow down past 0mph). This method will print out how much the motorcycle has slowed down or it will print an error message.

def get_speed(self): This method does not take in any input arguments as it only takes in self as an argument. Inside of the method, all it is doing is printing out the speed of the motorcycle.

def set_add_gas(self, amount): This method takes in one input argument which is the amount of gas you want to add to the gas tank. However, the method also checks if the amount of gas you want to add is greater than the amount of space in the tank itself. If the gas is too much, an error message is printed and nothing is added to the tank, if the gas is respecting the tank size, it will be added to the tank and printed out a message.

def set_remove_gas(self, amount): This method takes in one input argument which is the amount of gas you want to remove from the gas tank. However, the method also checks if the amount of gas you want to remove is greater than the amount of gas in the tank itself. If the gas is too much, an error message is printed and nothing is removed from the tank. If the gas wanting to be removed is respecting the tank size, it will be removed from the tank and printed out a message.

def get_gas(self): This method does not take in any input arguments as the only argument being passed through it is self. The method will print out the amount of gas in the tank / the tank size.






Demo Program Documentation

	The demo program I made is responsible for explaining how the class and methods work for the motorcycle class. It systematically goes through each method and related methods to show the user how to navigate the class and use it for themselves. Another thing to note is that in the demo program, I divided it with print statements printing “--------” to show important breaks in the output and make it easier to understand.	The way a user can run the demo program is through commenting certain parts of the code to “turn it off” or run the program and track the output back to the code that made that output.




