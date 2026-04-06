qtd_cidades = int(input())

print("Pega a sua trouxa, moleque. O ônibus pro sertão já vai sair.")
print(
  f"Se ajeita nesse banco, menino, que o chacoalho vai ser grande. A gente tem {qtd_cidades} cidade(s) de poeira pela frente até achar o tal do teu pai. Presta atenção no que o povo fala..."
)

achou_pai = False
cidade = 0
viajando = cidade < qtd_cidades
while viajando:
  cidade += 1
  viajando = cidade < qtd_cidades

  tem_E = False
  tem_I = False
  tem_L = False
  print(
    f"Atenção, {cidade}ª cidade! Carta de graça! A gente só quer informação da minha família em troca!"
  )

  pilha = ""
  # id -> ()
  # en -> {}
  # le -> []
  sinais_abertos = ""

  ultimo_sinal_aberto = ""
  tipo_ultimo_sinal_aberto = ""  # I, E ou L

  ouvindo = True
  while ouvindo:
    entrada = input()
    tipo_entrada = ""  # I, E ou L
    if entrada == "FIM":
      ouvindo = False
      if (not tem_I or not tem_E or not tem_L) and pilha == "":
        if cidade < qtd_cidades:
          print("Ô cidadezinha morta, Josué. Ninguém abriu a boca pra dar um pio do teu pai. Dobra essa mesa que aqui a gente só gastou saliva à toa.")
        
      elif tem_I and tem_E and tem_L and pilha == "":
        print("A história bateu, Josué. O povo falou a mesma coisa. Pega tuas coisas que a gente achou o caminho do teu pai.")
        viajando = False
        achou_pai = True
      else:
        if cidade < qtd_cidades:
          print("Essa conversa tá toda torta, um fala uma coisa, outro fala outra. Vamos embora, menino, a busca continua.")
    else:
      entrada += " "

      if (
        "sertao" in entrada or "bom jesus" in entrada
      ):  # se for do tipo endereco
        tipo_entrada = "E"
      elif (
        "jesus" in entrada or "isaias" in entrada or "moises" in entrada
      ):  # se for do tipo id
        tipo_entrada = "I"
      else:  # se for do tipo lembrança
        tipo_entrada = "L"

      if ultimo_sinal_aberto != "":  # se tiver algum sinal aberto
        if (
          "j" in ultimo_sinal_aberto
          or "i" in ultimo_sinal_aberto
          or "m" in ultimo_sinal_aberto
        ):
          tipo_ultimo_sinal_aberto = "I"
        elif "s" in ultimo_sinal_aberto or "b" in ultimo_sinal_aberto:
          tipo_ultimo_sinal_aberto = "E"
        else:
          tipo_ultimo_sinal_aberto = "L"

      if tipo_entrada != "L":
        if "bom jesus" in entrada:
          entrada = "b"
        elif "jesus" in entrada:
          entrada = "j"
        elif "isaias" in entrada:
          entrada = "i"
        elif "moises" in entrada:
          entrada = "m"
        elif "sertao" in entrada:
          entrada = "s"
      else:
        entrada = "L"
      # ===================================== identidade
      if tipo_entrada == "I":
        if entrada != ultimo_sinal_aberto:  # e se não tiver nenhum id aberto
          sinais_abertos = (
            entrada + "-" + sinais_abertos
          )  # abre o id pela esquerda
          ultimo_sinal_aberto = entrada  # guarda o último id aberto
          pilha = ")" + pilha  # adiciona o símbolo de id na pilha à esquerda

        else:  # se for o mesmo id do último aberto
          novo_ids_abertos = ""
          nova_pilha = ""
          ultimo_id_removido = False
          ultima_pilha_removido = False

          for id in sinais_abertos:
            if not ultimo_id_removido:  # se ainda não removeu o último id aberto não add ele na nova pilha
              ultimo_sinal_aberto = ""
              if id == "-":
                ultimo_id_removido = True
            else:
              if ultimo_sinal_aberto == "":
                ultimo_sinal_aberto = id
              novo_ids_abertos += id
          sinais_abertos = novo_ids_abertos  # remove o ultimo id pela esquerda

          for simbolos in pilha:
            if (
              not ultima_pilha_removido
            ):  # mesma lógica do id, só que para a pilha
              ultima_pilha_removido = True
            else:
              nova_pilha = simbolos + nova_pilha
          pilha = nova_pilha
          tem_I = True
      # ==================================== endereço
      elif tipo_entrada == "E":  # se for do tipo endereço
        if (
          entrada != ultimo_sinal_aberto
        ):  # e se não tiver nenhum endereco aberto
          sinais_abertos = (
            entrada + "-" + sinais_abertos
          )  # abre o endereco pela esquerda
          ultimo_sinal_aberto = entrada  # guarda o último endereco aberto
          pilha = (
            "}" + pilha
          )  # adiciona o símbolo de endereco na pilha à esquerda

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
          tem_E = True

      # ==================================== lembrança
      elif tipo_entrada == "L":  # se for do tipo lembrança
        if (
          tipo_entrada != tipo_ultimo_sinal_aberto
        ):  # e se não tiver nenhuma lembrança aberta
          sinais_abertos = (
            entrada + "-" + sinais_abertos
          )  # abre a lembrança pela esquerda
          ultimo_sinal_aberto = entrada  # guarda a última lembrança aberta
          pilha = (
            "]" + pilha
          )  # adiciona o símbolo de lembrança na pilha à esquerda

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
          tem_L = True

if not achou_pai:
  print("Não achamos eles nessas cidades, Dona Dora... Mas amanhã a gente bota a mesinha de novo, né? O Brasil é grande, uma hora a gente encontra.")
else:
    print("------------------------------------------------------------")
    print("✅ Pistas confirmadas. Josué encontrou os irmãos e uma carta de seu pai.")
    print("A missão de Dora terminou. Pela janela do ônibus, ela escreve para o menino que deixou para trás:")
    print("✉️ Dora: 'Você tem razão. Seu pai ainda vai aparecer e, com certeza, ele é tudo aquilo que você diz que ele é.'")
    print("✉️ Dora: 'Quando você estiver cruzando as estradas no seu caminhão enorme, espero que você lembre que fui eu a primeira pessoa a te fazer botar a mão no volante.'")
    print("✉️ Dora: 'No dia que você quiser lembrar de mim, dá uma olhada no retratinho que a gente tirou junto... Tenho medo que um dia você também me esqueça. Tenho saudade de tudo.'")
