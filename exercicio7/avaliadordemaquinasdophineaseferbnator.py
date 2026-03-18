nome_maquina1 = input()
quantidade_pecas1 = int(input())
reacao_candace1 = input()
pontuacao1 = len(nome_maquina1) + quantidade_pecas1

limite_pecas = 25
limite_nome = 15


if nome_maquina1 == "MáquinaDeBanhoForçado":
    pontuacao1 -= 20

if (
    "i" in nome_maquina1
    and "n" in nome_maquina1
    and "a" in nome_maquina1
    and "t" in nome_maquina1
    and "o" in nome_maquina1
    and "r" in nome_maquina1
):
    pontuacao1 -= 50

if (
    "P" in nome_maquina1
    and "e" in nome_maquina1
    and "r" in nome_maquina1
    and "y" in nome_maquina1
):
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

if nome_maquina2 == "MáquinaDeBanhoForçado":
    pontuacao2 -= 20

if (
    "i" in nome_maquina2
    and "n" in nome_maquina2
    and "a" in nome_maquina2
    and "t" in nome_maquina2
    and "o" in nome_maquina2
    and "r" in nome_maquina2
):
    pontuacao2 -= 50

if (
    "P" in nome_maquina2
    and "e" in nome_maquina2
    and "r" in nome_maquina2
    and "y" in nome_maquina2
):
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

if nome_maquina3 == "MáquinaDeBanhoForçado":
    pontuacao3 -= 20

if (
    "i" in nome_maquina3
    and "n" in nome_maquina3
    and "a" in nome_maquina3
    and "t" in nome_maquina3
    and "o" in nome_maquina3
    and "r" in nome_maquina3
):
    pontuacao3 -= 50

if (
    "P" in nome_maquina3
    and "e" in nome_maquina3
    and "r" in nome_maquina3
    and "y" in nome_maquina3
):
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


if nome_maquina4 == "MáquinaDeBanhoForçado":
    pontuacao4 -= 20

if (
    "i" in nome_maquina4
    and "n" in nome_maquina4
    and "a" in nome_maquina4
    and "t" in nome_maquina4
    and "o" in nome_maquina4
    and "r" in nome_maquina4
):
    pontuacao4 -= 50

if (
    "P" in nome_maquina4
    and "e" in nome_maquina4
    and "r" in nome_maquina4
    and "y" in nome_maquina4
):
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

primeiro = nome_maquina1
v_primeiro = pontuacao1
pc_primeiro = quantidade_pecas1

segundo = nome_maquina2
v_segundo = pontuacao2
pc_segundo = quantidade_pecas2

terceiro = nome_maquina3
v_terceiro = pontuacao3
pc_terceiro = quantidade_pecas3

quarto = nome_maquina4
v_quarto = pontuacao4
pc_quarto = quantidade_pecas4

# posições 1 e 2
if v_primeiro < v_segundo:
    primeiro, segundo = segundo, primeiro
    v_primeiro, v_segundo = v_segundo, v_primeiro
    pc_primeiro, pc_segundo = pc_segundo, pc_primeiro

# desempate entre 1 e 2
elif v_primeiro == v_segundo:
    params_primeiro = 0
    params_segundo = 0

    # parametros do primeiro
    if len(primeiro) > limite_nome:
        params_primeiro += 1

    # parametros do segundo
    if len(segundo) > limite_nome:
        params_segundo += 1

    # decisão de desempate
    if params_primeiro < params_segundo:
        primeiro, segundo = segundo, primeiro
        v_primeiro, v_segundo = v_segundo, v_primeiro
        pc_primeiro, pc_segundo = pc_segundo, pc_primeiro
    elif params_primeiro == params_segundo:

        # peças do primeiro
        if pc_primeiro > limite_pecas:
            params_primeiro += 1
        # peças do segundo
        if pc_segundo > limite_pecas:
            params_segundo += 1
        
        # decisão de desempate
        if params_primeiro < params_segundo:
            primeiro, segundo = segundo, primeiro
            v_primeiro, v_segundo = v_segundo, v_primeiro
            pc_primeiro, pc_segundo = pc_segundo, pc_primeiro
        elif params_primeiro == params_segundo:
            if len(primeiro) < len(segundo):
                primeiro, segundo = segundo, primeiro
                v_primeiro, v_segundo = v_segundo, v_primeiro
                pc_primeiro, pc_segundo = pc_segundo, pc_primeiro

