from prettytable import PrettyTable


mytable=PrettyTable(["Combination Distribution(i)","Observed Distribution(Oi)","Expected(Ei)","(Oi-Ei)^2/Ei"])


O=[3075,4935,1135,695,105,54,1]
E=[3024,5040,1080,720,90,45,1]

s=["Five different digits","Pairs","Two-pairs","Three of a kind","Full houses","Four of a kind","Five of a kind"]

sum=0

crit_value=16.8

for i in range (len(O)):
    z=((O[i]-E[i])**2)/E[i]

    sum+=z

    mytable.add_row([s[i],O[i],E[i],z])


print(mytable)

print("sum = ",sum)

if sum<= crit_value:
    print("answer is accepted")
else:
    print("answer is rejected")