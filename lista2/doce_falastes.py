songs = ""
num_of_songs = 0
runnig = True

while True:
    new_song = input()

    if new_song == "":
        break
    else:
        if songs != "":
        songs += new_song
        num_of_songs += 1
            songs += " - "


print("Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!")
print(f"A quantidade de músicas selecionadas foi {num_of_songs}")
print(f"Setlist de músicas: {songs}")
