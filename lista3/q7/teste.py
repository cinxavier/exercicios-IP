matriz = [
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3],
]
matriz_copia = []

for linha in matriz:
  matriz_copia.append(linha.copy())

for idx in range(len(matriz)):
  matriz_copia[idx][1] = 0
  print(matriz[idx], matriz_copia[idx])
