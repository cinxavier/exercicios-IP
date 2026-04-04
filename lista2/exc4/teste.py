senha = "123"
descoberta = ""
for letra in senha:
    descoberta += "_"
    
print(senha)
while True:
    chute = input("letra: ")
    nova_descoberta = ""
    
    if chute in senha:
        for letra_senha, letra_descoberta  in zip(senha, descoberta):
            if letra_descoberta == "_" and letra_senha == chute:
                nova_descoberta += chute
            elif letra_descoberta != "_":
              nova_descoberta += letra_descoberta
            else:
                nova_descoberta += "_"
        descoberta = nova_descoberta
    
    print(descoberta)
