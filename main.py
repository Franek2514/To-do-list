from tkinter import *

class Todolist:
    def __init__(self, master, window_title, **options):
        self.master = master
        self.master.title(str(window_title))
        
        

root = Tk()

my_todolist = Todolist(root, "moja lista")

root.mainloop()