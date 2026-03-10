num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("num1: ", num1)
print("num2: ", num2)

num1, num2 = num2, num1

print("----------------------------")

print("num1: ", num1)
print("num2: ", num2)

# alternativa

var1 = input("Enter the first value: ")
var2 = input("Enter the second value: ")

print("var1: ", var1)
print("var2: ", var2)

temp = var1
var1 = var2
var2 = temp

print("----------------------------")
print("var1: ", var1)
print("var2: ", var2)