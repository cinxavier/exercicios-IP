num1 = int(input("Enter the first number: "))

times = int(input("times: "))

res = 0
for i in range(times):
    res += num1
print("The result is: ", res)

# var = int(input("num"))
# print(var)

while num1 < times:
    num1 += 1
    res += num1