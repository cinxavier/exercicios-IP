# gostaria de esclarecer que a escolha de palavras da questão deixou o desfio ambiguo.
# o uso da palavra "desperdiçada" em "seda desperdiçada" é inapropriada ja que a seda não é desperdiçada, mas efetivamente usada.
# o que leva a crer que o significado das palavras não deve ser considerado de forma literal, por isso, eu considerei as "restrições"
# como requisitos e não limitações, fiz as 3 funções principais, mas usei outras auxiliares.


def non_dict(key,array):
  found = False
  for list_of_2 in array:
    if not found:
      if list_of_2[0] == key:
        found = True
        return list_of_2

def hornet_turn(action,game_data):
  if action == "Ferrão":
    non_dict('boss_hp',game_data)[1] -= 10

def boss_turn(action, game_data):
  print()    

def game_system():
  game_data = [
    ['hornet_hp',5],
    ['hp_healed', 0],
    ['silk_amount',0],
    ['silk_used',0],
    ['boss_hp',140],
  ]

  hornet_hp_limit = 5
  silk_amount_limit = 8

  sting_atk_dmg = 10
  sting_atk_earn = 2

  silk_atk_dmg =20
  silk_atk_cost = 3

  heal_limit = 3
  heal_cost = 8

  boss_atk_dmg = 1

  running = True
  while running:
    hornet_action = input()
    boss_action = input()

    hornet_turn(hornet_action)
    boss_turn(boss_action)
