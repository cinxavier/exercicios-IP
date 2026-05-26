def get_keys(dic: dict) -> tuple:
  tup = ()
  for key in dic:
    tup += ((key, dic[key]),)
  return tup


dic = {
  "item2": 2,
  "item3": 3,
  "item1": 1,
}

print(dict((get_keys(dic))))