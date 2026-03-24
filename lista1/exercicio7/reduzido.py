# HidromassagemAutomáticaDoPerry
# 30
# OK... ISSO É BEM ESTRANHO.


nome_maquina1 = input()
quantidade_pecas1 = int(input())
reacao_candace1 = input()
pontuacao1 = len(nome_maquina1) + quantidade_pecas1

limite_pecas = 25
limite_nome = 15

print("\npontuação: ", pontuacao1)

if nome_maquina1 == "MáquinaDeBanhoForçado":
    pontuacao1 -= 20
    print("pontuacao: -20 | total = ", pontuacao1)


if all(l in nome_maquina1 for l in ("i", "n", "a", "t", "o", "r")):
    pontuacao1 -= 50
    print("inator | -50 | total = ", pontuacao1)


if all(l in nome_maquina1 for l in ("P", "e", "r", "y")):
    pontuacao1 += 20
    print("perry | +20 | total = ", pontuacao1)

    # reação 1
if reacao_candace1 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao1 += 30
    print("reação 1 | +30 | total = ", pontuacao1)
    # reação 2
if reacao_candace1 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao1 += 20
    print("reação 2 | +20 | total = ", pontuacao1)
    # reação 3
if reacao_candace1 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao1 += 10
    print("reação 3 | +10 | total = ", pontuacao1)
    # reação 4
if reacao_candace1 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao1 += 0
    print("reação 4 | +0 | total = ", pontuacao1)

    # reação 5
if reacao_candace1 == "SÉRIO? SÓ ISSO?":
    pontuacao1 -= 5
    print("reação 5 | -5 | total = ", pontuacao1)

    # reação 6
if reacao_candace1 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao1 -= 10
    print("reação 6 | -10 | total = ", pontuacao1)

    # reação 7
if reacao_candace1 == "AH, ESQUECE…":
    pontuacao1 -= 15
    print("reação 7 | -15 | total = ", pontuacao1)


if nome_maquina1 == "HidromassagemAutomáticaDoPerry":
    pontuacao1 *= 2
    print("maquina do perry | x2 | total = ", pontuacao1)


primeiro = nome_maquina1
v_primeiro = pontuacao1

print("\n===========================\n")
print(f"1º lugar - {primeiro} : {v_primeiro} pontos")


# primeiro = nome_maquina1
# v_primeiro = pontuacao1

# segundo = nome_maquina2
# v_segundo = pontuacao2

# terceiro = nome_maquina3
# v_terceiro = pontuacao3

# quarto = nome_maquina4
# v_quarto = pontuacao4
