import math as mat
import matplotlib.pyplot as plt

v = 100.0; angle = 0; theta = 0; delv = 0; pi = 22.0/7.00
m = 30.0; c = 0.001; delt = 0.01; g = 9.8; x = 0.0; y = 0.0
delx = 0.0; dely = 0.0; dtheta = 0.0; xx =0.0; yy = 0
vel = []; rangee = [None]*6

m = float(input("Enter the value of mass m: "))
print()
mass = "Mass of the projcetile = {} Kg".format(m)
print("{:^80}".format("RANGE TABLE"))
print("{:^80}".format(mass))
print("{:^80}".format("Release Velocity (m/sec.)"))
print("{:^79}".format("_________________________________________________________________________________"))
print("{:<12}{:^12}{:^12}{:^12}{:^12}{:^12}{:^12}".format("Release Angle","100","110","120","130","140","150"))
print("{:^79}".format("_________________________________________________________________________________"))

for i in range(10+1):
    #angle = 30.0+(i*10)
    angle = 30.0+(i*5)
    for j in range(5+1):
        v = 100.0+(j*10.0)
        x = 0.0; y = 0.0001
        theta = angle * (pi/180.0)
        while(y>=0.0):
            delv = (-g*mat.sin(theta)-c*v*(v/m))*delt
            dtheta = -g*mat.cos(theta)*(delt/v)
            delx = v*mat.cos(theta)*delt
            dely = v*mat.sin(theta)*delt

            v = v + delv
            theta = theta + dtheta
            x = x + delx
            y = y + dely
        rangee[j] = round(x,2)
    print("{:^12}".format(angle),end = '')
    for k in range(5+1):
        print("{:^12}".format(rangee[k]),end = '')
    print()


