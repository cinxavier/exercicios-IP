nome_maquina1 = input()
quantidade_pecas1 = int(input())
reacao_candace1 = input()
pontuacao1 = len(nome_maquina1) + quantidade_pecas1

limite_pecas = 25
limite_nome = 15


if nome_maquina1 == "MaquinaDeBanhoForçado":
    pontuacao1 -= 20

if all(l in nome_maquina1 for l in ("i", "n", "a", "t", "o", "r")):
    pontuacao1 -= 50

if all(l in nome_maquina1 for l in ("P", "e", "r", "y")):
    pontuacao1 += 20

    # reação 1
if reacao_candace1 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao1 += 30
    # reação 2
if reacao_candace1 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao1 += 20
    # reação 3
if reacao_candace1 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao1 += 10
    # reação 4
if reacao_candace1 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao1 += 0

    # reação 5
if reacao_candace1 == "SÉRIO? SÓ ISSO?":
    pontuacao1 -= 5

    # reação 6
if reacao_candace1 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao1 -= 10

    # reação 7
if reacao_candace1 == "AH, ESQUECE…":
    pontuacao1 -= 15


if nome_maquina1 == "HidromassagemAutomáticaDoPerry":
    pontuacao1 *= 2

# ========================== maquina 2 =========================================

nome_maquina2 = input()
quantidade_pecas2 = int(input())
reacao_candace2 = input()
pontuacao2 = len(nome_maquina2) + quantidade_pecas2

if nome_maquina2 == "MaquinaDeBanhoForçado":
    pontuacao2 -= 20

if all(l in nome_maquina2 for l in ("i", "n", "a", "t", "o", "r")):
    pontuacao2 -= 50

if all(l in nome_maquina2 for l in ("P", "e", "r", "y")):
    pontuacao2 += 20

    # reação 1
if reacao_candace2 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao2 += 30
    # reação 2
if reacao_candace2 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao2 += 20
    # reação 3
if reacao_candace2 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao2 += 10
    # reação 4
if reacao_candace2 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao2 += 0

    # reação 5
if reacao_candace2 == "SÉRIO? SÓ ISSO?":
    pontuacao2 -= 5

    # reação 6
if reacao_candace2 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao2 -= 10

    # reação 7
if reacao_candace2 == "AH, ESQUECE…":
    pontuacao2 -= 15


if nome_maquina2 == "HidromassagemAutomáticaDoPerry":
    pontuacao2 *= 2

# ========================= maquina 3 =========================================

nome_maquina3 = input()
quantidade_pecas3 = int(input())
reacao_candace3 = input()
pontuacao3 = len(nome_maquina3) + quantidade_pecas3

if nome_maquina3 == "MaquinaDeBanhoForçado":
    pontuacao3 -= 20

if all(l in nome_maquina3 for l in ("i", "n", "a", "t", "o", "r")):
    pontuacao3 -= 50

if all(l in nome_maquina3 for l in ("P", "e", "r", "y")):
    pontuacao3 += 20

    # reação 1
if reacao_candace3 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao3 += 30
    # reação 2
if reacao_candace3 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao3 += 20
    # reação 3
if reacao_candace3 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao3 += 10
    # reação 4
if reacao_candace3 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao3 += 0

    # reação 5
if reacao_candace3 == "SÉRIO? SÓ ISSO?":
    pontuacao3 -= 5

    # reação 6
if reacao_candace3 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao3 -= 10

    # reação 7
if reacao_candace3 == "AH, ESQUECE…":
    pontuacao3 -= 15


if nome_maquina3 == "HidromassagemAutomáticaDoPerry":
    pontuacao3 *= 2


# ======================== maquina 4 =========================================

nome_maquina4 = input()
quantidade_pecas4 = int(input())
reacao_candace4 = input()
pontuacao4 = len(nome_maquina4) + quantidade_pecas4


if nome_maquina4 == "MaquinaDeBanhoForçado":
    pontuacao4 -= 20

if all(l in nome_maquina4 for l in ("i", "n", "a", "t", "o", "r")):
    pontuacao4 -= 50

if all(l in nome_maquina4 for l in ("P", "e", "r", "y")):
    pontuacao4 += 20

    # reação 1
if reacao_candace4 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao4 += 30
    # reação 2
if reacao_candace4 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao4 += 20
    # reação 3
if reacao_candace4 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao4 += 10
    # reação 4
if reacao_candace4 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao4 += 0

    # reação 5
if reacao_candace4 == "SÉRIO? SÓ ISSO?":
    pontuacao4 -= 5

    # reação 6
if reacao_candace4 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao4 -= 10

    # reação 7
if reacao_candace4 == "AH, ESQUECE…":
    pontuacao4 -= 15


if nome_maquina4 == "HidromassagemAutomáticaDoPerry":
    pontuacao4 *= 2


