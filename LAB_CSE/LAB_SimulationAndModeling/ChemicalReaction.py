m1=0.025
m2=0.01
time=15.00
c1=[0]*200
c2=[0]*200
c3=[0]*200
c1[0]=50.0
c2[0]=25.0
t=0.0
delta=0.1
i=0
print("Time\t\tC1\t\tC2\t\tC3")
while t<=time:
    print(f"{t}\t\t\t{c1[i]}\t{c2[i]}\t{c3[i]}")
    c1[i+1]=round((c1[i]+(m2*c3[i]-m1*c1[i]*c2[i])*delta),2)
    c2[i+1]=round((c2[i]+(m2*c3[i]-m1*c1[i]*c2[i])*delta),2)
    c3[i+1]=round((c3[i]+2.0*(m1*c1[i]*c2[i]-m2*c3[i])*delta),2)
    i=i+1
    t=round((t+delta),2)
    if t>=2.0:
        delta=0.2
    if t>=6.0:
        delta=0.4


