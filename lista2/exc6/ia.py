print("Pega a sua trouxa, moleque. O ônibus pro sertão já vai sair.")

qtd_cidades = int(input())

print("Se ajeita nesse banco, menino, que o chacoalho vai ser grande.")
print(
  f"A gente tem {qtd_cidades} cidade(s) de poeira pela frente até achar o tal do teu pai. Presta atenção no que o povo fala..."
)

familia_encontrada = False
num_cidade = 0

while num_cidade < qtd_cidades and not familia_encontrada:
  print(
    f"Atenção, {num_cidade + 1}ª cidade! Carta de graça! A gente só quer informação da minha família em troca!"
  )

  pilha = ""
  estrutura_valida = True

  tem_id = False
  tem_endereco = False
  tem_lembranca = False

  palavra_abriu_id = ""
  palavra_abriu_end = ""

  ouviu_um_babado = False
  ouvindo_as_fofocas = True

  while ouvindo_as_fofocas:
    informacao = input()

    if informacao == "FIM":
      ouvindo_as_fofocas = False
    else:
      ouviu_um_babado = True

      tipo_informacao = ""
      keyword = ""

      # identifica tipo da informação
      if (
        "jesus" in informacao
        or "isaias" in informacao
        or "moises" in informacao
      ):
        tipo_informacao = "I"

        if "jesus" in informacao:
          keyword = "jesus"
        elif "isaias" in informacao:
          keyword = "isaias"
        else:
          keyword = "moises"

        tem_id = True

      elif "sertao" in informacao or "bom jesus" in informacao:
        tipo_informacao = "E"
        if "sertao" in informacao:
          keyword = "sertao"
        else:
          keyword = "bom jesus"
        tem_endereco = True

      else:
        tipo_informacao = "L"
        tem_lembranca = True

      # ==================== processamento do id
      if tipo_informacao == "I":
        if palavra_abriu_id == "": # se não 
          pilha += "("
          palavra_abriu_id = keyword
        else:
          if keyword == palavra_abriu_id:
            if pilha != "":
              nova_pilha = ""
              removido = False
              for caractere in pilha:
                if caractere == "(" and not removido:
                  removido = True
                else:
                  nova_pilha += caractere
              pilha = nova_pilha
            else:
              estrutura_valida = False
            palavra_abriu_id = ""
          else:
            pilha += "("
            palavra_abriu_id = keyword

      # processamento tipo endereço
      elif tipo_informacao == "E":
        if palavra_abriu_end == "":
          pilha += "{"
          palavra_abriu_end = keyword
        else:
          if keyword == palavra_abriu_end:
            if pilha != "":
              nova_pilha = ""
              removido = False
              for caractere in pilha:
                if caractere == "{" and not removido:
                  removido = True
                else:
                  nova_pilha += caractere
              pilha = nova_pilha
            else:
              estrutura_valida = False
            palavra_abriu_end = ""
          else:
            pilha += "{"
            palavra_abriu_end = keyword

      # processamento tipo lembrança
      else:
        if pilha != "":
          nova_pilha = ""
          removido = False
          for caractere in pilha:
            if not removido:
              removido = True
            else:
              nova_pilha += caractere
          pilha = nova_pilha
        else:
          pilha += "["

  # cidade sem informações
  if not ouviu_um_babado:
    print(
      "Ô cidadezinha morta, Josué. Ninguém abriu a boca pra dar um pio do teu pai. Dobra essa mesa que aqui a gente só gastou saliva à toa."
    )
  else:
    # validação final
    if (
      pilha == ""
      and estrutura_valida
      and tem_id
      and tem_endereco
      and tem_lembranca
    ):
      print("")  # update
      familia_encontrada = True
    else:
      if num_cidade != qtd_cidades - 1:
        print(
          "Essa conversa tá toda torta, um fala uma coisa, outro fala outra. Vamos embora, menino, a busca continua."
        )

  num_cidade += 1

# caso não encontre a família
if not familia_encontrada:
  print(
    "Não achamos eles nessas cidades, Dona Dora... Mas amanhã a gente bota a mesinha de novo, né? O Brasil é grande, uma hora a gente encontra."
  )
