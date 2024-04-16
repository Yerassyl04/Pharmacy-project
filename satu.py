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

#lisbox of saaalllesss
def viewtran_command():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT user_email, medicine_name, manufacturer, totalprice FROM userbuy")
    rows = cur.fetchall()
    conn.close()
    list3.delete(0, END)
    for row in rows:
        list3.insert(END, row)
# page fronendddddddddddd

satu_window=Tk()
satu_window.geometry('1900x1080')
satu_window.resizable(1, 1)
satu_window.wm_title("Admin Page") #

bgImage = ImageTk.PhotoImage(file='adminpage.png')

bgLabel=Label(satu_window, image=bgImage)
bgLabel.place(x=0, y=0)


def admin_page():
    satu_window.destroy()
    import admin



closeButton=Button(satu_window, text="Артқа", font=('Lilita', 20), width=7, command=admin_page, bg='#C6D7FF') #Log out
closeButton.place(x=50, y=125)


# user labelssss-------------------------------

#transactions
tran=Label(satu_window, text="Сатылымдарды басқару", font=('Lalita', 40, 'bold'), bg='#ffffff', fg='#407BFF') #Sales Management
tran.place(x=700, y=50)

viewtranButton=Button(satu_window, text="Барлығын көрсету", font=('Lilita', 14), width =14, command=viewtran_command, bg='#C6D7FF') #View all
viewtranButton.place(x=200, y=200)

#sales list
list3=Listbox(satu_window, height=17, width=70)
list3.place(x=390, y=200)

sb33=Scrollbar(satu_window)
sb33.place(x=800, y=300)

list3.configure(yscrollcommand=sb33.set)
sb33.configure(command=list3.yview)

logo = Image.open('dlogo.png')
logo = logo.resize((100, 80), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)

logo_label = Label(satu_window, image=logo, borderwidth=0, highlightthickness=0)
logo_label.place(x=47, y=25)



satu_window.mainloop()