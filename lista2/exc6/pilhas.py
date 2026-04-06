pilha = ""
# id -> ()
# en -> {}
# le -> []
sinais_abertos = ""

ultimo_sinal_aberto = ""
tipo_ultimo_sinal_aberto = ""  # I, E ou L

ouvindo = True
while ouvindo:
  entrada = input("escreva: ")
  tipo_entrada = ""  # I, E ou L
  if entrada == "FIM":
    ouvindo = False
  else:
    if "a" in entrada or "b" in entrada:  # se for do tipo id
      tipo_entrada = "I"
    elif "1" in entrada or "2" in entrada:  # se for do tipo endereco
      tipo_entrada = "E"
    else:  # se for do tipo lembrança
      tipo_entrada = "L"

    if ultimo_sinal_aberto != "":  # se tiver algum sinal aberto
      if "a" in ultimo_sinal_aberto or "b" in ultimo_sinal_aberto:
        tipo_ultimo_sinal_aberto = "I"
      elif "1" in ultimo_sinal_aberto or "2" in ultimo_sinal_aberto:
        tipo_ultimo_sinal_aberto = "E"
      else:
        tipo_ultimo_sinal_aberto = "L"
    
    # ===================================== identidade
    if tipo_entrada == "I":
      if entrada != ultimo_sinal_aberto:  # e se não tiver nenhum id aberto
        sinais_abertos = entrada + "-" + sinais_abertos  # abre o id pela esquerda
        ultimo_sinal_aberto = entrada  # guarda o último id aberto
        pilha = ")" + pilha  # adiciona o símbolo de id na pilha à esquerda

      else:  # se for o mesmo id do último aberto
        novo_ids_abertos = ""
        nova_pilha = ""
        ultimo_id_removido = False
        ultima_pilha_removido = False

        for id in sinais_abertos:
          if (
            not ultimo_id_removido
          ):  # se ainda não removeu o último id aberto não add ele na nova pilha
            ultimo_sinal_aberto = ""
            if id == "-":
              ultimo_id_removido = True
          else:
            if ultimo_sinal_aberto == "":
              ultimo_sinal_aberto = id
            novo_ids_abertos += id
        sinais_abertos = novo_ids_abertos  # remove o ultimo id pela esquerda

        for simbolos in pilha:
          if not ultima_pilha_removido:  # mesma lógica do id, só que para a pilha
            ultima_pilha_removido = True
          else:
            nova_pilha = simbolos + nova_pilha
        pilha = nova_pilha

    # ==================================== endereço
    elif tipo_entrada == "E":  # se for do tipo endereço
      if (
        entrada != ultimo_sinal_aberto
      ):  # e se não tiver nenhum endereco aberto
        sinais_abertos = (
          entrada + "-" + sinais_abertos
        )  # abre o endereco pela esquerda
        ultimo_sinal_aberto = entrada  # guarda o último endereco aberto
        pilha = "}" + pilha  # adiciona o símbolo de endereco na pilha à esquerda

      else:  # se for o mesmo endereco do último aberto
        novo_enderecos_abertos = ""
        nova_pilha = ""
        ultimo_endereco_removido = False
        ultima_pilha_removido = False

        for endereco in sinais_abertos:
          if not ultimo_endereco_removido:  # se ainda não removeu o último endereco aberto não add ele na nova pilha
            ultimo_sinal_aberto = ""
            if endereco == "-":
              ultimo_endereco_removido = True
          else:
            if ultimo_sinal_aberto == "":
              ultimo_sinal_aberto = endereco
            novo_enderecos_abertos += endereco
        sinais_abertos = (
          novo_enderecos_abertos  # remove o ultimo endereco pela esquerda
        )

        for simbolos in pilha:
          if (
            not ultima_pilha_removido
          ):  # mesma lógica do endereco, só que para a pilha
            ultima_pilha_removido = True
          else:
            nova_pilha += simbolos
        pilha = nova_pilha

    # ==================================== lembrança
    elif tipo_entrada == "L":  # se for do tipo lembrança
      if (
        tipo_entrada != tipo_ultimo_sinal_aberto
      ):  # e se não tiver nenhuma lembrança aberta
        sinais_abertos = (
          entrada + "-" + sinais_abertos
        )  # abre a lembrança pela esquerda
        ultimo_sinal_aberto = entrada  # guarda a última lembrança aberta
        pilha = "]" + pilha  # adiciona o símbolo de lembrança na pilha à esquerda

      else:  # se for a mesma lembrança do último aberto
        nova_lembrancas_abertas = ""
        nova_pilha = ""
        ultima_lembranca_removida = False
        ultima_pilha_removido = False

        for lembranca in sinais_abertos:
          if not ultima_lembranca_removida:  # se ainda não removeu a última lembrança aberta não add ela na nova pilha
            ultimo_sinal_aberto = ""
            if lembranca == "-":
              ultima_lembranca_removida = True
          else:
            if ultimo_sinal_aberto == "":
              ultimo_sinal_aberto = lembranca
            nova_lembrancas_abertas += lembranca
        sinais_abertos = (
          nova_lembrancas_abertas  # remove a última lembrança pela esquerda
        )

        for simbolos in pilha:
          if (
            not ultima_pilha_removido
          ):  # mesma lógica da lembrança, só que para a pilha
            ultima_pilha_removido = True
          else:
            nova_pilha += simbolos
        pilha = nova_pilha
    print("pilha: ",pilha)
    print("sinais_abertos: ",sinais_abertos)
    print("ultimo_sinal_aberto: ",ultimo_sinal_aberto)
    print("tipo_ultimo_sinal_aberto: ",tipo_ultimo_sinal_aberto)
    print("tipo_entrada: ",tipo_entrada)
