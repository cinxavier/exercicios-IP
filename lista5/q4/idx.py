def make_matrix(n, matrix):
  if n == 0:
    return matrix
  line = input().split()
  matrix.append(line)
  return make_matrix(n - 1, matrix)


def close_way(matrix, y, x):
  matrix[y][x] = "#"


def dfs(matrix, n, y, x, keyword, limit):
  if y < 0 or x < 0 or y >= n or x >= n:
    return False

  curr_value = matrix[y][x]

  if curr_value == "0" or curr_value == "#":
    return False

  if curr_value == "2":
    return True

  if limit < 0:
    return False

  close_way(matrix, y, x)

  return (
    dfs(matrix, n, y + 1, x, keyword, limit - 1)
    or dfs(matrix, n, y - 1, x, keyword, limit - 1)
    or dfs(matrix, n, y, x + 1, keyword, limit - 1)
    or dfs(matrix, n, y, x - 1, keyword, limit - 1)
  )


print("Eu te amo tanto agora quanto da primeira vez em que eu vi você...")

n = int(input())
print("O mapa da floresta me parece esquisito, certo Pascal?")

keyword = input()
print("Minha querida Rapunzel, a palavra-chave é?")

pos = input().split(" ")
x = int(pos[0])
y = int(pos[1])
print("Vamos por aqui, esse deve ser o local certo para se descer!")

matrix = make_matrix(n, [])
print("Segundo o mapa essas são as informações da floresta:")

limit = int(input())
is_posisble = dfs(matrix, n, x, y, keyword, limit)
print("Eu não tenho todo o tempo do mundo!")


if is_posisble:
  print(
    "A CAÇADA TERMINOU! O SOL BRILHA NO HORIZONTE E O PIQUE-NIQUE REAL ESTÁ SERVIDO! JOSÉ FINALMENTE PODE DESCANSAR ENQUANTO PASCAL VIGIA A TORTA DE MAÇÃ."
  )
else:
  print(
    "O SOL SE PÔS NO REINO DE CORONA E AS ÚLTIMAS LANTERNAS SE APAGARAM. JOSÉ BEZERRA VAGOU POR HORAS, MAS O DESTINO FOI CRUEL: ELE NÃO CHEGOU AO PIQUE-NIQUE. ENQUANTO O CAVALO MAXIMUS SE DELICIA COM A ÚLTIMA FATIA DE TORTA DE MAÇÃ, JOSÉ TERÁ QUE SE CONTENTAR EM DIVIDIR UMA FRUTA SILVESTRE AZEDA COM O PASCAL. A CAÇADA FOI UM FRACASSO E A FOME VENCEU DESTA VEZ."
  )
