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

def raise_frame(frame): #function that allows to switch between two frames for implemnting different things
    frame.tkraise()


frame = Frame(root, relief='raised', borderwidth=2) #mainframe of page
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

copy_of_image = Image.open("images/firstimage.jpg")
photo = ImageTk.PhotoImage(copy_of_image)

label = Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

center_frame = Frame(frame, relief='raised',bg="pink",width=500,height=300) #center frame for the functionalities
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
w = Label(center_frame, text ="Welcome to Aadhiksha Society!",bg="lightskyblue",fg="black")
w.config(font=("Courier", 20))
w.place( anchor="n",relx=0.5,rely=0.2)

regButton = Button(center_frame,text="Register/Login to your Account!",bg="lightblue",fg="black",relief="raised",  command=lambda:raise_frame(register_frame)) #register button on first page
regButton.config(font=("Courier", 10))
regButton.place( anchor="n",relx=0.5,rely=0.4)


infoButton = Button(center_frame,text="View more info!",bg="lightblue",fg="black",relief="raised")
infoButton.config(font=("Courier", 10))
infoButton.place( anchor="n",relx=0.5,rely=0.6)

register_frame = Frame(frame, relief='raised',bg="pink",width=500,height=300)
register_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
w = Label(register_frame, text ="Register!",bg="lightskyblue",fg="black")
w.config(font=("Courier", 20))
w.place( anchor="n",relx=0.5,rely=0.2)
name = Label(register_frame,text ="First Name",bg="lightskyblue",fg="black") #Label box for name
name.config(font=("Courier",10))
name.place( anchor="n",relx=0.2,rely=0.4)
entry1 = Entry(register_frame) #entry box for name
entry1.place(anchor="n",relx=0.7,rely=0.4)
flat = Label(register_frame,text ="Flat no.",bg="lightskyblue",fg="black") #Label box for flat no.
flat.config(font=("Courier",10))
flat.place( anchor="n",relx=0.2,rely=0.6)
entry2 = Entry(register_frame) #entry box for flat no.
entry2.place(anchor="n",relx=0.7,rely=0.6)
tenants = Label(register_frame,text ="Number of tenants",bg="lightskyblue",fg="black") #Label box for tenants
tenants.config(font=("Courier",10))
tenants.place( anchor="n",relx=0.2,rely=0.8)
entry3 = Entry(register_frame) #entry box for tenants
entry3.place(anchor="n",relx=0.7,rely=0.8)

submitButton = Button(register_frame,text="Submit!",bg="lightblue",fg="black",relief="raised")
submitButton.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submitButton.place( anchor="n",relx=0.3,rely=0.9)



raise_frame(center_frame)
root.mainloop()