# ======================== ordenação das máquinas =========================================

# maquinas 1 e 2
if pontuacao1 < pontuacao2:
    nome_maquina1, nome_maquina2 = nome_maquina2, nome_maquina1
    pontuacao1, pontuacao2 = pontuacao2, pontuacao1

# elif pontuacao1 == pontuacao2:
#     parametros1 = len(nome_maquina1) + quantidade_pecas1
#     parametros2 = len(nome_maquina2) + quantidade_pecas2

#     if parametros1 < parametros2:
#         nome_maquina1, nome_maquina2 = nome_maquina2, nome_maquina1
#         pontuacao1, pontuacao2 = pontuacao2, pontuacao1

#     elif parametros1 == parametros2:
#         if nome_maquina1 < nome_maquina2:
#             nome_maquina1, nome_maquina2 = nome_maquina2, nome_maquina1
#             pontuacao1, pontuacao2 = pontuacao2, pontuacao1

# maquinas 1 e 3
if pontuacao1 < pontuacao3:
    nome_maquina1, nome_maquina3 = nome_maquina3, nome_maquina1
    pontuacao1, pontuacao3 = pontuacao3, pontuacao1

# elif pontuacao1 == pontuacao3:
#     parametros1 = len(nome_maquina1) + quantidade_pecas1
#     parametros3 = len(nome_maquina3) + quantidade_pecas3

#     if parametros1 < parametros3:
#         nome_maquina1, nome_maquina3 = nome_maquina3, nome_maquina1
#         pontuacao1, pontuacao3 = pontuacao3, pontuacao1

#     elif parametros1 == parametros3:
#         if nome_maquina1 < nome_maquina3:
#             nome_maquina1, nome_maquina3 = nome_maquina3, nome_maquina1
#             pontuacao1, pontuacao3 = pontuacao3, pontuacao1
            
# # maquinas 1 e 4
if pontuacao1 < pontuacao4:
    nome_maquina1, nome_maquina4 = nome_maquina4, nome_maquina1
    pontuacao1, pontuacao4 = pontuacao4, pontuacao1

# elif pontuacao1 == pontuacao4:
#     parametros1 = len(nome_maquina1) + quantidade_pecas1
#     parametros4 = len(nome_maquina4) + quantidade_pecas4

#     if parametros1 < parametros4:
#         nome_maquina1, nome_maquina4 = nome_maquina4, nome_maquina1
#         pontuacao1, pontuacao4 = pontuacao4, pontuacao1

#     elif parametros1 == parametros4:
#         if nome_maquina1 < nome_maquina4:
#             nome_maquina1, nome_maquina4 = nome_maquina4, nome_maquina1
#             pontuacao1, pontuacao4 = pontuacao4, pontuacao1

# maquinas 2 e 3
if pontuacao2 < pontuacao3:
    nome_maquina2, nome_maquina3 = nome_maquina3, nome_maquina2
    pontuacao2, pontuacao3 = pontuacao3, pontuacao2
    
# elif pontuacao2 == pontuacao3:
#     parametros2 = len(nome_maquina2) + quantidade_pecas2
#     parametros3 = len(nome_maquina3) + quantidade_pecas3

#     if parametros2 < parametros3:
#         nome_maquina2, nome_maquina3 = nome_maquina3, nome_maquina2
#         pontuacao2, pontuacao3 = pontuacao3, pontuacao2

#     elif parametros2 == parametros3:
#         if nome_maquina2 < nome_maquina3:
#             nome_maquina2, nome_maquina3 = nome_maquina3, nome_maquina2
#             pontuacao2, pontuacao3 = pontuacao3, pontuacao2

# maquinas 2 e 4
if pontuacao2 < pontuacao4:
    nome_maquina2, nome_maquina4 = nome_maquina4, nome_maquina2
    pontuacao2, pontuacao4 = pontuacao4, pontuacao2

# elif pontuacao2 == pontuacao4:
#     parametros2 = len(nome_maquina2) + quantidade_pecas2
#     parametros4 = len(nome_maquina4) + quantidade_pecas4

#     if parametros2 < parametros4:
#         nome_maquina2, nome_maquina4 = nome_maquina4, nome_maquina2
#         pontuacao2, pontuacao4 = pontuacao4, pontuacao2

#     elif parametros2 == parametros4:
#         if nome_maquina2 < nome_maquina4:
#             nome_maquina2, nome_maquina4 = nome_maquina4, nome_maquina2
#             pontuacao2, pontuacao4 = pontuacao4, pontuacao2

print(f"1º lugar - {nome_maquina1} : {pontuacao1} pontos")
print(f"2º lugar - {nome_maquina2} : {pontuacao2} pontos")
print(f"3º lugar - {nome_maquina3} : {pontuacao3} pontos")
print(f"4º lugar - {nome_maquina4} : {pontuacao4} pontos")


# codigo desnecessariexcessivamente longo

