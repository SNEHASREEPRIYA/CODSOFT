import tkinter

import tkinter.messagebox
import pickle

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Create GUI
root = tkinter.Tk()
root.title("TO DO LIST")
root.iconbitmap(r'C:\Users\ramsu\OneDrive\Desktop\GITHUB\TASK-2(TO DO LIST)\checklist.ico')
root.configure(background = "yellow")

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width=59,fg = "blue",bg = "light green")
listbox_tasks.pack(side=tkinter.LEFT)
listbox_tasks.config(font=('verdana',15))

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root,width=60,fg = "black",bg = "pink")
entry_task.pack()
entry_task.config(font=('verdana',15))

button_add_task = tkinter.Button(root, text="Add task", width=97,fg = "black",bg = "sky blue", command=add_task)
button_add_task.pack()
button_add_task.config(font=('verdana',10))

button_delete_task = tkinter.Button(root, text="Delete task", width=97,fg = "black",bg = "sky blue", command=delete_task)
button_delete_task.pack()
button_delete_task.config(font=('verdana',10))

button_save_tasks = tkinter.Button(root, text="Save tasks", width=97,fg = "black",bg = "sky blue", command=save_tasks)
button_save_tasks.pack()
button_save_tasks.config(font=('verdana',10))

root.mainloop()