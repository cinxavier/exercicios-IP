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


# transforma o dicionário em uma tupla de tuplas (key, value)
def tuplefy(dic: dict) -> tuple:
  tup = ()
  for key in dic:
    tup += ((key, dic[key]["goals"], dic[key]["ranking"]),)
  return tup


def sort_by_goals(item: tuple):
  return item[1]


def sort_by_rank(item: tuple):
  return item[1]


def sort_dict(dic: dict):
  partial_sorted_tup = tuple(sorted(tuplefy(dic), reverse=True, key=sort_by_goals))[:3]
  sorted_tup = ()
  return partial_sorted_tup


def get_history(dic: dict):
  while True:
    socker_input = input()
    if socker_input == "FIM":
      return

    if socker_input not in dic:
      dic[socker_input] = {
        "goals": 1,
        "ranking": ranking.index(socker_input.split(" - ")[1]),
      }
    else:
      dic[socker_input]["goals"] += 1


get_history(sockers)
print(sort_dict(sockers))
