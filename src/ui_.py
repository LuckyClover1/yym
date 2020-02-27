from tkinter import *
import tkinter.messagebox as messagebox

class base():
    def __init__(self):
        self.root= Tk()
        self.root.title("痒痒猫")
        self.root.geometry('500x500')
        self.frames = []

        self.frames.append(home(self.root))
        self.frames.append(setting(self.root))
        frm = Frame(self.root)
        Button(frm,text="首页",command = lambda :self.change('home')).pack(side=LEFT)
        Button(frm,text="配置",command = lambda :self.change('setting')).pack(side=LEFT)
        Button(frm,text="关于", command=h).pack(sid=RIGHT)
        frm.place(x=5,y=5)
        self.change('home')

    def change(self, name):
        for frame in self.frames:
            if frame.name == name:
                frame.display()
            else :
                frame.destroy()

class home():
    def __init__(self,master):
        self.master = master
        self.name = 'home'
        self.frame = Frame(self.master)

    def display(self):
        self.frame = Frame(self.master)
        Label(self.frame,text="fhdksjhfkdjs").pack()
        self.frame.place(x=5,y=50)

    def destroy(self):
        self.frame.destroy()

class setting():
    def __init__(self,master):
        self.master = master
        self.name = 'setting'
        self.frame = Frame(self.master)

    def display(self):
        self.frame = Frame(self.master)
        Label(self.frame,text="好看的交换机反馈会更快").pack()
        self.frame.place(x=5,y=50)

    def destroy(self):
        self.frame.destroy()

def create_ui():
    root = base()
    root.root.mainloop()

def h():
    messagebox.showinfo("版权","© 2020 Clover")

create_ui()