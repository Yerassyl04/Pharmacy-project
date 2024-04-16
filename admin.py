from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import psycopg2 as pg

#conn=pg.connect(host='localhost',database='Pharmacy', port='5432', user='postgres', password='admin')
            #mycursor=conn.cursor()

def create_connection():
    conn=pg.connect(host='localhost',database='Pharmacy', port='5432', user='postgres', password='admin')
    return conn
# database table medicine columns -------- medicine_name, uses, price, manufacturer,

#listbox of user ------------

def viewuser_command():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT email, username, password FROM userdata")
    rows = cur.fetchall()
    conn.close()
    list2.delete(0, END)
    for row in rows:
        list2.insert(END, row)


def searchuser_command():
    search_term = usernameEntry.get()
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT email, username, password FROM userdata WHERE username=%s", (search_term,))
    rows = cur.fetchall()
    conn.close()
    list2.delete(0, END)
    for row in rows:
        list2.insert(END, row)


def deleteuser_command():
    user_id = usernameEntry.get()
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM userdata WHERE username LIKE %s", (user_id,))
    conn.commit()
    conn.close()


# page fronendddddddddddd

admin_window=Tk()
admin_window.geometry('1900x1080')
admin_window.resizable(1,1)
admin_window.wm_title("Admin Page") #

bgImage = ImageTk.PhotoImage(file='adminpage.png')

bgLabel=Label(admin_window, image=bgImage)
bgLabel.place(x=0, y=0)


def signin_page():
    admin_window.destroy()
    import signin

def dari_page():
    admin_window.destroy()
    import dari

def satu_page():
    admin_window.destroy()
    import satu

#----------------------------

#functionsss -------------------------------------------------

closeButton=Button(admin_window, text="Шығу",font=('Lilita', 20),  width=7, command=signin_page, bg='#C6D7FF') #Log out
closeButton.place(x=50, y=125)


dariButton=Button(admin_window, text="Қойма",font=('Lilita', 20),  width=7, command=dari_page, bg='#C6D7FF') #Log out
dariButton.place(x=50, y=225)

satuButton=Button(admin_window, text="Сатылым",font=('Lilita', 20),  width=7, command=satu_page, bg='#C6D7FF') #Log out
satuButton.place(x=50, y=325)

# user labelssss-------------------------------
use=Label(admin_window, text="Қолданушыларды басқару", font=('Lalita', 40, 'bold'), bg='#ffffff', fg='#407BFF')  #User management
use.place(x=700, y=50)

username=Label(admin_window, text="Қолданушы есімі", font=('Lalita', 16, 'bold'), bg='#ffffff', fg='#000000') #Enter user name
username.place(x=200, y=200)

usernameEntry=Entry(admin_window, width=20, font=('Lalita', 16, 'bold'))
usernameEntry.place(x=400, y=200)

viewuserButton=Button(admin_window, text="Барлығын көрсету",font=('Lilita', 14), width =16, command=viewuser_command, bg='#C6D7FF') #View all
viewuserButton.place(x=200, y=300)

searchuserButton=Button(admin_window, text="Қолданушыны іздеу",font=('Lilita', 14), width=16, command=searchuser_command, bg='#C6D7FF') #Search username
searchuserButton.place(x=200, y=350)

deleteuserButton=Button(admin_window, text="Қолданушыны өшіру",font=('Lilita', 14), width=16, command=deleteuser_command, bg='#C6D7FF') #Delete user
deleteuserButton.place(x=200, y=400)


list2=Listbox(admin_window, height=17, width=70)
list2.place(x=390, y=300)

sb11=Scrollbar(admin_window)
sb11.place(x=800, y=300)

list2.configure(yscrollcommand=sb11.set)
sb11.configure(command=list2.yview)


logo = Image.open('dlogo.png')
logo = logo.resize((100, 80), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)

logo_label = Label(admin_window, image=logo, borderwidth=0, highlightthickness=0)
logo_label.place(x=47, y=25)




admin_window.mainloop()


