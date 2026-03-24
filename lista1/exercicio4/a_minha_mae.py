carne_misteriosa = float(input(""))
queijo_radioativo = float(input(""))
molho_especial = float(input(""))

if carne_misteriosa <= 0 or queijo_radioativo <= 0 or molho_especial <= 0:
    print("Vocês destruíram o parque! ESTÃO DESPEDIDOS!")
    exit()

print("A receita não explodiu!")
if carne_misteriosa == queijo_radioativo == molho_especial:
    print("Todas as medidas são iguais. Vocês criaram o Hambúrguer Supremo do Caos!")

elif carne_misteriosa > queijo_radioativo and carne_misteriosa > molho_especial:
    print("Havia muita carne! O Musculoso vai adorar esse Bifão de Dinossauro!")

elif queijo_radioativo > carne_misteriosa and queijo_radioativo > molho_especial:
    print("Tem queijo pra todo lado! Criamos uma Lasanha Dimensional!")

elif molho_especial > carne_misteriosa and molho_especial > queijo_radioativo:
    print("Panela cheia de molho e sorriso no rosto, criamos o Strogonoff da Paz!")
elif (
    molho_especial == carne_misteriosa
    or molho_especial == queijo_radioativo
    or queijo_radioativo == carne_misteriosa
):
    print("Tá tudo girando! Acabamos de criar um Buraco Negro Culinário!")
    
print("OOOOOOOH! Mandaram bem, caras!")
