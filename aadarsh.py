"""print("hello")
print("My name is Aadarsh")
name = "Aadarsh"
age = 20
price = 100.66
old = True
ad = None
print("my name is ",name,"and my age is ",age,)
print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(ad))"""

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
"""num = int(input("Enter a number: "))
if (num % 7 == 0):
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multiple of 7")"""


#list in python
"""students = ["Aadarsh", "Rohit", "Sakshi", "Arjun"]
print(students[1]) # Output: Rohit
students[0] = "Aaditya" # changing the value of the first element , Replacing the main value and adding new value
print(students) # Output: ['Aaditya', 'Rohit', 'Sakshi', 'Arjun']

list1 = [3, 1, 2, 5, 4]
list2 = [ 9, 8, 7, 6]
list3 = ["apple", "cherry", "banana"] # list also applicable for string
list1.append(6) # adding an element to the end of the list
print(list1) # Output: [3, 1, 2, 5, 4, 6]
list1.sort() # sorting the list in ascending order
print(list1) # Output: [1, 2, 3, 4, 5, 6]
list1.reverse() # reversing the list it mean not asecnding or descending it starts from backward
print(list1) # Output: [6, 5, 4, 3, 2, 1]
list2.sort(reverse=True) # sorting the list in descending order 
print(list2) # Output: [9, 8, 7, 6]
list3.sort() # sorting the list in ascending order
print(list3) # Output: ['apple', 'banana', 'cherry']
list3.reverse() # reversing the list
print(list3) # Output: ['cherry', 'banana', 'apple']
list2.insert(2, 10) # inserting an element at a specific index
print(list2) # Output: [9, 8, 10, 7, 6]
list2.remove(8) # removing an element from the list
print(list2) # Output: [9, 10, 7, 6]
list2.pop(1) # removing the element at index 1 from the list
print(list2) # Output: [9, 10, 7]   """


#tuples in python
"""tup = (1, 2, 3, 4, 5, 5, 5)
tup1 = (1,) #single element tuple should have a comma after the element
print(type(tup)) # Output: <class 'tuple'>
print(tup[2]) # Output: 3
print(tup1) # Output: (1,)
print(tup.index(5)) # Output: 4 # it will return the index of the first occurrence of the element
print(tup.count(5)) # Output: 3 # it will return the number of occurrences of the element"""

#WAP to ask the user to enter name of their 3 favorite movies & store them in a liste
"""a = input("enter your first favorite movie: " )
b = input("enter your second favorite movie: ")
c = input("enter your third favorite movie: ")
movies = [a, b, c]
print(movies)"""

#WAP to check is a list contains a palindrome of elemnets 
"""list1 =[1,2,3,2,1,]


copylist1 = list1.copy()
copylist1.reverse()

if(copylist1 == list1):
    print("palindrome")
else:
    print("not")"""

#WAP to count the number of students with "A" grade in the following tuple ["C","D","A","A","B","B","A"]
"""grade = ["C","D","A","A","B","B","A"]
print(grade.count("A"))"""

#store the above values in a list & sort them from "A" to "D"
"""list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)"""

#Dictionary in Python
"""dict = {
    "name": 'aadarsh',
    "sub": ['py',"java",'c'],
    "topic":("dic","set"),
    "age" : 20,
    22.2 : 22.5

}
print(type(dict)) 
print(dict["name"])#it will print only name from dictionary
dict["name"] = "adarshh"
dict["age"]  = '21'
dict["surname"] = "dubey"
print(dict)

null_dict ={}
print(null_dict)"""

#nested dictionary
student = {
    "name " : "aadarsh",
    "subject" : {
        "phy": 33,
        "chem": 44,
        "math": 55,
    }

}
#dictionary method
"""print(student)
print(student["subject"])#for only subject
print(student["subject"]["math"])# for math inside the sub
print(list(student.keys()))#will returns all keys #list will convert it into a list type
print(student.values())#eill returns all the values
print(student.items())#it eill returns in the form of pairs

#print(student["name2"]) #error
print(student.get("name2")) # no error
student.update({"city": "ashta"})
print(student)"""

#set in python
"""set1 = {1,2,3,4,"hello", 5, 5 ,"hello "} #it will never print in order #it will never print aney thing again
collection = set() #for empty set
print(set1)
print(len(set1))#ans is 7 repitted words are not included
collection.add (7) #to add somtion in aney set
set1.remove(5)#to remove somthing
print(collection)
set1.pop() #poprendom value
set1.clear()#willl clear all elemnt and make the set empty
print(set1)"""

#union and intersetion in set 
"""set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2)) #it will print {1,2,3,4,5}
print(set1.intersection(set2))#it will return {3}"""

#store following words meaning in a python dictionary [table  : "a piece of furniture","list of facts &figures"][cat:"a samall animal"]
"""dict = {
    "cat" : 'a samll animal',
    "table":['a pieace of furniture','list of fscts & figures']
}
print(dict)"""

#loop
"""i = 1
while i <=5:
    print("hello",i)
    i+=1
print ("loop ended")"""

#print number 1 to 100 with the help of loop
"""i = 1
while i <= 100: # stoping conditon
    print(i)
    i+=1"""

#print the number for 100 to 1 
"""i = 100
while i>=1: #stoping condition
    print(i)
    i-=1"""

#print the multiplication table of a number n=3
"""i = 1
while i<=10:
    print(3*i)
    i+=1"""

#pr::int the elements of the following list using a loop [1,4,9,16,25,36,49,64,81,100]
"""num = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(num):
    print(num[idx])
    idx +=1"""

"""num = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i < len(num):
    if num[i] == x:
        print("found", i)
        break
    i += 1"""

#break statument
"""i = 1
while i <= 5:
    print(i)
    if (i == 3):
        break   #loop will end when i is 3 
    i += 1

print('loop end')"""

#continue statment
"""i = 0 
while i <= 5:
    if(i == 3):
        i += 1
        continue #it will skio the current iteration and move to the next iteraton
    print(i)
    i += 1"""

#for loop
"""num = [1,2,3,4,5,6,7,8,9,10]

for val in num :
    print(val)"""

#for loop with else
"""str = "aadarsh dubey"

for char in str:
    print(char)
else:
    print("loop ended") """   

#for loop with brak
"""str = "aadarsh dubey"
for char in str:
    if char == "d":
        print("d is found")
        break
    print(char)
else:
    print("loop end") """   

# print the elements of the following list using a for loop [1,4,9,16,25,36,49,64,81,100]
"""num = [1,4,9,16,25,36,49,64,81,100]
for val in  num :
    print(val)"""

#search for a number x in this tuple using loop (1,4,9,16,25,36,49,64,81,100)
"""num = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter number"))
for i in num:
    if i == x:
        print("found")
        break
    else:
        print("not found")"""

# range function in python
"""seq = range(10) #it will generate a sequence of numbers from 0  to 9

for i in seq:
    print(i)"""

"""for i in range (10): # range(stop)
    print(i)"""

"""for i in range (1 ,10): #range(start,stop)
        print(i)"""

"""for i in range (1,10,2): #range(start,stop,step)
    print(i)"""

#print the multiplication table of a number n
"""n = int(input("enter number"))
for i in range(1,11):
    print(n*i)"""

#pass statement
"""for i in range (10):
    pass #it will do nothing it is used as a placeholder

print("aadarsh")"""

#wap to find the sum for natural number
n = 5 

sum = 0 
for i in range(1,n+1):
    sum += i


print ("total sum", sum)








