print("Radar de Fofocas de Copacabana iniciado!")

numero_rodadas = int(input())

# ======================================= rodadas
for rodada_atual in range(numero_rodadas):
  pontos = 15
  numero_fofocas = int(input())

  print(f"Rodada {rodada_atual + 1}/{numero_rodadas}")
  print(f"Fofocas registradas: {numero_fofocas}")
  print("Pontuação inicial: 15")

  # ======================================= fofocas
  fofocas = ""
  for _ in range(numero_fofocas):  # coleta as fofocas e separa com *
    fofocas += input() + " "

  palavra_proibida = input()

  keywords_usadas = ""
  anotando = pontos > 0
  while anotando:
    keyword = input()  # palavra que vai ser procurada
    num_keywords_achados = 0
    proibicao_aplicada = False
    keyword_repetida = False

    if keyword.lower() == "fim":  # comando para encerrar a rodada
      anotando = False
      print(f"Rodada encerrada! Pontuação final: {pontos}")
    else:
      if "_" + keyword + "_" in keywords_usadas:
        print(f"Você já investigou '{keyword}'. Tente outra.")
        keyword_repetida = True
      else:
        if palavra_proibida == keyword:
          pontos -= 5
          proibicao_aplicada = True
          print(f"Armadilha da Sueli! '{keyword}' era proibida! -5 pontos")
        else:
          palavra_em_analise = ""  # palavra da fofoca a ser comparada com a keyword

          for letra_fofoca in fofocas:
            if letra_fofoca != " ":  # ao esbarrar com o primeiro separador, o toggle é ativado
              palavra_em_analise += letra_fofoca
            else:  # se o toggle tiver sido ativado, a letra é adicionada à nova lista de fofocas_a_analisar
              if keyword == palavra_em_analise:
                pontos += 2
                num_keywords_achados += 1
              palavra_em_analise = ""  # palavra em análise é resetada

          if num_keywords_achados > 0:
            print(f"Investigação bem sucedida! '{keyword}' apareceu {num_keywords_achados} vez(es).")
          else:
            pontos -= 1
            print(f"Nada encontrado sobre '{keyword}'. -1 ponto")

        print(f"Pontuação atual: {pontos}")

        if pontos <= 0:
          print("Você ficou sem pontos! Sueli venceu essa rodada")
          anotando = False

      keywords_usadas += "_" + keyword + "_*"