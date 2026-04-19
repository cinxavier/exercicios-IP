# por se tratar de uma matriz, será usada a mesma lógica da questão anterior.
# o sistema de busca por palavras vai ser como o último algorítimo de busca pelo maior número.


# variaveis
n_lines = int(input())
n_columns = int(input())
matrix = []
"""
  [0] = linha
  [1] = coluna
"""
for line_idx in range(n_lines):
  line = list(input())
  matrix.append(line)

username = input()
SPECIAL_atts = input().split("-")
"""
  [0] = força\n
  [1] = percepção\n
  [2] = resistência\n
  [3] = carisma\n
  [4] = inteligência\n
  [5] = agilidade\n
  [6] = sorte
"""
secret = input()

# ========================== setup
for idx in range(len(SPECIAL_atts)):  # cenversão dos atributos para inteiro
  SPECIAL_atts[idx] = int(SPECIAL_atts[idx])

print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n")
print(f"USER {username} LOGGED IN SUCCESSFULLY\n")

# ========================== verificação do nome
if "Lucy" in username:
  print(
    "NORM: Minha irmãzona nunca mais foi a mesma depois que saiu do Vault... Será que ela ainda lembra como mexer em computadores ou a radiação derreteu o cérebro dela de vez?\n"
  )
elif "Maximus" in username:
  print(
    "NORM: Ah, então é o Maximus... Só porque chega com uma armadura brilhando ele acha que pode ficar com minha irmã? Vamos ver se por dentro dessa lata existe cérebro.\n"
  )
  SPECIAL_atts[4] -= 2  # inteligência -2
elif "Ghoul" in username or "Necrótico" in username or "Cooper" in username:
  print(
    "NORM: Cooper Howard, o astro de cinema, virou isso aí? A Wasteland não perdoa ninguém... nem celebridade.\n"
  )

is_name_valid = True
if "Norm" in username:
  print(
    "NORM: Teste? Pra mim? Por favor. Eu já sou a mente mais brilhante do Vault 33.\n"
  )
  is_name_valid = False

# ========================== validação dos atributos
is_atts_valid = False

if is_name_valid:  # se o
  running_loop = True

  while running_loop:  # loop pra a verificação dos atributos
    invalid_att_found = False  # variável de controle para saber se um atributo inválido foi encontrado

    for att in SPECIAL_atts:
      if (
        not invalid_att_found
      ):  # se nenhum atributo inválido foi encontrado até agora
        if 1 <= att <= 10:  # e se estiver dentro do range permitido
          is_atts_valid = True  # valida os atributos
        else:  # mas se o atributo for estiver fora do range permitido
          invalid_att_found = (
            True  # marca que um atributo inválido foi encontrado
          )
          is_atts_valid = False  # e invalida os SPECIAL_atts

    # depois da verificação
    if not is_atts_valid:  # se os atributos forem inválidos
      print("Atributos S.P.E.C.I.A.L. inválidos. Acesso negado.\n")
      new_atts = input().split("-")  # pede novos atributos

      for idx in range(len(new_atts)):  # cenversão dos atributos para inteiro
        new_atts[idx] = int(new_atts[idx])

      SPECIAL_atts = new_atts  # atualiza os atrubutos
    else:  # se os atributos forem válidos
      running_loop = False  # sai do loop

# ========================== verificação do atributo máximo
# variaveis
attribute_effect = "none"  # efeito que o atributo máximo vai ter no jogo
"""
  none = sem efeito
  finish = encerra o jogo
  lucky = o jogo acaba com um acerto
"""

if SPECIAL_atts[0] == 10:
  print(
    "NORM: Meu Deus, você quebrou o terminal na base da porrada?! Se derrotar um Deathclaw no soco for hobby, melhor eu te dar uma Nuka-Cola gelada agora mesmo..."
  )
  attribute_effect = "finish"
elif SPECIAL_atts[1] == 10:
  print(
    "NORM: Peraí... você tá arrombando a máquina de Nuka-Colas com uma chave de fenda e uma presilha? NÃO! ASSIM NÃO VALE!"
  )
  attribute_effect = "finish"
elif SPECIAL_atts[3] == 10:
  print(
    "NORM: Uau, esse nível de carisma é trapaça social. Você nem precisava desse teste, né? Toma uma Nuka-Cola Quantum, estrela do Vault."
  )
  attribute_effect = "finish"
elif SPECIAL_atts[4] == 10:
  print(
    "NORM: Alguém tão inteligente quanto eu? Finalmente uma conversa à altura. O teste não faz jus à sua cabeça, então pega uma Nuka-Cola Quantum e vamos planejar como usar o G.E.C.K. na superfície."
  )
  attribute_effect = "finish"
elif SPECIAL_atts[6] == 10:
  print(
    "NORM: Com essa sorte absurda, eu só vou fingir surpresa quando a máquina se abrir sozinha pra você.\n"
  )
  attribute_effect = "lucky"

