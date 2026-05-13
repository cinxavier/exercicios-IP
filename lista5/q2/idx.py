pile_height = int(input())


def make_pile(n: int, array: list[int] = []):
  if n == 0:
    return array
  array.append(n)
  return make_pile(n - 1, array)


# a base é:
# 1. origin -> goal
# 2. origin -> aux
# 1. goal -> aux
# 3. origin -> goal
# 1. aux -> origin
# 2. aux -> goal
# 1. origin -> goal


def hanoi(
  n: int,  # necessario pra saber quando parar
  origin: list[int],
  aux: list[int],
  goal: list[int],
):
  if n == 0:
    return
  hanoi(n - 1, origin, aux, goal)
  hanoi(n - 1, origin, goal, aux)
  hanoi(n - 1, goal, origin, aux)
  goal.append(origin.pop())


origin = make_pile(pile_height)
aux = []
goal = []

print(origin, aux, goal)

hanoi(pile_height, origin, aux, goal)

print(origin, aux, goal)
