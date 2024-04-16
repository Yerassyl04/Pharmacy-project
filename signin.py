# COLORSSS   #c6e8d0 color if bg  #46af6b color of fg
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import psycopg2 as pg
import tkinter as tk
from datetime import datetime

global current_user
global user_data

bgPic = None
#funct part
def forget_pass():
    global bgPic
    def change_password():
        if email_entry.get()=='' or password_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Қате', 'Барлық жолды толтырыңыз', parent=windows) #Error All Fields Are Required
        elif password_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Қате', 'Құпиясөздер сәйкес келмейді', parent=windows) #Passwords arent matching
        else:
            conn = pg.connect(host='localhost', database='Pharmacy', port='5432', user='postgres', password='admin')
            mycursor = conn.cursor()

            query = 'select * from userdata where email=%s'
            mycursor.execute(query, (email_entry.get(),))
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror('Қате', 'Бұндай почтасы бар қолданушы табылмады', parent=windows) #User with this email doesnt exist
            else:
                query='update userdata set password=%s where email=%s'
                mycursor.execute(query, (password_entry.get(), email_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Сәтті жүзеге асты', 'Құпиясөз өзгертілді', parent=windows) #Password is reset
                windows.destroy()

    def go_back():
        windows.destroy()
        login_window.deiconify()

    windows = Toplevel()
    windows.title('Құпиясөзді өзгерту') #Change Password

    bgPic= ImageTk.PhotoImage(file='newlogin.png')
    bg2Label = Label(windows, image=bgPic)
    bg2Label.grid()

    heading_label = Label(windows, text='Құпиясөзді жаңарту', font=('Lalita', 40, 'bold'),   #RESET PASSWORD
                                                                 bg='#ffffff', fg='#407BFF')
    heading_label.place(x=1160, y=200)

    emailLabel = Label(windows, text='Почта', font=('Lilita', 10), bd=0, bg='#ffffff', fg='black')  #Email
    emailLabel.place(x=1200, y=320)

    email_entry = Entry(windows, width=25, font=('Lilita', 20), bd=2, bg='#ffffff', fg='black')  #
    email_entry.place(x=1200, y=340)

    Frame(windows, width=350, height=3, bg='#8CB0FF').place(x=1220, y=380)

    passwordLabel = Label(windows, text='Жаңа құпиясөз', font=('Lilita', 10), bd=0, bg='#ffffff', fg='black') #New Password
    passwordLabel.place(x=1200, y=400)

    password_entry = Entry(windows, width=25, font=('Lilita', 20), bd=2, bg='#ffffff', fg='black')
    password_entry.place(x=1200, y=420)

    Frame(windows, width=350, height=3, bg='#8CB0FF').place(x=1220, y=460)

    confirmpassLabel = Label(windows, text='Құпиясөзді растау', font=('Lilita', 10), bd=0, bg='#ffffff', fg='black') #Confirm Password
    confirmpassLabel.place(x=1200, y=480)

    confirmpass_entry=Entry(windows, width=25, font=('Lilita', 20), bd=2, bg='#ffffff', fg='black')
    confirmpass_entry.place(x=1200, y=500)

    Frame(windows, width=350, height=3, bg='#8CB0FF').place(x=1220, y=540)

    backButton = Button(windows, text='АРТҚА',font=('Lilita', 20, 'bold'), #Back
                        bg='#407BFF', fg='white', cursor='hand2', bd=0, width=10, command=go_back)
    backButton.place(x=1205, y=580)

    submitButton = Button(windows, text='РАСТАУ',font=('Lilita', 20, 'bold'), #Submit
                        bg='#407BFF', fg='white', cursor='hand2', bd=0, width=10, command=change_password)
    submitButton.place(x=1405, y=580)

def login_user():
    global username  # Declare username as a global variable
    if usernameEntry.get() == 'admin' and passwordEntry.get() == 'admin':
        username = 'admin'  # Set username for admin
        admin_page()
    else:
        if usernameEntry.get()=='' or passwordEntry.get()=='':
             messagebox.showerror('Қате', 'Барлық жолды толтырыңыз') #Error All fields are required to fill

        else:
            try:
                conn = pg.connect(host='localhost', database='Pharmacy', port='5432', user='postgres', password='admin') #
                mycursor=conn.cursor()
                pass
            except:
                messagebox.showerror('Қате', 'Байланыс орнатылмады') #Connection is not established
                return

            mycursor = conn.cursor()
            query='Select username from userdata where username=%s and password=%s'
            mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
            row=mycursor.fetchone()
            if row == None:
                messagebox.showerror('Қате', 'Қолданушы лақабы немесе құпиясөз қате') #Invalid username or password
            else:
                user_page()

# Call the load_user_data function when the user page is loaded


def user_page():
    login_window.destroy()
    import Userpage # ОСы жер басқа бетке бұрады

def admin_page():
    login_window.destroy()
    import admin

def signup_page():
    login_window.destroy()
    import signup

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0, END)

#main part
login_window = Tk()
login_window.geometry('1900x1080')
login_window.resizable(1,1)
login_window.title('Кіру беті') #Login page

bgImage = ImageTk.PhotoImage(file='newlogin.png')

bgLabel=Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)
#-------------------------------------Time
def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    canvas.delete("time_text")
    canvas.create_text(100, 100, text=current_time, font=("Helvetica", 22), tag="time_text")
    login_window.after(1000, update_time)

