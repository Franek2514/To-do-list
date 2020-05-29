from tkinter import *

class Todolist:

    def __init__(self, master, window_title, **options):
        self.master = master
        self.master.title(str(window_title))

        self.task_adding_frame = LabelFrame(self.master, text="add task", width=5)
        self.task_adding_frame.pack(padx=8, pady=8)
       
        self.label_task_name = Label(self.task_adding_frame, text="task name:")
        self.input_task_name_entry = Entry(self.task_adding_frame)
    
        self.add_task_button = Button(self.task_adding_frame, text="add", command=self.put_task_to_box)
        self.add_task_button.configure(bd=4)
        
        self.label_task_name.grid(row=0, column=0)
        self.input_task_name_entry.grid(row=0, column=1)

        self.add_task_button.grid(row=0, column=2, padx=6, pady=6)

        self.tasks_list_frame = LabelFrame(self.master, text="tasks list")
        self.tasks_list_frame.pack(padx=20)

        self.tasks_box = Listbox(self.tasks_list_frame, width=50, height=5)
        self.tasks_box.pack(pady=5, padx=5)    

        self.delete_task_button = Button(self.tasks_list_frame, text="delete task", command=self.remove_task_from_box)
        self.delete_task_button.pack(pady=5)

    def put_task_to_box(self):
        if self.input_task_name_entry.get() != "":
            self.tasks_box.insert(END, self.input_task_name_entry.get())

            self.clear_task_name_entry()
        else:
            pass

    def remove_task_from_box(self):
        self.tasks_box.delete(ANCHOR)
        
    
    def clear_task_name_entry(self):
        self.input_task_name_entry.delete(0, END)
        print("Entry clear")

root = Tk()

my_todolist = Todolist(root, "tasklist")

root.mainloop()