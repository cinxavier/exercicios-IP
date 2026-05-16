matrix = [
  [1, 2, 3, 4, 5, 3, 5],
  [1, 2, 3, 4, 5, 3, 6],
  [1, 5, 3, 7, 4, 8, 3],
]

print(matrix)
def mexe(matrix):
  matrix[2][3] = "#"
  
mexe(matrix)
print(matrix)