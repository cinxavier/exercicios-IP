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
def tuplefy(dic:dict) -> tuple:
  tup = ()
  for key in dic:
    tup += ((key, dic[key]),)
  return tup

def sort_dict(dic: dict):
  new_dic = {}
  tup = tuplefy(dic)
  for item_idx in (range(len(tup) - 2)):
    if tup[item_idx][1] < tup[item_idx][1]

def get_history():
  while True:
    socker_input = input()
    if socker_input == "FIM":
      return
    
    if socker_input not in sockers:
      sockers[socker_input] = 1
    else:
      sockers[socker_input] += 1

sockers_keys = get_keys(sockers)
def get_ranking(dic:dict, n:int):
  pivot = dic[sockers_keys[0]]  
  
  
get_history()
print(sockers)