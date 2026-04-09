usuario_terminal = input()
dimensao_alvo = input()
fluido_portal = input()
status_federacao = input()
acao_historico = input()
historico_dimensoes = ["C-137", "Planeta Squanch"]

print("Sistema Operacional RickOS v3.14 - Inicializando Arma de Portais...")

if fluido_portal == "Suco de Limão":
  print(
    "BURP Morty, você colocou Suco de Limão onde devia ter número! O sistema pifou!"
  )
else:
  fluido_portal = int(fluido_portal)
  analise_dimencao = dimensao_alvo.replace(" ", "")
  if usuario_terminal == "Rick Prime" or usuario_terminal == "Evil Morty":
    print("Alerta Vermelho: Variante perigosa detectada no terminal!")
  elif analise_dimencao.isalpha() and analise_dimencao.isupper():
    print("Não precisa gritar, Morty! O painel da arma não é surdo!")

  if acao_historico == "anexar":
    historico_dimensoes.append(dimensao_alvo)
    print("Rastro anexado ao final do histórico.")

  elif acao_historico == "esconder":
    print("Apagando o último rastro... Federação idiota.")
    historico_dimensoes.pop()

  elif acao_historico == "priorizar":
    print("Sobrescrevendo prioridades. Nova dimensão no topo da lista!")
    historico_dimensoes.insert(0, dimensao_alvo)

  if (
    fluido_portal >= 50
    and status_federacao == "alta"
    and len(historico_dimensoes) > 2
  ):
    print(
      "Fuga tática ativada! Saltando por múltiplas dimensões para despistar os insetos!"
    )
  elif fluido_portal < 15:
    print("Ferrou! A Arma de Portais tá quase vazia. Pega a nave, Morty!")
  elif status_federacao == "baixa" and dimensao_alvo in historico_dimensoes:
    print(
      f"Ah, já estivemos na dimensão {dimensao_alvo}. Bora encher a cara no Blips and Chitz!"
    )
  else:
    print("Preparando salto interdimensional... Wubba Lubba Dub Dub!")
