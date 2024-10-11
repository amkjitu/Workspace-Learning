#This is single line comment
''' this is multi line comment '''

#Output Syntex: print('message')
print("Hello Python!")

#Input Systex: input()
name = input()
print("Hello {}".format(name))

'''
#int
i = 10
print(i)
#type conversion
ii = float(10)
print(ii)

#double/float
j = 1.3
print(j)
#type conversion
jj = int(1.3)
print(jj)

#char
charA = 'A'
print(charA)

#Tuple assigment
IP,Port,DNS = 192,80,"jitu.com"
print("IP :",IP, " Port :",Port, " DNS :",DNS)
'''


###There are many sequiences in PY : 
#0. String "Strings are immutable"
#1. List [List are mutable]
#2. Tuple (Tuples are immutable)
#3. Dictionary {Dictionary are mutable}
#4. Set ()

##strings are immutable in python
'''
#string
strName = "MyNameIsJitu"
print(strName)

#strings are immutable: strings can not be modified
#strName[0] = 'Y' #error occurs  'str' object does not support item assignment

#string[index]
print("strName[0] : "+ strName[0])
'''

##Array which is called "List" in python
'''
#List uses "[]"
#Lists are changable or can be modifed
ArrNum = [1,     3,     2,     4]
#                 [0]   [1]   [2]   [3]   ascending   indexing
#                 [-4] [-3] [-2] [-1]  descending indexing

#printing index wise ascending
print(ArrNum[0]) 
print(ArrNum[1])
print(ArrNum[2])
print(ArrNum[3])

#printing index wise descending
print(ArrNum[-4])
print(ArrNum[-3])
print(ArrNum[-2])
print(ArrNum[-1])

#printing in a range
print(ArrNum[:]) # all [start:end]  default[0:n-1]
print(ArrNum[:2]) # 0 - upto 2; [0],[1]
print(ArrNum[2:]) # 2 - upto 3; [2],[3]
print(ArrNum[1:3]) # 1 - upto 3; [1],[2]
print(ArrNum[1:4]) # 1 - upto 4; [1],[2],[3]
print(ArrNum[1:5]) # 1 - upto n; [1],[2],[3]
print(ArrNum[::]) # all [start:end:step]  default[0:n-1:1]
print(ArrNum[0:2:]) #  0 - upto 2; [0],[1] step: 1
print(ArrNum[0:4:2]) #  0 - upto 2; [0],[2] step: 2
print(ArrNum[0:4: -1]) #  3 to 0; [3],[2],[1],[0] step: -1 means reverse ordered index


#ascending sort
ArrNum.sort() #returns none
print(ArrNum[:]) # all 

#descending sort
ArrNum.sort(reverse = True) #returns none
print(ArrNum[:]) # all

New_sorted = sorted(ArrNum) #returns [New_sorted] list without effecting [ArrNum]

#deleting index 0
del ArrNum[0]
print(ArrNum[:])

#adding a element
ArrNum.append(10)
print(ArrNum[:])

#adding multiple elements
ArrNum.extend([20,30]) #ArrNum.append(20) is also used
print(ArrNum[:])
print("Length of the ArrNum :",len(ArrNum)) #length of the ArrNum


#List of List(two dimensional list)
ContactList = [[1,2],[3,4]]
print(ContactList[0][0]) #prints 1
print(ContactList[0][1]) #prints 2
print(ContactList[1][0]) #prints 3
print(ContactList[1][1]) #prints 4

#Iterating list of list using for loop
for row in ContactList:
    for cell in row:
        print(cell)
     

#Iterating list of list using for loop enumerate
for indexi,row in enumerate(ContactList):
    for indexj,col in enumerate(row):
        print(ContactList[indexi][indexj])
        


#Array of string 
Names = ["Jitu","Titu","Joti","Moti"]

#printing index wise
print(Names[0])
print(Names[1])
print(Names[2])
print(Names[3])

#printing index wise ascending 
Names.sort()
print(Names[0])
print(Names[1])
print(Names[2])
print(Names[3])

#deleting index 0
del Names[0]
print(Names[:])

#adding a element
Names.append(10)
print(Names[:])

#adding multiple elements
Names.extend(["Eshita","Khan"]) #Names.append() is also used
print(Names[:])
print("Length of the ArrNum :",len(Names)) #length of the Names

#Joining two lists : List of lists
ListOfNumName = [ArrNum,Names] #List ArrNum, Names
print(ListOfNumName)

#Iterating over Lists Using Enumerate
number = [10,20,30,40]
for index, x in enumerate(number):
    print("index: {}, value: {}".format(index,x))

#List Comprehensions
NaturalNumber = [x for x in range(10)]
print(NaturalNumber)

EvenNaturalNumber = [ x for x in range(10) if (x%2 == 0) ]
print(EvenNaturalNumber)
'''





