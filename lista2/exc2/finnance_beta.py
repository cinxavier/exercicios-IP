dinheiro_inicial = int(input())
qtd_compras = 0
custo_total = 0
amauri_action = False
runnig = True

print(f"A família possui {dinheiro_inicial} ainda, talvez ele fique tranquilo hoje")
while runnig:
  compra = input()

  if compra == "Amauri":
    print("Sabia que vocês estão loucos, hora de encerrar essa loucura!")
    amauri_action = True
    runnig = False
  else:
    custo = int(input())

    if custo <= dinheiro_inicial:
      custo_total += custo
      qtd_compras += 1
      dinheiro_inicial -= custo

      if custo > 500000:
        print(f"Enlouqueceram de vez {custo} reais num(a) {compra}")
      elif custo < 1000:
        print(f'Será que se acalmaram?! {compra} por "somente" {custo} reais')
      else:
        print(f"Gastaram {custo} reais para comprar um(a) {compra}")

      if compra == "carro":
        modelo = input()
        if modelo == "chevette":
          print("chevette : Relembrando as origens será?")
        if modelo == "jeep":
          print("jeep : Será que ele tá se preparando para outra aventura que não irá?")
        if modelo == "bmw":
          print("bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁")

    if dinheiro_inicial <= 0 or dinheiro_inicial - custo < 0:
      print("Enlouqueceram? Vocês estão falidos")
      runnig = False
if not amauri_action:
  print(f"{qtd_compras} - {custo_total} reais")
