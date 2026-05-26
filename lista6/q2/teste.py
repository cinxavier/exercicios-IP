dic = {
  'item1':1,
  'item3':3,
  'item2':2,
  'item4':4,
}
def tuplefy(dic: dict) -> tuple:
  tup = ()
  for key in dic:
    tup += ((key, dic[key]),)
  return tup


# a logica disso é parecida com um bubble sort em um array, mas é um pouco mais dificil de entender pela verbosidade
def sort_dict(dic: dict):
  new_dic = {}
  tup = tuplefy(dic)
  return sorted(tup)

print(tuple(sort_dict(dic)))