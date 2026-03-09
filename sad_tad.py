quantidade_pessoas = input("quantas pessoas? ") # int

pessoas = [ ] # string[]
lugar = ""
quant_media_cervejas = 0

def get_pessoas():
    for pessoa in range(quantidade_pessoas):
        if len(pessoa) == 0:
            pessoas.append(input("quem vai? "))
        else:
            pessoas.append(input("quem mais? "))

def get_lugar():
    

