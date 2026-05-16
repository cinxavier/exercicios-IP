data = input().split(" ")


def is_digit(n: str):
  if (
    "0" in n
    or "1" in n
    or "2" in n
    or "3" in n
    or "4" in n
    or "5" in n
    or "6" in n
    or "7" in n
    or "8" in n
    or "9" in n
  ):
    return True
  return False


def save_prince(n: int, data: list[str], stamina: int, trinkets: int):
  if stamina <= 0:
    print("A correnteza está muito forte... não consigo continuar.")
    return False

  if n == len(data):
    return trinkets

  if is_digit(data[n]):
    return save_prince(n + 1, data, stamina - 1, trinkets + int(data[n]))
  if data[n] == "Linguado":
    print("Obrigada, Linguado! Vamos rápido!")
    return save_prince(n + 1, data, stamina + 1, trinkets)
  if data[n] == "Polvo":
    print("Cuidado com os servos da bruxa!")
    return save_prince(n + 1, data, stamina - 3, trinkets)
  if data[n] == "~":
    return save_prince(n + 1, data, stamina - 1, trinkets)


res = save_prince(n=0, data=data, stamina=6, trinkets=0)
if not is_digit(str(res)):
  print("O príncipe afundou... Úrsula venceu desta vez.")
else:
  print(f"Eric foi salvo! E Ariel ainda guardou {res} bugigangas na sua gruta.")
