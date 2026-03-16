nome_maquina1 = input()
quantidade_pecas1 = int(input())
reacao_candace1 = input()
pontuacao1 = len(nome_maquina1)

nome_maquina2 = input()
quantidade_pecas2 = int(input())
reacao_candace2 = input()
pontuacao2 = len(nome_maquina2)

nome_maquina3 = input()
quantidade_pecas3 = int(input())
reacao_candace3 = input()
pontuacao3 = len(nome_maquina3)

nome_maquina4 = input()
quantidade_pecas4 = int(input())
reacao_candace4 = input()
pontuacao4 = len(nome_maquina4)

limite_pecas = 25
limite_nome = 15

if nome_maquina1 == "HidromassagemAutomáticaDoPerry":
    pontuacao1 *= 2
if nome_maquina2 == "HidromassagemAutomáticaDoPerry":
    pontuacao2 *= 2
if nome_maquina3 == "HidromassagemAutomáticaDoPerry":
    pontuacao3 *= 2
if nome_maquina4 == "HidromassagemAutomáticaDoPerry":
    pontuacao4 *= 2

if nome_maquina1 == "MaquinaDeBanhoForçado":
    pontuacao1 -= 20

if nome_maquina2 == "MaquinaDeBanhoForçado":
    pontuacao2 -= 20

if nome_maquina3 == "MaquinaDeBanhoForçado":
    pontuacao3 -= 20

if nome_maquina4 == "MaquinaDeBanhoForçado":
    pontuacao4 -= 20

if all(l in nome_maquina1 for l in ("i", "n", "a", "t", "o", "r")):
    pontuacao1 -= 50

if all(l in nome_maquina2 for l in ("i", "n", "a", "t", "o", "r")):
    pontuacao2 -= 50

if all(l in nome_maquina3 for l in ("i", "n", "a", "t", "o", "r")):
    pontuacao3 -= 50

if all(l in nome_maquina4 for l in ("i", "n", "a", "t", "o", "r")):
    pontuacao4 -= 50

if all(l in nome_maquina1 for l in ("p","e","r","r","y")):
    pontuacao1 += 20

if all(l in nome_maquina2 for l in ("p","e","r","r","y")):
    pontuacao2 += 20

if all(l in nome_maquina3 for l in ("p","e","r","r","y")):
    pontuacao3 += 20

if all(l in nome_maquina4 for l in ("p","e","r","r","y")):
    pontuacao4 += 20


primeiro = nome_maquina1
p_primeiro = pontuacao1

segundo = nome_maquina2
v_segundo = pontuacao2

terceiro = nome_maquina3
v_terceiro = pontuacao3

quarto = nome_maquina4
v_quarto = pontuacao4
