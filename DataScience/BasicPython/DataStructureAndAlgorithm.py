##1. An array in python is called "list"
#index starts at 0
#random access is possible
#mutable
#supports multiple data type as an item

number = [10,23,34,100.4,"Jitu",'x',]
print(number[0])
number[0] = 20
print(number[0])

#index-wise
for i in range(len(number)):
    print(number[i])

#iterative
for i in number:
   print(i)

