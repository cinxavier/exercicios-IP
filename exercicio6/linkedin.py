robin_disponibilidade = input().capitalize()
estelar_disponibilidade = input().capitalize()
ciborgue_disponibilidade = input().capitalize()
ravena_disponibilidade = input().capitalize()
mutano_disponibilidade = input().capitalize()

num_candidatos = 0
nao_lista = ""
escolhido = ""
condicao = ""  # betisse | disputa | sequestro

if robin_disponibilidade == "S":
    nao_lista += "Robin"
    num_candidatos += 1
if ravena_disponibilidade == "S":
    nao_lista += "Ravena"
    num_candidatos += 1
if estelar_disponibilidade == "S":
    nao_lista += "Estelar"
    num_candidatos += 1
if ciborgue_disponibilidade == "S":
    nao_lista += "Ciborgue"
    num_candidatos += 1
if mutano_disponibilidade == "S":
    nao_lista += "Mutano"
    num_candidatos += 1

if num_candidatos == 0:
    escolhido = "Ninguem"
    print(
        "Parece que ninguém quer participar da Liga da Justiça, o Batman vai ter que ouvir um Super-Esculacho do Super-Homem por não ter conseguido ninguém super forte!"
    )

elif num_candidatos == 1:
    escolhido = nao_lista
    print(
        "Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!"
    )

if num_candidatos == 2:
    # caso tenha só o robin, ele vai | se a estelar estiver, ele sai
    if "Robin" in nao_lista:
        if "Estelar" in nao_lista:
            escolhido = "Estelar"
            condicao = "betisse"
        else:
            escolhido = "Robin"

    elif "Ravena" in nao_lista:
        escolhido = "Ravena"
        if "Mutano" in nao_lista:
            condicao = "betisse"

    elif "Estelar" in nao_lista:
        escolhido = "Estelar"

    # caso o mutano esteja com a ravena, ele sai | se o ciborgue estiver, ele briga
    elif "Mutano" in nao_lista:
        if "Ciborgue" in nao_lista:
            condicao = "disputa"
            quantidade_mutano = int(input())
            quantidade_ciborgue = int(input())

            if quantidade_ciborgue == quantidade_mutano:
                nome_escolhido = input()
                escolhido = nome_escolhido
            else:
                escolhido = (
                    "Mutano" if quantidade_mutano > quantidade_ciborgue else "Ciborgue"
                )

if num_candidatos == 3 or num_candidatos == 4:
    if "Robin" in nao_lista:
        escolhido = "Robin"
    else:
        escolhido = "Ravena"
        if "Ravena" not in nao_lista:
            condicao = "sequestro"

if num_candidatos == 5:
    escolhido = "Ninguem"
    print(
        "Em toda a vida do Batman, ele nunca viu um lugar tão caótico quanto a torre dos titãns depois da notícia, nem mesmo Gotham, com isso ele percebe que não seria ali o local ideal para encontrar o novo salvador da terra!"
    )


if 2 <= num_candidatos <= 4:
    print(
        f"Mesmo com {num_candidatos} candidatos, o(a) {escolhido} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {escolhido}!"
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
elif num_candidatos == 5:
    print(
        "Poxa, mas que pena, os Titãns vão ter que esperar mais um pouco antes de darem mais um passo na carreira, se continuar assim, vão assinar a CLT."
    )

if condicao == "betisse":
    print("Parece que o cavalherismo ainda não morreu não é mesmo?")
elif condicao == "disputa":
    print("Nem uma competição árdua assim pode abalar a amizade desses caras!")
elif condicao == "sequestro":
    print(
        "O Batman não iria perder a chance de ter um dos seres mais poderosos do Universo DC no time, o preparo dele não permite isso!"
    )
else:
    if 0 < num_candidatos < 5:
        print("Que bom que tudo deu certo, sem dificuldades!")
