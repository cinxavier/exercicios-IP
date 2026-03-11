def s(a,b):
  print(a, b)
  return b

array = [1,2,3,4]

array.sort(key=s)

print(array)
