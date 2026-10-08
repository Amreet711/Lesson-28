# 1) Create a class named `IOString`.
class IOString:
# 2) Define the constructor method `__init__(self)`:
#    a) Initialize an instance variable `self.str1` with an empty string "".
    def __int__(self):
        self.str1 = ""
# 3) Define a method `get_String(self)` to take input from the user:
#    a) Ask the user to enter a string.
#    b) Store the input in `self.str1`.
    def get_String(self):
        self.str1 = input("Enter String: ")
# 4) Define a method `print_String(self)` to display the string in uppercase:
#    a) Convert `self.str1` to uppercase using `.upper()`.
#    b) Print the result.
    def print_String(self):
        print("Entered String in Upper Case: ",self.str1.upper())
# 5) Create an object of the class `IOString` and store it in `str1`.
st1 = IOString()
# 6) Call the method `get_String()` using the object to read input from the user.
st1.get_String()
# 7) Call the method `print_String()` using the object to print the uppercase string.
st1.print_String()