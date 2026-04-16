# Querido e gentil monitor, por fins de maior qualidade de vida,
# sujiro que você copie esse código e cole no ÚNICO editor de código existente
# na atualidade, o VScode, para que possas usufruir do recurso de notação de aspas triplas
# e possa relembra, com facilidade, o que significa cada índice de cada lista, e manter suas madeixas
# em sua cabeça, não fique calvo por ler código mal diagramado
# assinado: Lady Elma Maria.

# ============================================== coleta
# variaveis
searching = True
missao = ["Capacitor de Fluxo", "Válvula de Vácuo", "Fragmento do Ponto-Zero"]
bonus = ["Escopeta Lendária", "Vira-Vira", "Peixinho-Dourado Mítico"]
lixo = ["Lata Enferrujada", "Bota Velha", "Cogumelo Mordido"]

coletados = []
"""
idx [0] = nome\n
idx [1] = quantidade\n
idx [2] = ordem de chegada
"""

while searching:
  item_achado = input()

  if item_achado == "Fim Da Coleta!":
    searching = False  # acaba o loop

  elif item_achado not in lixo:  # se n for lixo
    its_in_invent = False

    for item_coletado in coletados:
      if item_coletado[0] == item_achado:  # se o item tem registro
        item_coletado[1] += 1  # adiciona em quantidade
        its_in_invent = True  # e avisa que foi pego

    if not its_in_invent:  # se não foi pego antes
      coletados.append(
        [item_achado, 1, len(coletados) + 1]
      )  # adiciona item ao inventário

print("desordenados:", coletados)  # print
# ============================================== ordenação
for _ in coletados:
  for idx in range(len(coletados) - 1):
    atual = coletados[idx]
    prox = coletados[idx + 1]
    if atual[1] < prox[1]:
      coletados[idx], coletados[idx + 1] = (
        coletados[idx + 1],
        coletados[idx],
      )
    elif atual[1] == prox[1]:
      if atual[2] > prox[2]:
        coletados[idx], coletados[idx + 1] = coletados[idx + 1], coletados[idx]

print("ordenados:", coletados)  # print
# ============================================== contagem de missão
# variaveis
has_mission_item = False
pontos = 0

for item_coletado in coletados:
  if item_coletado[0] in missao:  # se estiver na lista de objetivo de missão
    has_mission_item = True  # está em objetivo de missão

# ============================================== pontuação
if has_mission_item:
  for item_coletado in coletados:
    if item_coletado[0] in missao:
      pontos += 30 * item_coletado[1]

    elif item_coletado[0] in bonus:
      pontos += 10 * item_coletado[1]

    else:
      pontos -= 5 * item_coletado[1]

    if pontos > 100:
      pontos = 100
    elif pontos < 0:
      pontos = 0

  print("pontos:", pontos)  # print
else:
  print("Nenhum item de missão coletado.")  # print

# ============================================== mapeamento
#  variaveis
n_lines = int(input())
n_cols = int(input())
matrix = []
"""
  [\n
    [ 1, 2, 3 ],\n
    [ 4, 5, 6 ],\n
    [ 7, 8, 9 ],\n
  ]
"""
radar = []
"""
  [\n
    [ "X", " . ", " . " ],\n
    [ " . ", " . ", " . " ],\n
    [ " . ", " . ", " . " ],\n
  ]
"""
radaring = True  # radareando...?
char_coods = [0, 0]
"""
 [0] = linha\n
 [1] = coluna
  a LINHA vem antes do COLUNA em todos os casos de acesso aos floats
 
"""
# criação da matrix
for line in range(n_lines - 1):
  inp_lines = input().split(" - ")
  for el in inp_lines:  # conversão de str pra float
    el = float(el)

  matrix.append(inp_lines)

# criação do radar
for line in range(n_lines):
  for char in range(n_cols):
    radar[line][char] = "."

radar[char_coods[0]][char_coods[1]] = "X" # marca do ponto de partida

while radaring:
  LINE = char_coods[0]  # eixo Y do personagem
  COLUMN = char_coods[1]  # eixo X do personagem

  highest_value = ["center", matrix[char_coods[0][1]]]
  """
    [ 0 ] = direção (str)
    [ 1 ] = valor (float)
  """

  #  validadndo arredores
  if matrix.index(matrix[LINE]) > 0:
    up_coords = [LINE - 1, COLUMN]
    if matrix[up_coords[0]][up_coords[1]] > highest_value[1]:
      radar[LINE][COLUMN], radar[up_coords[1]][up_coords[0]] = "^", "X"
      char_coods = up_coords

  if matrix.index(matrix[LINE]) < n_lines - 1:
    down_coords = [LINE + 1, COLUMN]
    if matrix[down_coords[0]][down_coords[1]] > highest_value[1]:
      radar[LINE][COLUMN], radar[down_coords[1]][down_coords[0]] = "v", "X"
      char_coods = down_coords

  if matrix[LINE].index(matrix[LINE][COLUMN]) > 0:
    left_coords = [LINE, COLUMN - 1]
    if matrix[left_coords[0]][left_coords[1]] > highest_value[1]:
      radar[LINE][COLUMN], radar[left_coords[1]][left_coords[0]] = "<", "X"
      char_coods = left_coords

  if matrix[LINE].index(matrix[LINE][COLUMN]) < n_cols:
    right_coords = [LINE, COLUMN + 1]
    if matrix[right_coords[0]][right_coords[1]] > highest_value[1]:
      radar[LINE][COLUMN], radar[right_coords[1]][right_coords[0]] = ">", "X"
      char_coods = right_coords

