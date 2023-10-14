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

###Lists###
#A list is a datastructure which is used to hold multiple values
#These values may or may not be of the same type
#Data structure is a format for storing data
#A list contains items separated by commas
#These items are enclosed within square brackets
#A variable can be used to store a list

list1 = [1,3,6,7,9]
list2 = [4,'hi',6,'me',78]

#The items in a list are identified using their positions
#These positions are known as 'indexes'
#Indexes start from 0

##Accessing data from lists
#The items in the list are accessed using their index numbers
#To access an item in the list we write the name of the list followed by the index ofd the item we want to access inside square brackets

print(list1[1]) 
#will display
3

#You can also access multiple itmes in a list
#To do so we need to specify the starting index and the ending index, separated by a colon
#Thus if we want to access the values of 3,6 and 7, we can write:

a = list1[1:4]

#And the output of the above snippet will be 
[4,5,6] #The first number is inclusive, the second number is exclusive

#To access all the items we can write the name of the list, or index all the elements explicitly:

list1 = [1,3,6,7,9]
list1

#To access items beginning from index 0, we can write:

list1[:5]

#When no index is specified before the colon, indexing starts at 0. To access the elements from index 1 till the end we can write:

list1[2:]

#When no index is specified after the colon, the indexing ends at the last element

##Updating data in Lists
#To update an item in a list, we will first access the item and then assign a new value to it

#For instance, consider a list:

list2 = [4,55,6,7,8,9,90]

#In order to update the value of the item at index 4 (which has a value 8), we write:

list2[4] = 88

#After which the updated list looks like [4,55,6,7,88,9,90]
#We can also add an item at the end instead of replacing the present ones

##To add an item at the end of the list we use the append() function

list2.append(150)

#This will add 150 at the end of the list and the updated list will look like:

[4,55,6,7,88,9,90,150]

#Similarly, repeatedly using append() you can add as many element you want in the list

##Deleting data in lists
#Just as we add items to the list, we can also remove them
#To delete items from the list we use `del` statement followed by the name of the list and the index in brackets

#Consider, we want to delete 4th item in list1 = [4,5,6,2,1]
#To do so, we write:

del list1[3]

#This will delete the item at index 3 (ie the 4th item) and return:
[4,5,6,1]

#We can use the remove() function in order to get the same result
#In remove() we need to specify the element which we wish to delete

list1 = [4,5,6,2,1]
list1.remove[5]
print(list1)

#The above snippet will remove 5 from the list and will display
[4,6,2,1]

##In summary, remove is used to eliminate specific values by their content,
#  while del is used to remove elements by their index in the list. 
# The choice between them depends on your specific requirements.

##Lists Summary
#A list is a data structure which can hold multiple values of different or same types
#We can add items to the list using the append() function
#Also we can update any value using the bracket notation and index of the item followed by a new value
#To delete any item, `del` statement can be used, simmilarly, the remove() function is also used to delete items from the list

###Tuples###
#A tuple is a data structure just like a list which is used to hold multiple values
#These values may or may not be of the same type
#But if it was exactly the same as a list then we wouldn't need it right?!

##Creating a tuple
#A tuple is a sequence of items separated by commas
#These items are enclosed within round brackets
#A variable can be used to store a tuple
#Tuple = (2,4,5,6,7,2)
#A tuple,like a list,can store values of different types
#tuple2 = (4,'hi',6,'me',78)

#Just like lists, items in tuples are also identified by indexes
#In tuples also, index starts from 0

tuple1 = (2,3,5,6,7,2)

#Thus in the tuple1 defined above, 2 is at index 0,5 is at index 2,and so on

##Accessing data from a tuple
#The values inside a tuple are accessed using their index numbers
#To access an item in a tuple we write the name of the tuple followed by the index of the
#item we want to access inside square brackets,just like we did in lists

#We can also access multiple subsequent items in a tuple the same way we do in lists
#To do so we need to use the starting index followed by a colon followed the index of the item #up to which we want to access the items

#To access all the items we write 

tuple1

#This will return (2,4,5,6,7,2)

#Similarly,to access items beginning from index 0, we can write:

tuple1[:5]

#Same for all items up until the end of the tuple:

tuple1[2:]

##Updating data from a tuple
#Unlike lists,tuples are immutable
#`Immutable` refers to the fact that the items in a tuple cannot be updated or deleted
#So,there is no update or deletions of items in tuples
#But we can update an entire tuple

#To delete a tuple we us `del` statement
#`del` is followed by the name of the tuple
#Thus to delete tuple1 we need to write:

 tuple1

##Tuple summary
#We learned that a tupleis very similar to a list
#The main difference is that we cannot update or delete items within a tuple
#However,we can delete the entire tuple using the `del` statement

###Dictionaries###
##What is a dictionary?
#Just like a traditional dictionary has words and their meanings,
#A Python dictionary is a data structure which contains data in the form of pairs of keys and values
#A key and value pair forms an item in the dictionary. A key is usually a string

##Creating a dictionary
#Items in a dictionary are separated by a comma. Note that the last item doesn't have a comma following it
#Keys and values are separated by a colon
#Items in a dictionary are enclosed within curly brackets

dic1 = {'name':'alfie','age':30,'hobby':'running'}

#dic1 is a dictionary that contains 3 items
#First one is 'name' with value 'alfie' etc.

##Accessing data from a dictionary
#The items in a dictionary are accessed using their keys
#To access an item in a dictionary we write the name of the dictionary followed by the key of the item
#we want to access inside square brackets

dict1['age']

#writing print(dict1) will display all of the items

##Updating data in a dictionary
#In a dictionary, we can either add a key-value pair or update an existing one
#To update an existing entry we need to first access the item and then assign a new value to it
#For instance:

dic1['name'] = 'abc'

#The name will be updated to the value 'abc'

##Adding a new item to a dictionary
#To add a new key-value pair to the dictionary, we can use a key which is not present in the dictionary and assign a value to it
#For instance, writing dic1['profession'] = 'pilot' will add a new key 'profession' with a value 'pilot' to dic1

##Deleting data in a dictionary
#In a dictionary, we can either remove an individual item or the entire dictionary

#To remove an individual item `del` statement is used followed by the name of the dictionary and the key inside square brackets

del dict1['name']

#The statement will remove the item with the key 'name' from the dictionary

#To remove the entire dictionary, `del` statement is used followed by the name of the dictionary

del dict1 #will delete the entire dictionary

#Instead of deleting the entire dictionary, we can also just remove all the items and empty the dictionary
#To do so, we need to use the clear() function
#Writing `dict1.clear()` will remove all items from dict1
#If we write `print(dict1)` after the clear statement, we will get {} as the output, indicating a dictionary with no items

##Dictionary Summary
#We learned that a dictionary is a data structure which contains keys and values separated by a comma and enclosed within curly braces
#To access any item in a dictionary we can use a dictionary name followed by key names inside square brackets
#To update an item we first access the item and assign it the value we want
#To delete an item we can use `del` followed by the dictionary name and key in brackets
#To remove all items we can use `clear()` function
#And to delete the entire dictionary we can use `del` followed by the dictionary name
