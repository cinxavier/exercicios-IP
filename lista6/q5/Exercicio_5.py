#SISTEMA DE ESTATÍSTICAS AVANÇADO DA COPA DO MUNDO

#Função para achar o melhor
def melhor(candidatos):
    ordenado = dict() #*Dicionário que receberá os valores ordenados
    for posicao in range(len(candidatos)): #*Realiza para cada jogador
        ###Definindo Variáveis
        maior_gols = maior_assistencia = menor_vermelhos = menor_amarelo = mais_passes = -1 
        valor = 0
        key_nova = ''
        key_maior = ''
        pais = jogador = ''

        for i in candidatos: #*Para cada jogador roda uma vez | i recebe a chave do primeiro e segue de um em um
            
            ###Descobre o maior_gols
            if candidatos[i][2] > maior_gols: #*Se fez mais gols
                valor = candidatos[i]
                key_nova = f"{posicao + 1}"
                key_maior = i
                jogador = candidatos[i][0]
                pais = candidatos[i][1]
                maior_gols = candidatos[i][2]
                maior_assistencia = candidatos[i][3]
                mais_passes = candidatos[i][4]
                menor_amarelo = candidatos[i][5]
                menor_vermelhos = candidatos[i][6]

            elif candidatos[i][2] == maior_gols: #*Se fez gols iguais
                if candidatos[i][3] > maior_assistencia: #*Ve quem tem maior num de assistências
                    valor = candidatos[i]
                    key_nova = f"{posicao + 1}"
                    key_maior = i
                    jogador = candidatos[i][0]
                    pais = candidatos[i][1]
                    maior_gols = candidatos[i][2]
                    maior_assistencia = candidatos[i][3]
                    mais_passes = candidatos[i][4]
                    menor_amarelo = candidatos[i][5]
                    menor_vermelhos = candidatos[i][6]

                elif candidatos[i][3] == maior_assistencia: #*Se for o mesmo numero de assistencias
                    if candidatos[i][6] < menor_vermelhos or menor_vermelhos < 0: #*Pega quem recebeu menos cartões vermelhos
                        valor = candidatos[i]
                        key_nova = f"{posicao + 1}"
                        key_maior = i
                        jogador = candidatos[i][0]
                        pais = candidatos[i][1]
                        maior_gols = candidatos[i][2]
                        maior_assistencia = candidatos[i][3]
                        mais_passes = candidatos[i][4]
                        menor_amarelo = candidatos[i][5]
                        menor_vermelhos = candidatos[i][6]
                    
                    elif candidatos[i][6] == menor_vermelhos: #*Se empatar nisso
                        if candidatos[i][5] < menor_amarelo or menor_amarelo < 0: #*Pega quem recebeu menos cartões amarelos
                            valor = candidatos[i]
                            key_nova = f"{posicao + 1}"
                            key_maior = i
                            jogador = candidatos[i][0]
                            pais = candidatos[i][1]
                            maior_gols = candidatos[i][2]
                            maior_assistencia = candidatos[i][3]
                            mais_passes = candidatos[i][4]
                            menor_amarelo = candidatos[i][5]
                            menor_vermelhos = candidatos[i][6]
                        
                        elif candidatos[i][5] == menor_amarelo: #*Se empatarem novamente
                            if candidatos[i][4] > mais_passes: #Verifica quem fez mais passes
                                valor = candidatos[i]
                                key_nova = f"{posicao + 1}"
                                key_maior = i
                                jogador = candidatos[i][0]
                                pais = candidatos[i][1]
                                maior_gols = candidatos[i][2]
                                maior_assistencia = candidatos[i][3]
                                mais_passes = candidatos[i][4]
                                menor_amarelo = candidatos[i][5]
                                menor_vermelhos = candidatos[i][6]

                            elif candidatos[i][4] == mais_passes: #*Se houver mais um empate:
                                if candidatos[i][1] < pais: #*Verifica ordem alfabetica dos paises
                                    valor = candidatos[i]
                                    key_nova = f"{posicao + 1}"
                                    key_maior = i
                                    jogador = candidatos[i][0]
                                    pais = candidatos[i][1]
                                    maior_gols = candidatos[i][2]
                                    maior_assistencia = candidatos[i][3]
                                    mais_passes = candidatos[i][4]
                                    menor_amarelo = candidatos[i][5]
                                    menor_vermelhos = candidatos[i][6]
                                
                                elif candidatos[i][1] == pais: #*Se forem do mesmo país
                                    if candidatos[i][0] < jogador: #*Vê ordem alfabetica dos nomes
                                        valor = candidatos[i]
                                        key_nova = f"{posicao + 1}"
                                        key_maior = i
                                        jogador = candidatos[i][0]
                                        pais = candidatos[i][1]
                                        maior_gols = candidatos[i][2]
                                        maior_assistencia = candidatos[i][3]
                                        mais_passes = candidatos[i][4]
                                        menor_amarelo = candidatos[i][5]
                                        menor_vermelhos = candidatos[i][6]

        ordenado[key_nova] = (valor) #*Adiciona o valor no dicionário ordenado
        candidatos.pop(key_maior) #*Apaga valores ordenados do dicionário não ordenado

    return ordenado #*Retorna o dicionário organizado


