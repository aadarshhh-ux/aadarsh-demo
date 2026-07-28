"""#print("hello")
#print("My name is Aadarsh")
#name = "Aadarsh"
#age = 20
#price = 100.66
#old = True
#ad = None
#print("my name is ",name,"and my age is ",age,)
#print(type(name))
#print(type(age))
#print(type(price))
#print(type(old))
#print(type(ad))"""

#airthmatic oprations
"""a = 2
b = 3
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)#remainder
print(a**b)#power #a ki power b"""

#relational oprations
"""a = 33
b = 55
print(a==b) #answer is false
print(a!=b) #answer is true
print(a>b) #answer is false
print(a<b) #answer is true
print(a>=b) #answer is false
print(a<=b) #answer is true """

#assignment oprations
"""num = 20
num += 5 #num = num + 5
print( "num:",num)
num -= 5 #num = num - 5
print( "num:",num)
num *= 5 #num = num * 5
print( "num:",num)
num /= 5 #num = num / 5
print( "num:",num)  
num %= 5 #num = num % 5
print( "num:",num)
num **= 5 #num = num ** 5
print( "num:",num)"""

#logical oprations
"""print( not True) #answer is false
print( not False) #answer is true
a = 40 
b = 20
print(not (a>b ))
print(not (a<b ))
print((a>b ))
print( (a<b ))
val1 = True
val2 = False
print(val1 and val2) #answer is false
print(val1 or val2) #answer is true"""

#type conversion
"""a = int ("2")
b = 2.5
print(type(a))
print(a+b)"""

 #input function
"""name = input("Enter your name: ")
age = input("Enter your age: ")

print("My name is ",name,"and my age is ",age)
val = input ("enter some value :")
print(type (val),val)"""

# write a program to take two numbers from user and print their sum, difference, product, division and remainder
"""num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)
print("Remainder:", num1 % num2)"""

# WAP to input of a square and print its area 
"""side = float(input("enter side: "))
print("Area of the square:", side * side)"""

#WAP to input 2 floating point number & print their average
"""a = float(input("enter first number:"))
b = float(input("enter second number:"))
average = (a+b)/2
print("Average of two numbers:", average)"""

#WPA to input 2 int number a and b print True if a is greater than  or equal to b if not print false
"""a = int(input("enter number" ))
b = int(input("enter number"))
print (a>=b)"""

#for next line in print statement we can use \n
#for space we can use \t
"""a = "hii my name is aadarsh \nmy age is 20 "
b = "\nhii my name is aadarsh \t my age is 20 "
print(a,b)"""

# for adding two strings we can use + operator
#and for finding length of string we can use len() function
"""str1 = "hii my name is aadarsh"
str2 = " my age is 20"
final_str = str1 + " "+ str2
print(final_str)
length = len(final_str)
print("length of final string is:", length)"""

#to finde specific character in string we can use indexing
#for example if we want to find 1st character of string we can use index
"""str = "aadarsh dubey"
print(str[1])  # Output: a
str1 = " my age is 20 "
print(str1[3])  # Output: # it also print empty space because space is also a character"""

#slicing in string
#for example if we want to find 1st character of string we can use index
#also we have negative indexing in string
"""str = "aadarsh dubey"
print(str[0:3])  # Output: aad
print(str[8:len(str)]) # Output:  dubey # len(str) is used to find the length of string it will print till the end of string
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]
print(str[-5:-1]) # Output: ube # it will print from 5th last character to 1st last character"""

#string functions
"""str = "hii my name is aadarsh"
str1 = "my age is 30"
print(str.endswith("rsh")) # Output: True
print(str.startswith("hii")) # Output: True
print(str.capitalize()) # Output: Hii my name is aadarsh
print(str1.replace("30","20"))# Output: my age is 20
print(str1.find("age")) # Output: 3 # it will return the index of the first occurrence of the substring
print(str1.count("is")) # Output: 2 # it will return the number of occurrences of the substring"""


#WAP to input users name and print the length of the name
"""name = input("enter name")
print("length of name is ",len(name))"""

# if else statement
"""light = input("Enter the color of the traffic light (red, yellow, green): ")

if (light == "red"):
    print("Stop")
elif (light == "yellow"):
    print("Get ready to move")
elif (light == "green"):
    print("Go")
else:
    print("Invalid color")

age = int(input("Enter your age: "))
if(age >= 18):
    if(age>=90):
        print("you are too old to drive")
    else:
        print("you can drive")
else:
    print("you are too young to drive")"""


#WAP to check is a number entered by user is even or odd
"""int = int(input("Enter a number: "))
if (int%2 ==0):
    print("number is even")
else:
    print("number is odd")"""

#WAP to finde the greatest of 3 number entered by the user 
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a >= b) and (a >= c):
    print("The greatest number is:", a)
elif (b >= a) and (b >= c):
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)"""

#WAP to check if a number is a multiple of 7 or not
num = int(input("Enter a number: "))
if (num % 7 == 0):
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multiple of 7")
    

