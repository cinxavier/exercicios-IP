pile_height = int(input())


def make_pile(n: int, array: list[int] = []):
  if n == 0:
    return array
  array.append(n)
  return make_pile(n - 1, array)


def hanoi(n:int, origin:list[int], aux:list[int], goal:list[int]):
  if n == 0:
    return
  hanoi(n - 1, origin, goal, aux)
  goal.append(origin.pop())
  hanoi(n - 1, goal, aux, origin)


origin = make_pile(pile_height)
aux = []
goal = []

print(origin, aux, goal)

hanoi(pile_height, origin, goal, aux)

print(origin, aux, goal)