##Arrays can be of  "Tuple" in python
'''
#Tuple uses "()"
#Tuples are not changable or  can't be modifed : can't append, can't delete elements  

#a tuple ArrNum1
ArrNum1 = (11,51,33)
print(ArrNum1)

#Assignment invalid for Tuple
#ArrNum1[0]=12
#print(ArrNum1)

#Deletion invalid for Tuple
#del ArrNum1[1]
#print(ArrNum1)

#a tuple ArrNum4
ArrNum4 = (65,3,78)

#List of tuples 
ListOfNum2AndNum4 = [ArrNum1,ArrNum4]
print(ListOfNum2AndNum4)

#Tuple of tuples 
TupleOfNum2AndNum4 = (ArrNum1,ArrNum4)
print(TupleOfNum2AndNum4)

#Tuple containing one string only
ArrNum2 = ("22,43,33")
print(ArrNum2)

#List using split () function
ArrNum3 = ("22,43,33".split(','))
print(ArrNum3)

#Tuple assignment with split() function
N1,N2,N3 = ("100.200.300".split('.'))
print(N1,N2,N3)
'''


##Arrays can be of  "Dictionary" in python
'''
#Dictionary uses "{}"
#Dictionary uses keys and value
#Syntex : DicName = {'key' : "value", so on}
#Dictionaries are changable or  can  be modifed : can be appended, can be deleted elements  

#A Dictionary Student
Student = {'Name' : "Jitu", 'ID' : 28, 'Regular' : True}

print(Student['Name'])
print(Student['ID'])
print(Student['Regular'])

#Assignment valid for Dictionary
Student['Name'] = "Eshita"

print(Student['Name'])
print(Student['ID'])
print(Student['Regular'])

#Iteration over Dictionary using for loop
prime = {'firstPrime':2, 'secondPrime':5, 'thirdPrime':7, 'fourPrime':11}
for n in prime:
    print(n,prime[n])

#Deletion valid for Dictionary
del Student['Regular']
print(Student)

#Lists in Dictionary 
Employee = {'Department' : "Admin", 'Staff' : ['Jitu','Habib']}
print(Employee['Staff']) # prints ['Jitu','Habib']
print(Employee['Department']) # prints Admin
print(Employee) # prints {'Department': 'Admin', 'Staff': ['Jitu', 'Habib']}

print(Employee['Staff'][0]) #prints Jitu
print(Employee['Staff'][1]) #prints Habib

#Initially empty Dictionary
Day = {}
Day['One'] = "Friday"
Day['Two'] = "Saterday"
Day['Three'] = "Monday"
Day['Four'] = "Tuesday"
Day['Five'] = "Wednessday"
print(Day['Five'])
print(Day)
print(Day.get('One'))
print(Day.get('Saterday'))

#Iterating over the Contents of a Dictionary
file_count = {"jpg": 10, "txt":14, "csv": 2, "py": 23}
print(file_count)
#for file_format,file_count in file_count.items(): # dictionary.items() returns touple with key,value pair
#    print("There are {} files with the .{}".format(file_count,file_format))
#for file_format in file_count.keys(): # dictionary.keys() returns only keys
#   print("There are {}".format(file_format))
for file_count in file_count.values(): # dictionary.keys() returns only keys
    print("There are {} files".format(file_count))
'''

##set()
'''
#A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.
#Since sets are unordered, we cannot access items using indexes like we do in lists.
#set uses "{}"
#set uses only value
#Syntex : setName = {value1,value1,..}
#sets are changable or  can  be modifed : can be appended, can be deleted elements  

#set initialization 1
naturalNumberSet1 = {5,5,1,2,3}
print(naturalNumberSet1)

#set initialization 2
naturalNumberSet2 = set()
naturalNumberSet2.add(1)
naturalNumberSet2.add(3)
naturalNumberSet2.add(2)
naturalNumberSet2.add(2)
print(naturalNumberSet2)

#deletion in set
naturalNumberSet2.remove(2)
print(naturalNumberSet2)

#iterating set using for loop 
for number in  naturalNumberSet1:
    print(number)

#iterating set using for loop and enumerate
for number in  enumerate(naturalNumberSet2):
    print(number)

#Getting set from a list
LetterList = ['a', 'a', 'b', 'd', 'c', 'c']
print(LetterList)
LetterSet = set(LetterList)
print(LetterSet)
'''

##frozenset()
'''
#A Frozen set is an unordered collection data type that is iterable, immutable and has no duplicate elements.
#frozensets are not changable or  can not  be modifed : can not be appended, can not be deleted elements  

oneDozen =  [1,2,3,4,4]
oneDozenSet = frozenset(oneDozen)
print(oneDozenSet)

#frozenset can not be appended
#oneDozenSet.add(2)

#frozenset can not be deleted
#oneDozenSet.remove(2)
'''



'''
##Loops in PY : for , while
#for loop

#List
even = [2,4,6,8]

for n in range(len(even)):
    print(even[n])

for n in even:
    print(n)

i=0;
while i<4: 
    print(even[i])
    i += 1

#Tuple
odd = (1,3,5,7)
for no in odd:
    print(no, end = " ")
print()

i=0;
while i<4: 
    print(odd[i])
    i = i + 1
print()

'''

