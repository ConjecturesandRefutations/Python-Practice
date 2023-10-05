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

###COMPARISON OPERATORS###
#Basically the same as in JavaScript

###Walrus Operator###
#It is a recent addition to the new version of python
#Walrus-operator is another name for assignment expressions
#According to the official documentation, it a way to assign a value to a variable within an expression.

##For example:

#using assignment operator:
variable = False
print(variable)

#using walrus operator 
print(variable:=False)

#Thus we are allowed to combine those two statements using the Walrus operator

###IF STATEMENTS###
if condition:
    statements if True

#A colon(:) is used in Python to make the code more readable and to separate the different parts of an expression.

if 5==5:
    print('You successfully learned the if statement')

#==(equal to) operator is used to compare two entities

if 5>9:
    print('Oops! Not this time.')

#In the above statement, the condition is evaluated as false. Thus the statement following it will never be computed.

if condition:
    statements is True
else:
    statements is False

#If we want to check multiple conditions we can use elif statements:
if condition1:
    statements
elif condition2:
    statements
elif condition3:
    statements
else:
    statements

#elif will always come after an if statement, it cannot exist individually
#elif statements will be checked in the order in which they appear

if 5==4:
    print('An if statement. Oh!')
elif 4==4:
    print("That's something new")
elif 4>=9:
    print("Really?")
else: print('Not this time')

#If all the conditions were evaluated as false, then the else block would be executed

###LOOPS###

#There are two types of loops in Python:
#1. For Loop
#2. While Loop

###For Loop###
for variable in sequence:
    statements

for num in range(1,101):
    print(num)

#range is a function in Python. range() takes a starting value and an ending value
#It generates a list of numbers between them inclusive of starting value and excluding the ending value. In our case from 1 inclusive to 101 exclusive.
#If only one value is passed to range(), it assumes that the starting value is 0 and generates a list of numbers.
#range(100) and range(0,100) gives the same result.

#A third parameter can also be passed to the range function, which represents the 'step'.
#A step is a number by which the index will change every time the loop executes.
#By default a step is 1.

range(0,10,2)
#will return:
[0,2,4,6,8]

###While Loop###
#A while loop works based on the condition:

while condition:
    statement

#It repeatedly executes the following statements until the condition is evaulated as false.

num=0
while (num<10):
    print(num)
    num = num + 1 #update the value of num by 1

