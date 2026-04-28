days = int(input())
target_info = []
favorites = [3, 5]


def getTargetClass(target_info) -> str:
  """
  target_info_interface: \\
  [0] = nome (str) \\
  [1] = nivel de ameaça (int) \\
  [2] = armado (sim | nao)
  """

  threat_level = int(target_info[1])
  isArmed = target_info[2] == "sim"

  if threat_level >= 7 and isArmed:
    return "Elite"

  elif threat_level >= 7 and isArmed:
    return "Executor"

  elif 4 <= threat_level < 7 and isArmed:
    return "Veterano"

  elif 4 <= threat_level < 7 and isArmed:
    return "Operador"

  elif threat_level < 4:
    return "Iniciante"


def calculateMission(attempts) -> bool:
  """
  tries = str[]
  """
  totalSum = 0
  for attempt in attempts:
    totalSum += int(attempt)

  isMissionPassed = totalSum % len(attempts) == 0
  return isMissionPassed


def getReflected(enemy_atks):
  """
  enemy_atks = str[]
  """

  atks_reflected = 0
  for atk in enemy_atks:
    already_calc = False
    for favorite in favorites:
      if not already_calc:  # se o ataque ja foi refletido, efetivamente, não faz nada
        if int(atk) % favorite == 0:
          atks_reflected += 1
          already_calc = True

  return atks_reflected


print("Entendo… Vamos começar do começo.")

zero_died = False
for day in range(days, -1, -1):
  if not zero_died:
    print()

    song_info = input().split(" - ")  # nume - autor
    target_info = input().split(" - ")  # nome - ameaca - armado

    song_name = song_info[0]
    song_autor = song_info[1]

    print(f"====== Restam {day} dias. ======")
    print(f"Escutando: {song_name} - {song_autor}")

    special_case = False
    if song_autor == "DJ Electrohead" and target_info[0] == "DJ Electrohead":
      print(
        "DJ Electrohead é morto na sua frente. Lhe avisaram para NÃO FALAR com ele."
      )
      special_case = True

    if not special_case:
      missionComplete = False
      print(
        f"Analisando alvo: {target_info[0]}... Classificação: {getTargetClass(target_info)}"
      )
      tries = input().split()  # try try try
      missionComplete = calculateMission(tries)

      if not missionComplete:
        print(
          "Missão Fracassou! ZERO não foi capaz de assassinar o alvo e acabou morrendo. Nunca descobrirá o que realmente aconteceu. "
        )
        zero_died = True
      else:
        print(f"Missão Completa. | Manipulação temporal: {len(tries)} tentativa(s)")
        enemy_atks = input().split()
        reflectedAtks = getReflected(enemy_atks)
        print(f"Dragão refletiu {reflectedAtks} ataque(s)!")

if not zero_died:
  print()
  print("====== FIM DAS MISSÕES ======")
  print(
    "Parabéns Subject ZERO! Seu trabalho deve ser recompensado. Nova dose do seu remédio esta aqui."
  )
