print(
  "Édipo: Inicializando sistema de embarque. Tripulantes atuais: Zaphod Beeblebrox, Ford Prefect, Arthur Dent, Marvin"
)
num_operacoes = int(input())
tripulantes = ["Zaphod Beeblebrox", "Ford Prefect", "Arthur Dent", "Marvin"]
for i in range(num_operacoes):
  operacao = input().split(" ")
  tipo_operacao = operacao[0]
  tripulante = ""

  if tipo_operacao != "mover":
    tripulante = " ".join(operacao[1:3])
  else:
    len_operacoes = len(operacao)

    if len_operacoes == 3:
      tripulante = operacao[1]
    else:
      tripulante = " ".join(operacao[1:3])

  if tipo_operacao == "embarcar":
    tripulantes.append(tripulante)

    if tripulante == "Trillian":
      print("Finalmente alguém sensata a bordo! Bem-vinda, Trillian!")

  elif tipo_operacao == "mover":
    novo_idx = int(operacao[2])

    tripulantes.remove(tripulante)
    tripulantes.insert(novo_idx, tripulante)

    if novo_idx == 0:  # se for movido para o primeiro lugar
      if tripulante == "Zaphod Beeblebrox":
        print("EU SOU O PRESIDENTE DA GALAXIA! Primeiro lugar é pouco!")

      elif tripulante == "Ford Prefect":
        print("Sou um escritor do Guia! Mereço destaque!")

  elif tipo_operacao == "priorizar":
    tripulantes.remove(tripulante)
    tripulantes.insert(0, tripulante)

    if tripulante == "Zaphod Beeblebrox":
      print("EU SOU O PRESIDENTE DA GALAXIA! Primeiro lugar é pouco!")

    elif tripulante == "Ford Prefect":
      print("Sou um escritor do Guia! Mereço destaque!")

  elif tipo_operacao == "remover":
    tripulantes.remove(tripulante)
    if tripulante == "Marvin":
      print("Ninguem se importa comigo mesmo. Tchau")

    if tripulante == "Arthur Dent":
      print("Eu só queria poder tomar chá... vou descer no próximo planeta")

num_tripulantes = len(tripulantes)

if num_tripulantes == 0:
  print(
    "Édipo: Graças à improbabilidade, os novos comandantes são: ninguém... a nave está vazia!"
  )
else:
  print(
    f"Édipo: Graças à improbabilidade, os novos comandantes são: {tripulantes[0]}, {tripulantes[1]} e {tripulantes[2]}."
  )
  print("Convocando tripulantes:")
  if num_tripulantes < 3:
    for tripulante in tripulantes:
      print(f"- {tripulante}")
  else:
    for i in range(3, num_tripulantes):
      print(f"- {tripulantes[i]}")
