energia_danny  = input()
tipo_fantasma  = input().lower()
energia_fantasma  = input()
nome_fantasma  = input().lower()
portal_instavel  = input().lower()

print("CInFantasma - Defesa Sobrenatural do CIn!")

if not energia_danny.isdigit() or not energia_fantasma.isdigit():
  print("Erro no Scanner Fenton: nível de energia inválido!")
  exit()

energia_danny  = int(energia_danny)
energia_fantasma  = int(energia_fantasma)
  
if nome_fantasma.__contains__("king") or nome_fantasma.__contains__("lord"):
  print("O Scanner detectou um possível fantasma de elite!")

if nome_fantasma.count("",1) > 12:
  print("O nome do fantasma é assustadoramente longo...")

if portal_instavel == "sim":
  print("O portal da Zona Fantasma continua instável!")
else: 
  print("O portal parece estar temporariamente estável.")

if tipo_fantasma != "comum" and tipo_fantasma != "raro" and tipo_fantasma != "chefe" and energia_danny >= 70:
  print("Um fantasma misterioso apareceu no CIn!")

if tipo_fantasma == "chefe" and 80 <= energia_fantasma <= energia_danny :
  print("Danny ativou o Modo Fantasma Total!")

elif tipo_fantasma == "raro" and 50 <= energia_fantasma <= energia_fantasma:
  print("Danny capturou o fantasma com o Fenton Thermos!" )

elif energia_fantasma < 20 :
  print("Danny decidiu apenas observar o fantasma.")

elif energia_fantasma > energia_danny:
  print("Danny percebeu que o fantasma é forte demais e decidiu recuar!")
else:
  print("Danny enfrentou o fantasma normalmente!")
