from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
import PIL.ImageGrab as ImageGrab

# ^ Modules Imports

# Main Screen
root = Tk()
root.title("Paint App")
root.geometry("1200x700+160+60")
root.config(bg='grey30')

# Variables
pen_color=StringVar()
pen_color.set('black')
previousColor1=StringVar()
previousColor1.set('black')
previousColor2=StringVar()
previousColor2.set('grey')

pen_size=IntVar()
pen_size_last=IntVar()
pen_size_last.set(1)
option=[1,2,4,6,8,10,12,14,18,24]

preCondinate=[0,0]
curCondinate=[0,0]

# Funtions 

def usePencil():
    pen_color.set("black")
    canvas["cursor"] = "tcross"
    pen_size.set(pen_size_last.get())

def defaultPen_Size():
    pen_size.set(1)

def selectColor():
    selectedcolor=colorchooser.askcolor("red",title="Select Color")
    if selectedcolor[1]==None:
        pen_color.set('black')
    else:
        pen_color.set(selectedcolor[1])
        previousColor2.set(previousColor1.get())
        previousColor1.set(selectedcolor[1])
        preColor1['bg']=previousColor1.get()
        preColor2['bg']=previousColor2.get()

def backcolor():
    backgroundcolor=colorchooser.askcolor("white",title="Select Color")
    if backgroundcolor[1]==None:
        canvas['bg']='white'
    else:
        if messagebox.askokcancel("Paint App Confirmation","This will clear the workspace.Do you want to continue?"):
            canvas.delete('all')
            canvas['bg']=backgroundcolor[1]

def useEraser():
    if canvas['bg']!='white':
        pen_color.set(canvas['bg'])
    else:
        pen_color.set("white")
    canvas["cursor"] = "dotbox"
    pen_size_last.set(pen_size.get())
    pen_size.set(24)

def saveImage():
    try:
        fileLocation = filedialog.asksaveasfilename(defaultextension="jpg")
        i=canvas.winfo_rootx()
        j=canvas.winfo_rooty()
        img=ImageGrab.grab(bbox=(i+87,j+40,1700,964))
        img.save(fileLocation)
        showImage = messagebox.askyesno("Open Image" , "Do you want to open image?")
        if showImage:
            img.show()

    except Exception as e:
        messagebox.showinfo("Paint App: Not Save" , "Error Occured : Not Saved")

def clear():
    if messagebox.askokcancel("Paint App Confirmation","Clearing workspace..."):
        canvas.delete('all')

def createnew():
    if messagebox.askyesno("Paint App Confirmation","Do you want to Save workspace"):
        saveImage()
    clear()
    canvas['bg']='white'

def helpbar():
    helpwin= Toplevel(root)
    helpwin.geometry("650x450+160+60")
    helpwin.title("Help")
    head_helpframe=Frame(helpwin,height=50,)
    head_helpframe.grid(row=0,column=0,sticky=NW,padx=250,pady=20)
    body_helpframe=Frame(helpwin,height=350)
    body_helpframe.grid(row=1,column=0,sticky=S,pady=20,padx=30)
    Label(head_helpframe, text="Paint Version 1.0.0"+'\n'+"2023 Work", font=('Helvetica 13 bold')).grid(row=0,column=0)
    Label(body_helpframe,wraplength=600, text="Paint app is a software application that allows users to create digital drawings, sketches or paintings using a computer.The app provides tools such as pencil, colors, and erasers to help users create their artwork.", font=('Helvetica 10')).grid(sticky=W,row=0,column=0)
    Label(body_helpframe,wraplength=600, text="Some of Tools are:", font=('Helvetica 10')).grid(sticky=W,row=1,column=0)
    Label(body_helpframe,wraplength=600, text="Pencil:Using pencil you can create your artwork on workspace", font=('Helvetica 10')).grid(sticky=W,row=2,column=0)
    Label(body_helpframe,wraplength=600, text="Eraser:Using Eraser you can Erase what is written by pencil", font=('Helvetica 10')).grid(sticky=W,row=3,column=0)
    Label(body_helpframe,wraplength=600, text="Default & Pen Size:Using pensize dropdown list you can select pen size. Default will make your pen size default which is 1", font=('Helvetica 10')).grid(sticky=W,row=4,column=0)
    Label(body_helpframe,wraplength=600, text="Background Color:Your can use this button to change background color of workspace", font=('Helvetica 10')).grid(sticky=W,row=5,column=0)
    Label(body_helpframe,wraplength=600, text="New:You can create new workspace with this button", font=('Helvetica 10')).grid(sticky=W,row=6,column=0)
    Label(body_helpframe,wraplength=600, text="Save:You can save your work from workspace into system storage using this.Default filetype is .jpg", font=('Helvetica 10')).grid(sticky=W,row=7,column=0)
    Label(body_helpframe,wraplength=600, text="Clear:This will clear your workspace", font=('Helvetica 10')).grid(sticky=W,row=8,column=0)
    helpwin.wm_attributes('-toolwindow', 'True') 

