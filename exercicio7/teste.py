# nome1 = "n1"
# valor1 = 37

# nome2 = "n2"
# valor2 = 49

# nome3 = "n3"
# valor3 = 25


# primeiro = nome1
# v_primeiro = valor1

# segundo = nome2
# v_segundo = valor2

# terceiro = nome3
# v_terceiro = valor3


# print("valores antigos:")
# print(f"{primeiro}: {v_primeiro}")
# print(f"{segundo}: {v_segundo}")
# print(f"{terceiro}: {v_terceiro}")

# print("============================================")

# if v_primeiro < v_segundo:
#     primeiro, segundo = segundo, primeiro
#     v_primeiro, v_segundo = v_segundo, v_primeiro

# if v_primeiro < v_terceiro:
#     primeiro, terceiro = terceiro, primeiro
#     v_primeiro, v_terceiro = v_terceiro, v_primeiro

# if v_segundo < v_terceiro:
#     segundo, terceiro = terceiro, segundo
#     v_segundo, v_terceiro = v_terceiro, v_segundo

# print("valores novos:")
# print(f"{primeiro}: {v_primeiro}")
# print(f"{segundo}: {v_segundo}")
# print(f"{terceiro}: {v_terceiro}")
nome_maquina1 = "pery"

if all(l in nome_maquina1 for l in ("p","e","r","r","y")):
    print("foi")