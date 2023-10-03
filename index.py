# Is  used to write comments in Python
"""
Multiline
Comment
Here
"""
1+2
1-2
3+4
3-4
variable = "Hello World"
list = ["Alfie", "Bob"]
list[1]
list + [1,2,3,4,5]

#Python was developed by Guido Van Rossum


###PRINT###
#To tell the computer to write to the screen, we use the print statement
#print() is a built-in function in Python to display things on the screen
#The text to be printed has to be enclosed in quotes (" ")
#A built-in function is a function which is predefined and can be used directly

print("Hello Python")

#The concept of indentation has to be kept in mind while writing code in Python
#True or False starts with a capital letter in Python

###INPUT###
#To ask for any information or input from the user in Python, we just need to use the input() function.
#This will ask the user for some input
""" E.g. """ input("Enter your name")
name = input("Enter your name")
print(name)
#Python treats user input as a string value
#Thus while processing information for numeric type, we need to tell the interpreter about it
""" E.g. """ age = int(input("Enter your age:"))
temperature = float(input("Enter the temperature"))

###ADDITION EXAMPLE###
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3 = num1+num2
print("addition is:" num3)