#INICIO
print("Bem, amigos da rede! Sistema de Estatísticas VAR Edition no ar. Aguardando comandos...")
dados_copa = dict()
fim_copa = False

while not fim_copa:

    informacao = str(input()).split() #*Cria uma lista que guarda cada dado importante
    comando = informacao[0] #*Armazena o comando dado no input fornecido

    ##Condição de adicionar jogador
    if comando == "*ADD":
        jogador, selecao = informacao[1], informacao[2] #*Armazena o jogador à ser adicionado e sua seleção
        gols, assistencias, passes_certos, amarelos, vermelhos = int(informacao[3]), int(informacao[4]), int(informacao[5]), int(informacao[6]), int(informacao[7]) #*Aloca nas váriaveis as informações correspondentes

        if (jogador+'-'+selecao) in dados_copa: #*Se o jogador já estiver nos dados, incrementa suas informações correspondentes com as novas
            gols_antigos, assistencias_antigas, passes_certos_antigos, amarelos_antigos, vermelhos_antigos = dados_copa[jogador+'-'+selecao][1], dados_copa[jogador+'-'+selecao][2], dados_copa[jogador+'-'+selecao][3], dados_copa[jogador+'-'+selecao][4], dados_copa[jogador+'-'+selecao][5]
            dados_copa[jogador+'-'+selecao] = (selecao, gols + gols_antigos, assistencias + assistencias_antigas, passes_certos + passes_certos_antigos, amarelos + amarelos_antigos, vermelhos + vermelhos_antigos)

        else: #*Caso contrário, adiciona ele
            dados_copa[jogador+'-'+selecao] = (selecao, gols, assistencias, passes_certos, amarelos, vermelhos)

    ##Condição de jogador expulso/lesionado
    elif comando == "*DEL":
        jogador, selecao = informacao[1], informacao[2] #*Armazena o jogador à ser adicionado e sua seleção
        chave = jogador+'-'+selecao #*Pega a chave do dicionário

        if chave in dados_copa: #*Se for uma chave válida
            dados_copa.pop(chave) #*Apaga dos dados
        
        else: #*Se não
            while chave not in dados_copa: #*Pede uma chave válida
                print(f"O jogador: {jogador} da seleção: {selecao} não foi encontrado insira uma outra combinação de jogador e seleção:")
                tentativa = str(input()).split()
                jogador, selecao = tentativa[0], tentativa[1]
                chave = jogador+'-'+selecao

            dados_copa.pop(chave) #*Agora, com a chave válida, apaga dos dados

        print(f"O jogador: {jogador} da seleção: {selecao} foi retirado do sistema")

    ##Condição de busca
    elif comando == "*BUSCAR":
        jogador, selecao = informacao[1], informacao[2] #*Armazena o jogador à ser adicionado e sua seleção
        chave = jogador+'-'+selecao #*Pega a chave do dicionário

        if chave not in dados_copa and jogador == "Neymar": #*Caso especial
            print("E o pessoal tá lá: 'será que Carlo Ancelotti vai convocar o Neymar?'")

        elif chave not in dados_copa: #*Se o jogador não for encontrada
            print(f"Jogador não encontrado na seleção {selecao}")

        else: #*Caso encontrado
            g, a, p, ca, cv = dados_copa[jogador+'-'+selecao][1], dados_copa[jogador+'-'+selecao][2], dados_copa[jogador+'-'+selecao][3], dados_copa[jogador+'-'+selecao][4], dados_copa[jogador+'-'+selecao][5]
            print(f"{jogador} ({selecao}): {g}G, {a}A, {p}P, {ca}CA, {cv}CV")

    ##Caso do Destaque
    elif comando == "*DESTAQUE_SELECAO":
        selecao = informacao[1] #*Recebe a seleção que será analisada
        candidatos = dict() #*Temporario usado para organizar os dados

        for jogadores in dados_copa: #*Pega os jogadores daquela seleção
            if selecao == dados_copa[jogadores][0]:
                candidatos[jogadores] = (jogadores.split('-')[0],) + dados_copa[jogadores]
        
        if candidatos == {}: #*Caso niguém tenha jogado por aquela seleção
            print(f"Nenhum dado encontrado para a seleção {selecao}")

        else:
            dic_podio = melhor(candidatos) #*Pega o dicionário organizado para os prints

            jogador, g, a = dic_podio['1'][0], dic_podio['1'][2], dic_podio['1'][3]
            print(f"Destaque da {selecao}: {jogador} {g} gols, {a} assistências")

    ##Caso Bola de Ouro
    elif comando == "*BOLA_DE_OURO":
        candidatos = dict() #*Temporario usado para organizar os dados

        for jogadores in dados_copa: #*Pega os jogadores da copa
            candidatos[jogadores] = (jogadores.split('-')[0],) + dados_copa[jogadores]
        
        dic_podio = melhor(candidatos) #*Pega o dicionário organizado para os prints

        if dic_podio == {}: #*Se ninguém for cadastrado
            print("Nenhum jogador registrado no torneio")

        else:
            jogador, selecao, g = dic_podio['1'][0], dic_podio['1'][1], dic_podio['1'][2]
            print(f"Bola de Ouro atual: {jogador} {selecao} com {g} gols")

    ##Caso FIM DA COPA
    elif comando == "*FIM":
        candidatos = dict()#*Temporario usado para organizar os dados

        for jogadores in dados_copa: #*Pega os jogadores da copa
            candidatos[jogadores] = (jogadores.split('-')[0],) + dados_copa[jogadores]
        
        fim_copa = True
        dic_podio = melhor(candidatos) #*Pega o dicionário organizado para os prints

        if dic_podio == {}: #*Se ninguém for cadastrado
            print("Nenhum jogador registrado para o ranking final.")

        else:
            print("Ranking Final:")

            for jogadores_copa in dic_podio:
                jogador = dic_podio[jogadores_copa][0]
                selecao = dic_podio[jogadores_copa][1]
                g = dic_podio[jogadores_copa][2]
                a = dic_podio[jogadores_copa][3]
                p = dic_podio[jogadores_copa][4]
                ca = dic_podio[jogadores_copa][5]
                cv = dic_podio[jogadores_copa][6]
                print(f"{jogadores_copa}. {jogador} ({selecao}) - G: {g}, A: {a}, P: {p}, CA: {ca}, CV: {cv}")
