from tkinter import *
from PIL import Image, ImageTk

def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

root = Tk()
root.title("Title")
root.geometry('600x600')

frame = Frame(root, relief='raised', borderwidth=2)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

copy_of_image = Image.open("images/firstimage.jpg")
photo = ImageTk.PhotoImage(copy_of_image)

label = Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

center_frame = Frame(frame, relief='raised',bg="pink",width=500,height=300)
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
w = Label(center_frame, text ="Welcome to Aadhiksha Society!",bg="lightskyblue",fg="black")
w.config(font=("Courier", 20))
w.place( anchor="n",relx=0.5,rely=0.2)

regButton = Button(center_frame,text="Register/Login to your Account!",bg="lightblue",fg="black",relief="raised")
regButton.config(font=("Courier", 10))
regButton.place( anchor="n",relx=0.5,rely=0.4)

infoButton = Button(center_frame,text="View more info!",bg="lightblue",fg="black",relief="raised")
infoButton.config(font=("Courier", 10))
infoButton.place( anchor="n",relx=0.5,rely=0.6)

root.mainloop()