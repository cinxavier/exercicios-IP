numbers = "0123456789"
victory_points = 3
draw_points = 1

score = {}
br_sokers = {}


def tuplefy(dic: dict) -> tuple:
  tup = ()
  for key in dic:
    tup += (
      (
        key,
        dic[key]["points"],
        dic[key]["vic"],
        dic[key]["def"],
        dic[key]["draw"],
        dic[key]["balance"],
      ),
    )
  return tup


def sort(len_limit: int, tup: tuple):
  if len_limit == 0:
    return ()

  highest_value = ("", -1)
  highest_value_idx = 0

  for item_idx in range(len(tup)):
    curr_value = tup[item_idx]

    if curr_value[1] > highest_value[1]:  # ardenação baseada nos pontos
      highest_value = curr_value
      highest_value_idx = item_idx

    elif curr_value[1] == highest_value[1]:
      if curr_value[-1] > highest_value[-1]:  # ardenação baseada no saldo de gols
        highest_value = curr_value
        highest_value_idx = item_idx

      elif curr_value[-1] == highest_value[-1]:
        if curr_value[0] < highest_value[0]:  # ardenação alfabética
          highest_value = curr_value
          highest_value_idx = item_idx

  return (highest_value,) + sort(
    len_limit - 1, tup[:highest_value_idx] + tup[highest_value_idx + 1 :]
  )


def index(tup: tuple, value: tuple) -> int:
  for idx in range(len(tup)):
    if value in tup[idx]:
      return idx


for _ in range(6):  # fase de grupos sempre tem 6 jogos
  game = input()  # dados do jogo
  scoreboard = ()  # requisito não funcional

  br_goals = -1

  for game_data in game.split(" x "):  # retorna ["str int", "int str"]
    for team_data in game_data.split():  # retorna ["str", "int"] ou ["int", "str"]
      if team_data[0] not in numbers:  # caso seja um nome
        if team_data not in score:  # inicializa a registro da seleção
          score[team_data] = {
            "points": 0,
            "vic": 0,
            "def": 0,
            "draw": 0,
            "balance": 0,
          }
      else:  # caso seja um número
        team_data = int(team_data)  # conversão de numeros

        if "Brasil" in game_data:
          br_goals = team_data
      scoreboard += (team_data,)

  # dados dos times
  team_1_name = scoreboard[0]
  team_1_goals = scoreboard[1]

  team_2_name = scoreboard[3]
  team_2_goals = scoreboard[2]

  # saldo
  score[team_1_name]["balance"] += team_1_goals - team_2_goals
  score[team_2_name]["balance"] += team_2_goals - team_1_goals

  if team_1_goals > team_2_goals:
    score[team_1_name]["points"] += victory_points  # atribuição de pontos
    score[team_1_name]["vic"] += 1  # registro de vitória

    score[team_2_name]["def"] += 1  # registro de derrota

  elif team_1_goals < team_2_goals:
    score[team_2_name]["points"] += victory_points
    score[team_2_name]["vic"] += 1

    score[team_1_name]["def"] += 1

  else:
    score[team_1_name]["points"] += draw_points
    score[team_1_name]["draw"] += 1  # registro de vitória

    score[team_2_name]["points"] += draw_points
    score[team_2_name]["draw"] += 1

  # análise do Brasil
  while br_goals > 0:
    socker_inp = input()
    socker_data = tuple(socker_inp.split())
    br_goals -= int(socker_data[1])

    if socker_data[0] not in br_sokers:
      br_sokers[socker_data[0]] = 0
    br_sokers[socker_data[0]] += int(socker_data[1])


final_score = sort(4, tuplefy(score))
print("------- Grupo C -------")

for team_idx in range(len(final_score)):
  print(
    f"{team_idx + 1}º | {final_score[team_idx][0]} | {final_score[team_idx][1]} | {final_score[team_idx][2]} | {final_score[team_idx][3]} | {final_score[team_idx][4]} | {final_score[team_idx][5]}"
  )

br_goals = 0
for i in br_sokers:
  br_goals += br_sokers[i]

print()

print("-- Desempenho Brasileiro --")
print(f"Posição: {index(final_score, 'Brasil') + 1}")
print(f"Gols Marcados: {br_goals}")
# eu poderia teradicionado o total de gols sofridos, mas eu teria de alterar as dependências e to sem energia mental pra isso
print(f"Gols Sofridos: {br_goals - score['Brasil']['balance']}")

if len(br_sokers)> 0:
  socker_tup = ()
  for key in br_sokers:
    print(f"{key}: {br_sokers[key]}")
    socker_tup += ((key, br_sokers[key]),)


  print(
    f"Artilheiro: {tuple(sorted(socker_tup, reverse=True, key=lambda item: item[1]))[0][0]}"
  )
