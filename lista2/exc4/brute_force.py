num_pendrives = int(input())
pen_abertos = 0
print("Avenida Brasil: A Vingança de Nina!")

for num_pen_atual in range(num_pendrives):
  print(f"Descriptografando pendrive {num_pen_atual + 1} de {num_pendrives}...")

  senha = input()  # senha do pendrive
  chances = (
    len(senha) * 2
  )  # numero de chances que o cabra tem pra chutar a senha do pendrive
  letras_chutadas = ""  # todas as letras que o cabra chutou e errou
  descoberta = ""  # as letras que o cabra acertou
  tentativas = 0  # numero de tentativas que o cabra já fez
  for letra in senha:
    if letra == " ":  # se a letra for um espaço
      descoberta += " "  # continua sendo um espaço
    else:
      descoberta += "_"  # mas letras são letras

  for chance in range(chances):
    if (
      descoberta != senha and tentativas <= chances
    ):  # enquanto o cabra não tiver descoberto a senha, o jogo continua
      tentativas += 1
      chute = input()  # letra que o chabra chutou
      nova_descoberta = ""  # holder pra a nova resposta

      if chute in letras_chutadas:
        print("Max: Ele já tentou isso, Carminha...")
      else:
        for letra_senha, letra_descoberta in zip(senha, descoberta):
          letras_chutadas += chute  # adiciona o chute às letras chutadas
          if letra_descoberta == "_":  # se a resposta for inédita
            if letra_senha == chute:  # e se o chute for correto
              nova_descoberta += chute

            else:  # se o chute for errado, mantém o espaço vazio
              nova_descoberta += "_"
          else:
            nova_descoberta += letra_descoberta  # mantém a resposta já descoberta
        if chute in senha:
          print("Nina: Boa, Tufão! Menos uma mentira da Carminha.")
        else:
          print("Carminha: Você é um idiota, Tufão! Isso não faz sentido.")
        descoberta = nova_descoberta  # a descoberta é atualizada
      print(f"Senha: {descoberta}")  # mostra a descoberta atualizada
  if descoberta == senha and tentativas <= chances:
    print(
      f"Tufão: Agora eu sei de toda a verdade! O pendrive {num_pen_atual +1} está aberto."
    )
    pen_abertos += 1
  else:
    print(
      f"Carminha: Consegui! As fotos do pendrive {num_pen_atual + 1} estão a salvo comigo."
    )

print(f"Conseguimos abrir {pen_abertos} de {num_pendrives} pendrives!")

percent_acertos = (pen_abertos / num_pendrives) * 100
if percent_acertos == 0:
  print("Tufão continuará sendo enganado para sempre...")
elif 0 < percent_acertos <= 50:
  print("Tufão descobriu algumas coisas, mas Carminha ainda tem poder.")

elif 50 < percent_acertos < 100:
  print("A casa caiu para a Carminha! Quase todas as provas foram recuperadas.")

elif percent_acertos == 100:
  print("Justiça por Rita! Todas as provas estão nas mãos de Tufão.")
