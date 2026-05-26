dic = {
  "item0": 17,
  "item1": 25,
  "item2": 12,
  "item4": 64,
  "item5": 11,
  "item6": 4,
}


def tuplefy(dic: dict) -> tuple:
  tup = ()
  for key in dic:
    tup += ((key, dic[key]),)
  return tup


tup = tuplefy(dic)


def sort_by_goals(len_limit: int, tup: tuple):
  if len_limit == 0:
    return ()

  highest_value = (0,0)
  highest_value_idx = 0
  for item_idx in range(len(tup)):
    curr_value = tup[item_idx]
    if curr_value[1] > highest_value[1]:
      highest_value = curr_value
      highest_value_idx = item_idx
  return highest_value + sort_by_goals(
    len_limit - 1, tup[:highest_value_idx] + tup[highest_value_idx+1:]
  )


print(sort_by_goals(3,tup))