def about():
    aboutwin= Toplevel(root)
    aboutwin.geometry("450x250+160+60")
    aboutwin.title("About")
    Label(aboutwin, text="Paint Version 1.0.0"+'\n'+"2023 Work", font=('Helvetica 13 bold')).pack(fill=BOTH, anchor="n",pady=30)
    Label(aboutwin, text="Thank for using this program", font=('Helvetica 10')).pack(padx=30,fill=BOTH)
    Label(aboutwin, text="Project by Gaurav Kumar Ladhar and Ankit Jhangir", font=('Helvetica 10')).pack(padx=30,fill=BOTH)
    aboutwin.wm_attributes('-toolwindow', 'True') 

def servicedelay():
    messagebox.showinfo("Paint App","In Devlopment"+'\n'+"This feature will come soon")

def paint(event):
    global preCondinate,curCondinate
    x=event.x
    y=event.y
    curCondinate=[x,y]
    if preCondinate != [0,0] :
        canvas.create_line(preCondinate[0],preCondinate[1], event.x, event.y,width=pen_size.get(),fill=pen_color.get(),capstyle=ROUND, smooth=TRUE,splinesteps=20)
    preCondinate=curCondinate
    if event.type == "5" :
        preCondinate=[0,0]

# >>> Menu 

#File Menu
menubar=Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=createnew)
filemenu.add_command(label="Save",command=saveImage)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#Help Menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Learn to use Paint Application",command=helpbar)
helpmenu.add_command(label="Paint App FAQ",command=servicedelay)
menubar.add_cascade(label="Help", menu=helpmenu,command=saveImage)

Aboutmenu = Menu(menubar, tearoff=0)
Aboutmenu.add_command(label="About",command=about)
menubar.add_cascade(label="About", menu=Aboutmenu)

# >>> Main GUI

# Main GUI root object
frame1=Frame(root,height=700,width=160,bg='grey15')
frame1.grid(row=0,column=0,sticky=N)
colorframe=Frame(root,width=160,borderwidth=10,bg='grey96')
colorframe.grid(row=0,column=0,sticky=N,pady=30)
toolframe=Frame(root,width=160,bg='grey96')
toolframe.grid(row=0,column=0,sticky=S,pady=20)

# >> Color Buttons

