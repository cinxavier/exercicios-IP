# ============================================== coleta
# variaveis
searching = True
missao = ["Capacitor de Fluxo", "Válvula de Vácuo", "Fragmento do Ponto-Zero"]
bonus = ["Escopeta Lendária", "Vira-Vira", "Peixinho-Dourado Mítico"]
lixo = ["Lata Enferrujada", "Bota Velha", "Cogumelo Mordido"]

# idx [0] = nome
# idx [1] = quantidade
# idx [2] = ordem de chegada
coletados = []
while searching:
  item_achado = input()

  if item_achado == "Fim Da Coleta!":
    searching = False

  elif item_achado in missao or item_achado in bonus:
    its_in_invent = False

    for item_coletado in coletados:
      if item_coletado[0] == item_achado:
        item_coletado[1] += 1
        its_in_invent = True

    if not its_in_invent:
      coletados.append([item_achado, 1, len(coletados) + 1])

print("desordenados:", coletados) # print
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

print("ordenados:", coletados) # print
# ============================================== contagem de missão
# variaveis
has_mission_item = False
pontos = 0

for item_coletado in coletados:
  if item_coletado[0] in missao:
    has_mission_item = True

# ============================================== pontuação
if has_mission_item:
  for item_coletado in coletados:
    if item_coletado[0] in missao:
      pontos += 30
    elif item_coletado[0] in bonus:
      pontos += 10
    elif item_coletado[0] in lixo:
      pontos = pontos
    else:
      pontos -= 5

    if pontos > 100:
      pontos = 100
    elif pontos < 0:
      pontos = 0

  print("pontos:", pontos) # print
else:
  print("Nenhum item de missão coletado.") # print
# ============================================== coleta
