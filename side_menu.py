from tkinter import *
import tkinter as t
from tkinter import ttk,messagebox
import tkinter.messagebox
def side(window_name):
    side_menu=t.Menu()
    more_options=t.Menu(side_menu,tearoff=False,bd=15,font="Times 30 bold") 
    side_menu.add_cascade(label="More Options",menu=more_options)
    def Help():
        top=t.Tk()
        top.title("Help")
        top.geometry("500x350+0+0")
        faq_box=LabelFrame(top,text="Shortcut Keys",font="Times 25 ",foreground="black",bd=0)
        faq_box.grid(row=0,column=0)
        labels=['Costumer  --> 1','Item      --> w','Invoice   --> e','Report    --> r','Account   --> t','Billing   --> y','Purchase  --> u','Back      --> Escape','Exit App  --> Escape ']
        for i in range(len(labels)):
            cur_label="label"+str(i)
            cur_label=t.Label(faq_box,text=labels[i],font="consolas 12")
            cur_label.grid(row=i,column=0,sticky=t.W)
        def bck(event):
            top.destroy()
        top.bind("<Escape>",bck)
        top.focus_force()
        top.resizable(0,0)
    more_options.add_command(label="Help",compound=t.LEFT,command=Help,accelerator="",font="Times 16",background="powder blue")
    def dev():
        top=t.Tk()
        top.title("About")
        top.geometry("500x350+0+0")
        faq_box=LabelFrame(top,bd=0)
        faq_box.grid(row=0,column=0)
        Label(faq_box,text="GST Invoice",font="Times 20 bold").grid(row=0,column=0,pady=5,sticky=t.W)
        Label(faq_box,text="Version: 0.1 (Stable)",font="Helvetica 10").grid(row=1,column=0,sticky=t.W)
        Label(faq_box,text="Copyright (c) 2020.All rights reserved",font="Helvetica 10").grid(row=2,column=0,sticky=t.W)
        Label(faq_box,text="Developed by: Arish Ahmad",font="Times 20 bold").grid(row=3,column=0,pady=5,sticky=t.W)
        Label(faq_box,text="For any queries,bug reports or Feedback",font="Helvetica 10").grid(row=4,column=0,sticky=t.W)
        Label(faq_box,text="Contact at :",font="Helvetica 10").grid(row=5,column=0,sticky=t.W)
        Label(faq_box,text="arishahmad70@gmail.com",font="Helvetica 10",fg="blue").grid(row=5,column=0)
        def bck(event):
            top.destroy()
        top.bind("<Escape>",bck)
        top.focus_force()
        top.resizable(0,0)
    more_options.add_command(label="About",compound=t.LEFT,accelerator="",command=dev,font="Times 16",background="powder blue")
    def exit():
        if messagebox.askyesno(parent=window_name,title="Exit",message="Are you sure?"):
            window_name.quit()
    more_options.add_command(label="Exit Application",compound=t.LEFT,accelerator="Esc",command=exit,background="powder blue",font="Times 16")
    return side_menu