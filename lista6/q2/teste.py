dic = {
  "Endrick - Brasil": {"goals": 3, "rank": 5},
  "CR7 - Portugal": {"goals": 3, "rank": 4},
  "Messi - Argentina": {"goals": 1, "rank": 2},
}


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

  return (highest_value,) + sort(
    len_limit - 1, tup[:highest_value_idx] + tup[highest_value_idx + 1 :]
  )
