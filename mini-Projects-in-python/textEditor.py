# import tkinter module(1 file) & library(collection of module):
# (for) GUI app 

import tkinter as tk
from tkinter import filedialog, messagebox  #sub module;

#main Window Code
root = tk.Tk()
root.title("mytextEditor")
root.geometry("800x600")

# textArea
text= tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvrtica",20),

)

text.pack(expand=True,fill=tk.BOTH)

#Main
#to create new file
def new_file():
    text.delete(1.0,tk.END)
#to open new file
def open_file():
    file_path= filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if file_path:
        # openFile
        with open(file_path,"r") as file:
            # clear old text
            text.delete(1.0, tk.END)
            text.insert(tk.END,file.read())

# Save the file :

def save_file():
    #  open save file diloge
    file_path= filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if file_path: 
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))

    messagebox.showinfo("Info", "file save successfully")
# Menubar
menu= tk.Menu(root)
root.config(menu=menu)

file_menu= tk.Menu(menu)

# new open save exit:


menu.add_cascade(label="File", menu=file_menu) #to add file menu to menu bar

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()

file_menu.add_command(label="Exit",command=root.quit)



root.mainloop() #to start;






