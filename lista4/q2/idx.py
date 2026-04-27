days = int(input())
target_info = []
"""
  [0] = nome (str)\\
  [1] = nivel de ameaça (int)\\
  [2] = armado (sim | nao)
"""
for day in range(days, -1, -1):
  song = input()  # nume - autor
  target_info = input().split(" - ")
  tries = input()  # try try try

  autor = song.split(" - ")[1]
  threat_level = ""

  if autor != "DJ Electrohead":
    if target_info[1] >= 7 and target_info[2] == "sim":
      threat_level = "Elite"

    elif target_info[1] >= 7 and target_info[2] == "nao":
      threat_level = "Executor"

    elif 4 <= target_info[1] < 7 and target_info[2] == "sim":
      threat_level = "Veterano"

    elif 4 <= target_info[1] < 7 and target_info[2] == "nao":
      threat_level = "Operador"

    elif target_info[1] < 4:
      threat_level = "Iniciante"
