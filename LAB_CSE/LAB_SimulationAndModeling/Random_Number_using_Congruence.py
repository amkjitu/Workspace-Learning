import matplotlib.pyplot as plt
import random
seed=int(input('Enter a seed: '))
number=seed
m=random.randint(1,100)
a=random.randint(1,100)
c=random.randint(1,100)
x=[]
for i in range(10000):
    if ((a*number+c)%m)!=0:
        number=(a*number+c)%m
        x.append(number)

print(x)
plt.scatter(range(10000),x)
plt.grid()
plt.show()