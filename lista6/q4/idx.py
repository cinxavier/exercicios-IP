dic = {
  'EN':{},
  'ES':{}
} 
times = int(input())
for _ in range(times):
  inp = input()
  data = inp.split()
  command = data[0]
  lang = data[1]
  if command == "1":
    pt_word = data[2]
    lang_word = data[3]
    dic[lang][lang_word] = pt_word
  
  elif command == "2":
    pt_word = []
    give_up = False
    
    for lang_word in data[2:]:
      if lang_word in dic[lang]:
        pt_word.append(dic[lang][lang_word])

      else:
        give_up = True
    
    if not give_up:
      print(' '.join(pt_word))
    else:
      print(f"Não entendi nada daqui, faltam palavras no meu dicionário de {lang}!")