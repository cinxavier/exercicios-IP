times = int(input())


def rec(times: int = times):
  if times == 0:
    return 0

  n = int(input())
  return n + rec(times - 1)


print(rec(times))
