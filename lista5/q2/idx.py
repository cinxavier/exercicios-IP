# desde ja peço desculpas aos monitores que vao corrijir minhas respostas
# não comentei os códigos por motivos de: sem tempo irmão.
# estou evocando esse feitiço com meu grimório portátil na longa transição de senário do campo pra a base
# (tô codando pelo celular no ônibus de volta pra casa com 2 horas de viagem).

pile_height = int(input())


def make_pile(n: int, array: list[int] = []):
  if n == 0:
    return array
  array.append(n)
  return make_pile(n - 1, array)


def move(origin: list[int], goal: list[int]):
  goal.append(origin.pop())


def hanoi(
  n: int,  # necessario pra saber quando parar
  origin: list[int],
  aux: list[int],
  goal: list[int],
  moves: int,
):
  if n == 1:
    move(origin, goal)
    moves += 1

  else:
    hanoi(n - 1, origin, goal, aux, moves)
    move(origin, goal)
    moves += 1

    hanoi(n - 1, aux, origin, goal, moves)


def hanoi_moves(pile_height: int):
  if pile_height == 1:
    return pile_height

  return hanoi_moves(pile_height) + hanoi_moves(pile_height)


print(hanoi_moves(pile_height))

# origin = make_pile(pile_height)
# aux = []
# goal = []
# moves = 0

# print(origin, aux, goal)
# hanoi(pile_height, origin, aux, goal, moves)
# print(moves)

# print(origin, aux, goal)
