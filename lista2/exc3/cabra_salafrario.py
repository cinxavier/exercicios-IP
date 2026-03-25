moedas = 0

print("Ô promessa sem jeito…")
print()

for i in range(7):
  dia = i +1
  print(f"Dia {dia}: Quantas moedas João Grilo conseguiu arrecadar hoje?")
  
  moedas += int(input())
  
  print(f"No dia {dia}, o baú já tem R$ {moedas}")

print()
print(f"Total arrecadado após o plano: R$ {moedas}")
print()

if moedas <= 0:
  print("João Grilo não conseguiu arrecadar nada... direto para o plano B!!")
  
  print()
  print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
  print()
  
  quantidade_desculpas = int(input())
  
  for num_desc in range(quantidade_desculpas):
    print(f"Digite a {num_desc + 1}ª desculpa:")
    desculpa = input()
    print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")
else:
  print("João Grilo começa a despedida da cachorra:")
  print("'Canis Mortus, Dinherus no Bolsus'")
  print("'Caro nostra quae in patina eius est, canis.'")

  print()

  print("João Grilo, o padeiro acreditou?")
  sinal = input().lower()

  if sinal == "sim":    
    print("O padeiro acreditou! Chicó pode se casar com Rosinha!")
    print("Como o padeiro acreditou?")

  if sinal == "não":
    print("O padeiro não acreditou... João Grilo parte para o Plano B!")
    
    print()
    print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
    print()
    
    quantidade_desculpas = int(input())
    
    for num_desc in range(quantidade_desculpas):
      print(f"Digite a {num_desc +1}ª desculpa:")
      desculpa = input()
      print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")
    
print("Chicó: 'Não sei, só sei que foi assim!'")