inp_bin = input()
initial_int = 0  # número em formato decimal
goal_int = 88
num_of_operations = 0

prev_bin = inp_bin
bin_holder = list(inp_bin)  # auxiliar para a inversão do binário

print("bin_holder:", bin_holder)

# inversão da lista, pra converter bin -> int
for idx in range(len(bin_holder)):
  last_idx = len(bin_holder) - idx - 1
  if idx >= last_idx:
    bin_holder[idx], bin_holder[last_idx] = (
      bin_holder[last_idx],
      bin_holder[idx],
    )
inp_bin = "".join(bin_holder)  # volta a ser string

print("bin_holder:", bin_holder)

# conversão do binário passado no input pra inteiro
for idx in range(len(inp_bin)):
  if inp_bin[idx] == "1":
    initial_int += 2**idx
print("initial_int:", initial_int)

# contagem das operações
for curr_int in range(initial_int + 1, goal_int + 1):
  # holder do número atual que será usado para obter sua versão binária
  curr_int_holder = curr_int
  curr_bin = ""
  print("prev_bin:", prev_bin)

  for _ in range(7):  # sempre serão 7 bits
    # trunca a casa decimal float -> int, a divisão retorna um float,
    # então é necessário truncar pra continuar a conversão |
    curr_int_holder = int(curr_int_holder)

    # conversão de int pra binário
    curr_bin = str(curr_int_holder % 2) + curr_bin
    curr_int_holder = curr_int_holder / 2

  print("curr_bin:", curr_bin)

  for idx in range(7):
    if prev_bin[idx] != curr_bin[idx]:  # verificação das diferenças
      num_of_operations += 1
  print(num_of_operations)
  prev_bin = curr_bin
