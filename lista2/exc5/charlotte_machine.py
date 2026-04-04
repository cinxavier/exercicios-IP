print("Radar de Fofocas de Copacabana iniciado!")

numero_rodadas = int(input())
for rodada_atual in range(numero_rodadas):
  pontos = 15
  numero_fofocas = int(input())

  print(f"Rodada {rodada_atual + 1}/{numero_rodadas}")
  print(f"Fofocas registradas: {numero_fofocas}")
  print("Pontuação inicial: 15")
  keywords_usadas = ""
  num_keywords_achados = 0

  fofocas = ""
  for i in range(numero_fofocas - 1):  # coleta as fofocas e separa com -
    fofocas += "*" + input()
    palavra_proibida = input()

    anotando = pontos > 0
    while anotando:
      keyword = input()  # palavra que vai ser procurada
      keywords_usadas += keyword + " "

      # ======================================= deparação das fofocas
      fofocas_a_analisar = fofocas  # lista de fofocas originais
      fofoca_em_analise = ""  # fofoca que está sendo analisada no momento

      if keyword.lower() == "fim":  # comando para encerrar a rodada
        anotando = False
      else:
        novas_fofocas_a_analisar = ""
        nova_fofoca_em_analise = ""

        direction_switch = False  # toggle para indicar se ja foi feita a triagem da primeira fofoca
        for letra_fofoca in fofocas_a_analisar:
          if letra_fofoca == "*":  # ao esbarrar com o primeiro separador, o toggle é ativado
            direction_switch = True

          if not direction_switch:  # se o toggle não tiver sido ativado, a letra é adicionada à fofoca_em_análise
            nova_fofoca_em_analise += letra_fofoca
          else:  # se o toggle tiver sido ativado, a letra é adicionada à nova lista de fofocas_a_analisar
            if letra_fofoca == "*":
              # se aprimeira letra for um separador, essa letra é ignorada, mas as próximas são adicionadas normalmente
              if novas_fofocas_a_analisar != "":
                novas_fofocas_a_analisar += letra_fofoca
            else:  # se a letra não for um separador, ela é adicionada normalmente a lista de fofocas_a_analisar
              novas_fofocas_a_analisar += letra_fofoca
        fofocas_a_analisar = novas_fofocas_a_analisar  # a lista de fofocas_a_analisar é atualizada
        fofoca_em_analise = nova_fofoca_em_analise  # a fofoca_em_análise é atualizada

        # ======================================= separação das palavras

        palavra_em_analise = ""  # palavra da fofoca a ser comparada com a keyword
        novas_palavras_a_analisar = ""  # lista de palavras da fofoca que ainda não foram analisadas

        direction_switch = False  # toggle para indicar se ja foi feita a separação da palavra
        
        for letra_fofoca in fofocas_a_analisar:
          if letra_fofoca == " ":  # ao esbarrar com o primeiro separador, o toggle é ativado
            direction_switch = True

          if not direction_switch:  # se o toggle não tiver sido ativado, a letra é adicionada à palavra_em_analise
            palavra_em_analise += letra_fofoca
          else:  # se o toggle tiver sido ativado, a letra é adicionada à nova lista de fofocas_a_analisar
            if letra_fofoca == " ":
              # se aprimeira letra for um separador, essa letra é ignorada, mas as próximas são adicionadas normalmente
              if novas_palavras_a_analisar != "":
                novas_palavras_a_analisar += letra_fofoca
            else:  # se a letra não for um separador, ela é adicionada normalmente a lista de fofocas_a_analisar
              novas_palavras_a_analisar += letra_fofoca
              
            # análise da palavra
            if palavra_proibida == keyword:
              pontos -= 5
            if keyword == palavra_em_analise:
              pontos += 2
              num_keywords_achados += 1