canvas = tk.Canvas(login_window, width=200, height=200, bd=0, bg='#ffffff', highlightthickness=0)
canvas.place(x=1690, y=2)

update_time()
#---------------------------------------Time
heading=Label(login_window, text=' ЖҮЙЕГЕ КІРУ', font=('Lilita',46, 'bold'), bg='#ffffff', fg='#407BFF') #USER LOGIN
heading.place(x=1230,y=200)

usernameLabel=Label(login_window, text='ҚОЛДАНУШЫ ЛАҚАБЫ', font=('Lalita', 10, 'bold'), bg='#ffffff') #Username
usernameLabel.place(x=1260, y=320)

usernameEntry = Entry(login_window, width=25, font=('Lilita', 20), bd=2, bg='#ffffff', fg='black')
usernameEntry.place(x=1260, y=340)

frame1 =Frame(login_window, width=330, height=3, bg='#8CB0FF')
frame1.place(x=1290, y=380)

passwordEntryLabel=Label(login_window, text='ҚҰПИЯСӨЗ', font=('Lalita', 10, 'bold'), bg='#ffffff')
passwordEntryLabel.place(x=1260, y=400)

passwordEntry = Entry(login_window, width=25, font=('Lilita', 20), bd=2 ,bg='#ffffff', fg='black')
passwordEntry.place(x=1260, y=420)

frame2 =Frame(login_window, width=330, height=3, bg='#8CB0FF')
frame2.place(x=1280, y=460)

forgetButton =Button(login_window,text='Құпиясөзді ұмыттыңыз?', bd=0, bg='#ffffff', #Forget password?
                     activebackground='#88D8C0', cursor='hand2', font=('Lilita', 12, 'underline'), command=forget_pass) #
forgetButton.place(x=1450, y=480)

loginButton= Button(login_window, text='КІРУ', font=('Open Sans', 20, 'bold'), #Login
                    bg='#407BFF', fg='white', cursor='hand2', bd=0, width=15, command=login_user) #
loginButton.place(x=1320 , y=530)

frame3 =Frame(login_window, width=330, height=3, bg='#8CB0FF')
frame3.place(x=1980, y=600)


newaccountButton=Button(login_window, text='Жаңа аккаунт құру',font=('Lilita', 14, 'underline'), #Create an new account
                    bg='#ffffff', fg='black', cursor='hand2', bd=0, width=20, command=signup_page) #
newaccountButton.place(x=1330, y=590)



logo = Image.open('dlogo.png')
logo = logo.resize((170, 60), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)

logo_label = Label(login_window, image=logo, borderwidth=0, highlightthickness=0)
logo_label.place(x=1150, y=880)

kukukLabel=Label(login_window, text='Pharma.kz | Барлық құқықтары қорғалған | 2024', font=('Lalita', 12, 'bold'), bg='#ffffff', fg='#407BFF')
kukukLabel.place(x=1350, y=910)


login_window.mainloop()

