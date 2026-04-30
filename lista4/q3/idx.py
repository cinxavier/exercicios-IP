days = int(input())
energy = 100


# bubble_sort. funciona
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
  """returna False caso falhe"""

  names = input()
  if not names:
    return False

  names_list = names.split(" ")  # lista de nomes
  sorted_list: list[str] = bubble_sort(names_list)  # lista ordenada de nomes
  energy_gen = (
    sorted_list[0] + sorted_list[len(sorted_list - 1)]
  ) * 20  # calculo da energia gerada

  return energy_gen


def yesod():
  """ 
    returna um array\\
    [0] - tem corrupção\\
    [1] - código comprimido
  """
  sequence = input()
  theres_corruption = False

  compression = ""

  prevChar = ""
  times = 0

  for char in sequence:
    if not theres_corruption:
      if char == "&":
        theres_corruption = True
        compression += str(times) + prevChar if times > 1 else prevChar

      else:
        if prevChar == "":  # se for a contagem ainda estiver no início
          # o programa inicia a contagem
          prevChar = char
          times = 1

        elif char == prevChar:  # se o char passado se repetir
          times += 1  # soma as aparições

        else:  # se um novo char aparecer
          compression += (str(times) + prevChar if times > 1 else prevChar)  # registra as aparições do char anterior   # fmt: skip
          prevChar = char  # regitra o novo char
          times = 1  # reseta a contagem

  return [theres_corruption, compression]


for day in range(days):
  sefirot = input()
  if sefirot == "Malkuth":
    malkuth()
