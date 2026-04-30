days = int(input())
energy = 100


def bubble_sort(list: list[str]) -> list[str]:
  list_copy = list.copy()
  for el_idx in range(len(list_copy)):
    for compare_idx in range(len(list_copy)):
      if len(list_copy[el_idx]) > len(list_copy[compare_idx]):
        list_copy[el_idx], list_copy[compare_idx] = (
          list_copy[compare_idx],
          list_copy[el_idx],
        )
  return list_copy


def malkuth():
  names = input()
  if not names:
    return False

  names_list = names.split(" ")
  sorted_list: list[str] = bubble_sort(names_list)
  energy_gen = (sorted_list[0] + sorted_list[len(sorted_list - 1)]) * 20

  return energy_gen

def yesod():
  sequence = input()
  compression = ""
  for char in sequence:
    

for day in range(days):
  sefirot = input()
  if sefirot == "Malkuth":
    malkuth()
  elif sefirot == "":

