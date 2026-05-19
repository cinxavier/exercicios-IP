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

def qsort(to_sort):
    if to_sort == []: 
        return []
    else:
        pivot = to_sort[0]
        smaller = qsort([x for x in to_sort[1:] if x < pivot])
        bigger = qsort([x for x in to_sort[1:] if x >= pivot])
        return smaller + [pivot] + bigger
