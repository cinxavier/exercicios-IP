items_carol = input().split(", ")
items_caminhoes = []
items_faltando = items_carol.copy()

anotando = True

while anotando:
  inp = input()
  if inp == "--":
    anotando = False
  else:
    items_caminhoes.append(inp.split(", "))

print("Pedido recebido! Vamos alocar os itens nos caminhões disponíveis.")

for items_caminhao in items_caminhoes:
  items_encontrados = []

  for item in items_caminhao:
    if item in items_carol:
      items_encontrados.append(item)
      if item in items_faltando:
        items_faltando.remove(item)

  if len(items_encontrados) == 0:
    print("Não encontramos nada que a Carol pediu nesse caminhão.")
  else:
    print(f"Ótimo, esse caminhão trouxe {items_encontrados}!")
  if len(items_faltando) > 0:
    print(f"Ainda precisamos de {items_faltando}.")

if len(items_faltando) > 0:
  print("Não conseguimos reunir todos os itens que a Carol precisa :(")
else:
  print("Conseguimos! A Carol ficará muito feliz :)")