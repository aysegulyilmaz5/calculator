print("Operation?")
print("1 : Sum")
print("2 : Sub")
print("3 : Div")
print("4 : Mult")

selection = input("Operation selection?")

num1 = int(input("First number :"))
num2 = int(input("Second number:"))


def sum(num1,num2):
  return num1 + num2

def sub(num1,num2):
  return num1 -num2

def mult(num1,num2):
  return num1*num2

def div(num1,num2):
  return num1 /num2


if selection == '1':
  print("Sum :" + str(sum(num1,num2)))
elif selection == '2':
  print("Sub : "+ str(sub(num1,num2)))

elif selection == '3':
  print(" Div : "+str(div(num1,num2)))

elif selection == '4':
  print("Mult : " +str(mult(num1,num2)))

else:
  print("Invalid selection")






