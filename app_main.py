import os
import sys
import tkinter as tk
from FileManager import get_files_path, get_sorted_files
from datetime import datetime

class Window(tk.Tk):
    songs_files_list = None
    songs_name_list = None
    songs_list_box = None
    last_selection_time = datetime.now()
    current_search_str = []
    # debug_selected_song_label = None
    # debug_search_label = None

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tslil ppt launcher")
        self.minsize(200,300)
        self.wm_iconbitmap('tslil.ico')
        self.init_songs()
        self.init_songsListbox()
        # self.init_debug_title()

    def init_songs(self):
        fp = get_files_path(os.path.dirname(os.path.realpath(__file__)), extantions=['ppt', 'pptx'])
        # fp = get_files_path(r'C:\Users\oferfrid\Downloads\ppt', extantions=['ppt', 'pptx'])
        sorted_file_names, sorted_files_path = get_sorted_files(fp)
        self.songs_files_list = sorted_files_path
        self.songs_name_list = sorted_file_names

    # def  init_debug_title(self):
    #     label = tk.Label(self)
    #     label.pack()  # grid(row=3, column=3)
    #     self.debug_selected_song_label = label
    #     label = tk.Label(self)
    #     label.pack()  # grid(row=3, column=3)
    #     self.debug_search_label = label

    def init_songsListbox(self):
        listbox = tk.Listbox(self, selectmode='SINGLE')
        listbox.pack(fill=tk.BOTH, expand=1) #grid(row=3, column=3)
        listbox.bind("<KeyPress>", self.keydown)
        listbox.bind("<KeyRelease>", self.keyup)
        for item in self.songs_name_list:
            listbox.insert(tk.END, item)
        listbox.select_set(0)
        listbox.focus_set()
        self.songs_list_box = listbox

    def keydown(self,e):
        # print('doun', e.char)
        # print('doun', e.keysym)
        if e.keysym == 'Return':
            ppt_file_path = self.songs_files_list[self.songs_list_box.curselection()[0]]
            # self.debug_selected_song_label['text'] = ppt_file_path
            self.current_search_str = []
            self.last_selection_time = datetime.now()
            os.startfile(ppt_file_path,'show')
        elif e.keysym=='Up' or e.keysym=='Down':
            self.current_search_str = []
            self.last_selection_time = datetime.now()
            # self.update_search_selection()
        elif e.keysym=='BackSpace':
            self.current_search_str = []
            self.last_selection_time = datetime.now()
        elif (e.char!=''):
            # is char
            if ((1488<=ord(e.char)) & (ord(e.char)<=1514)) or e.char==' ':
                # hebrew char
                if (datetime.now()-self.last_selection_time).seconds>2:
                    self.last_selection_time = datetime.now()
                    self.current_search_str = [e.char]
                else:
                    self.current_search_str += [e.char]
                    self.last_selection_time = datetime.now()
                self.update_search_selection()
            # elif e.char==' ':
            #     # space char
            #     self.current_search_str += [e.char]
            #     self.last_selection_time = datetime.now()
            #     self.update_search_selection()

    def update_selection(self,index):
        self.songs_list_box.selection_clear(0, tk.END)
        self.songs_list_box.select_set(index)
        self.songs_list_box.activate(index)
        self.songs_list_box.focus_set()
        self.songs_list_box.see(index)

    def update_search_selection(self):
        search_str = ''.join(self.current_search_str)
        # self.debug_search_label['text'] = search_str
        if len(search_str)>0:
            found_indexes = [i for i,t in enumerate(self.songs_name_list) if t.startswith(search_str)]
            if len(found_indexes)>0:
                self.update_selection(found_indexes[0])

    def keyup(self,e):
        # print('up', e.char)
        if e.keysym == 'Up' or e.keysym == 'Down':
            self.update_selection(self.songs_name_list.index(self.songs_list_box.get(tk.ACTIVE)))

window = Window()
window.mainloop()