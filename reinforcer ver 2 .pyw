
from ast import excepthandler
from fileinput import filename
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo    
import os
from tkinter import font
import threading
from tkinter import *
from tkinter import ttk
import time


root=Tk()
root.geometry("440x530")
root.config(bg='#fbeae2')
root.attributes("-alpha",0.95)
root.resizable(0,0)
done=False
fn=False
name="Output image.png"
fileloc = StringVar()
saveloc = StringVar()
c=0

def brain():
    done=False
    global filename
    global names
    names=""
    try:
        for i in filename:
            print(i)
    except :
        showinfo(title='File error inbound',message="Try browsing the file using browse button !")
        # list(filename0.append(ebox.get())            
    try:
        if len(filename) == 0:
            showinfo(title='File error inbound',message="No files or directories selected !")
    except TypeError:
            showinfo(title='File error inbound',message="No files or directories selected !")  
            return    
    try:
        for i in filename:
                
                Reformat_Image_With_Ratio(i)           
                names = i
        if fn!=True:
            showinfo(title='Processing task status...',message="Task completed successfully") 
    except Exception as e :
        showinfo(title='Processing task status...',message="Task incomplete !\n "+str(e) )                     
    # try:        
    #     for i in filename:
            
    #         Reformat_Image_With_Ratio(i)        
    # except Exception as e:
    #      showinfo(title='User error inbound',message=e)
        

def Reformat_Image_With_Ratio(imt):
    global done
    done=False
    global c
    global name
    from PIL import Image
    ImageFilePath=imt
    target_width, target_height=width.get(),hieght.get()
    im = Image.open(ImageFilePath, 'r')
    target_ratio = target_height / target_width
    im_ratio = im.height / im.width
    if target_ratio > im_ratio:
        # It must be fixed by width
        resize_width = target_width
        resize_height = round(resize_width * im_ratio)
        print("Resizing image with ratio ")
    else:
        # Fixed by height
        resize_height = target_height
        resize_width = round(resize_height / im_ratio)
    print(resize_width,resize_height)
    image_resize = im.resize((resize_width, resize_height), Image.NEAREST)
    # image_resize.show()
    background = Image.new('RGBA', (target_width, target_height), (255, 255, 255, 255))
    offset = (round((target_width - resize_width) / 2), round((target_height - resize_height) / 2))
    background.paste(image_resize, offset)
    # background.show()
    background=background.convert('RGB')
    # path=os.path.split(ebox3.get())
    path=(ebox3.get())
    name='Output image.png'
    print(path)
    print(name)
    if os.path.exists(path+"\\"+name):
        print('file exist')
        c=c+1
        name="Output image"+str(c)+".png"
    else:
        c=0
        name="Output image"+".png"
    fpath=path+"//"+name

    if os.path.exists(ebox3.get()):
        print(fpath)
        background.save(fpath)
        fn=False
    else:
         showinfo(title='Save error inbound',message="Directory name invalid ! Check your directory \n name and try again")    
         fn=True 
         
    done=True

# def Reformat_Image_With_Ratio_old():
#     global done
#     global c
#     global name
#     done=False
#     from PIL import Image
#     ImageFilePath=ebox.get()
#     desired_aspect_ratio=width.get()/hieght.get()
#     image = Image.open(ImageFilePath, 'r')
#     width1 = image.width
#     height1 = image.height
#     img_aspect_ratio = width1/height1
#     print()
#     if (img_aspect_ratio != desired_aspect_ratio):
#         if width1 > height1:
#             bigside = width1
#         else:
#             bigside = height1    
#         other_side = int(bigside * desired_aspect_ratio)
#         background = Image.new('RGBA', (other_side, bigside), (255,255,255))
#         offset = (int(round(((bigside - width1) / 2), 0)), int(round(((bigside - height1) / 2),0)))
#         image= image.resize((width.get()*1000, hieght.get()*1000), Image.ANTIALIAS)
#         background.paste(image, offset)
#         path=os.path.split(ebox3.get())
#         if os.path.exists(path[0]+"\\"+name):
#             c=c+1
#             name="Output image"+str(c)+".png"
#         else:
#             c=0
#             name="Output image"+".png"
#         fpath=path[0]+"\\"+name
#         print(fpath)
        
#         background.save(fpath)
#         background.show()
#         print("Image has been resized !")

#     else:
#         print("Image is already a valid aspect ratio, it has not been resized !")
#     done=True

frame=Frame(root,bg=root.cget('bg'),relief="flat",bd=0)
frame.place(x=-1,y=20,relwidth=11, relheight=0.18,)

frame23=Frame(root,bg=root.cget('bg'),relief="flat",bd=0)
frame23.place(x=-1,y=510,relwidth=11, relheight=0.18,)



l1=Label(root,text=" Image Reinforcer ",font=("bauhaus 93","36","bold"),bg="#3f2829",fg="#fbeae2")
l1.place(x=10,y=215,)
root.update()
c=0
while c!=1:
    c=c+1
    time.sleep(0.2)
    # for i in ["#88c194",root.cget('bg')]:
    #     l1.config(fg=i)
    #     time.sleep(0.2) 
    #     root.update()

for i in reversed(range(35,200)):
    l1.place(x=11,y=i)
    root.update()
frame.config(bg="#3f2829")
frame23.config(bg="#3f2829")  
Lc=Label(frame23,text="FRIDAY © Copyright 2022 ",font=("bauhaus 93","9"),bg="#3f2829",fg="#fbeae2")
Lc.place(x=220,y=10,anchor="center")  
l1=Label(root,text="Image Location",font=("bauhaus 93","16",),fg="#3f2829",bg=root.cget('bg'))
l1.place(x=90,y=150,anchor="center")

