from tkinter import *
def newfile():
    print("New File")
root = Tk()
root.title("Notepad")
root.geometry("990x990")
textarea = Text(root, height="990", width="990")
textarea.pack()

mainmenubar = Menu(root)
# first menu
m1 = Menu(mainmenubar, tearoff=0)
m1.add_command(label="New", command=newfile)
m1.add_command(label="Save")
m1.add_command(label="open")
root.config(menu=mainmenubar)
mainmenubar.add_cascade(label="File", menu=m1)


# second menu
m2 = Menu(mainmenubar, tearoff=0)
m2.add_command(label="New", command=newfile)
m2.add_command(label="Save")
m2.add_command(label="open")
mainmenubar.add_cascade(label="Edit", menu=m2)
root.mainloop()
