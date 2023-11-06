import os

def get_song_list():
    song_list = []
    for file in os.listdir("song_list"):
        if file.endswith(".txt"):
            song_list.append(file)
    return song_list

def get_song_lyrics(song_name):
    song_lyrics = []
    with open("song_list/" + song_name, "r", encoding="utf-8") as file:
        for line in file:
            song_lyrics.append(line)
    return song_lyrics