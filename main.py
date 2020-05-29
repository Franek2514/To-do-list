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

        self.add_task_button = Button(self.task_adding_frame, text="add task")


        self.label_task_name.grid(row=0, column=0)
        self.input_task_name_entry.grid(row=1, column=0)

        self.deadline_date_label.grid(row=2, column=0)
        self.deadline_date_input.grid(row=3, column=0)

        self.add_task_button.grid(row=4, column=0, pady=10)


        self.tasks_list_frame = LabelFrame(self.master, text="tasks list")
        self.tasks_list_frame.pack(padx=30, pady=40)


root = Tk()

my_todolist = Todolist(root, "my to do list")

root.mainloop()