def song_decoder(song):
    if len(song) == 0: return ""
    return " ".join([ i for i in song.split("WUB") if i != ""])
