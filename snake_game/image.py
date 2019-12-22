from tkinter import *

# pip install pillow
from PIL import Image, ImageTk
from tkinter import messagebox


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        messagebox.showwarning("Game Over!", "Your snake became an Ouroboros!")

        load = Image.open("Ouroboros.jpg")
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)



root = Tk()
app = Window(root)
root.wm_title("Snake Game")
root.geometry("220x200")
root.mainloop()




