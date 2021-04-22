from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import MySQLdb
connection=MySQLdb.connect(host='localhost',database='society', user='root',password='root')

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

copy_of_image = Image.open("images/building.jpg")
photo = ImageTk.PhotoImage(copy_of_image)

label = Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)
#-----------------------------------Main Page------------------------------------#
center_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #center frame for the functionalities
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


watchButton = Button(center_frame,text="Login watchman/secretary!",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(watch_frame))
watchButton.config(font=("Courier", 10))
watchButton.place( anchor="n",relx=0.5,rely=0.8)
#-----------------------------------Register Page------------------------------#
def submit():
    r_name=namee.get()
    r_flat_no=flat_no.get()
    r_password=paswd.get()
    cursor = connection.cursor()
    strr='INSERT INTO residents(r_name,r_flat_no,r_password) VALUES(%s,%s,%s)'
    data=(r_name,r_flat_no,r_password)
    cursor.execute(strr,data)
    connection.commit()
    if(cursor.execute(strr,data)):
        submit_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #frame after clicking on submit
        submit_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg = Label(submit_frame, text ="You are registered successfully!",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        loginButton = Button(submit_frame,text="Login",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(login_frame))
        loginButton.config(font=("Courier", 10))
        loginButton.place( anchor="n",relx=0.5,rely=0.7)
    else:
        submit_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #frame after clicking on submit
        submit_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg = Label(submit_frame, text ="please try again!",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        backbutton = Button(submit_frame,text="back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(register_frame))
        backbutton.config(font=("Courier", 10))
        backbutton.place( anchor="n",relx=0.6,rely=0.5)
        
namee=StringVar()
flat_no=StringVar()
paswd=StringVar()
register_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
register_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
w = Label(register_frame, text ="Register!",bg="lightskyblue",fg="black")
w.config(font=("Courier", 20))
w.place( anchor="n",relx=0.5,rely=0.1)
name = Label(register_frame,text ="First Name",bg="lightskyblue",fg="black") #Label box for name
name.config(font=("Courier",10))
name.place( anchor="n",relx=0.2,rely=0.3)
entry1 = Entry(register_frame,bd=5,textvariable=namee) #entry box for name
entry1.place(anchor="n",relx=0.7,rely=0.3)
flat = Label(register_frame,text ="Flat no.",bg="lightskyblue",fg="black") #Label box for flat no.
flat.config(font=("Courier",10))
flat.place( anchor="n",relx=0.2,rely=0.5)
entry2 = Entry(register_frame,bd=5,textvariable=flat_no) #entry box for flat no.
entry2.place(anchor="n",relx=0.7,rely=0.5)
password = Label(register_frame,text ="Password",bg="lightskyblue",fg="black") #Label box for password
password.config(font=("Courier",10))
password.place( anchor="n",relx=0.2,rely=0.7)
entry3 = Entry(register_frame,bd=5,textvariable=paswd) #entry box for password
entry3.place(anchor="n",relx=0.7,rely=0.7)

submitButton = Button(register_frame,text="Submit!",bg="lightblue",fg="black",relief="raised",command=submit)
submitButton.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submitButton.place( anchor="n",relx=0.2,rely=0.9)

loginButton = Button(register_frame,text="Already have an account? Login",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(login_frame))
loginButton.config(font=("Courier", 10)) #incase user already has an account he can login
loginButton.place( anchor="n",relx=0.6,rely=0.9)

#----------------------Login Page--------------------------#
def login():
    l_flat=lo_flat.get()
    l_pass=lo_pass.get()
    sql_select_Query = 'select * from residents where r_flat_no=%s and r_password=%s'
    data=(l_flat,l_pass)
    cursor = connection.cursor()
    cursor.execute(sql_select_Query,data)
    if(cursor.execute(sql_select_Query,data)):
        print(l_flat)
        l_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #frame after clicking on login
        l_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg = Label(l_frame, text ="You are logged in!.Welcome flatno."+l_flat,bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        proceed_button = Button(l_frame,text="proceed",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(residents_main_frame))#ye proceed button click ke baad fuctions for residents should be visible.residents_main_frame ab iss function ke bahar likhna
        proceed_button.config(font=("Courier", 10))
        proceed_button.place( anchor="n",relx=0.5,rely=0.9)
    else:
        print("failed")
        l_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #frame after clicking on submit
        l_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg = Label(l_frame, text ="please try again!",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        backbutton = Button(l_frame,text="back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(login_frame))
        backbutton.config(font=("Courier", 10))
        backbutton.place( anchor="n",relx=0.6,rely=0.5)
    

lo_flat=StringVar()
lo_pass=StringVar()
login_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
w1 = Label(login_frame, text ="Login!",bg="lightskyblue",fg="black")
w1.config(font=("Courier", 20))
w1.place( anchor="n",relx=0.2,rely=0.1)


flat1 = Label(login_frame,text ="Flat no.",bg="lightskyblue",fg="black") #Label box for flat no.
flat1.config(font=("Courier",10))
flat1.place( anchor="n",relx=0.2,rely=0.5)
entry21 = Entry(login_frame,bd=5,textvariable=lo_flat) #entry box for flat no.
entry21.place(anchor="n",relx=0.7,rely=0.5)
password1 = Label(login_frame,text ="Password",bg="lightskyblue",fg="black") #Label box for password
password1.config(font=("Courier",10))
password1.place( anchor="n",relx=0.2,rely=0.7)
entry31 = Entry(login_frame,bd=5,textvariable=lo_pass) #entry box for password
entry31.place(anchor="n",relx=0.7,rely=0.7)

submitButton = Button(login_frame,text="login!",bg="lightblue",fg="black",relief="raised", command=login)
submitButton.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submitButton.place( anchor="n",relx=0.5,rely=0.9)



#----------------------watchman/secretary Login Page--------------------------#
def login_watch():
    l_wpass=lo_wpassword.get()
    l_wuser=lo_wusername.get()
    global l_frame
    if(l_wuser=='aadhiksha_wat123' and l_wpass=='12345'):
        l_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #frame after clicking on login
        l_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        msg = Label(l_frame, text ="You are logged in!.\nWelcome to aadhiksha cabinet(watchman).",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        proceed_button = Button(l_frame,text="proceed",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(watchman_frame))#ye proceed button click ke baad fuctions for watchman should be visible.watchman_main_frame ab iss function ke bahar likhna
        proceed_button.config(font=("Courier", 10))
        proceed_button.place( anchor="n",relx=0.5,rely=0.9)
    elif(l_wuser=='aadhiksha_sec123' and l_wpass=='12345'):
        l_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #frame after clicking on login
        l_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg = Label(l_frame, text ="You are logged in!.\nWelcome to aadhiksha cabinet(secretary).",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        proceed_button = Button(l_frame,text="proceed",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(secretary_main_frame))#ye proceed button click ke baad fuctions for secretary should be visible.secretary_main_frame ab iss function ke bahar likhna
        proceed_button.config(font=("Courier", 10))
        proceed_button.place( anchor="n",relx=0.5,rely=0.9)
    else:
        
        msg = Label(l_frame, text ="please try again!",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        backbutton = Button(l_frame,text="back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(watch_frame))
        backbutton.config(font=("Courier", 10))
        backbutton.place( anchor="n",relx=0.6,rely=0.5)





lo_wpassword=StringVar()
lo_wusername=StringVar()
watch_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
watch_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
w2 = Label(watch_frame, text ="Login!",bg="lightskyblue",fg="black")
w2.config(font=("Courier", 20))
w2.place( anchor="n",relx=0.5,rely=0.1)

flat2 = Label(watch_frame,text ="Username",bg="lightskyblue",fg="black") #Label box for flat no.
flat2.config(font=("Courier",10))
flat2.place( anchor="n",relx=0.2,rely=0.5)
entry4 = Entry(watch_frame,bd=5,textvariable=lo_wusername) #entry box for flat no.
entry4.place(anchor="n",relx=0.7,rely=0.5)
password1 = Label(watch_frame,text ="Password",bg="lightskyblue",fg="black") #Label box for password
password1.config(font=("Courier",10))
password1.place( anchor="n",relx=0.2,rely=0.7)
entry5 = Entry(watch_frame,bd=5,textvariable=lo_wpassword) #entry box for password
entry5.place(anchor="n",relx=0.7,rely=0.7)

submitButton = Button(watch_frame,text="login!",bg="lightblue",fg="black",relief="raised", command=login_watch)
submitButton.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submitButton.place( anchor="n",relx=0.2,rely=0.9)
backlogin = Button(watch_frame,text="Back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(center_frame))
backlogin.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
backlogin.place( anchor="n",relx=0.6,rely=0.9)

#----------------------------Resident's Frames----------------------------------------#
def res_notice():
    notices=" "
    f=open("notices.txt")
    notices=f.read()
    raise_frame(residents_notice_frame)
    notsec = Label(residents_notice_frame, text =notices,bg="lightskyblue",fg="black")
    notsec.config(font=("Courier", 10))
    notsec.place( anchor="n",relx=0.5,rely=0.1)
    backnotButton = Button(residents_notice_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(residents_main_frame))
    backnotButton.config(font=("Courier", 10)) 
    backnotButton.place( anchor="n",relx=0.5,rely=0.9)

residents_main_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #first screen after watchman logs in
residents_main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
welres = Label(residents_main_frame, text ="Welcome Resident!",bg="lightskyblue",fg="black")
welres.config(font=("Courier", 20))
welres.place( anchor="n",relx=0.5,rely=0.1)
viewNotice = Button(residents_main_frame,text="View Notices!",bg="lightblue",fg="black",relief="raised",command=res_notice)
viewNotice.config(font=("Courier", 10)) 
viewNotice.place( anchor="n",relx=0.2,rely=0.4)
backresButton = Button(residents_main_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(login_frame))
backresButton.config(font=("Courier", 10)) 
backresButton.place( anchor="n",relx=0.6,rely=0.4)
residents_notice_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #first screen after watchman logs in
residents_notice_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
notres = Label(residents_notice_frame, text ="Notices Section",bg="lightskyblue",fg="black")
notres.config(font=("Courier", 10))
notres.place( anchor="n",relx=0.5,rely=0.01)


#------------------------------------Watchman's Functions-----------------------------------#
def notices_fun(): #function for writing the notices entered by the watchman on the file.
    date_notice=notice_d.get()
    content_notice=notice_con.get()
    f=open("notices.txt","a") #notices.txt is the text file to which the notice is to be written.
    f.write("\n")
    f.write(date_notice)
    f.write("       ")
    f.write(content_notice)
def displaymsgbox():
    messagebox.askokcancel("Notice Creation","Your notice has been created!") 
#----------------------------------Tkinter Stuff for Notices by watchman--------------------------#
watchman_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #first screen after watchman logs in
watchman_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
w2 = Label(watchman_frame, text ="Welcome watchman!",bg="lightskyblue",fg="black")
w2.config(font=("Courier", 20))
w2.place( anchor="n",relx=0.5,rely=0.1)
noticeButton = Button(watchman_frame,text="Create notice for residents",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(notices_frame))
noticeButton.config(font=("Courier", 10)) 
noticeButton.place( anchor="n",relx=0.5,rely=0.4)
backwatchButton = Button(watchman_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(watch_frame))
backwatchButton.config(font=("Courier", 10)) 
backwatchButton.place( anchor="n",relx=0.5,rely=0.8)
notices_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
notices_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
w2 = Label(notices_frame, text ="Section for notices!",bg="lightskyblue",fg="black")
w2.config(font=("Courier", 20))
w2.place( anchor="n",relx=0.5,rely=0.1)

notice_d=StringVar() #variable to take in date of notice
notice_con=StringVar() #variable to take in content of notice
date = Label(notices_frame,text ="Date of notice",bg="lightskyblue",fg="black") #Label box for date of notice
date.config(font=("Courier",10))
date.place( anchor="n",relx=0.2,rely=0.3)
entryd = Entry(notices_frame,bd=5,textvariable=notice_d) #entry box for date of notice
entryd.place(anchor="n",relx=0.7,rely=0.3)
content = Label(notices_frame,text ="Notice",bg="lightskyblue",fg="black") #Label box for notice.
content.config(font=("Courier",10))
content.place( anchor="n",relx=0.2,rely=0.5)
entryc = Entry(notices_frame,bd=5,textvariable=notice_con) #entry box for notice.
entryc.place(anchor="n",relx=0.7,rely=0.5)
submitnotice = Button(notices_frame,text="Create Notice",bg="lightblue",fg="black",relief="raised", command=lambda:[notices_fun(),displaymsgbox()])
submitnotice.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submitnotice.place( anchor="n",relx=0.2,rely=0.9)
backnotice = Button(notices_frame,text="Back",bg="lightblue",fg="black",relief="raised", command=lambda:raise_frame(watchman_frame))
backnotice.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
backnotice.place( anchor="n",relx=0.6,rely=0.9)
#begin secretary_main_frame . fuctions for secretary should be visible


raise_frame(center_frame)
root.mainloop()


