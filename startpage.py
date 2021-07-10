from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import re
import MySQLdb
connection=MySQLdb.connect(host='localhost',database='society', user='root',password='')
cursor=connection.cursor()

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
    r_flat_no=flat_noo.get()
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
flat_noo=StringVar()
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
entry2 = Entry(register_frame,bd=5,textvariable=flat_noo) #entry box for flat no.
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
        msg = Label(l_frame,text ="please try again!",bg="lightskyblue",fg="black")
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
b_log = Button(login_frame,text="Back",bg="lightblue",fg="black",relief="raised", command=lambda:raise_frame(center_frame))
b_log.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
b_log.place( anchor="n",relx=0.6,rely=0.9)



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
        l_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #frame after clicking on login
        l_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
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
flat2.place( anchor="n",relx=0.2,rely=0.3)
entry4 = Entry(watch_frame,bd=5,textvariable=lo_wusername) #entry box for flat no.
entry4.place(anchor="n",relx=0.7,rely=0.3)
password1 = Label(watch_frame,text ="Password",bg="lightskyblue",fg="black") #Label box for password
password1.config(font=("Courier",10))
password1.place( anchor="n",relx=0.2,rely=0.5)
entry5 = Entry(watch_frame,bd=5,textvariable=lo_wpassword) #entry box for password
entry5.place(anchor="n",relx=0.7,rely=0.5)

