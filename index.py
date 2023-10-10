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

###FUNCTIONS###

def functionName (parameters):
    statements
    return something

#def is used to declare a function
#functionName is the name of the function
#A function may take in parameters, or may not. Parameters consist of variables used by the function, e.g. two numbers to be summed.
#statements are the operations which we need to perform
#A return statement marks the end of the function and can be used to return the output. You can avoid putting it in, if you don't have to return any value.

def helloWorld():
    print("Hello World")

#This function takes no parameters, and prints "Hello World" every time it is called.

def addNumbers(num1,num2):
    sum = num1+num2
    return sum

###Calling a function###

#To use a function we can defined, we need to make a call to the function
#Calling a function uses the following syntax:

functionName(parameters)

def addNumbers(num1, num2):
    sum = num1+num2
    print(sum)
    return
addNumbers(2,3)
addNumbers(4,5)

###Lambda Functions###

#Lambdas, also known as anonymous functions, are small, restricted functions which do not need a name
#In Python, lambda expressions (or lambda forms) are utilized to construct anonymous functions
#To do so, you will use the 'lambda' keyword (just as you use 'def' to define normal functions)

#Every anonymous function you define in Python will have 3 essential parts:
# 1. The 'lambda' keyword
# 2. The parameters (or bound variables)
# 3. The function body

#Moreover, a lamba is writeen in a single line of code and can also be invoked immediately

#Syntax:

#lambda p1, p2: expression

#Here p1 and p2 are the parameters which are passed to the lambda function. You can add as many or as few parameters as you need

#Example:
adder = lambda x, y: x+y
print (adder 1,2)

#Here we define a variable that will hold the result returned by the lambda function

#To Summarise Functions#:

#1. Functions are reusable blocks of code written to perform specific tasks
#2. Functions in Python are declared using the 'def' keyword
#3. 'def' is followed by the function name followed by the functions#s parameters. The function body contains the statements to be executed
#4. Functions can be called by their function name followed by brackets and parameters, if any
#5. Lambda functions are defined using 'lambda' keyword
#6. Lambda function can help shorten the code

###Operations on Numbers###

#Python provides numerous built-in functions which can be used to perform many complex operations

##pow()##
#The pow() function takes two numbers and returns the result of the first number raised to the power of the second
#But to use all the functions that we will be discussing we need to import a math module
#A module is an external Python file that contains functions that are used by other Python programmes
#To import a module, the import statement is used

import moduleName

#To access any function of the math module we write math.functionName()
#In case of pow:

import math
math.pow(4,3)

#This will return 4 raised to the power of 3 which is 64

##Floor and ceil functions##
#Floor and ceil functions are other widely used functions.
##math.floor() takes in a number as a parameter and returns the largest integer equal to or less than the number passed as the parameter

import math
a = math.floor(4.3)
b = math.floor(10.9)
print(a)
print(b)

#The output of the above code snippet will be
4
10

##math.ceil() takes in a number as a parameter and returns the smallest integer equal to or greater than the number passed as the parameter

import math
a = math.ceil(4.3)
b = math.ceil(10.9)
print(a)
print(b)

#The output of the above snippet will be:
5
11

##fabs() function
#fabs() function takes in one parameter and returns its absolute value
#An absolute value is the magnitude of a number irrespective of its sign, i.e +ve or -ve

a = math.fabs(10)
a = math.fabs(-10)
print(a)
print(b)

#The output of the above snippet will be 
10
10

##math.log()
#math.log() is used for finding the logarithm of a number
#math.log() can take either one parameter or two
#When one parameter is passed, it returns the natural logarithm of that number
#When two parameters are passed, it returns the logarithm of the first number to the base of the second number

import math
a = math.log(10)
b = math.log(10,2)
print(a)
print(b)

#The output of the above snippet will be:
2.3025850
3.3219280

##math.sqrt()
#math.sqrt() takes in a single parameter and returns the square root of the number

import math
a = math.sqrt(9)
b = math.sqrt(16)
print(a)
print(b)

#The output of the above code snippet will be
3.0
4.0

#The math modules consists of numerous other functions, which also includes trigonometric and hyperbolic functions

##A Note on Strings##
#A string enclosed within triple quotes ''' ''' can span multiple lines and all the whitespace will be included in the string.
#""" """ can also be used in place of ''' '''
num3 = '''this looks somewhat
different
it is really different'''

###String Functions###

##.capitalize() function
#It returns the string in Sentence case, ie with the first letter capitalized and the rest small.
#To use string functions we write:
str.functionName()
#where str is the string we want to manipulate

#E.g.
str = "here I Am"
str.capitalize()
#This is return `Here I am`. Take note that the value of str is still the same, capitalize() returns a new string.

##.count()
#A str.count() function returns the number of occurrences of the substring specified as the parameter.
str = "here I am"
str.count('e')
##str.count will return 2 because there are two 'e's in the str
#similarly,
str = "here I am"
str.count('am') #will return 1

##.find()
#A str.find() function returns the location of the first occurence of a substring passed in find() as a parameter if it exists in str
str = "here I am"
a = str.find('h')
print(a)
#The output of the above snippet will be:
0
#Similarly, str.find('I') will return `5`.
#Also, str.find('d') will return -1 because d is not found in the string

##str.join
#A str.join() function return the concatenated string of the sequence of strings passed to it.
#In this case, str contains the separator to be used while concatenating those strings.
str = " "
iter = ('I', 'am', 'awesome.')
a = str.join(iter)
print(a)
#The output of the above snippet will be 
I am awesome.
