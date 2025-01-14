# Variables
# Compiled vs interpreted
# Dynamically Typed
my_number = 1

my_string = "test" # Stored as array of chars

my_dict = {
    "Hello": "World"
} # key: value, if you don't give keys, it will be a set and that is unordered.

is_active = True

my_list = ["Hello", "World"]

my_tuple = ("this", "is", "a", "tuple") # Tuple items are ordered, unchangeable, and allow duplicate values.

my_empty = None # this is the null type in python



# Functions
# Python doesn't use {}, it uses indentation to identify functions, loops, ... Always make sure to apply the correct indentation for a code block
def my_function():
    print("Hello world!")
        #print("test") --> This indentation would throw an error. I can only go down a level to drop out of the function but going up requires something that uses the : (function, loop, ...)
# With parameters
def my_function(name: str): ## Sometimes adding a typed parameter can be useful
    print(f"Hello {name}")



# Simple example
def sum(n1, n2, n3):
    return n1 + n2 + n3



# conditions
email = "admin@test.com"
password = "Beheerder1"



# Basic changes:
# Null check: if (!variable) {} --> if not variable:
if email == "test@admin.com": # Python doesn't require () around the condition
    print("access granted")
# elif is the keyword you would use to handle else if cases
# elif email = "...":
else:
    print("access denied")



# Loops
# For
def simple_sum(my_numbers: list):
    sum = 0
    for number in my_numbers:
        sum += number
    return



# While
def simple_sum_while(my_numbers: list):
    sum, counter = 0
    while(counter < len(my_number)):
        sum += my_numbers[counter]
        counter += 1 # ++ doesn't exist is python
    return sum



# OOP
class Player:
    name: str
    health: int
    damage: int
    dead: bool = False # True/False always with capital letters

    # Python always uses the self variable to handle properties. Class functions/methods should always take self as the first argument, even the constructor!
    # Properties can be called using self.property_name
    def __init__(self, name, health, damage): ## The constructor is always called using __init__(self, ...)
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        if not self.dead:
            self.health -= damage
        else: # Note the indentation change without brackets!
            print("You cannot take damage when you are dead")
            return

# Inheritance
class Warrior(Player):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage)
        self.armor = armor



# Handy basic predefined functions
list_size = len(my_list) # 2
# Iterating list using enumerate to get both index and element
for i, name in enumerate(my_list):
    print(f"Index {i}: {name}")
# use range() to only get the indexes
for i in range(len(my_list)):
    print(my_list[i]) # This will return the elements at these indexes, but it is best practice to use the enumerate functions



# running your python file
def main():
    print("running main")

if __name__ == "__main__": # Python’s if __name__ == "__main__" idiom allows code to run only when the script is executed, not when it’s imported.
    main()



# Error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")



# Modules
import math
print(math.sqrt(16)) # 4.0
