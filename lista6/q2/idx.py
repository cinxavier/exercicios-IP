ranking = (
  "França",
  "Espanha",
  "Argentina",
  "Inglaterra",
  "Portugal",
  "Brasil",
  "Holanda",
  "Marrocos",
  "Bélgica",
  "Alemanha",
  "Croácia",
  "Colômbia",
  "Senegal",
  "México",
  "Estados Unidos",
  "Uruguai",
  "Japão",
  "Suíça",
  "Irã",
  "Turquia",
  "Equador",
  "Áustria",
  "Coreia Do Sul",
  "Australia",
  "Argélia",
  "Egito",
  "Canadá",
  "Noruega",
  "Panamá",
  "Costa Do Marfim",
  "Suécia",
  "Paraguai",
  "Tchéquia",
  "Escócia",
  "Tunísia",
  "Républica Democrática Do Congo",
  "Uzbequistão",
  "Catar",
  "Iraque",
  "Africa Do Sul",
  "Arábia Saudita",
  "Jordânia",
  "Bósnia-Herzgovina",
  "Cabo Verde",
  "Gana",
  "Curaçao",
  "Haiti",
  "Nova Zelândia",
)

sockers = {}


# transforma o dicionário em uma tupla de tuplas (key, (goals, rank))
def tuplefy(dic: dict) -> tuple:
  tup = ()
  for key in dic:
    tup += (
      (
        key.split(" - ")[0],
        dic[key]["goals"],
        dic[key]["rank"],
      ),
    )
  return tup


def sort(len_limit: int, tup: tuple):
  if len_limit == 0:
    return ()

  # -1 é para evitar problemas com jogadores (tipo o Gabriel Jesus na copa de 2018 e 2022) que marcaram 0 gols
  highest_value = ("Fernandinho - Brasil", -1, 0)  # ele fez -1 gols na copa de 2018   # fmt: skip
  highest_value_idx = 0

  for item_idx in range(len(tup)):
    curr_value = tup[item_idx]

    if curr_value[1] > highest_value[1]:
      highest_value = curr_value
      highest_value_idx = item_idx

    elif curr_value[1] == highest_value[1]:
      if curr_value[2] < highest_value[2]:
        highest_value = curr_value
        highest_value_idx = item_idx

      elif curr_value[2] == highest_value[2]:
        

  return (highest_value,) + sort(
    len_limit - 1, tup[:highest_value_idx] + tup[highest_value_idx + 1 :]
  )


def get_history(dic: dict):
  while True:
    socker_input = input()
    if socker_input == "FIM":
      return

    if socker_input not in dic:
      dic[socker_input] = {
        "goals": 1,
        "rank": ranking.index(socker_input.split(" - ")[1]),
      }
    else:
      dic[socker_input]["goals"] += 1


get_history(sockers)
podium = sort(3, tuplefy(sockers))

print("Somente o melhor deve ser lembrado")
print(f"O artilheiro foi {podium[0][0]} com {podium[0][1]} gols")
print(
  f"Eu poderia falar do {podium[1][0]} mas ele é somente o primeiro a ser esquecido"
)
print(f"O {podium[2][0]} então, nem pensar")
