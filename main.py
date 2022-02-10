from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()
root.title("Untitled - Angel's Text Editor!")
root.iconbitmap("icon.ico")
root.geometry("500x610")

# filename
global open_status_name
open_status_name = None

# selected text
global selected
selected = False

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

### HELPER FUNCTION    
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

# cut text
def cut_text(e):
    global selected
    # check to see if we used keyboard shortcuts
    if e:
        selected = root.clipboard_get()
    elif text.selection_get():
        # get selected text from text box
        selected = text.selection_get()
        # delete selected text from text box
        text.delete("sel.first", "sel.last")
        # clear the clipboard and then append
        root.clipboard_clear()
        root.clipboard_append(selected)

# copy text
def copy_text(e):    
    global selected
    # check to see if we used keyboard shortcuts
    if e:
        selected = root.clipboard_get()
    elif text.selection_get():
        # get selected text from text box
        selected = text.selection_get()
        # clear the clipboard and then append
        root.clipboard_clear()
        root.clipboard_append(selected)

# paste text
def paste_text(e):
    global selected
    # check to see if we used keyboard shortcuts
    if e:
        selected = root.clipboard_get()
    elif selected:
        position = text.index(INSERT) # position of cursor
        text.insert(position, selected)

# bold text
def bold_it():
    
    # define current tags
    current_tags = text.tag_names("sel.first")

    # check if tag has been set already
    # text is both bold and italic
    if "bold_italic" in current_tags:
        text.tag_remove("bold_italic", "sel.first", "sel.last")
        text.tag_add("italic", "sel.first", "sel.last")
    # text is bold but not italic
    elif "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    # text is italic but not bold
    elif "italic" in current_tags:
        text.tag_remove("italic", "sel.first", "sel.last")
        text.tag_add("bold_italic", "sel.first", "sel.last")
    # text is not italic nor bold
    else:
        text.tag_add("bold", "sel.first", "sel.last")



# italics text
def italics_it():
    # define current tags
    current_tags = text.tag_names("sel.first")

    # check if tag has been set already
    # text is both bold and italic
    if "bold_italic" in current_tags:
        text.tag_remove("bold_italic", "sel.first", "sel.last")
        text.tag_add("bold", "sel.first", "sel.last")
    # text is italic but not bold
    elif "italic" in current_tags:
        text.tag_remove("italic", "sel.first", "sel.last")
    # text is bold but not italic
    elif "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
        text.tag_add("bold_italic", "sel.first", "sel.last")
    # text is not italic nor bold
    else:
        text.tag_add("italic", "sel.first", "sel.last")

# change selected text color
def text_color():
    # pick a color
    color = colorchooser.askcolor()[1] # hex color code

    # if a color is chosen
    if color:
        # update status bar
        status_bar.config(text = color)
        
        # get the font
        color_font = font.Font(text, text.cget("font"))
        print(color_font)
        # configure a tag
        text.tag_configure("text_colored", font = color_font, foreground = color)

        # define current tags
        current_tags = text.tag_names("sel.first")
        # add colored tag
        text.tag_add("text_colored", "sel.first", "sel.last")

# change selected text background color
def background_color():
    # pick a color
    color = colorchooser.askcolor()[1] # hex color code

    # if a color is chosen
    if color:
        # update status bar
        status_bar.config(text = color)
        
        # get the font
        color_font = font.Font(text, text.cget("font"))
        # configure a tag
        text.tag_configure("background_colored", font = color_font, background = color)

        # define current tags
        current_tags = text.tag_names("sel.first")
        # add colored tag
        text.tag_add("background_colored", "sel.first", "sel.last")

# change page color  
def page_color():
    # pick a color
    color = colorchooser.askcolor()[1] # hex color code

    # if a color is chosen
    if color:
        text.config(bg = color)

def update_font(format):
    pass


def clear_font():
    # formatting tags
    possible_tags = ["bold", "italic", "bold_italic", "text_colored", "background_colored"]
    # remove all formatting text from selected text
    for tag in possible_tags:
        text.tag_remove(tag, "sel.first", "sel.last")

# create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill = X)

# create main frame
frame = Frame(root)
frame.pack(pady = 5)

# create Y scrollbar
ver_scroll = Scrollbar(frame)
ver_scroll.pack(side = RIGHT, fill = Y)

# create X scrollbar
hor_scroll = Scrollbar(frame, orient = "horizontal")
hor_scroll.pack(side = BOTTOM, fill = X)

# create text box
text = Text(
    frame, width = 97, height = 19, 
    font = ("Helvetica", 15), 
    selectbackground = "yellow", 
    selectforeground = "black", 
    undo = True, 
    yscrollcommand = ver_scroll.set,
    xscrollcommand = hor_scroll.set,
    wrap = "none" # word wrap
)
text.pack()

### fonts
# bold font
bold_font = font.Font(text, text.cget("font"))
bold_font.configure(weight = "bold")
# bold tag
text.tag_configure("bold", font = bold_font)
# italic font
italics_font = font.Font(text, text.cget("font"))
italics_font.configure(slant = "italic")
# italic tag
text.tag_configure("italic", font = italics_font)
# bold and italic font
bold_italic = font.Font(text, text.cget("font"))
bold_italic.configure(weight = "bold", slant = "italic")
# bold and italic tag
text.tag_configure("bold_italic", font = bold_italic)

# configure scrollbar
ver_scroll.config(command = text.yview)
hor_scroll.config(command = text.xview)

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
edit_menu.add_command(label = "Cut", 
    command = lambda: cut_text(False), accelerator = "(Ctrl+X)")
edit_menu.add_command(label = "Copy", 
    command = lambda: copy_text(False), accelerator = "(Ctrl+C)")
edit_menu.add_command(label = "Paste", 
    command = lambda: paste_text(False), accelerator = "(Ctrl+V)")
edit_menu.add_separator()
edit_menu.add_command(label = "Undo", 
    command = text.edit_undo, accelerator = "(Ctrl+Z)")
edit_menu.add_command(label = "Redo", 
    command = text.edit_redo, accelerator = "(Ctrl+Y)")

# add statur bar at the bottom
status_bar = Label(root, text = "Ready        ", anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 15)

# edit bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

# create buttons
# bold button
bold_button = Button(toolbar_frame, text = "Bold", command = bold_it)
bold_button.grid(row = 0, column = 0, sticky = W, padx = 5) # west side of the bar
# italics button
bold_button = Button(toolbar_frame, text = "Italics", command = italics_it, padx = 5)
bold_button.grid(row = 0, column = 1)

# colors
# text color
color_text_button = Button(toolbar_frame, text = "Text Color", command = text_color)
color_text_button.grid(row = 0, column = 4, padx = 5)
# background color
color_background_button = Button(toolbar_frame, text = "Background Color", command = background_color)
color_background_button.grid(row = 0, column = 5, padx = 5)
# background color
page_color = Button(toolbar_frame, text = "Page Color", command = page_color)
page_color.grid(row = 0, column = 6, padx = 5)
# clear all font formats
clear_button = Button(toolbar_frame, text = "Clear Font", command = clear_font)
clear_button.grid(row = 0, column = 7, padx = 5)


root.mainloop()