# ========================== mapeamento da matriz
if (
  attribute_effect != "finish"
):  # se o jogo não tiver acabado por causa do atributo máximo
  # variavies
  words_map = []
  """
  um array que guarda as palavras da frase secreta\\
  cada palavra é um array de letras [0] e as coordenadas dessa letra [1]\\
  as coordenadas também são um array de números, [0] = linha, [1] = coluna\\
  exemplo:\\
  a matriz ........ "WORD" é mapeada\\
  [W, B, G, D] .... [ "W", [0, 0] ]\\
  [A, O, C, D] .... [ "O", [1, 1] ]\\
  [E, F, R, H] ..... [ "R", [2, 2] ]\\
  [P, J, K, D] ..... [ "D", [3, 3] ]
  """

  matrix_copy = []  # cópia da matriz para não alterar a original
  secret_words = secret.split()  # separa as palavras da frase secreta

  for line in matrix:  # cópia da matriz
    matrix_copy.append(line.copy())

  for word in secret_words:  # análise de cada palavra
    word_map = []  # array que vai guardar as letras e coordenadas da palavra
    for letter in word:  # análise de cada letra
      has_found = False  # variável de controle para não encontrar a mesma letra mais de uma vez

      for line_idx in range(n_lines):  # varre a matriz
        for column_idx in range(n_columns):
          # se encontrar a letra
          if matrix_copy[line_idx][column_idx] == letter and not has_found:
            # guarda a letra e suas coordenadas
            word_map.append([letter, [line_idx, column_idx]])

            holder = matrix_copy[line_idx].copy()
            holder[column_idx] = "."
            # substitui a letra por um ponto para não encontrá-la de novo
            matrix_copy[line_idx] = holder.copy()

            has_found = True  # marca que a letra foi encontrada para não encontrar outra igual
    words_map.append(word_map)  # guarda o mapeamento da palavra no mapa geral

  # ========================== jogo
  found_words = []
  chances = len(secret.split()) * (int(SPECIAL_atts[4]) // 2)
  attempts = 0

  print(
    f"Palavras encontradas: {', '.join(found_words)}\nTentativas: {attempts}/{chances}.\n"
  )
  for line in matrix:
    print("ㅤ".join(line))
  print()
  print()

  player_won = False
  for attempt in range(chances):
    if not player_won:
      guess = input()  # linha-coluna
      coords_guess = guess.split("-")  # separa a linha e a coluna
      """
      [0] = linha
      [1] = coluna
      """
      is_coords_valid = False

      print(f"Nova tentativa: Coordenada {guess}\n")
      for idx in range(len(coords_guess)):  # conversão para inteiro
        coords_guess[idx] = int(coords_guess[idx])

      if (
        0 <= coords_guess[0] < n_lines and 0 <= coords_guess[1] < n_columns
      ):  # se as coordenadas forem válidas
        if matrix[coords_guess[0]][
          coords_guess[1]
        ].isalpha():  # e se a coordenada tiver uma letra
          is_coords_valid = True  # valida as coordenadas

      if not is_coords_valid:
        print(
          "NORM: Coordenada inválida. O terminal é avançado demais ou você só digitou no susto?\n"
        )
      else:
        matrix_letter = matrix[coords_guess[0]][coords_guess[1]]
        word_found = []
        full_word = ""
        if matrix_letter.isalpha():
          for idx in range(len(words_map)):
            word_data = words_map[idx]
            for letter_data in word_data:
              if letter_data[1] == coords_guess:
                word_found = word_data

        for letter in word_found:
          full_word += letter[0]

        if full_word in found_words:
          print(
            "NORM: Essa palavra você já encontrou, gênio. Mira em outra coordenada.\n"
          )
        else:
          found_words.append(full_word)
          print(
            f"NORM: Boa! A coordenada {str(coords_guess[0]) + '-' + str(coords_guess[1])} pegou o caractere {matrix_letter} da palavra {full_word}.\n"
          )
          for letter_data in word_found:
            matrix[letter_data[1][0]][letter_data[1][1]] = (
              "*"  # substitui as letras da palavra encontrada por pontos na matriz para não encontrá-las de novo
            )
      attempts += 1

      print(
        f"Palavras encontradas: {', '.join(found_words)}\nTentativas: {attempts}/{chances}.\n"
      )

      for el in matrix:
        print("ㅤ".join(el))
      print()
      print()

      if attempts == 1 and attribute_effect == "lucky":
        print(
          "NORM: Ah, sortudo(a) miserável!! Não acredito que você acertou de primeira... Toma uma Nuka-Cola Quantum antes que eu mude de ideia!"
        )
        player_won = True
      elif len(found_words) == len(secret_words):
        print(
          f"NORM: Parabéns, {username}! Você encontrou todas as palavras secretas. Considerando tudo, foi até elegante. Sua Nuka-Cola geladinha está garantida!"
        )
        player_won = True

  if not player_won:
    print(
      "NORM: Meu desafio continua supremo! Em breve eu supero até os sistemas de segurança de Robert House... e você ainda vai pedir revanche."
    )
