words = ""
current_word = ""

asking = True
while asking:
  answer = input("digite: ")
  if answer.lower() == "fim":
    asking = False
  else:
    if words == "":
      words += answer
    else:
      words += "-" + answer

print("frases coletadas: ", words)
print()

while words != "":
  new_words = ""
  new_current_word = ""

  direction_switch = False

  for word in words:
    if word == "-":
      direction_switch = True

    if not direction_switch:
        new_current_word += word
    else:
      if word == "-":
        if new_words != "": 
          new_words += word
      else:
        new_words += word
        
  current_word = new_current_word
  words = new_words
  print("palavra atual: ", current_word)
  print("palavras restantes: ", words)