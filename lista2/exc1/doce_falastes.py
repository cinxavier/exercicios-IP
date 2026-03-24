songs = ""
num_of_songs = 0
runnig = True

while runnig:
    new_song = str(input())

    if new_song.lower() == "voa, voa brabuleta":
        runnig = False
    elif len(new_song) > 0:
        songs += new_song if songs == "" else " - " + new_song 
        num_of_songs += 1


print("Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!")
print(f"A quantidade de músicas selecionadas foi {num_of_songs}")
print(f"Setlist de músicas: {songs}")
