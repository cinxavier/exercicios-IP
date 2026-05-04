game_data = [
  ["hornet_hp", 5],
  ["hp_healed", 0],
  ["silk_amount", 0],
  ["silk_used", 0],
  ["boss_hp", 140],
]


def non_dict(key, array=game_data):
  found = False
  for list_of_2 in array:
    if not found:
      if list_of_2[0] == key:
        found = True
        return list_of_2


def hornet_turn(action, game_data):
  if action == "Ferrão":
    non_dict("boss_hp", game_data)[1] -= 10


def game_system():
  print(game_data)
  hornet_turn("Ferrão", game_data)
  print(game_data)


game_system()

boo = False

print(boo)
def change(boolean):
  return not boolean

boo = change(boo)
print(boo)

