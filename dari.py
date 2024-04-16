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

# listbox of medicine       -----
def view_command():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT medicine_name, uses, price, manufacturer FROM medicine")
    rows = cur.fetchall()
    conn.close()
    list1.delete(0, END)
    for row in rows:
        list1.insert(END, row)

def search_command():
    medname = e1.get()
    uses = e3.get()
    price = e2.get()
    manu = e4.get()
    conn = create_connection()
    cur = conn.cursor()

    query = "SELECT medicine_name, uses, price, manufacturer FROM medicine WHERE TRUE"
    parameters = []

    if medname:
        query += " AND medicine_name LIKE %s"
        parameters.append('%' + medname + '%')

    if uses:
        query += " AND uses LIKE %s"
        parameters.append('%' + uses + '%')

    if price:
        query += " AND price = %s"
        parameters.append(price)

    if manu:
        query += " AND manufacturer LIKE %s"
        parameters.append('%' + manu + '%')

    cur.execute(query, parameters)
    rows = cur.fetchall()
    conn.close()

    list1.delete(0, END)
    for row in rows:
        list1.insert(END, row)

def add_command():
    data = (e1.get(), e2.get(), e3.get(), e4.get())
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO medicine VALUES (%s, %s, %s, %s)", data)
    conn.commit()
    conn.close()

def update_command():
    data = (e2.get(), e3.get(), e4.get(), e1.get())
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE medicine SET price=%s, uses=%s, manufacturer=%s WHERE medicine_name LIKE %s", data)
    conn.commit()
    conn.close()

def delete_command():
    med_id = e1.get()
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM medicine WHERE medicine_name LIKE %s", (med_id,))
    conn.commit()
    conn.close()

# page fronendddddddddddd

dari_window=Tk()
dari_window.geometry('1900x1080')
dari_window.resizable(1, 1)
dari_window.wm_title("Admin Page") #

bgImage = ImageTk.PhotoImage(file='adminpage.png')

bgLabel=Label(dari_window, image=bgImage)
bgLabel.place(x=0, y=0)


def admin_page():
    dari_window.destroy()
    import admin

phar=Label(dari_window, text="Дәрілер қоймасы", font=('Lalita', 40, 'bold'), bg='#ffffff', fg='#407BFF') # Medicine management
phar.place(x=800, y=50)


l1=Label(dari_window, text="Дәрі атауы", font=('Lalita', 16, 'bold'), bg='#ffffff', fg='#000000') #Medicine name
l1.place(x=200, y=200)

l2=Label(dari_window, text="Бағасы", font=('Lalita', 16, 'bold'), bg='#ffffff', fg='#000000') #Price
l2.place(x=600, y=200)

l3=Label(dari_window, text="Қолданыс аясы", font=('Lalita', 16, 'bold'), bg='#ffffff', fg='#000000') #Uses
l3.place(x=200, y=250)

l4=Label(dari_window, text="Өңдіруші", font=('Lalita', 16, 'bold'), bg='#ffffff', fg='#000000') #Manufacturer
l4.place(x=600, y=250)

#----------------------------

e1=Entry(dari_window, width=15, font=('Lalita', 16, 'bold')) #entryname
e1.place(x=400, y=200)

e2=Entry(dari_window, width=15, font=('Lalita', 16, 'bold'))  #price
e2.place(x=750, y=200)

e3=Entry(dari_window, width=15, font=('Lalita', 16, 'bold'))
e3.place(x=400, y=250)

e4=Entry(dari_window, width=15, font=('Lalita', 16, 'bold'))   #manf
e4.place(x=750, y=250)


list1=Listbox(dari_window, height=30, width=128)
list1.place(x=400, y=300)

sb1=Scrollbar(dari_window)
sb1.place(x=1150, y=300)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


sb2=Scrollbar(dari_window)
sb2.place(x=1150, y=730)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

#functionsss -------------------------------------------------

viewButton=Button(dari_window, text="Барлығын көру", font=('Lilita', 14), width =12, command=view_command, bg='#C6D7FF') #View all
viewButton.place(x=200, y=300)

searchButton=Button(dari_window, text="Дәріні іздеу", font=('Lilita', 14), width=12, command=search_command, bg='#C6D7FF')  #Search Entry
searchButton.place(x=200, y=350)

addButton=Button(dari_window, text="Дәріні қосу", font=('Lilita', 14), width=12, command=add_command, bg='#C6D7FF') #Add Entry
addButton.place(x=200, y=400)

updateButton=Button(dari_window, text="Жаңарту", font=('Lilita', 14), width=12, command=update_command, bg='#C6D7FF') #Update
updateButton.place(x=200, y=450)

deleteButton=Button(dari_window, text="Өшіру", font=('Lilita', 14), width=12, command=delete_command, bg='#C6D7FF') #Delete
deleteButton.place(x=200, y=500)

closeButton=Button(dari_window, text="Артқа", font=('Lilita', 20), width=7, command=admin_page, bg='#C6D7FF') #Log out
closeButton.place(x=50, y=125)



logo = Image.open('dlogo.png')
logo = logo.resize((100, 80), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)

logo_label = Label(dari_window, image=logo, borderwidth=0, highlightthickness=0)
logo_label.place(x=47, y=25)



dari_window.mainloop()