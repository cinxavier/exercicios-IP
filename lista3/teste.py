matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]
char_coods = [0, 2]

radar = matrix.copy()

n_lines = len(matrix)
n_cols = len(matrix[0])

for line in range(n_lines):
  for char in range(n_cols):
    radar[line][char] = "."

radar[char_coods[1]][char_coods[0]] = "X"



def print_matrix(matrix):
  for line in matrix:
    for char in line:
      print(char, end=" ")
    print()

while True:
  print_matrix(radar)

  inp_direction = input()

  COLUNA = char_coods[0]  # eixo X do personagem
  LINHA = char_coods[1]  # eixo Y do personagem

  up_coords = 0
  down_coords = 0
  left_coords = 0
  right_coords = 0

  if matrix.index(matrix[LINHA]) > 0:
    up_coords = [COLUNA, LINHA - 1]

  if matrix.index(matrix[LINHA]) < n_lines - 1:
    down_coords = [COLUNA, LINHA + 1]

  if matrix[LINHA].index(matrix[LINHA][COLUNA]) > 0:
    left_coords = [COLUNA - 1, LINHA]

  if matrix[LINHA].index(matrix[LINHA][COLUNA]) < n_cols:
    right_coords = [COLUNA + 1, LINHA]

  if inp_direction == "w":
    if up_coords != 0:
      radar[LINHA][COLUNA], radar[up_coords[1]][up_coords[0]] = "^", "X"
      char_coods = up_coords
  elif inp_direction == "s":
    if down_coords != 0:
      radar[LINHA][COLUNA], radar[down_coords[1]][down_coords[0]] = "v", "X"
      char_coods = down_coords
  elif inp_direction == "a":
    if left_coords != 0:
      radar[LINHA][COLUNA], radar[left_coords[1]][left_coords[0]] = "<", "X"
      char_coods = left_coords
  elif inp_direction == "d":
    if right_coords != 0:
      radar[LINHA][COLUNA], radar[right_coords[1]][right_coords[0]] = ">", "X"
      char_coods = right_coords