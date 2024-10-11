#DNA no. 1 er dhorgho = 100mm, DNA no. 2 er dhorgho = 10mm
Length_of_DNA_1 = 100  
Length_of_DNA_2 = 10

Sum_of_DNA = Length_of_DNA_1 + Length_of_DNA_2 

print( "Sum of DNA: " + str(Sum_of_DNA) ) # "110"

ave_of_DNA =  (Sum_of_DNA/2)

print("Average of DNA: " + str(ave_of_DNA))

number = [ 1,2,3,4,5 ]
sum = 0
for x in number:
    sum = sum + x
print(sum)

def sumfectory(number):
    sum = 0
    for x in number:
        sum = sum + x
    return sum

numbermy = [ 1,2,3,4,5,6,19,23,434,4353,53,53,53,53,53,53,5,35 ]
print( sumfectory(numbermy) )







