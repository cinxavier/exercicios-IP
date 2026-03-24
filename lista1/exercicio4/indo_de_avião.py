ingredients = [
    ("carne_misteriosa", float(input())),
    ("queijo_radioativo", float(input())),
    ("molho_especial", float(input())),
]
last_ingredient = len(ingredients) - 1

recipes_by_most_ingredients = {
    "carne_misteriosa": {
        "name": "Bifão de Dinossauro",
        "phrase": "Havia muita carne! O Musculoso vai adorar esse Bifão de Dinossauro!",
    },
    "queijo_radioativo": {
        "name": "Lasanha Dimensional",
        "phrase": "Tem queijo pra todo lado! Criamos uma Lasanha Dimensional!",
    },
    "molho_especial": {
        "name": "Strogonoff da Paz",
        "phrase": "Panela cheia de molho e sorriso no rosto, criamos o Strogonoff da Paz!",
    },
    "two": {
        "name": "Buraco Negro Culinário",
        "phrase": "Tá tudo girando! Acabamos de criar um Buraco Negro Culinário!",
    },
    "perfect": {
        "name": "Hambúrguer Supremo",
        "phrase": "Todas as medidas são iguais. Vocês criaram o Hambúrguer Supremo do Caos!",
    },
}

is_black_hole = None
is_perfect = None
food_made = ""


def sortMostOne(e):
    return e[1]


ingredients.sort(key=sortMostOne, reverse=True)

is_black_hole = False if ingredients[0][1] != ingredients[1][1] else True
is_perfect = (
    True if ingredients[0][1] == ingredients[1][1] == ingredients[2][1] else False
)

if ingredients[last_ingredient][1] <= 0:
    print("Vocês destruíram o parque! ESTÃO DESPEDIDOS!")
    exit()

print("A receita não explodiu!")

if is_perfect:
    food_made = recipes_by_most_ingredients["perfect"]["name"]
    print(recipes_by_most_ingredients["perfect"]["phrase"])
    
elif is_black_hole:
    food_made = recipes_by_most_ingredients["two"]["name"]
    print(recipes_by_most_ingredients["two"]["phrase"])

elif ingredients[0][0] in recipes_by_most_ingredients.keys():
    food_made = recipes_by_most_ingredients[ingredients[0][0]]["name"]
    print(recipes_by_most_ingredients[ingredients[0][0]]["phrase"])
  


print("OOOOOOOH! Mandaram bem, caras!")