submitButton = Button(watch_frame,text="login!",bg="lightblue",fg="black",relief="raised", command=login_watch)
submitButton.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submitButton.place( anchor="n",relx=0.2,rely=0.8)
backlogin = Button(watch_frame,text="Back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(center_frame))
backlogin.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
backlogin.place( anchor="n",relx=0.6,rely=0.9)



#----------------------------Resident's Frames----------------------------------------#
def res_notice():
    from datetime import date,datetime
    today=str(date.today())
    notices=" "
    newstr=""
    f=open("notices.txt")
    f1=open("today_notice.txt","a")
    for x in f:
        x=x.strip("\n")
        t=re.findall(r'\d{4}-\d{2}-\d{2}',x)
        newstr=newstr.join(t)
        if newstr==today:
            f1.write(x)
            f1.write("\n")
            
               
    f.close() 
    f1.close()
    f1=open("today_notice.txt","r+")
    today_notice=f1.read()
    nottod = Label(residents_notice_frame, text=today_notice,bg="lightskyblue",fg="black")
    nottod.config(font=("Courier", 10))
    nottod.place( anchor="n",relx=0.5,rely=0.7)
    f1.truncate(0)
    f1.close()

    f=open("notices.txt") 
    notices=f.read()
    raise_frame(residents_notice_frame)
    notsec = Label(residents_notice_frame, text =notices,bg="lightskyblue",fg="black")
    notsec.config(font=("Courier", 10))
    notsec.place( anchor="n",relx=0.5,rely=0.1)
    f.close()
    backnotButton = Button(residents_notice_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(residents_main_frame))
    backnotButton.config(font=("Courier", 10)) 
    backnotButton.place( anchor="n",relx=0.5,rely=0.9)

class Maintain:
    def __init__(self):
        
        option_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
        option_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg3 = Label(option_frame, text ="Maintenance",bg="lightskyblue",fg="black")
        msg3.config(font=("Courier", 20))
        msg3.place( anchor="n",relx=0.5,rely=0.1)
        water_button3 = Button(option_frame,text="Water supply",b=CENTER)
        msg3 = Label(option_frame, text ="Maintenance",bg="lightskyblue",fg="black")
        msg3.config(font=("Courier", 20))
        msg3.place( anchor="n",relx=0.5,rely=0.1)
    def Options():
        option_frame = Frame(frame, relief="raised",bg="grey",width=700,height=350) #
        option_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        water_button3 =Button(option_frame, text="water charges",bg="lightblue",fg="black",relief="raised",command=Water.Wat)
        water_button3.config(font=("Courier", 10))
        water_button3.place( anchor="n",relx=0.5,rely=0.6)
        elec_button3 = Button(option_frame,text="Electrical repairs",bg="lightblue",fg="black",relief="raised",command=Electrical.Elec)
        elec_button3.config(font=("Courier", 10))
        elec_button3.place( anchor="n",relx=0.5,rely=0.7)
        fest_button3 = Button(option_frame,text="Festive occasions",bg="lightblue",fg="black",relief="raised",command=Festival.Fest)
        fest_button3.config(font=("Courier", 10))
        fest_button3.place( anchor="n",relx=0.5,rely=0.5)
        clean_button3 = Button(option_frame,text="Cleaning charges",bg="lightblue",fg="black",relief="raised",command=Cleaning.Clean)
        clean_button3.config(font=("Courier", 10))
        clean_button3.place( anchor="n",relx=0.5,rely=0.3)
        bill = Button(option_frame,text="Total Bill",bg="lightblue",fg="black",relief="raised",command=Totbill.Bill)
        bill.config(font=("Courier", 10))
        bill.place( anchor="n",relx=0.5,rely=0.8)
        backButton = Button(option_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=Maintain.back)
        backButton.config(font=("Courier", 10)) 
        backButton.place( anchor="n",relx=0.5,rely=0.9)
        raise_frame(option_frame)

    def pay_bill():
        strr="update residents set maintenance_paid=%s where r_flat_no=%s and maintenance_paid=%s"
        data=("yes",lo_flat.get(),"no")
        cursor.execute(strr,data)
        connection.commit()
        if(cursor.rowcount>0):
            pay_frame=Frame(frame, relief='raised',bg="grey",width=700,height=350)
            pay_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            Labell=Label(pay_frame, text ="Thank you.\nPlease pay the amount at society office",bg="lightskyblue",fg="black")
            Labell.config(font=("Courier", 15))
            Labell.place( anchor="n",relx=0.5,rely=0.4)
            back2Button = Button(pay_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=Maintain.Options)
            back2Button.config(font=("Courier", 10)) 
            back2Button.place( anchor="n",relx=0.5,rely=0.7)
        strr="select * from residents where r_flat_no=%s and sec_maintenance_received=%s"
        data=(lo_flat.get(),"yes")
        cursor.execute(strr,data)
        if(cursor.rowcount>0):
            pay_frame=Frame(frame, relief='raised',bg="grey",width=700,height=350)
            pay_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            Labell=Label(pay_frame, text ="You have already paid the amount\nThank You.",bg="lightskyblue",fg="black")
            Labell.config(font=("Courier", 15))
            Labell.place( anchor="n",relx=0.5,rely=0.4)
            back2Button = Button(pay_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=Maintain.Options)
            back2Button.config(font=("Courier", 10)) 
            back2Button.place( anchor="n",relx=0.5,rely=0.7)

    def back():
        raise_frame(residents_main_frame)

class Festival(Maintain):
    def __init__(self):
        Maintain.__init__(self)
    def Fest():
        f_frame=Frame(frame, relief='raised',bg="grey",width=700,height=350) #
        f_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        Labell=Label(f_frame, text ="Amount to be paid for festive occasions: Rs. 300",bg="lightskyblue",fg="black")
        Labell.config(font=("Courier", 15))
        Labell.place( anchor="n",relx=0.5,rely=0.4)
        back2Button = Button(f_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=Maintain.Options)
        back2Button.config(font=("Courier", 10)) 
        back2Button.place( anchor="n",relx=0.5,rely=0.9)
        
class Electrical(Maintain):
    def __init__(self):
        Maintain.__init__(self)
    def Elec():    
        e_frame=Frame(frame, relief='raised',bg="grey",width=700,height=350) #
        e_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        ele=Label(e_frame, text ="Amount to be paid for Electrical repairs : 200",bg="lightskyblue",fg="black")
        ele.config(font=("Courier", 15))
        ele.place( anchor="n",relx=0.5,rely=0.4)
        back3Button = Button(e_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=Maintain.Options)
        back3Button.config(font=("Courier", 10)) 
        back3Button.place( anchor="n",relx=0.5,rely=0.9)        

class Water(Maintain):
    def __init__(self):
        Maintain.__init__(self)
    def Wat():    
        wt_frame=Frame(frame, relief='raised',bg="grey",width=700,height=350) #
        wt_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        watmsg=Label(wt_frame, text ="Amount to be paid for Water supply : 400",bg="lightskyblue",fg="black")
        watmsg.config(font=("Courier", 15))
        watmsg.place( anchor="n",relx=0.5,rely=0.4)
        back4Button = Button(wt_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=Maintain.Options)
        back4Button.config(font=("Courier", 10)) 
        back4Button.place( anchor="n",relx=0.5,rely=0.9)

class Cleaning(Maintain):
    def __init__(self):
        Maintain.__init__(self)
    def Clean():    
        cl_frame=Frame(frame, relief='raised',bg="grey",width=700,height=350) #
        cl_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        clemsg=Label(cl_frame, text ="Amount to be paid for the maintenance and cleaning of building : 500",bg="lightskyblue",fg="black")
        clemsg.config(font=("Courier", 13))
        clemsg.place( anchor="n",relx=0.5,rely=0.4)
        backsButton = Button(cl_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=Maintain.Options)
        backsButton.config(font=("Courier", 10)) 
        backsButton.place( anchor="n",relx=0.5,rely=0.9)

class Totbill(Maintain):
    def __init__(self):
        Maintain.__init__(self)
    def Bill():    
        bill_frame=Frame(frame, relief='raised',bg="grey",width=700,height=350) #
        bill_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        clemsg=Label(bill_frame, text ="Total Bill:1,400rs",bg="lightskyblue",fg="black")
        clemsg.config(font=("Courier", 13))
        clemsg.place( anchor="n",relx=0.5,rely=0.4)
        pay_button = Button(bill_frame,text="Pay Bill",bg="lightblue",fg="black",relief="raised",command=Maintain.pay_bill)
        pay_button.config(font=("Courier", 10)) 
        pay_button.place( anchor="n",relx=0.5,rely=0.7)
        backsButton = Button(bill_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=Maintain.Options)
        backsButton.config(font=("Courier", 10)) 
        backsButton.place( anchor="n",relx=0.5,rely=0.9)

        
residents_main_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #first screen after watchman logs in
residents_main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
welres = Label(residents_main_frame, text ="Welcome Resident!",bg="lightskyblue",fg="black")
welres.config(font=("Courier", 20))
welres.place( anchor="n",relx=0.5,rely=0.1)
viewNotice = Button(residents_main_frame,text="View Notices!",bg="lightblue",fg="black",relief="raised",command=res_notice)
viewNotice.config(font=("Courier", 10)) 
viewNotice.place( anchor="n",relx=0.2,rely=0.4)
viewMaintenance = Button(residents_main_frame,text="Maintenance charges!",bg="lightblue",fg="black",relief="raised",command=Maintain.Options)
viewMaintenance.config(font=("Courier", 10)) 
viewMaintenance.place( anchor="n",relx=0.5,rely=0.4)
backresButton = Button(residents_main_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(login_frame))
backresButton.config(font=("Courier", 10)) 
backresButton.place( anchor="n",relx=0.8,rely=0.4)
residents_notice_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #first screen after watchman logs in
residents_notice_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
notres = Label(residents_notice_frame, text ="Notices Section",bg="lightskyblue",fg="black")
notres.config(font=("Courier", 10))
notres.place( anchor="n",relx=0.5,rely=0.01)
today_notice = Label(residents_notice_frame, text ="Today's Notice",bg="lightskyblue",fg="black")
today_notice.config(font=("Courier", 10))
today_notice.place( anchor="n",relx=0.5,rely=0.6)
watchconButton = Button(residents_main_frame,text="View message from Watchman",bg="lightblue",fg="black",relief="raised",command=lambda:display_msg(lo_flat.get()))
watchconButton.config(font=("Courier", 10)) 
watchconButton.place( anchor="n",relx=0.5,rely=0.6)

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
noticeButton.place( anchor="n",relx=0.5,rely=0.3)
contactButton = Button(watchman_frame,text="Contact individual residents",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(flatnumbers_frame))
contactButton.config(font=("Courier", 10)) 
contactButton.place( anchor="n",relx=0.5,rely=0.5)
backwatchButton = Button(watchman_frame,text="Back!",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(watch_frame))
backwatchButton.config(font=("Courier", 10)) 
backwatchButton.place( anchor="n",relx=0.5,rely=0.7)
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

class myerror(Exception):
    pass

class amount_receivedError(myerror):
    pass

def sec_maintain():
    try:
        strr="update residents set sec_maintenance_received=%s where r_flat_no=%s and maintenance_paid=%s and sec_maintenance_received=%s"
        data=("yes",m_flat_no.get(),"yes","no")
        cursor.execute(strr,data)
        connection.commit()
        print(cursor.rowcount)
        if cursor.rowcount>0:
            sm1 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
            sm1.place(relx=0.5, rely=0.5, anchor=CENTER)
            m1 = Label(sm1, text ="Data updated successfully\nThank You.",bg="lightskyblue",fg="black")
            m1.config(font=("Courier", 20))
            m1.place( anchor="n",relx=0.5,rely=0.2)
            m3= Button(sm1,text="back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(maintain_frame))
            m3.config(font=("Courier", 10)) 
            m3.place( anchor="n",relx=0.5,rely=0.7)
        else:
            raise amount_receivedError
    except:
        sm1 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
        sm1.place(relx=0.5, rely=0.5, anchor=CENTER)
        m1 = Label(sm1, text ="Amount received error\nAmount was paid earlier\nData is already updated.",bg="lightskyblue",fg="black")
        m1.config(font=("Courier", 20))
        m1.place( anchor="n",relx=0.5,rely=0.2)
        m3= Button(sm1,text="back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(maintain_frame))
        m3.config(font=("Courier", 10)) 
        m3.place( anchor="n",relx=0.5,rely=0.7)

secretary_main_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350) #first screen after watchman logs in
secretary_main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

checkmaintenance = Button(secretary_main_frame,text="manage maintenance details",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(maintain_frame))
checkmaintenance.config(font=("Courier", 10)) 
checkmaintenance.place( anchor="n",relx=0.5,rely=0.3) 

m_flat_no=StringVar()
maintain_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
maintain_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
m1 = Label(maintain_frame, text ="Enter flat no whose maintenance is received:",bg="lightskyblue",fg="black")
m1.config(font=("Courier", 10))
m1.place( anchor="n",relx=0.5,rely=0.2)
m2 = Entry(maintain_frame,bd=5,textvariable=m_flat_no) #entry box 
m2.place(anchor="n",relx=0.5,rely=0.5)
m3= Button(maintain_frame,text="submit",bg="lightblue",fg="black",relief="raised",command=sec_maintain)
m3.config(font=("Courier", 10)) 
m3.place( anchor="n",relx=0.5,rely=0.7)

#--------------home deliveries part-----------------------------------#
delivery_msg = StringVar()
def sub_delivery(flat):
    print(flat)
    
    
    strr_sub="update residents set wat_delivery_msg=%s where r_flat_no=%s"
    data_sub=(delivery_msg.get(),flat)
    cursor.execute(strr_sub,data_sub)
    connection.commit()
    if cursor.rowcount>0:
        homedeliveries_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
        homedeliveries_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        topmsg1 = Label(homedeliveries_frame, text ="Msg sent successfully",bg="lightskyblue",fg="black") #watchman's side of communication
        topmsg1.config(font=("Courier", 20))
        topmsg1.place( anchor="n",relx=0.5,rely=0.2)
        back_sub= Button(homedeliveries_frame,text="back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(flatnumbers_frame))
        back_sub.config(font=("Courier", 10)) 
        back_sub.place( anchor="n",relx=0.5,rely=0.7)
    else:
        homedeliveries_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
        homedeliveries_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        topmsg1 = Label(homedeliveries_frame, text ="try again",bg="lightskyblue",fg="black") #watchman's side of communication
        topmsg1.config(font=("Courier", 20))
        topmsg1.place( anchor="n",relx=0.5,rely=0.2)
        back_sub= Button(homedeliveries_frame,text="back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(flatnumbers_frame))
        back_sub.config(font=("Courier", 10)) 
        back_sub.place( anchor="n",relx=0.5,rely=0.7)



def flat_no(flat):
    homedeliveries_frame1 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
    homedeliveries_frame1.place(relx=0.5, rely=0.5, anchor=CENTER)
    raise_frame(homedeliveries_frame1)
    topmsg1 = Label(homedeliveries_frame1, text ="Your message please",bg="lightskyblue",fg="black") #watchman's side of communication
    topmsg1.config(font=("Courier", 20))
    topmsg1.place( anchor="n",relx=0.5,rely=0.2)
    
    enter_message =Entry(homedeliveries_frame1,bd=5,textvariable=delivery_msg)
    enter_message.config(font=("Courier", 20))
    enter_message.place( anchor="n",relx=0.5,rely=0.4)

    msg_sub= Button(homedeliveries_frame1,text="submit",bg="lightblue",fg="black",relief="raised",command=lambda:sub_delivery(flat))
    msg_sub.config(font=("Courier", 10)) 
    msg_sub.place( anchor="n",relx=0.5,rely=0.6)
    back_sub= Button(homedeliveries_frame1,text="back",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(flatnumbers_frame))
    back_sub.config(font=("Courier", 10)) 
    back_sub.place( anchor="n",relx=0.5,rely=0.8)





flatnumbers_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
flatnumbers_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
topmsg = Label(flatnumbers_frame, text ="Flat number you want to contact:",bg="lightskyblue",fg="black")
topmsg.config(font=("Courier", 20))
topmsg.place( anchor="n",relx=0.5,rely=0.2)
a101= Button(flatnumbers_frame,text="101",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("101"))
a101.config(font=("Courier", 10)) 
a101.place( anchor="n",x=100,y=140)
a102= Button(flatnumbers_frame,text="102",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("102"))
a102.config(font=("Courier", 10)) 
a102.place( anchor="n",x=100,y=200)
a103= Button(flatnumbers_frame,text="103",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("103"))
a103.config(font=("Courier", 10)) 
a103.place( anchor="n",x=100,y=260)
a201= Button(flatnumbers_frame,text="201",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("201"))
a201.config(font=("Courier", 10)) 
a201.place( anchor="n",x=180,y=140)
a202= Button(flatnumbers_frame,text="202",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("202"))
a202.config(font=("Courier", 10)) 
a202.place( anchor="n",x=180,y=200)
a203= Button(flatnumbers_frame,text="203",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("203"))
a203.config(font=("Courier", 10)) 
a203.place( anchor="n",x=180,y=260)
a301= Button(flatnumbers_frame,text="301",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("301"))
a301.config(font=("Courier", 10)) 
a301.place( anchor="n",x=260,y=140)
a302= Button(flatnumbers_frame,text="302",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("302"))
a302.config(font=("Courier", 10)) 
a302.place( anchor="n",x=260,y=200)
a303= Button(flatnumbers_frame,text="303",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("303"))
a303.config(font=("Courier", 10)) 
a303.place( anchor="n",x=260,y=260)
a401= Button(flatnumbers_frame,text="401",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("401"))
a401.config(font=("Courier", 10)) 
a401.place( anchor="n",x=340,y=140)
a402= Button(flatnumbers_frame,text="402",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("402"))
a402.config(font=("Courier", 10)) 
a402.place( anchor="n",x=340,y=200)
a403= Button(flatnumbers_frame,text="403",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("403"))
a403.config(font=("Courier", 10)) 
a403.place( anchor="n",x=340,y=260)
a501= Button(flatnumbers_frame,text="501",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("501"))
a501.config(font=("Courier", 10)) 
a501.place( anchor="n",x=420,y=140)
a502= Button(flatnumbers_frame,text="502",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("502"))
a502.config(font=("Courier", 10)) 
a502.place( anchor="n",x=420,y=200)
a503= Button(flatnumbers_frame,text="503",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("503"))
a503.config(font=("Courier", 10)) 
a503.place( anchor="n",x=420,y=260)
a601= Button(flatnumbers_frame,text="601",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("601"))
a601.config(font=("Courier", 10)) 
a601.place( anchor="n",x=500,y=140)
a602= Button(flatnumbers_frame,text="602",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("602"))
a602.config(font=("Courier", 10)) 
a602.place( anchor="n",x=500,y=200)
a603= Button(flatnumbers_frame,text="603",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("603"))
a603.config(font=("Courier", 10)) 
a603.place( anchor="n",x=500,y=260)
a701= Button(flatnumbers_frame,text="701",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("701"))
a701.config(font=("Courier", 10)) 
a701.place( anchor="n",x=580,y=140)
a702= Button(flatnumbers_frame,text="702",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("702"))
a702.config(font=("Courier", 10)) 
a702.place( anchor="n",x=580,y=200)
a703= Button(flatnumbers_frame,text="703",bg="lightblue",fg="black",relief="raised",command=lambda:flat_no("703"))
a703.config(font=("Courier", 10))
a703.place( anchor="n",x=580,y=260)
proceedd = Button(flatnumbers_frame,text="back",bg="lightpink",fg="black",relief="raised",command=lambda:raise_frame(watchman_frame))
proceedd.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
proceedd.place( anchor="n",relx=0.5,rely=0.9)



    


def display_msg(fflat_no):

    res_wat_com = Frame(frame, relief='raised',bg="grey",width=700,height=350) #resident's side of communication.
    res_wat_com.place(relx=0.5, rely=0.5, anchor=CENTER)
    lambda:raise_frame(res_wat_com)
    str_msg="select wat_delivery_msg from residents where r_flat_no=%s"
    data_msg=(fflat_no,)
    cursor.execute(str_msg,data_msg)
    record=cursor.fetchone()
    print(record[0])
    res=record[0]
    print_msg1 = Label(res_wat_com, text="messages section:-",bg="lightskyblue",fg="black") #watchman's side of communication
    print_msg1.config(font=("Courier", 20))
    print_msg1.place( anchor="n",relx=0.5,rely=0.2)
    print_msg = Label(res_wat_com, text=res,bg="lightskyblue",fg="black") #watchman's side of communication
    print_msg.config(font=("Courier", 20))
    print_msg.place( anchor="n",relx=0.5,rely=0.4)

    msg_back = Button(res_wat_com,text="back",bg="lightpink",fg="black",relief="raised",command=lambda:raise_frame(residents_main_frame))
    msg_back.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
    msg_back.place( anchor="n",relx=0.5,rely=0.8)


raise_frame(center_frame)
root.mainloop()

