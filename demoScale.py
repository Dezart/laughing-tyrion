from tkinter import *
root = Tk()
scl = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10)
scl.pack(side=LEFT, expand=YES, fill=Y)


def report():
    print(scl.get())

Button(root, text="State", command=report).pack(side=RIGHT)
root.mainloop()