lista = [
  ["adx1", 2, "batata1"],
  ["Bdx2", 2, "batata2"],
  ["idx3", 3, "batata3"],
  ["idx4", 4, "batata4"],
  ["idx5", 5, "batata5"],
  ["idx6", 6, "batata6"],
]

for _ in range(len(lista) - 1):
  for i in range(len(lista) - 1):
    first = lista[i]
    second = lista[i + 1]
    if first[1] < second[1]:
      lista[i], lista[i + 1] = lista[i + 1], lista[i]
    elif first[1] == second[1]:
      if first[0][0][0].lower() < second[0][0][0].lower():
        lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(lista)