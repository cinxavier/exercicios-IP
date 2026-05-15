# desde ja peço desculpas aos monitores que vao corrijir minhas respostas
# não comentei os códigos por motivos de: sem tempo irmão.
# estou evocando esse feitiço com meu grimório portátil na longa transição de senário da BF pra a base
# (tô codando pelo celular no ônibus de volta pra casa com 2 horas de viagem. Sem comentários, literalmente).

pile_height = int(input())


def make_pile(n: int,array = []):
  if n == 0:
    return array
  array.append(n)
  return make_pile(n - 1, array)


def move(origin, goal):
  goal.append(origin.pop())


def hanoi(
  n: int,  # necessario pra saber quando parar
  origin,
  aux,
  goal,
):
  if n == 1:
    move(origin, goal)

  else:
    hanoi(n - 1, origin, goal, aux)
    move(origin, goal)

    hanoi(n - 1, aux, origin, goal)


def hanoi_moves(pile_height: int) -> int:
  if pile_height == 1:
    return pile_height
  if pile_height == 2:
    return pile_height + 1

  return hanoi_moves(pile_height - 1) * 2 + 1


origin = make_pile(pile_height)
aux = []
goal = []
moves = hanoi_moves(pile_height)

hanoi(pile_height, origin, aux, goal)

print(
  f"Bela moveu os {pile_height} livros em {moves} movimentos para o Pedestal de Marfim."
)
