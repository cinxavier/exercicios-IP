# Querido e gentil monitor, por fins de maior qualidade de vida, hei-me de comentar o código.
# Ademais, sujirirvo-ei-me que vossa mercê copie esse código e cole no ÚNICO editor de código existente
# na atualidade, o VScode, para que possas usufruir do recurso de notação de aspas triplas
# e possa relembra, com facilidade, o que significa cada índice de cada adjacent_values, e manter suas madeixas
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
é uma lista de listas

idx [0] = nome\n
idx [1] = quantidade\n
idx [2] = ordem de chegada
"""

print("FASE 1:")
print("Marty McFly: Vamos buscar os Recursos que o Doc pediu.")

while searching:
  item_achado = input()

  if item_achado == "Fim Da Coleta!":
    searching = False  # acaba o loop
    print("Marty McFly: Nossa coleta termina aqui.")

  elif item_achado not in lixo:  # se n for lixo
    its_in_invent = False

    for item_coletado in coletados:  # faz varredura pelos itens coletados
      if item_coletado[0] == item_achado:  # se o item tem registro
        item_coletado[1] += 1  # adiciona em quantidade
        its_in_invent = True  # e avisa que foi pego

    # verifica se é item de missão
    if not its_in_invent:  # se não foi pego antes
      # adiciona item ao inventário
      coletados.append([item_achado, 1, len(coletados) + 1])

      if item_achado in missao:  # e caso seja um item de missão
        print("Marty McFly: Boa Embananado, estávamos precisando disso.")
    else:  # caso ja tenha sido pego antes
      if item_achado in missao:  # e caso seja um item de missão
        print("Marty McFly: Por via das dúvidas, vamos levar mais.")

    if item_achado in bonus:  # caso seja um item de bonus
      print("Marty McFly: Não podemos deixar uma raridade dessas pra trás né?!")
  else:  # caso seja lixo
    print(
      "Marty McFly: Pra que eu preciso disso? Só vai encher meu inventário."
    )
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

# ============================================== contagem de missão
# variaveis
has_mission_item = False

for item_coletado in coletados:
  if (
    item_coletado[0] in missao
  ):  # se estiver na adjacent_values de objetivo de missão
    has_mission_item = True  # está em objetivo de missão

# ============================================== pontuação
# variaveis
has_egnough_points = False
pontos = 0
if not has_mission_item:  # caso não tenha nenhum item de missão
  print(
    "Marty McFly: Infelizmente não encontramos nenhum dos objetivos, não poderemos continuar com a missão."
  )
else:  # caso tenha pelo menos um item de missão
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

  print(f"PONTUAÇÃO DA COLETA = {pontos}")
  if pontos < 30:
    print(
      "Marty McFly: Pontuação Insuficiente, não poderemos continuar com a missão."
    )
  else:
    has_egnough_points = True
# ============================================== mapeamento
if has_egnough_points:  # caso tenha pontos suficientes pra continuar
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
  char_coods = [0, 0]
  """
  [0] = LINHA\n
  [1] = COLUNA
    a LINHA vem antes do COLUNA em todos os casos de acesso aos floats
  
  """
  steps = 0  # distância percorrida pelo personagem
  radaring = True  # radareando...?

  print()
  print("FASE 2:")
  print(
    "Doc Brown: De onde estão vindo esses sinais de rádio-frequência dimensional? Eles formam uma matriz perfeita!"
  )
  # criação da matrix
  for _ in range(n_lines):
    inp_lines = input().split(" - ")
    for idx in range(len(inp_lines)):  # conversão de str pra float
      inp_lines[idx] = float(inp_lines[idx])

    matrix.append(inp_lines)

  # criação do radar
  for line in range(n_lines):
    new_line = []
    for char in range(n_cols):
      new_line.append(".")
    radar.append(new_line)

  radar[char_coods[0]][char_coods[1]] = "X"  # marca do personagem

  while radaring:
    LINE = char_coods[0]  # eixo Y do personagem
    COLUMN = char_coods[1]  # eixo X do personagem

    center_value = matrix[char_coods[0]][char_coods[1]]
    adjacent_values = []
    """
      [ 0 ] = direção (str)
      [ 1 ] = valor (float)
    """
    up_coords = 0
    down_coords = 0
    left_coords = 0
    right_coords = 0
    #  validadndo arredores
    if matrix.index(matrix[LINE]) > 0:  # verifica se é possível subir
      up_coords = [LINE - 1, COLUMN]  # registra as coordenadas acima

      if (
        matrix[up_coords[0]][up_coords[1]] > center_value
      ):  # verifica se o valor acima é maior
        adjacent_values.append(
          ["up", matrix[up_coords[0]][up_coords[1]]]
        )  # registro de valor
    # daqui pra baixo só repete o processo acima pra baixo, esquerda e direita, respectivamente
    if matrix.index(matrix[LINE]) < n_lines - 1:
      down_coords = [LINE + 1, COLUMN]

      if matrix[down_coords[0]][down_coords[1]] > center_value:
        adjacent_values.append(
          ["down", matrix[down_coords[0]][down_coords[1]]]
        )  # registro de valor
    if matrix[LINE].index(matrix[LINE][COLUMN]) > 0:
      left_coords = [LINE, COLUMN - 1]

      if matrix[left_coords[0]][left_coords[1]] > center_value:
        adjacent_values.append(
          ["left", matrix[left_coords[0]][left_coords[1]]]
        )  # registro de valor
    if matrix[LINE].index(matrix[LINE][COLUMN]) < n_cols - 1:
      right_coords = [LINE, COLUMN + 1]

      if matrix[right_coords[0]][right_coords[1]] > center_value:
        adjacent_values.append(
          ["right", matrix[right_coords[0]][right_coords[1]]]
        )  # registro de valor
    if not adjacent_values:  # se não tiver nenhum valor maior
      radaring = False  # termina o loop
    else:  # se existir um valor maior
      # bubble sort de cria
      for _ in adjacent_values:
        for idx in range(len(adjacent_values) - 1):
          atual = adjacent_values[idx][1]
          prox = adjacent_values[idx + 1][1]
          if atual < prox:
            adjacent_values[idx], adjacent_values[idx + 1] = (
              adjacent_values[idx + 1],
              adjacent_values[idx],
            )
      if adjacent_values[0][0] == "up":
        radar[LINE][COLUMN], radar[up_coords[0]][up_coords[1]] = "^", "X"
        char_coods = up_coords
      elif adjacent_values[0][0] == "down":
        radar[LINE][COLUMN], radar[down_coords[0]][down_coords[1]] = "v", "X"
        char_coods = down_coords
      elif adjacent_values[0][0] == "left":
        radar[LINE][COLUMN], radar[left_coords[0]][left_coords[1]] = "<", "X"
        char_coods = left_coords
      elif adjacent_values[0][0] == "right":
        radar[LINE][COLUMN], radar[right_coords[0]][right_coords[1]] = ">", "X"
        char_coods = right_coords
      steps += 1

  for line in radar:  # print do radar
    print("".join(line))

  print(
    f"Doc Brown: Os sinais vêm da posição [{char_coods[0]}][{char_coods[1]}]!"
  )
  print(
    f"Localização triangulada com sucesso após {steps} movimentos pela grade dimensional."
  )

  # ============================================== calculo do binário
  # eu decide fazer a conversão de binario na mão, o motivo: deu vontade
  # variáveis
  inp_bin = input()
  initial_int = 0  # número em formato decimal
  goal_int = 88
  num_of_operations = 0

  prev_bin = inp_bin
  print()
  print("FASE 3:")
  print("Doc Brown: Está quase tudo pronto para voltarmos para casa!")

  bin_holder = list(inp_bin)  # auxiliar para a inversão do binário
  # inversão da lista, pra converter bin -> int
  for idx in range(len(bin_holder)):
    last_idx = len(bin_holder) - idx - 1
    if idx >= last_idx:
      bin_holder[idx], bin_holder[last_idx] = (
        bin_holder[last_idx],
        bin_holder[idx],
      )
  inp_bin = "".join(bin_holder)  # volta a ser string

  # conversão do binário passado no input pra inteiro
  for idx in range(len(inp_bin)):
    if inp_bin[idx] == "1":
      initial_int += 2**idx

  # contagem das operações
  for curr_int in range(initial_int + 1, goal_int + 1):
    # holder do número atual que será usado para obter sua versão binária
    curr_int_holder = curr_int
    curr_bin = ""
    for _ in range(7):  # sempre serão 7 bits
      # trunca a casa decimal float -> int, a divisão retorna um float,
      # então é necessário truncar pra continuar a conversão |
      curr_int_holder = int(curr_int_holder)

      # conversão de int pra binário
      curr_bin = str(curr_int_holder % 2) + curr_bin
      curr_int_holder = curr_int_holder / 2

    for idx in range(7):
      if prev_bin[idx] != curr_bin[idx]:  # verificação das diferenças
        num_of_operations += 1
    prev_bin = curr_bin

  print("SISTEMA SINCRONIZADO!")
  print(
    f"Doc Brown: Marty, para acelerarmos de {initial_int} até 88 mph, o Capacitor teve que realizar {num_of_operations} trocas de estado nos bits de processamento!"
  )
  print("--- #1 VICTORY ROYALE: Bem-Vindos a 1985! ---")
