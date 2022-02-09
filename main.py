from tkinter import *
import tkinter.filedialog

filename = None

# create a new file
def new_file():
    global filename
    filename = "Untitled"
    text.delete(0.0, END) # from 0 row 0 column to the end

# save the text to an existing file
def save_file():
    global filename
    t = text.get(0.0, END)
    f = open(filename, "w")
    f.write(t)
    f.close

# save the text as a new file
def save_as():
    # get the file name from user
    f = asksaveasfilename(mode = "w", defaulttextension = ".txt")
    # text content
    t = text.get(0.0, END)
    try:
        # write text into the file, stripping the white spaces
        f.write(t.rstrip())
    except:
        showerror(title = "Error", message = "Unable to save file...")

# open a file
def open_file():
    # read from existing file
    f = askopenfile(mode = "r")
    t = f.read()
    # remove text from current text box
    text.delete(0.0, END)
    # insert the read text
    text.insert(0.0, t)

# font size
def font_size_increase():
    global text
    size = int(text.font.cget("size"))
    size = max(size + 2, 72)
    text.font.configure(size=size)
def font_size_decrease():
    global text
    size = int(text.font.cget("size"))
    size = min(size - 2, 1)
    text.font.configure(size=size)

# font color
def font_color_red():
    pass
def font_color_blue():
    pass
def font_color_green():
    pass
def font_color_black():
    pass

# font style
def font_style_xxx():
    pass



# create the root
root = Tk()
# title
root.title("Angel's Text Editor")
# prevent user from resizing the text editor
root.minsize(width = 500, height = 400)
root.maxsize(width = 500, height = 400)
# put the text box on the page and size it to the full page
text = Text(root, width = 500, height = 400)
text.pack()

# menu bar
menubar = Menu(root)

# file menu. operates on files
filemenu = Menu(menubar)
filemenu.add_command(label = "New", command = new_file)
filemenu.add_command(label = "Open", command = open_file)
filemenu.add_command(label = "Save", command = save_file)
filemenu.add_command(label = "Save As...", command = save_as)
filemenu.add_separator()
filemenu.add_command(label = "Quit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)

# font menu
fontmenu = Menu(menubar)
# font size
font_size = Menu(fontmenu)
font_size.add_command(label = "+", command = font_size_increase)
font_size.add_command(label = "-", command = font_size_decrease)
fontmenu.add_cascade(label = "Size", menu = font_size)
# font color
font_color = Menu(fontmenu)
font_color.add_command(label = "Red", command = font_color_red)
font_color.add_command(label = "Blue", command = font_color_blue)
font_color.add_command(label = "Green", command = font_color_green)
font_color.add_command(label = "Black", command = font_color_black)
fontmenu.add_cascade(label = "Color", menu = font_color)
# font style
font_style = Menu(fontmenu)
font_style.add_command(label = "xxx", command = font_style_xxx)
fontmenu.add_cascade(label = "Stype", menu = font_style)
# add to the menu bar
menubar.add_cascade(label = "Font", menu = fontmenu)



root.config(menu = menubar)
root.mainloop()

'''
### 2 selections of font ###
def FontHelvetica():
    global text
    text.config(font = "Helvetica")

def FontCourier():
    global text
    text.config(font = "Courier")

# font button
font = Menubutton(root, text = "Font")
# put font button on the page
font.grid()
# set font menu
font.menu = Menu(font, tearoff = 0)
font["menu"] = font.menu
courier = IntVar()
helvetica = IntVar()

font.menu.add_checkbutton(label = "Courier", variable = courier,command = FontCourier)
font.menu.add_checkbutton(label = "Helvetica", variable = helvetica, command = FontHelvetica)


'''