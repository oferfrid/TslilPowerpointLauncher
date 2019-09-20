import tkinter as tk
from tkinter import ttk

from FileManager import get_files_path, get_sorted_files


class Window(tk.Tk):
    songs_files_list = None
    songs_name_list = None
    songs_list_box = None
    selected_song_label = None

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tzlil ppt launcher")
        self.minsize(600,400)
        # self.wm_iconbitmap('icon.ico')
        self.init_songs()
        self.init_songsListbox()
        self.init_song_title()

    def init_songs(self):
        fp = get_files_path(r'C:\Users\oferfrid\Downloads\ppt', extantions=['ppt', 'pptx'])
        sorted_file_names, sorted_files_path = get_sorted_files(fp)
        self.songs_files_list = sorted_files_path
        self.songs_name_list = sorted_file_names

    def  init_song_title(self):
        label = tk.Label(self)
        label.pack()  # grid(row=3, column=3)
        self.selected_song_label = label

    def init_songsListbox(self):
        listbox = tk.Listbox(self)
        listbox.pack() #grid(row=3, column=3)
        listbox.bind("<KeyPress>", self.keydown)
        listbox.bind("<KeyRelease>", self.keyup)
        for item in self.songs_name_list:
            listbox.insert(tk.END, item)
        listbox.select_set(0)
        listbox.focus_set()
        self.songs_list_box = listbox

    def keydown(self,e):
        print('doun', e.char)
        if e.keysym == 'Return':
            self.selected_song_label['text'] = self.songs_files_list[self.songs_list_box.curselection()[0]]

    def keyup(self,e):
        print('up', e.char)




window = Window()
window.mainloop()