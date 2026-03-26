num_pendrives = int(input())

print("Avenida Brasil: A Vingança de Nina!")

for curr in range(num_pendrives):
  print(f"Descriptografando pendrive {curr + 1} de {num_pendrives}...")
  senha = input()  # senha do pendrive
  chances = (
    len(senha) * 2
  )  # numero de chances que o cabra tem pra chutar a senha do pendrive

  erros = ""  # todas as letras que o cabra chutou e errou
  acertos = ""  # as letras que o cabra acertou

  for chance in range(chances):
    chute = input()  # letra que o chabra chutou
    if chute not in senha:  # se o chute for errado, o chute é errado
      erros += chute  # registra os erros
    else:  #verifica onde está o acerto
      acertos += chute
    
    parcial = ""
    for letra_certa in acertos:
      for letra_senha in senha: 
        if letra_senha == letra_certa:  # se acertar
          parcial += letra_certa  # põe no lugar

        else:  # senão
          parcial += "_"  # não põe... dãah

    print(parcial)
