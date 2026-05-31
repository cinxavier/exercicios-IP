db = {}
teams = []


def add(soccer_data: list, db: dict = db):
  jogador = soccer_data[0]
  selecao = soccer_data[1]
  soccer_id = f"{jogador} {selecao}"
  gols = soccer_data[2]
  assistencias = soccer_data[3]
  passes_certos = soccer_data[4]
  amarelos = soccer_data[5]
  vermelhos = soccer_data[6]

  if soccer_id not in db:
    db[soccer_id] = (
      selecao,
      int(gols),
      int(assistencias),
      int(passes_certos),
      int(amarelos),
      int(vermelhos),
    )
    teams.append(soccer_id)
  else:
    db[soccer_id] = (
      selecao,
      db[soccer_id][1] + int(gols),
      db[soccer_id][2] + int(assistencias),
      db[soccer_id][3] + int(passes_certos),
      db[soccer_id][4] + int(amarelos),
      db[soccer_id][5] + int(vermelhos),
    )


def delete(soccer_id: str, db: dict = db):
  name, team = soccer_id.split()[0], soccer_id.split()[1]
  if soccer_id in db:
    db.pop(soccer_id)
    teams.pop(teams.index(soccer_id))
    print(f"O jogador: {name} da seleção: {team} foi retirado do sistema")
  else:
    print(
      f"O jogador: {name} da seleção: {team} não foi encontrado insira uma outra combinação de jogador e seleção:"
    )
    new_soccer_data = input()
    delete(new_soccer_data, db)


name = 0
team = 1
goals = 2
assists = 3
passes = 4
yellow = 5
red = 6


def get_status(soccer_id: str, db: dict = db, toStr: bool = False):
  soccer_name, soccer_team = soccer_id.split()[0], soccer_id.split()[1]

  if toStr:
    if soccer_name == "Neymar":
      if "Neymar" not in db:
        return "E o pessoal tá lá: 'será que Carlo Ancelotti vai convocar o Neymar?'"

    if soccer_id not in db:
      return f"Jogador não encontrado na seleção {soccer_team}"
    else:
      soccer = db[soccer_id]
      return f"{soccer_name} ({soccer_team}): {soccer[1]}G, {soccer[2]}A, {soccer[3]}P, {soccer[4]}CA, {soccer[5]}CV"
  else:
    if soccer_id not in db:
      return False
    else:
      soccer = (soccer_name,) + db[soccer_id]
      return soccer


def sorter(highest_id: tuple, current_id: tuple, metric: int = 0):
  if current_id == highest_id:
    return False

  highest = get_status(highest_id)
  current = get_status(current_id)
  metrics = (
    (current[goals] > highest[goals], current[goals] == highest[goals]),  # mais gols
    (
      current[assists] > highest[assists],
      current[assists] == highest[assists],
    ),
    (  # mais assistencias
      current[red] < highest[red],
      current[red] == highest[red],
    ),  # menos vermelhos
    (
      current[yellow] < highest[yellow],
      current[yellow] == highest[yellow],
    ),  # menos amarelos
    (
      current[passes] > highest[passes],
      current[passes] == highest[passes],
    ),  # mais passes
    (
      current[team] < highest[team],
      current[team] == highest[team],
    ),  # alfabetico no nome do time
    (
      current[name] < highest[name],
      current[name] == highest[name],
    ),  # alfabetico no nome do jogador
  )

  if metrics[metric][0]:
    return True

  if not metrics[metric][0] and metrics[metric][1]:
    return sorter(highest_id, current_id, metric + 1)

  if not metrics[metric][0]:
    return False


def get_team_mvp(team_name: str, db: dict = db):
  soccers_ids = ()  # lista dos jogadores

  # filtro dos jogadores do time escolhido
  for key in db:
    if team_name in key:
      soccers_ids += (key,)

  # sort do melhor
  if len(soccers_ids) > 0:
    da_best_id = soccers_ids[0]

    for soccer_id in soccers_ids:
      if sorter(da_best_id, soccer_id):
        da_best_id = soccer_id

    return da_best_id  # retorno do id
  else:
    return False


def get_comp_mvp(teams_list: list, db: dict = db):
  best_soccers = ()
  if len(teams_list) > 0:
    for team_name in teams_list:
      best_soccers += (get_team_mvp(team_name, db),)

    best_soccer = best_soccers[0]
    for soccer in best_soccers:
      if sorter(best_soccer, soccer):
        best_soccer = soccer
    return best_soccer
  else:
    return False


def end(n: int, teams_list: list):
  if n == 0:
    return ()
  da_best = get_comp_mvp(teams_list)
  idx = teams_list.index(da_best)
  return (get_status(da_best),) + end(n - 1, teams_list[:idx] + teams_list[idx + 1 :])


print(
  "Bem, amigos da rede! Sistema de Estatísticas VAR Edition no ar. Aguardando comandos..."
)
running = True
while running:
  command = input()
  if "*ADD" in command:
    add_data = command.split()[1:]
    add(add_data)

  elif "*BUSCAR" in command:
    soccer_id = command.split()[1:]
    print(get_status(" ".join(soccer_id), toStr=True))

  elif "*DEL" in command:
    soccer_id = command.split()[1:]
    delete(" ".join(soccer_id))

  elif "*DESTAQUE_SELECAO" in command:
    team_name = command.split()[1]
    best_of_team = get_team_mvp(team_name)
    if best_of_team:
      soccer_data = get_status(best_of_team)
      print(
        f"Destaque da {soccer_data[team]}: {soccer_data[name]} {soccer_data[goals]} gols, {soccer_data[assists]} assistências"
      )
    else:
      print(f"Nenhum dado encontrado para a seleção {team_name}")

  elif "*BOLA_DE_OURO" in command:
    best_soccer = get_comp_mvp(teams)
    if best_soccer:
      soccer_data = get_status(best_soccer)
      print(f"Bola de Ouro atual: {best_soccer} com {soccer_data[goals]} gols")
    else:
      print("Nenhum jogador registrado no torneio")

  elif "*FIM" in command:
    running = False
    ranking = end(len(teams), teams)
    if len(ranking) > 0:
      print("Ranking Final:")
      for soccer_data_idx in range(len(ranking)):
        print(
          f"{soccer_data_idx + 1}. {ranking[soccer_data_idx][name]} ({ranking[soccer_data_idx][team]}) - G: {ranking[soccer_data_idx][goals]}, A: {ranking[soccer_data_idx][assists]}, P: {ranking[soccer_data_idx][passes]}, CA: {ranking[soccer_data_idx][yellow]}, CV: {ranking[soccer_data_idx][red]}"
        )
    else:
      print("Nenhum jogador registrado para o ranking final.")
