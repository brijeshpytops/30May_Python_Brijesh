import tkinter as tk
import os
import random
import pygame

screen = tk.Tk()

screen.title("My Musics")

screen.geometry('400x400')

lbl = tk.Label(screen, text = "My musics list...").grid(row=2,column=1) 

musics_path = r'C:\xampp\htdocs\PYTHONMaster\batch\30May_Python_Brijesh\advance-python\GUI\musics'

musics = os.listdir(musics_path)

sleceted_musics = []

listbox = tk.Listbox(screen)

def shuffle_musics():
    random.shuffle(musics)
    for index, music in enumerate(musics):
        listbox.insert(index+1, music)
    sleceted_musics.extend(musics)

def loop_musics():
    for index, music in enumerate(musics):
        listbox.insert(index+1, music)
    sleceted_musics.extend(musics)

def play_musics():
    # Initialize the pygame mixer
    pygame.mixer.init()

    for music in sleceted_musics:
        print(musics_path + '\\' + music)
        pygame.mixer.music.load(musics_path + '\\' + music)

        # Play the MP3 file
        pygame.mixer.music.play()

        # Keep the script running while the music is playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

listbox.grid(row=3,column=1)

tk.Button(screen, text='Play', command=play_musics).grid(row=0,column=0)
tk.Button(screen, text='Shuffle', command=shuffle_musics).grid(row=1,column=0)
tk.Button(screen, text='loop', command=loop_musics).grid(row=1,column=1)

screen.mainloop()