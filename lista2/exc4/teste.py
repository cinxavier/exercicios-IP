senha = "123"
linhas = ""
for n in senha:
  linhas += "_"

strings = list(zip(senha, linhas))
print(strings)
while True:
  char = str(input("letra: "))

  for i in strings:
    print(i[0], i[1])
    if i[0] == char and i[1] == "_":
      i = ("1","2") 

  parte_senha = ""
  for i in strings:
    parte_senha += i[1]

  print(parte_senha)