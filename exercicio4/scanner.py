class Scanner:
  energia_danny = ""
  tipo_fantasma = ""
  energia_fantasma = ""
  nome_fantasma = ""
  portal_instavel = ""
  
  def __init__(self):
    self.energia_danny  = input()
    self.tipo_fantasma  = input().lower()
    self.energia_fantasma  = input()
    self.nome_fantasma  = input().lower()
    self.portal_instavel  = input().lower()

    print("CInFantasma - Defesa Sobrenatural do CIn!")

  def verify_data_type(self):
    return not self.energia_danny.isdigit() or not self.energia_fantasma.isdigit()

  def convert_data(self):
    self.energia_danny  = int(self.energia_danny)
    self.energia_fantasma  = int(self.energia_fantasma)
    
  def get_sitiaion(self):
    if self.nome_fantasma.__contains__("king") or self.nome_fantasma.__contains__("lord"):
      print("O Scanner detectou um possível fantasma de elite!")

    if self.nome_fantasma.count("",1) > 12:
      print("O nome do fantasma é assustadoramente longo...")

    if self.portal_instavel == "sim":
      print("O portal da Zona Fantasma continua instável!")
    else: 
      print("O portal parece estar temporariamente estável.")

    if self.tipo_fantasma == "desconhecido" and self.energia_danny >= 70:
      print("Um fantasma misterioso apareceu no CIn!")

  def get_danny_action(self):
    if self.tipo_fantasma == "chefe" and 80 <= self.energia_fantasma <= self.energia_danny :
      print("Danny ativou o Modo Fantasma Total!")

    if self.tipo_fantasma == "raro" and 50 <=self.energia_fantasma <= self.energia_fantasma:
      print("Danny capturou o fantasma com o Fenton Thermos!" )

    if self.energia_fantasma < 20 :
      print("Danny decidiu apenas observar o fantasma.")

    if self.energia_fantasma > self.energia_danny:
      print("Danny percebeu que o fantasma é forte demais e decidiu recuar!")
    if self.energia_danny == 100 and self.energia_fantasma < 10: 
      print("Danny enfrentou o fantasma normalmente!")

scanner = Scanner()

if scanner.verify_data_type():
    print("Erro no Scanner Fenton: nível de energia inválido!")
else:
  scanner.convert_data()
  scanner.get_sitiaion()
  scanner.get_danny_action()