from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Sliders")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")
root.geometry("400x400")

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get() + 400) + "x" + str(vertical.get() + 400))

vertical = Scale(root, from_=0, to=200, orient=VERTICAL)
vertical.pack()

horizontal = Scale(from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_button = Button(text="resize", command=slide).pack()

mainloop()
