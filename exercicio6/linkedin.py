robin_disponibilidade = input()
estelar_disponibilidade = input()
ciborgue_disponibilidade = input()
ravena_disponibilidade = input()
mutano_disponibilidade = input()

num_candidatos = 0
nao_lista = ""
escolhido = ""
disputa = False

if robin_disponibilidade == "S":
    nao_lista += "Robin "
if estelar_disponibilidade == "S":
    nao_lista += "Estelar "
if ciborgue_disponibilidade == "S":
    nao_lista += "Ciborgue "
if ravena_disponibilidade == "S":
    nao_lista += "Ravena "
if mutano_disponibilidade == "S":
    nao_lista += "Mutano "

nao_lista = nao_lista.strip()
num_candidatos = len(nao_lista.split(" "))

if num_candidatos == 0:
    print(
        "Parece que ninguém quer participar da Liga da Justiça, o Batman vai ter que ouvir um Super-Esculacho do Super-Homem por não ter conseguido ninguém super forte!"
    )
if num_candidatos == 1:
      escolhido = nao_lista
      print(
          "Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!"
      )

while num_candidatos> 1:
  if num_candidatos == 2:
      if nao_lista.__contains__("Robin"):
          if nao_lista.__contains__("Estelar"):
              escolhido = "Estelar"
          else:
            escolhido = "Robin"

      if nao_lista.__contains__("Mutano"):
          escolhido = "Mutano"
          if nao_lista.__contains__("Ravena"):
              escolhido = "Ravena"

          if nao_lista.__contains__("Ciborgue"):
              disputa = True
              quantidade_mutano = int(input())
              quantidade_ciborgue = int(input())

              if quantidade_ciborgue == quantidade_mutano:
                  nome_escolhido = input()
                  escolhido = nome_escolhido
              else:
                  escolhido = (
                      "Mutano" if quantidade_mutano > quantidade_ciborgue else "Ciborgue"
                  )

      print(
          f"Mesmo com {num_candidatos} candidatos, o(a) {escolhido} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {escolhido}!"
      )
  if num_candidatos == 3 or num_candidatos == 4:
      if nao_lista.__contains__("Robin"):
          escolhido = "Robin"
      elif nao_lista.__contains__("Ravena"):
          escolhido = "Ravena"
      elif nao_lista.__contains__("Estelar"):
          escolhido = "Estelar"
      print(
          f"Mesmo com {num_candidatos} candidatos, o(a) {escolhido} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {escolhido}!"
      )

  if num_candidatos == 5:
      escolhido = ""
      print(
          "Em toda a vida do Batman, ele nunca viu um lugar tão caótico quanto a torre dos titãns depois da notícia, nem mesmo Gotham, com isso ele percebe que não seria ali o local ideal para encontrar o novo salvador da terra!"
      )
  if escolhido == "Robin":
      print(
          "Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!"
      )
  elif escolhido == "Ravena":
      print(
          "Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!"
      )
  elif escolhido == "Mutano":
      print(
          "O herói mais versátil da torre está pronto para mostrar que tamanho não é documento, especialmente se ele virar um tiranossauro!"
      )
  elif escolhido == "Ciborgue":
      print(
          "BOOYAH! A tecnologia de ponta do Ciborgue agora faz parte do arsenal da Liga. Até parece que já foi antes..."
      )
  elif escolhido == "Estelar":
      print(
          "Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!"
      )
  elif escolhido == "":
      print(
          "Poxa, mas que pena, os Titãns vão ter que esperar mais um pouco antes de darem mais um passo na carreira, se continuar assim, vão assinar a CLT."
      )

if (
    num_candidatos < 5
    and nao_lista.__contains__("Robin")
    and nao_lista.__contains__("Estelar")
    or num_candidatos < 5
    and nao_lista.__contains__("Mutano")
    and nao_lista.__contains__("Ravena")
):
    print("Parece que o cavalherismo ainda não morreu não é mesmo?")
if disputa:
    print("Nem uma competição árdua assim pode abalar a amizade desses caras!")
else:
    if 0 < num_candidatos < 5:
      print("Que bom que tudo deu certo, sem dificuldades!")
