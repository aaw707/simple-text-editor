'''
https://www.youtube.com/watch?v=rUgAC_Ssflw
'''

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Untitled - Angel's Text Editor!")
root.iconbitmap("icon.ico")
root.geometry("500x600")

# filename
global open_status_name
open_status_name = None

# file types compatible with this editor
filetypes = (
            ("Text Files", "*.txt"), 
            ("HTML Files", "*.html"), 
            ("Python Files", "*.py"), 
            ("All Files", "*.*"))

# create a new file
def new_file():
    # empty the text box
    text.delete(1.0, END) # from 0 row 0 column to the end
    # update title
    root.title("New File - Angel's Text Editor!")
    # update status bar
    status_bar.config(text = "New File        ")
    # set open_status_name
    global open_status_name
    open_status_name = None

# save the text to an existing file
def save_file():
    global open_status_name
    if open_status_name:
        # save the file
        text_file = open(open_status_name, "w")
        text_file.write(text.get(1.0, END))
        # close file
        text_file.close()
        # update status bar
        status_bar.config(text = f"Saved: {open_status_name}        ")
    else:
        save_as_file()

# save the text as a new file
def save_as_file():

    # get the file name from user
    file_path = filedialog.asksaveasfilename(
        defaultextension = ".*",
        initialdir = "./",
        title = "Save File",
        filetypes = filetypes
        )
    if file_path: 
        update_file(file_path)
    
    # save the file
    text_file = open(file_path, "w")
    text_file.write(text.get(1.0, END))
    # close file
    text_file.close()
    

# open a file
def open_file():

    # remove text from current text box
    text.delete(1.0, END)

    # get the file
    file_path = filedialog.askopenfilename(
        initialdir = "./", 
        title = "Open File", 
        filetypes = filetypes
        )
    if file_path:
        update_file(file_path)

    # open the file
    text_file = open(file_path, "r")
    content = text_file.read()
    # add file to the page
    text.insert(END, content)
    # close the opened file
    text_file.close()

### helper functions
# when create/open/save a new file, update the file name and status bar
def update_file(file_path):
    # update status bar
    status_bar.config(text = f"{file_path}        ")
    # strip file name
    file_name = file_path.split("/")[-1]
    # update title
    root.title(f"{file_name} - Angel's Text Editor!")
    # update open_status_name
    global open_status_name
    open_status_name = file_path


# create main frame
frame = Frame(root)
frame.pack(pady = 5)

# create scrollbar
text_scroll = Scrollbar(frame)
text_scroll.pack(side = RIGHT, fill = Y)

# create text box
text = Text(
    frame, width = 97, height = 19, 
    font = ("Helvetica", 15), 
    selectbackground = "yellow", 
    selectforeground = "black", 
    undo = True, 
    yscrollcommand = text_scroll.set
)
text.pack()

# configure scrollbar
text_scroll.config(command = text.yview)

# create menu
menu = Menu(root)
root.config(menu = menu)

# add file menu
file_menu = Menu(menu, tearoff = False)
menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_command(label = "Save As", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

# add edit menu
edit_menu = Menu(menu, tearoff = False)
menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut")
edit_menu.add_command(label = "Copy")
edit_menu.add_command(label = "Paste")
edit_menu.add_command(label = "Undo")
edit_menu.add_command(label = "Redo")

# add statur bar at the bottom
status_bar = Label(root, text = "Ready        ", anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)



root.mainloop()