print("Bem vindos, exploradores! Começaremos à Missão Lazarus!")
lista_planetas = []
planetas_desc = 0

for planeta in input().split(", "):
  lista_planetas.append(planeta.split(" - "))

print("Planetas armazenados. Fim da Missão Lazarus.")
print("Hora de escolher os melhores planetas para habitarmos!")

idx_lista_planetas = 0
while idx_lista_planetas < len(lista_planetas):
  planeta = lista_planetas[idx_lista_planetas]
  nivel_hab = int(planeta[1])
  status_sonda = planeta[2]

  if status_sonda == "falha" or nivel_hab < 6:
    idx = lista_planetas.index(planeta)
    lista_planetas.pop(idx)
    planetas_desc += 1
  else:
    idx_lista_planetas += 1

for _ in lista_planetas:
  for i in range(len(lista_planetas) - 1):
    atual = lista_planetas[i]
    prox = lista_planetas[i + 1]
    if atual[1] < prox[1]:
      lista_planetas[i], lista_planetas[i + 1] = (
        lista_planetas[i + 1],
        lista_planetas[i],
      )
    elif atual[1] == prox[1]:
      if atual[0][0][0].lower() > prox[0][0][0].lower():
        lista_planetas[i], lista_planetas[i + 1] = lista_planetas[i + 1], lista_planetas[i]


if len(lista_planetas) > 0:
  nomes = [nome[0] for nome in lista_planetas]
  print(f"Planetas habitáveis encontrados: {', '.join(nomes)}.")
else:
  print("Planetas habitáveis encontrados: nenhum.")

print(f"Quantidade de planetas desconsiderados: {planetas_desc}.")