# ==============================

# posições 1 e 3
if v_primeiro < v_terceiro:
    primeiro, terceiro = terceiro, primeiro
    v_primeiro, v_terceiro = v_terceiro, v_primeiro
    pc_primeiro, pc_terceiro = pc_terceiro, pc_primeiro

# desempate entre 1 e 3
elif v_primeiro == v_terceiro:
    params_primeiro = 0
    params_terceiro = 0

    if len(primeiro) > limite_nome:
        params_primeiro += 1
    if len(terceiro) > limite_nome:
        params_terceiro += 1

    if params_primeiro < params_terceiro:
        primeiro, terceiro = terceiro, primeiro
        v_primeiro, v_terceiro = v_terceiro, v_primeiro
        pc_primeiro, pc_terceiro = pc_terceiro, pc_primeiro
    elif params_primeiro == params_terceiro:
        if pc_primeiro > limite_pecas:
            params_primeiro += 1
        if pc_terceiro > limite_pecas:
            params_terceiro += 1

        if params_primeiro < params_terceiro:
            primeiro, terceiro = terceiro, primeiro
            v_primeiro, v_terceiro = v_terceiro, v_primeiro
            pc_primeiro, pc_terceiro = pc_terceiro, pc_primeiro
        elif params_primeiro == params_terceiro:
            if len(primeiro) < len(terceiro):
                primeiro, terceiro = terceiro, primeiro
                v_primeiro, v_terceiro = v_terceiro, v_primeiro
                pc_primeiro, pc_terceiro = pc_terceiro, pc_primeiro

# ==============================

# posições 1 e 4
if v_primeiro < v_quarto:
    primeiro, quarto = quarto, primeiro
    v_primeiro, v_quarto = v_quarto, v_primeiro
    pc_primeiro, pc_quarto = pc_quarto, pc_primeiro

# desempate entre 1 e 4
elif v_primeiro == v_quarto:
    params_primeiro = 0
    params_quarto = 0

    if len(primeiro) > limite_nome:
        params_primeiro += 1
    if len(quarto) > limite_nome:
        params_quarto += 1

    if params_primeiro < params_quarto:
        primeiro, quarto = quarto, primeiro
        v_primeiro, v_quarto = v_quarto, v_primeiro
        pc_primeiro, pc_quarto = pc_quarto, pc_primeiro
    elif params_primeiro == params_quarto:
        if pc_primeiro > limite_pecas:
            params_primeiro += 1
        if pc_quarto > limite_pecas:
            params_quarto += 1

        if params_primeiro < params_quarto:
            primeiro, quarto = quarto, primeiro
            v_primeiro, v_quarto = v_quarto, v_primeiro
            pc_primeiro, pc_quarto = pc_quarto, pc_primeiro
        elif params_primeiro == params_quarto:
            if len(primeiro) < len(quarto):
                primeiro, quarto = quarto, primeiro
                v_primeiro, v_quarto = v_quarto, v_primeiro
                pc_primeiro, pc_quarto = pc_quarto, pc_primeiro

# =============================

# posições 2 e 3
if v_segundo < v_terceiro:
    segundo, terceiro = terceiro, segundo
    v_segundo, v_terceiro = v_terceiro, v_segundo
    pc_segundo, pc_terceiro = pc_terceiro, pc_segundo

