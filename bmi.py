import math
Kg = float (input("plese enter your weight"))
m = float (input ("please enter your height"))
BMI = Kg /(m*m)
print (BMI)

if BMI < 18.5:
    print("underweight")

if  18.5 < BMI < 24.9:
    print(" normal weight")

if  25 < BMI < 29.9:
    print("ower weight")

if 35 < BMI < 39.9:
    print("extrem obesity")   

