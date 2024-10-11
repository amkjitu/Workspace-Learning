import math, random
import math

n = int(input("Enter the number of OTPs you want to Generate: "))

OTPlist = []
def generateOTP(n) :
    digits = "0123456789"
    #OTP = ""
    for j in range(n):
        OTP = ""
        for i in range(4) :
            OTP += digits[math.floor(random.random() * 10)]
        OTPlist.append(OTP)
    return OTPlist

generateOTP(n)
print("{:^5}{:^15}".format("No.","OTP"))
print("----------------------")
for i in range(n):
    print("{:^5}{:^15}".format(i+1,OTPlist[i]))