# desempate entre 2 e 3
elif v_segundo == v_terceiro:
    params_segundo = 0
    params_terceiro = 0

    if len(segundo) > limite_nome:
        params_segundo += 1
    if len(terceiro) > limite_nome:
        params_terceiro += 1

    if params_segundo < params_terceiro:
        segundo, terceiro = terceiro, segundo
        v_segundo, v_terceiro = v_terceiro, v_segundo
        pc_segundo, pc_terceiro = pc_terceiro, pc_segundo
    elif params_segundo == params_terceiro:
        if pc_segundo > limite_pecas:
            params_segundo += 1
        if pc_terceiro > limite_pecas:
            params_terceiro += 1

        if params_segundo < params_terceiro:
            segundo, terceiro = terceiro, segundo
            v_segundo, v_terceiro = v_terceiro, v_segundo
            pc_segundo, pc_terceiro = pc_terceiro, pc_segundo
        elif params_segundo == params_terceiro:
            if len(segundo) < len(terceiro):
                segundo, terceiro = terceiro, segundo
                v_segundo, v_terceiro = v_terceiro, v_segundo
                pc_segundo, pc_terceiro = pc_terceiro, pc_segundo

# =============================

# posições 2 e 4
if v_segundo < v_quarto:
    segundo, quarto = quarto, segundo
    v_segundo, v_quarto = v_quarto, v_segundo
    pc_segundo, pc_quarto = pc_quarto, pc_segundo

# desempate entre 2 e 4
elif v_segundo == v_quarto:
    params_segundo = 0
    params_quarto = 0

    if len(segundo) > limite_nome:
        params_segundo += 1
    if len(quarto) > limite_nome:
        params_quarto += 1

    if params_segundo < params_quarto:
        segundo, quarto = quarto, segundo
        v_segundo, v_quarto = v_quarto, v_segundo
        pc_segundo, pc_quarto = pc_quarto, pc_segundo
    elif params_segundo == params_quarto:
        if pc_segundo > limite_pecas:
            params_segundo += 1
        if pc_quarto > limite_pecas:
            params_quarto += 1

        if params_segundo < params_quarto:
            segundo, quarto = quarto, segundo
            v_segundo, v_quarto = v_quarto, v_segundo
            pc_segundo, pc_quarto = pc_quarto, pc_segundo
        elif params_segundo == params_quarto:
            if len(segundo) < len(quarto):
                segundo, quarto = quarto, segundo
                v_segundo, v_quarto = v_quarto, v_segundo
                pc_segundo, pc_quarto = pc_quarto, pc_segundo

# ============================

# posições 3 e 4
if v_terceiro < v_quarto:
    terceiro, quarto = quarto, terceiro
    v_terceiro, v_quarto = v_quarto, v_terceiro
    pc_terceiro, pc_quarto = pc_quarto, pc_terceiro

# desempate entre 3 e 4
elif v_terceiro == v_quarto:
    params_terceiro = 0
    params_quarto = 0

    if len(terceiro) > limite_nome:
        params_terceiro += 1
    if len(quarto) > limite_nome:
        params_quarto += 1

    if params_terceiro < params_quarto:
        terceiro, quarto = quarto, terceiro
        v_terceiro, v_quarto = v_quarto, v_terceiro
        pc_terceiro, pc_quarto = pc_quarto, pc_terceiro
    elif params_terceiro == params_quarto:
        if pc_terceiro > limite_pecas:
            params_terceiro += 1
        if pc_quarto > limite_pecas:
            params_quarto += 1

        if params_terceiro < params_quarto:
            terceiro, quarto = quarto, terceiro
            v_terceiro, v_quarto = v_quarto, v_terceiro
            pc_terceiro, pc_quarto = pc_quarto, pc_terceiro
        elif params_terceiro == params_quarto:
            if len(terceiro) < len(quarto):
                terceiro, quarto = quarto, terceiro
                v_terceiro, v_quarto = v_quarto, v_terceiro
                pc_terceiro, pc_quarto = pc_quarto, pc_terceiro


print(f"1º lugar - {primeiro} : {v_primeiro} pontos")
print(f"2º lugar - {segundo} : {v_segundo} pontos")
print(f"3º lugar - {terceiro} : {v_terceiro} pontos")
print(f"4º lugar - {quarto} : {v_quarto} pontos")

# codigo desnecessariexcessivamente longo
