from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import ImageTk, Image
import psycopg2 as pg
# COLORSSS   #c6e8d0 color if bg  #46af6b color of fg

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Қате','Барлық жолды толтырыңыз') #All fields should be filled
    elif  passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Қате','Құпиясөздер сәйкес келмейді') #Password doesnt match
    elif check.get()==0:
        messagebox.showerror('Қате','Талаптар мен шарттарға келісім беріңіз') #Please accept Terms and Conditions
    else:
        try:
            conn=pg.connect(host='localhost',database='Pharmacy', port='5432', user='postgres', password='admin')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Қате', 'Байланыс орнатылмады') #Connection is not established
            return

        mycursor = conn.cursor()
        query='Select * from userdata where email = %s'
        mycursor.execute(query, (emailEntry.get(),))
        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Қате', 'Почта бұрын соңды жүйеге тіркелген') #Email Already Exists
        else:
            query = 'INSERT INTO userdata(email, username, password) VALUES (%s, %s, %s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Сәтті', 'Жүйеге сәтті тіркелдіңіз') #Registration is successful
            clear()
            signup_window.destroy()
            import signin



def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()
signup_window.geometry('1900x1080')
signup_window.title('Тіркелу беті') #Signin Window


background=ImageTk.PhotoImage(file='newsignup.png')

bgLabel=Label(signup_window, image=background)
bgLabel.grid()

frame=Frame(signup_window, width=60, height=20, bg='#ffffff')
frame.place(x=1090, y=280)

heading=Label(signup_window, text='Жаңа аккаунт құру', font=('Lalita', 40, 'bold'), bg='#ffffff', fg='#407BFF') #CREATE AN ACCOUNT
heading.place(x=1100, y=200)

emailLabel=Label(frame, text='Электронды почта', font=('Lalita', 10, 'bold'), bg='#ffffff') #Email
emailLabel.grid(row=1, column=0, sticky='w', padx=25)

emailEntry=Entry(frame, width=30,  font=('Lalita', 20, 'bold'))
emailEntry.grid(row=2, column=0, sticky='w', padx=30)

usernameLabel=Label(frame, text='Қолданушы лақабы', font=('Lalita', 10, 'bold'), bg='#ffffff') #Username
usernameLabel.grid(row=3, column=0, sticky='w', padx=30)

usernameEntry=Entry(frame, width=30,  font=('Lalita', 20, 'bold'))
usernameEntry.grid(row=4, column=0, sticky='w', padx=30)

passwordLabel=Label(frame, text='Құпиясөз', font=('Lalita', 10, 'bold'), bg='#ffffff') #Password
passwordLabel.grid(row=5, column=0, sticky='w', padx=30)

passwordEntry=Entry(frame, width=30,  font=('Lalita', 20, 'bold'))
passwordEntry.grid(row=6, column=0, sticky='w', padx=30)

confirmLabel=Label(frame, text='Құпиясөзді растау', font=('Lalita', 10, 'bold'), bg='#ffffff') #Confirm Password
confirmLabel.grid(row=7, column=0, sticky='w', padx=25)

confirmEntry=Entry(frame, width=30,  font=('Lalita', 20, 'bold'))
confirmEntry.grid(row=8, column=0, sticky='w', padx=30)

check=IntVar()
termsandconditions=Checkbutton(frame, text='Барлық шарттар мен талаптармен келісемін',
                               font=('Lalita', 12, 'bold'), bg='#ffffff', variable=check) #I agree to the Terms and Conditions
termsandconditions.grid(row=9, column=0, pady=20)

signupButton=Button(frame, width=20,  text='ТІРКЕЛУ',font=('Lalita',15, 'bold'), bg='#407BFF', fg='#ffffff', command=connect_database) #Signup
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount= Label(frame,text='Жүйеге бұрын тіркелдіңіз бе?', font=('Lalita',14,), bg='#ffffff') #Already have an account?
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton=Button(frame, text='Кіру', font=('Lalita',13, 'underline'),
                   command=login_page, bd=0, bg='#ffffff', fg='#B8519F')
loginButton.place(x=360, y=374)



logo = Image.open('dlogo.png')
logo = logo.resize((170, 60), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)

logo_label = Label(signup_window, image=logo, borderwidth=0, highlightthickness=0)
logo_label.place(x=1150, y=880)

kukukLabel=Label(signup_window, text='Pharma.kz | Барлық құқықтары қорғалған | 2024', font=('Lalita', 12, 'bold'), bg='#ffffff', fg='#407BFF')
kukukLabel.place(x=1350, y=910)


signup_window.mainloop()