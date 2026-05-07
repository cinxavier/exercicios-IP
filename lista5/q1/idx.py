days = int(input())
# eu acho que sem essa questão eu nunca descobriria
# que anão em ingles é dwarf kkkkkkk parece o nome do dwight de the office
dwarves = 7


def count_fibonacci(num: int):
  if num <= 1:
    return num
  previous_num = count_fibonacci(num - 1)
  before_previous = count_fibonacci(num - 2)
  return previous_num + before_previous


apples = count_fibonacci(days)
print("Espelho, espelho meu, quantas maçãs a árvore deu?")
print(f"A árvore rendeu {apples} maçãs no dia {days}.")

if apples < dwarves:
  print("Oh não! A colheita não foi suficiente para os sete anões.")
else:
  rest = apples % dwarves
  print(
    f"Cada anão receberá {int(apples / dwarves)} maçã(s) e Branca de Neve ficará com a sobra de {rest} maçã(s)."
  )
  if rest == 0:
    print("A divisão foi perfeita! Nenhuma maçã sobrou para a torta da Branca de Neve.")
