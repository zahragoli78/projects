import math
name = input()
family = input()
a = float (input("please inter your first number:"))
b = float (input("please inter your secound number:"))
c = float (input(" please enter your third number:"))
avrage = (a + b + c ) / 3

if avrage >= 17 :
    print("great")

elif 17 > avrage >= 12 :
    print ("normal")

elif avrage < 12 :
    print ("fail !")
