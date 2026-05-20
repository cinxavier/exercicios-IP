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

def get_keys(dic: dict):
  tup = ()
  for key in dic:
    tup += (key,)
  return tup

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