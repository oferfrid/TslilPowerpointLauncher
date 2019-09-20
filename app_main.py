import tkinter as tk
from tkinter import ttk

from FileManager import get_files_path, get_sorted_files


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tzlil ppt launcher")
        self.minsize(600,400)
        # self.wm_iconbitmap('icon.ico')

        self.songsListbox()

    def songsListbox(self):
        listbox = tk.Listbox(self)
        listbox.pack() #grid(row=3, column=3)
        listbox.insert(tk.END, "a list entry")
        listbox.bind("<KeyPress>", self.keydown)
        listbox.bind("<KeyRelease>", self.keyup)
        listbox.focus_set()
        listbox.select_set(0)

        fp = get_files_path('/home/oferfrid/Documents/Ofer/3d/temp')
        sorted_file_names, sorted_files_path = get_sorted_files(fp)

        for item in sorted_file_names:
            listbox.insert(tk.END, item)

    def keyup(self,e):
        print('up', e.char)


    def keydown(self,e):
        print('doun', e.char)

window = Window()
window.mainloop()