'''
##range function
#Syntex1: range(start : stop : step) here stop is upto
#Syntex2: range(start : stop) here stop is upto, step = 1
#Syntex3: range(stop) here stop is upto, start = 0, step = 1
#NOTE: "range()" is not valid because it trends to infinite loop

#range function in list
print("range function in list")
print(list(range(1,10,2)))
print(list(range(1,10)))
print(list(range(10))) #atleast one argument is mendatory which indicates the stop value and start = 0, step = 1 by default

#range function in list
print("range function in tuple")
print(tuple(range(1,10,2))) # start : 1, stop : upto 10, step/increment 2
print(tuple(range(1,10))) # start : 1, stop : upto 10
print(tuple(range(10))) #atleast one argument is mendatory which indicates the stop value and start = 0, step = 1 by default

#same kaj ta dict e korte gesi wrong khaisi

#A Simple total price calculation using dictionary and for loop
price = {'amm': 80, 'jamm': 76, 'lichu': 999}
quantity = {'amm': 8, 'jamm': 7, 'lichu': 1.3}

Tcost = 0
for x in price :
    Tcost = Tcost + (price[x]*quantity[x])
print("Total cost: ", Tcost)
'''

'''
##funciton
#return void 
def addition ():
    print("A + B = " , 4+5)
#calling
addition()

#return int 
def Addition (a,b):
    x = a
    y = b
    sum = x+y
    return sum
#calling
SumOfAB = Addition(2,3)
print(SumOfAB)

#return (int,int) using tuple
def AddMul (a,b):
    x = a+b
    y = a*b
    return x,y
#calling
AddMulOfAB = AddMul(2,3)
print(AddMulOfAB)

#A function number of even number 
def CountEven (n):
    Ceven = 0
    for x in range(n):
        if x%2==0 :
            Ceven+=1

    return Ceven
#calling
NoOfEvens = CountEven(10)
print("Total Even Number : ", NoOfEvens)
'''

'''
#A recursive function will usually have this structure:
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
'''

'''
###OOP###
##class and object

#Below class has empty body
class Apple:
    pass

#Below class has body with instance vairables and method
class Car:
    brand = ""
    color = ""
    mileage = 45
    def getSpeed(self):
        return self.mileage


#First create the object of the class
myCar = Car()
myCar.brand = "Mazda"
myCar.color = "Blue"
myCar.mileage = 10

print("My car is {} in {} color with {} mileage".format(myCar.brand,myCar.color, myCar.mileage))
print(myCar.getSpeed())


## class, object, method and constructor
#Below class has body with instance vairables, method, a constructor and a special method __str__ 
#And the documentation of the classes and methods are done using """docstring"""
class Pen:
    """This is class of Pen. Pen class has brand,color and duration"""
    brand = ""
    color = ""
    duration = 0
    def __init__(self,brand,color,duration): #constructor
        """Constructor takes brand,color and duration"""
        self.brand = brand
        self.color = color
        self.duration = duration
    def __str__(self): #special method
        """The special method ___str___ used to print the whole object as a string format"""
        return "Pen : {}, Color: {}, Duration: {}".format(self.brand,self.color,self.duration)
    def getlifetime(self): #method
        """This is a life time of the pen"""
        return self.duration*20

mypen = Pen("High School","Green",30)
print("My pen is {} and color is {} and used {} days".format(mypen.brand,mypen.color,mypen.duration))
print("But it's duration was {} days".format(mypen.getlifetime()))
print(mypen)

help(mypen)
'''

##Inheritance
'''
#parent class
class Person:
    name = ""
    age = 0
    gender = ""
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def walk(self):
        return "{} is walking".format(self.name)

#child class Student extending Person
class Student(Person):
    profession = "student"
student = Student("jitu",23,"male")
print("Name: {}, Age: {}, Gender: {}, Profession: {}".format(student.name,student.age,student.gender,student.profession))
print(student.walk())
'''

'''
###File
#Syntex: file_object  = open("filename", "mode") 
#Here,
#filename: gives name of the file that the file object has opened.
#mode: attribute of a file object tells you which mode a file was opened in.
#   Mode	            Description
#     'r'	          This is the default mode. It Opens file for reading.
#     'w'	          This Mode Opens file for writing.
#                       If file does not exist, it creates a new file.
#                       If file exists it truncates the file.
#     'x'	          Creates a new file. If file already exists, the operation fails.
#     'a'	          Open file in append mode.
#                       If file does not exist, it creates a new file.
#     't'	          This is the default mode. It opens in text mode.
#     'b'	          This opens in binary mode.
#     '+'	          This will open a file for reading and writing (updating)
#NB: It is always safe to close the file after open

##Creating file 'name.txt'
file = open('name.txt','w')
for line in range(10):
    ##writing to file
    file.write("This is line %d\n"%(line+1))
file.close()

##appeinding to file
file = open('name.txt','a')
file.write("This is last line")
file.close()

##reading from file
file = open('name.txt','r')

#reads the file in a string format
nametxt =  file.read()
print(nametxt)

#reads the file in a list of strings format. list is created by new lines (\n)
file.seek(0) # after reading file from above the pointer points at the last position. So it must be seek to 0 to read the lines  
nametxtline =  file.readlines()

print(nametxtline)

##Ereases the text file
#open('name.txt','w').close()
'''






