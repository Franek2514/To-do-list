from tkinter import *

class Todolist:

    def __init__(self, master, window_title, **options):
        self.master = master
        self.master.title(str(window_title))

        self.task_adding_frame = LabelFrame(self.master, text="add task")
        self.task_adding_frame.pack()
       
        self.label_task_name = Label(self.task_adding_frame, text="task name:")
        self.input_task_name_entry = Entry(self.task_adding_frame)

        self.deadline_date_label = Label(self.task_adding_frame, text="deadline date:")
        self.deadline_date_input = Entry(self.task_adding_frame)
    
        self.add_task_button = Button(self.task_adding_frame, text="add task", command=self.put_task_to_box)
        

        self.label_task_name.grid(row=0, column=0)
        self.input_task_name_entry.grid(row=1, column=0)

        self.deadline_date_label.grid(row=2, column=0)
        self.deadline_date_input.grid(row=3, column=0)

        self.add_task_button.grid(row=4, column=0)

        self.tasks_list_frame = LabelFrame(self.master, text="tasks list")
        self.tasks_list_frame.pack()

        self.tasks_box = Listbox(self.tasks_list_frame)
        self.tasks_box.pack()    

        self.delete_task_button = Button(self.tasks_list_frame, text="delete task", command=self.remove_task_from_box)
        self.delete_task_button.pack()

    def put_task_to_box(self):
        self.tasks_box.insert(END, self.input_task_name_entry.get())
        print("add: ", self.input_task_name_entry.get())
        self.clear_task_name_entry()

    def remove_task_from_box(self):
        self.tasks_box.delete(ANCHOR)
        
    
    def clear_task_name_entry(self):
        self.input_task_name_entry.delete(0, END)
        print("Entry clear")

root = Tk()

my_todolist = Todolist(root, "my to do list")

root.mainloop()