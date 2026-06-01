db = {}
times = 5


for _ in range(times):  # produtos
  name = input()
  db[name] = 0


for i in range(times):  # produtos
  value = int(input())
  for idx, key in zip(range(len(db)), db):
    if idx == i:
      db[key] = value

min_value = int(input())
found_items = 0

for key in db:
  if db[key] < min_value:
    found_items += 1

if found_items == 0:
  print("ok")
else:
  print(found_items)