ebox=Entry(root,width=30,font=("times","15"),bg="#c19c7d",bd=2,relief="flat")
ebox.place(x=70,y=180)

l1=Label(root,text="Image Size (pixals)",font=("bauhaus 93","16",),fg="#3f2829",bg=root.cget('bg'))
l1.place(x=110,y=250,anchor="center")

width=IntVar()
hieght=IntVar()

ebox1=Entry(root,width=5,font=("times","15"),bg="#c19c7d",textvariable=width,relief="flat")
ebox1.place(x=70,y=280)

l1=Label(root,text="X",font=("bauhaus 93","12",),fg="#3f2829",bg=root.cget('bg'))
l1.place(x=129,y=282)


ebox2=Entry(root,width=5,font=("times","15"),bg="#c19c7d",textvariable=hieght,relief="flat")
ebox2.place(x=150,y=280)

# sp = Spinbox(root,value=['  Instagram post','  Instagram story','  custom'],font=("times","15"),width=14,bg="#c19c7d",relief="flat")
# sp.place(x=225,y=280)

def type_req(e):
    typ=combobox.get()
    if str(typ).strip()=="Instagram post(Square Photo)":
        ebox1.delete(0,END)
        ebox2.delete(0,END)
        ebox1.insert(END,1080)
        ebox2.insert(END,1080)
    if str(typ).strip()=="Instagram post(Landscape Photo)":
        ebox1.delete(0,END)
        ebox2.delete(0,END)
        ebox1.insert(END,1080)
        ebox2.insert(END,608)
    elif str(typ).strip()=="Instagram post(Potrait Photo)":
        ebox1.delete(0,END)
        ebox2.delete(0,END)
        ebox1.insert(END,1080)
        ebox2.insert(END,1350)
    elif str(typ).strip()=="Instagram story":
        ebox1.delete(0,END)
        ebox2.delete(0,END)
        ebox1.insert(END,1080)
        ebox2.insert(END,1920)
    elif str(typ).strip()=="custom":
        ebox1.delete(0,END)
        ebox2.delete(0,END)
    else:
        print("Unknown")
    

def defocus(event):
    event.widget.master.focus_set()
    
def type_req2(e):
    print("sd")
    combobox.set(" custom")    
    
current_var = StringVar()
combobox = ttk.Combobox(root,values=[' Instagram post(Square Photo)',' Instagram post(Potrait Photo)',' Instagram post(Landscape Photo)',' Instagram story',' custom'],font=("times","15"),width=14,textvariable=current_var)
combobox.place(x=219,y=280)
combobox.config(state="readonly")
combobox.bind("<FocusIn>", defocus)
combobox.bind('<<ComboboxSelected>>', type_req)
ebox1.bind('<KeyRelease>', type_req2)
ebox2.bind('<KeyRelease>', type_req2)

l1=Label(root,text="Save Location",font=("bauhaus 93","16",),fg="#3f2829",bg=root.cget('bg'))
l1.place(x=90,y=350,anchor="center")

ebox3=Entry(root,width=30,textvariable=saveloc,font=("times","15"),bg="#c19c7d",bd=2,relief="flat")
ebox3.place(x=70,y=380)


def update(e):
    print("ha")
    ebox.insert(END,Spinbox.get())
    
    
    
def start():
    if ebox.get()=="":
        showinfo(title='Feature not avaliable',message="No files selected ")    
        return    
    t2=threading.Thread(target=brain)
    t2.start()        
    while done!=True:
        bt.config(text=" Processing...  ")
        root.update()
    bt.config(text="  Pocess image  ")        




def directoryloc():
    global loc,length,filename
    loc=[]
    filetypes = (
        ('Image files', ['*.jpg','*.png','*.jpeg','*.svg','*.ico','*.raw','*.webp']),
        ('All files', '*.*')
    )

    filename = fd.askopenfilenames(
        title='select files',
        initialdir='/',
        filetypes=filetypes)
    if len(filename)==0:
        showinfo(title='Selected File',message="No files selected")
    else:        
        showinfo(
            title='Selected File',
            message=filename
        )  
        length=len(filename) 
        ebox.delete(0,END)
    c=0
    for i in filename:
        # c=c+1
        if length==1:
            ebox.insert(END,i) 
        else:            
            loc.append(i) 
            ebox.insert(END,os.path.split(i)[1]+",") 
        
def directoryloc1():
    # filetypes = (
    #     ('Image files', ['*.jpg','*.png','*.jpeg','*.svg','*.ico','*.raw','*.webp']),
    #     ('All files', '*.*')
    # )

    filename = fd.askdirectory(
        title='select files',
        initialdir='/',)
    
    if len(filename)==0:
        showinfo(title='Selected File',message="No directory selected")
    else:        
        showinfo(
            title='Selected File',
            message=filename
        )  
        
    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )   
    
    ebox3.delete(0,END)
    ebox3.insert(END,filename) 
        

        
bt=Button(root,text="  Pocess image  ",width=20,font=("bauhaus 93","12",),bg="#88c194",bd=0,command=start)
bt.place(x=220,y=467,anchor="center",)

bt2=Button(root,text=" Browse ",font=("times","11",),bg="#c19c7d",bd=0,command=directoryloc)
bt2.place(x=313,y=181)

bt3=Button(root,text=" Browse ",font=("times","11",),bg="#c19c7d",bd=0,command=directoryloc1)
bt3.place(x=313,y=381)


# sp.bind('<<SpinboxSelected>>',update)
root.mainloop()
        
# Reformat_Image_With_Ratio("C:\\Users\\admin\Downloads\wp2562689-fhd-wallpapers.jpg",4/5)        