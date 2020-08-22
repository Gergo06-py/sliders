from tkinter import *

root = Tk()
root.title("Sliders")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")
root.geometry("400x400")
root.resizable(False, False)


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get() * 100 + 400) + "x" + str(vertical.get() * 100 + 400))


vertical = Scale(root, from_=0, to=2, orient=VERTICAL, showvalue=FALSE)
vertical.pack()

horizontal = Scale(from_=0, to=4, orient=HORIZONTAL, showvalue=FALSE)
horizontal.pack()

my_button = Button(text="resize", command=slide).pack()

mainloop()
