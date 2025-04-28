import os
import pygame
import time
folder ="/home/islam/الموسيقى/Data/genres_original/blues"
songs = os.listdir(folder)
print("choose a song:")
for index,song in enumerate(songs):
    print(f"{index+1}.{song}")
player_choice=input("Please type the song name exactly (without number):")
if player_choice in songs:
    print("good choice nigga!!")
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(folder, player_choice))
    pygame.mixer.music.play()
    print("Playing now...")
    
    
    while True:
        choice=input("write stop to stop:").lower()
        if choice == "stop":
            pygame.mixer.music.stop()
            print("Song stopped.")
            break
else:
    print("pls choice a song and without the number")
