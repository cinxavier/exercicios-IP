def make_matrix(n, matrix):
  if n == 0:
    return matrix
  line = input().split()
  matrix.append(line)
  return make_matrix(n - 1, matrix)

def close_way(matrix, i, j):
  matrix[i][j] = "#"
  return matrix


def dfs(matrix, n, i, j, keyword, limit):
  if i < 0 or j < 0 or i >= n or j >= n:
    return False

  valor = matrix[i][j]

  if valor == "0" or valor == "#":
    return False

  if valor == "2":
    return True

  if limit < 0:
    return False

  new_matrix = close_way(matrix, i, j)

  return (
    dfs(new_matrix, n, i + 1, j, keyword, limit - 1)
    or dfs(new_matrix, n, i - 1, j, keyword, limit - 1)
    or dfs(new_matrix, n, i, j + 1, keyword, limit - 1)
    or dfs(new_matrix, n, i, j - 1, keyword, limit - 1)
  )


print("Eu te amo tanto agora quanto da primeira vez em que eu vi você...")

n = int(input())
print("O mapa da floresta me parece esquisito, certo Pascal?")

keyword = input()
print("Minha querida Rapunzel, a keyword-chave é?")

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