color1=Button(colorframe,height=1,width=3,bg='red',relief=FLAT,command=lambda:pen_color.set('red'))
color1.grid(row=0,column=0,pady=2,padx=1)
color2=Button(colorframe,height=1,width=3,bg='gold',relief=FLAT,command=lambda:pen_color.set('gold'))
color2.grid(row=0,column=1,pady=2,padx=1)
color3=Button(colorframe,height=1,width=3,bg='darkgreen',relief=FLAT,command=lambda:pen_color.set('darkgreen'))
color3.grid(row=0,column=2,pady=2,padx=1)
color4=Button(colorframe,height=1,width=3,bg='orange',relief=FLAT,command=lambda:pen_color.set('orange'))
color4.grid(row=1,column=0,pady=2,padx=1)
color5=Button(colorframe,height=1,width=3,bg='yellow',relief=FLAT,command=lambda:pen_color.set('yellow'))
color5.grid(row=1,column=1,pady=2,padx=1)
color6=Button(colorframe,height=1,width=3,bg='green',relief=FLAT,command=lambda:pen_color.set('green'))
color6.grid(row=1,column=2,pady=2,padx=1)
color7=Button(colorframe,height=1,width=3,bg='brown',relief=FLAT,command=lambda:pen_color.set('brown'))
color7.grid(row=2,column=0,pady=2,padx=1)
color8=Button(colorframe,height=1,width=3,bg='black',relief=FLAT,command=lambda:pen_color.set('black'))
color8.grid(row=2,column=1,pady=2,padx=1)
color9=Button(colorframe,height=1,width=3,bg='darkblue',relief=FLAT,command=lambda:pen_color.set('darkblue'))
color9.grid(row=2,column=2,pady=2,padx=1)
color10=Button(colorframe,height=1,width=3,bg='grey',relief=FLAT,command=lambda:pen_color.set('grey'))
color10.grid(row=3,column=0,pady=2,padx=1)
color11=Button(colorframe,height=1,width=3,bg='white',relief=FLAT,command=lambda:pen_color.set('white'))
color11.grid(row=3,column=1,pady=2,padx=1)
color12=Button(colorframe,height=1,width=3,bg='blue',relief=FLAT,command=lambda:pen_color.set('blue'))
color12.grid(row=3,column=2,pady=2,padx=1)

ColorBoxButton=Button(colorframe,height=4,width=8,bg='grey80',text="Color",relief=FLAT,command=selectColor)
ColorBoxButton.grid(row=4,column=0,pady=5,columnspan=2,rowspan=2,padx=1)
preColor1=Button(colorframe,height=1,width=2,bd=5,bg='black',relief=FLAT,command=lambda:pen_color.set(previousColor1.get()))
preColor1.grid(row=4,column=2,padx=3)
preColor2=Button(colorframe,height=1,width=2,bd=5,bg='grey',relief=FLAT,command=lambda:pen_color.set(previousColor2.get()))       
preColor2.grid(row=5,column=2,padx=3)

# >> Tools Buttons
pencil=Button(toolframe,height=3,width=6,text="Pencil",bg='grey75',relief=FLAT,command=usePencil)
pencil.grid(row=2,column=0,padx=5,pady=7)
eraser=Button(toolframe,height=3,width=6,text="Eraser",bg='grey75',relief=FLAT,command=useEraser)
eraser.grid(row=2,column=1,padx=5,pady=7)
pensize_d=Button(toolframe,height=3,width=6,text="Default",bg='grey75',relief=FLAT,command=defaultPen_Size)
pensize_d.grid(row=3,column=0,padx=5,pady=7)
sizelist=OptionMenu(toolframe, pen_size, *option)
sizelist.config(height=3,width=2,highlightthickness=0,bg='grey75',relief=FLAT)
sizelist.grid(row=3,column=1,padx=5,pady=7)
bodycolor=Button(toolframe,height=2,width=15,text="Backgroung Color",bg='grey75',relief=FLAT,command=backcolor)
bodycolor.grid(row=4,column=0,columnspan=2,pady=7)
newimage=Button(toolframe,height=2,width=15,text="New",bg='grey75',relief=FLAT,command=createnew)
newimage.grid(row=5,column=0,columnspan=2,pady=7)
saveimage=Button(toolframe,height=2,width=15,text="Save",bg='grey75',relief=FLAT,command=saveImage)
saveimage.grid(row=6,column=0,columnspan=2,pady=7)
clearimage=Button(toolframe,height=2,width=15,text="Clear",bg='grey75',relief=FLAT,command=clear)
clearimage.grid(row=7,column=0,columnspan=2,pady=7)

canvas= Canvas(root,height=660,width=1020,bg='white')
canvas.grid(row=0,column=1,padx=10,sticky=W)

canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>",paint)

root.wm_attributes('-toolwindow', 'True')
root.resizable(False,False)
root.config(menu=menubar)
root.mainloop()