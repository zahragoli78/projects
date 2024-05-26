import math 
print ("hello to my calculator")
print ("+: sum")
print ("-: sub")
print ("*: mul")
print ("/: div")
print ("sin")
print ("log")
print ("cos")
print ("tan")
print ("cot")
print("!:factorial")
print ("sqrt")
print("please enter your choice:")
op = n = input ()
if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("please enter first number:"))
    b = float(input("plasee enter secound number:"))
else :
    a = float(input("please enter first number:"))
   
if op ==  "sin" or op == "cos" or op == "cot" or op == "tan":
    ( n * math.pi / 180)   
  
if op == "+":
    result = a + b

elif op == "-":
    result = a - b

elif op == "*":
    result = a * b

elif op == "/" :
    result = a / b

elif op == "sin" :
    result = math.sin(a)

elif op == "cos" :
    result = math.cos(a)

elif op == "log" :
    result = math.log(a)

elif op == "tan" :
    result = math.tan(a)

elif op == "cot" :
    result = math.cot(a)

elif op == "factorial" :
    result = math.factorial(a)

    print (result)
        





         

