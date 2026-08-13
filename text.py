import tkinter as tk
from tkinter import filedialog, Menu, Listbox, Frame, Label, END
import pygame
import os

pygame.init()
pygame.mixer.init()

root = tk.Tk()
root.title("🎵 Music Player")
root.geometry("700x500")
root.configure(bg="#1e1e1e")

playlist = []
current_song = ""
is_paused = False
music_folder = ""

title = Label(root,
              text="🎵 Advanced Music Player",
              font=("Arial",18,"bold"),
              bg="#1e1e1e",
              fg="white")
title.pack(pady=10)

song_label = Label(root,
                   text="No Song Selected",
                   bg="#1e1e1e",
                   fg="cyan",
                   font=("Arial",12))
song_label.pack()

status = Label(root,
               text="Ready",
               bg="#1e1e1e",
               fg="lightgreen")
status.pack()

song_list = Listbox(root,
                    width=70,
                    height=15,
                    bg="#2b2b2b",
                    fg="white",
                    selectbackground="green")
song_list.pack(pady=15)

def load_music():

    global music_folder,current_song

    folder = filedialog.askdirectory()

    if folder == "":
        return

    music_folder = folder

    playlist.clear()

    song_list.delete(0,END)

    for file in os.listdir(folder):

        if file.lower().endswith((".mp3",".wav")):
            playlist.append(file)

    playlist.sort()

    for song in playlist:
        song_list.insert(END,song)

    if playlist:
        song_list.selection_set(0)
        current_song = playlist[0]
        song_label.config(text=current_song)
        status.config(text="Playlist Loaded")

menu = Menu(root)
root.config(menu=menu)

song_menu = Menu(menu,tearoff=0)
song_menu.add_command(label="Open Folder",command=load_music)

menu.add_cascade(label="Songs",menu=song_menu)
# ==========================

# ==========================

def play_music(event=None):
    global current_song, is_paused

    if len(playlist) == 0:
        return

    selected = song_list.curselection()

    if selected:
        current_song = playlist[selected[0]]

    try:
        if is_paused:
            pygame.mixer.music.unpause()
            is_paused = False
        else:
            path = os.path.join(music_folder, current_song)
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()

        song_label.config(text=current_song)
        status.config(text="▶ Playing")

    except Exception as e:
        status.config(text=f"Error: {e}")


def pause_music():
    global is_paused

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        is_paused = True
        status.config(text="⏸ Paused")


def stop_music():
    global is_paused

    pygame.mixer.music.stop()
    is_paused = False
    status.config(text="⏹ Stopped")


def next_song():
    global current_song

    if len(playlist) == 0:
        return

    index = playlist.index(current_song)
    index = (index + 1) % len(playlist)

    song_list.selection_clear(0, tk.END)
    song_list.selection_set(index)
    song_list.activate(index)

    current_song = playlist[index]

    play_music()


def previous_song():
    global current_song

    if len(playlist) == 0:
        return

    index = playlist.index(current_song)
    index = (index - 1) % len(playlist)

    song_list.selection_clear(0, tk.END)
    song_list.selection_set(index)
    song_list.activate(index)

    current_song = playlist[index]

    play_music()


song_list.bind("<Double-Button-1>", play_music)
# ==========================

# ==========================

from tkinter import Button, Scale, HORIZONTAL

# -------- Button Frame --------

button_frame = Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

play_btn = Button(
    button_frame,
    text="▶ Play",
    width=10,
    bg="green",
    fg="white",
    command=play_music
)
play_btn.grid(row=0, column=0, padx=5)

pause_btn = Button(
    button_frame,
    text="⏸ Pause",
    width=10,
    bg="orange",
    fg="white",
    command=pause_music
)
pause_btn.grid(row=0, column=1, padx=5)

stop_btn = Button(
    button_frame,
    text="⏹ Stop",
    width=10,
    bg="red",
    fg="white",
    command=stop_music
)
stop_btn.grid(row=0, column=2, padx=5)

prev_btn = Button(
    button_frame,
    text="⏮ Previous",
    width=12,
    command=previous_song
)
prev_btn.grid(row=0, column=3, padx=5)

next_btn = Button(
    button_frame,
    text="⏭ Next",
    width=10,
    command=next_song
)
next_btn.grid(row=0, column=4, padx=5)



Label(
    root,
    text="🔊 Volume",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 10)
).pack(pady=(10,0))

volume = Scale(
    root,
    from_=0,
    to=100,
    orient=HORIZONTAL,
    length=250,
    command=lambda v: pygame.mixer.music.set_volume(float(v)/100)
)
volume.set(70)
volume.pack()

pygame.mixer.music.set_volume(0.7)



def auto_next():
    global is_paused

    if (not pygame.mixer.music.get_busy()) and (not is_paused) and playlist:
        next_song()

    root.after(1000, auto_next)

auto_next()

# -------- Footer --------

Label(
    root,
    text="Made with Python + Tkinter + Pygame ❤️",
    bg="#1e1e1e",
    fg="gray",
    font=("Arial", 9)
).pack(side="bottom", pady=10)

# -------- Start --------

root.mainloop()

