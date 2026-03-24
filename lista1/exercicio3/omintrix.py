aliens = ["Chama", "XLR8", "Diamante", "Besta", "Ultra-T"]
alien = ""

alien = input()

print("Ben: Tá na hora de virar herói!")

if alien in aliens:
    print(f"Ben: Bora lá, {alien}!")
    print("Gwen: Boa, Ben, agora vamos, temos que encontrar Azmuth.")
else:
    print(f"Ben: Droga, Não consigo me transformar no {alien}.")
    print("Gwen: Ben Tennyson! Pare com a Bobeira.")

if alien == "Insectoide":
    print("Gwen: Ben, de todos os seus bichos, você tentou escolher esse?")

elif alien == "Fantasmático":
    print("Ben: Zs'skayr... Ainda bem que o relógio não funcionou.")

elif alien == "XLR8":
    print("Ben: Vamos encontrar ele bem rápido com o XLR8!")

elif alien == "Chama":
    print("Ben: Eu tô pegando fogo!")
