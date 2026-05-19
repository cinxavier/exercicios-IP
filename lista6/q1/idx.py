num_of_teams = int(input())
score = {
  "fase de grupos": {},
  "oitavas": {},
  "quartas": {},
  "semifinal": {},
  "final": {},
}

for _ in range(num_of_teams):
  is_running = True
  team_name = ""

  while is_running:
    champ_data = input()
    if champ_data == "*":
      is_running = False
    else:
      if team_name == "":
        team_name = champ_data
      else:
        champ_data = champ_data.split(maxsplit=-1)
        stage, team_score = " ".join(champ_data[:-1]), champ_data[-1]
        score[stage][team_name] = int(team_score)
        

def arith_mean(dic: dict):
  stages = dic.keys()
  res = {'arith_mean': 0, 'stage': ''}
  for stage in stages:
    teams = dic[stage].keys()
    if len(teams) > 1:
      total = 0
      for team in teams:
        total += dic[stage][team]

      m = total / len(teams)
      if m > res["arith_mean"]:
        res["arith_mean"] = m
        res["stage"] = stage

  return res["stage"]


arith_mean = arith_mean(score)
print(arith_mean)


stages = score.keys()
for stage in stages:
  if len(score[stage]) > 0:
    print()
    print(stage)

    teams = score[stage].keys()
    for team in list(teams):
      print(f"{team} - {score[stage][team]}")

# if "arith_mean" in score[stage]:
        #   score[stage]["arith_mean"] += int(team_score)
        # else:
        #   score[stage]["arith_mean"] = 0

# def sort(dic: dict, keys_list: list):
#   for _ in range(len(keys_list) // 2 + 1):
#     for k_idx in range(len(keys_list) - 1):
#       curr_key = keys_list[k_idx]
#       next_key = keys_list[k_idx + 1]


#       if dic[curr_key] < dic[next_key]:
#         keys_list[k_idx], keys_list[k_idx + 1] = keys_list[k_idx + 1], keys_list[k_idx]
#   return keys_list
