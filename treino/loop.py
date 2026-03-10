num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
res = num1

while num1 < num2:
    num1 += 1
    res += num1

print("The sum of the numbers is: ", res)

