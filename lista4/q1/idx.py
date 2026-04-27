# variaveis

game_data = [
  ["hornet_hp", 5],
  ["hornet_hp_healed", 0],
  ["silk_amount", 0],
  ["silk_created", 0],
  ["silk_used", 0],
  ["boss_hp", 140],
]

# regras do jogo
hornet_hp_limit = 5
silk_amount_limit = 8
sting_atk_dmg = 10
sting_atk_earn = 2
silk_atk_dmg = 20
silk_atk_cost = 3
heal_limit = 3
heal_cost = 8
boss_atk_dmg = 1


# key (str)                 - palavra-chave da estrutura de dados que não é um objeto\\
# array ([[str, int]])  - estrutura de dados que não é um objeto
def get(key, array=game_data):
  """
    hornet_hp\\
    hp_healed\\
    hornet_hp_healed\\
    silk_amount\\
    silk_created\\
    silk_used\\
    boss_hp
  """
  found = False
  for list_of_2 in array:
    if not found:
      if list_of_2[0] == key:
        found = True
        return list_of_2[1]


def put(key, array=game_data):
  """
    hornet_hp\\
    hp_healed\\
    hornet_hp_healed\\
    silk_amount\\
    silk_created\\
    silk_used\\
    boss_hp
  """
  found = False
  for list_of_2 in array:
    if not found:
      if list_of_2[0] == key:
        found = True
        return list_of_2


def hornet_turn(action):
  if action == "Ferrão":
    put("boss_hp")[1] -= sting_atk_dmg  # boss perde hp
  
    put("silk_amount")[1] += sting_atk_earn  # faz mas seda
    put("silk_created")[1] += sting_atk_earn  # registra que fez mais seda

    if get("silk_amount") > silk_amount_limit:
      put("silk_amount")[1] = silk_amount_limit


  elif action == "Ataque de Seda":
    if get("silk_amount") >= silk_atk_cost:  # se hornet tiver seda o suficiente
      put("boss_hp")[1] -= silk_atk_dmg  # boss perde hp
      put("silk_amount")[1] -= silk_atk_cost  # hornet usa seda
      put("silk_used")[1] += silk_atk_cost  # registra a seda usada

  elif action == "Vincular":
    if get("silk_amount") >= heal_cost:  # se hornet tiver seda o suficiente
      if get("hornet_hp") < hornet_hp_limit - heal_limit:  # se o hp da hornet for menor do que a cura máxima possivel   # fmt: skip
        put("hornet_hp")[1] += heal_limit  # ela cura o máximo possivel
        put("hornet_hp_healed")[1] += heal_limit  # registra o hp restaurado

        put("silk_amount")[1] -= heal_cost  # remove o que usou
        put("silk_used")[1] += heal_cost  # remove o que usou

      else:  # se o hp não estiver tão baixo
        hp_need = hornet_hp_limit - get("hornet_hp")  # calcula o quanto ela precisa
        put("hornet_hp")[1] += hp_need  # ela se cura completamente sem ultrapassar o limite   # fmt: skip
        put("hornet_hp_healed")[1] += hp_need  # registra o quanto ela se curou
        put("silk_amount")[1] -= heal_cost  # remove o que usou
        put("silk_used")[1] += heal_cost  # remove o que usou


def boss_turn(action):
  if action == "Acerto":
    put("hornet_hp")[1] -= boss_atk_dmg
  if action == "Acerto Duplo":
    put("hornet_hp")[1] -= boss_atk_dmg * 2


def game_system():
  running_game = True
  if get("hornet_hp") <= 0:
    print("Hornet: Hm?")
    print(f"Vida Restante: {get('boss_hp')}")
    running_game = False

  elif get("boss_hp") <= 0:
    print("RESULTADOS DA BATALHA")
    print(f"Máscaras restantes: {get('hornet_hp')}")
    print(f"Máscaras recuperadas: {get('hornet_hp_healed')}")
    print(f"Seda restante: {get('silk_amount')}")
    print(f"Seda desperdiçada: {get('silk_created') - get('silk_used')}")
    print()
    print("Hornet: Não cairei tão fácil.")
    running_game = False

  return running_game


boss_name = input()

if boss_name == "Tessela":
  print("Tessela: Ha Ha Ha! Parece que a aranha retornou.")
elif boss_name == "Grande Mãe Seda":
  print("Hornet: Monarca, seu reino de tirania acaba aqui!")
elif boss_name == "A Última Juíza":
  print("Hornet: Não posso recuar agora, a cidadela está logo ali.")
else:
  print(f"Hornet: {boss_name}, levante sua lâmina!")

print()

running = True
while running:
  hornet_action = input()
  hornet_turn(hornet_action)
  running = game_system()

  if running:
    boss_action = input()
    boss_turn(boss_action)
    running = game_system()
