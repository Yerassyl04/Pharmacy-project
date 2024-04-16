import requests
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import psycopg2 as pg
from io import BytesIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# database commands
def create_connection():
    conn=pg.connect(host='localhost',database='Pharmacy', port='5432', user='postgres', password='admin')
    return conn

def signin_page():
    user_window.destroy()
    import signin

def search_command():
    medname = mednameEntry.get()
    uses = usesEntry.get()
    manu = manEntry.get()
    conn = create_connection()
    cur = conn.cursor()

    query = "SELECT med_id, medicine_name, uses, price, manufacturer FROM medicine WHERE TRUE"
    parameters = []

    if medname:
        query += " AND medicine_name LIKE %s"
        parameters.append('%' + medname + '%')

    if uses:
        query += " AND uses LIKE %s"
        parameters.append('%' + uses + '%')

    if manu:
        query += " AND manufacturer LIKE %s"
        parameters.append('%' + manu + '%')

    cur.execute(query, parameters)
    rows = cur.fetchall()
    conn.close()

    list1.delete(0, END)
    for row in rows:
        list1.insert(END, row)

def addbasket():
    selected_item = list1.get(list1.curselection())
    if selected_item:
        basketList.insert(END, selected_item)

def removeitem():
    selected_indices = basketList.curselection()
    if selected_indices:
        for index in selected_indices[::-1]:
            basketList.delete(index)
def prices():
    total = 0
    for item in basketList.get(0, END):
        price = float(item[3])
        total += price
    return total

def buyitem():
    totalprice = prices()
    user_email= emailEntry.get()
    messagebox.showinfo("Ақпарат", f"Total Price: ${totalprice:.2f}\nТолық соммасы Сатып алғаныңызға рақмет, Біз сізге хабарласамыз") #Thank you for your purchase, We will call back!
    conn = create_connection()
    cur = conn.cursor()

    for item in basketList.get(0, END):
        med_id = item[0]
        medicine_name = item[1]
        price = item[3]
        manufacturer = item[4]

        cur.execute("INSERT INTO userbuy (user_email, med_id, medicine_name, price, manufacturer, totalprice) VALUES (%s, %s, %s, %s, %s, %s)", (user_email, med_id, medicine_name, price, manufacturer, totalprice))

    conn.commit()
    conn.close()
    basketList.delete(0, END)

def buyitem():
    totalprice = prices()
    user_email = emailEntry.get()
    basket_items = basketList.get(0, END)

    sender_email = "iskakivich@mail.ru"
    sender_password = "3Suu0ACbUSgM1DbVqVfP"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = "Сатып алуды растау"

    body = f"Сіз сатып алдыңыз!\n\nЖалпы сомма: ${totalprice:.2f}\n\nСатып алған дәрі-дәрмектер:\n"
    for item in basket_items:
        body += f"- {item[1]} - ${item[3]}\n"
    body += "\nБіз сізге қайтадан хабарласамыз."
    body += "\nБайланыс үшін +77071373705."
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, user_email, text)
        server.quit()
        messagebox.showinfo("Ақпарат", f"Почтаға жөңелтілді!")
    except Exception as e:
        messagebox.showerror("Қате", f"Error: {str(e)}")

    conn = create_connection()
    cur = conn.cursor()

    for item in basketList.get(0, END):
        med_id = item[0]
        medicine_name = item[1]
        price = item[3]
        manufacturer = item[4]

        cur.execute("INSERT INTO userbuy (user_email, med_id, medicine_name, price, manufacturer, totalprice) VALUES (%s, %s, %s, %s, %s, %s)", (user_email, med_id, medicine_name, price, manufacturer, totalprice))

    conn.commit()
    conn.close()
    basketList.delete(0, END)




# other pagesss--------------------
def aboutus():
    global aboutus_window
    aboutus_window = Toplevel() #new windowww
    aboutus_window.title("Біз жайлы")  #About Us

    img = Image.open("newaboutus.png")
    photo = ImageTk.PhotoImage(img)
    label = Label(aboutus_window, image=photo)
    label.image = photo
    label.pack()
    gobackButton = Button(aboutus_window, text="Артқа", font=('Lilita', 18), width=11, command=user_page,
                         bg='#C6D7FF')  # Log out
    gobackButton.place(x=25, y=125)

def user_page():
    aboutus_window.destroy()


def contacts():
    global aboutus_window
    aboutus_window = Toplevel() #new windowww
    aboutus_window.title("Байланыс") #Contacts

    img = Image.open("newcontacts.png")
    photo = ImageTk.PhotoImage(img)
    label = Label(aboutus_window, image=photo)
    label.image = photo
    label.pack()
    closeButton = Button(user_window, text="Жүйеден шығу", font=('Lilita', 18), width=11, command=signin_page,
                         bg='#C6D7FF')  # Log out
    closeButton.place(x=25, y=125)
    gobackButton = Button(aboutus_window, text="Артқа", font=('Lilita', 18), width=11, command=user_page,
                          bg='#C6D7FF')  # Log out
    gobackButton.place(x=25, y=125)

def user_page():
    aboutus_window.destroy()


# main configs
user_window=Tk()
user_window.geometry('1900x1080')
user_window.resizable(1,1)
user_window.wm_title("User Page")

bgImage = ImageTk.PhotoImage(file='adminpage.png')

bgLabel=Label(user_window, image=bgImage)
bgLabel.place(x=0, y=0)


def show_image(event):
    index = list1.curselection()
    if index:
        selected_item = list1.get(index)
        med_id = selected_item[0]

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT image_url FROM medicine WHERE med_id=%s", (med_id,))
        image_url = cursor.fetchone()[0] if cursor.rowcount > 0 else None
        conn.close()

        if image_url:
            response = requests.get(image_url)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((200, 300))
            photo = ImageTk.PhotoImage(img)

            canvas.delete("all")
            canvas.create_image(0, 0, anchor=NW, image=photo)
            canvas.image = photo


# --------------------------------------------- #FFFFFF   #407BFF қою көк        #C6D7FF дәрі арты
phar=Label(user_window, text="Дәріханаға қош келдіңіз", font=('Bandal', 40, 'bold'), bg='#FFFFFF', fg='#407BFF') #Басты бет
phar.place(x=700, y=20)

closeButton=Button(user_window, text="Жүйеден шығу",font=('Lilita', 18),  width=11, command=signin_page, bg='#C6D7FF') #Log out
closeButton.place(x=25, y=125)

aboutButton=Button(user_window, text="Біз жайлы",font=('Lilita', 18),  width=10, command=aboutus, bg='#C6D7FF') #About us
aboutButton.place(x=25, y=225)

contButton=Button(user_window, text="Байланыс",font=('Lilita', 18),  width=10, command=contacts, bg='#C6D7FF') #Contacts
contButton.place(x=25, y=325)

# Listboxxx ----------------------------------
list1=Listbox(user_window, height=20, width=100) #bg='#c6e8d0'
list1.place(x=1200, y=350)

list1.bind("<<ListboxSelect>>", show_image)

sb1=Scrollbar(user_window)
sb1.place(x=1781, y=350)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

basketList=Listbox(user_window, height=10, width=100) #bg='#c6e8d0'
basketList.place(x=1200, y=750)

canvas = Canvas(user_window, width=230, height=320, bg='white')
canvas.place(x=900, y=350)

img = PhotoImage(file='familmask.png')
save = Canvas(user_window, width=650, height=500)
save.place(x=200, y=200)
save.create_image(325, 250, image=img)


mybasketLabel=Label(user_window, text="Себетім", font=('Lalita', 18, 'bold'), bg='#ffffff', fg='#385b66') #My Basket
mybasketLabel.place(x=1450, y=700)

imageLabel=Label(user_window, text="Дәрі-дәрмек суреті", font=('Lalita', 12, 'bold'), bg='#ffffff', fg='#385b66') #Medicine image
imageLabel.place(x=955, y=650)

# med functionsssssssssssssssssss
mednameLabel=Label(user_window, text="Дәрі-дәрмек атауы", font=('Lalita', 18, 'bold'), bg='#ffffff', fg='#385b66') #Medicine name
mednameLabel.place(x=900, y=200)

mednameEntry=Entry(user_window, width=15, font=('Lalita', 18, 'bold'))
mednameEntry.place(x=1200, y=200)

usesLabel=Label(user_window, text="Қай жеріңіз ауырады", font=('Lalita', 18, 'bold'), bg='#ffffff', fg='#385b66') #Uses
usesLabel.place(x=900, y=250)

usesEntry=Entry(user_window, width=15, font=('Lalita', 18, 'bold'))   #manf
usesEntry.place(x=1200, y=250)

manLabel=Label(user_window, text="Өндіруші", font=('Lalita', 18, 'bold'), bg='#ffffff', fg='#385b66') #Manufacturer
manLabel.place(x=900, y=300)

manEntry=Entry(user_window, width=15, font=('Lalita', 18, 'bold'))   #manf
manEntry.place(x=1200, y=300)

emailEntry = Entry(user_window, width=25, font=('Lalita', 18, 'bold'))
emailEntry.place(x=1200, y=150)

emailLabel=Label(user_window, text="Почтаңызды еңгізіңіз", font=('Lalita', 18, 'bold'), bg='#ffffff', fg='#385b66') #Enter your email
emailLabel.place(x=900, y=150)

searchButton=Button(user_window, text="Дәрі іздеу",font=('Lilita', 14), width=13, command=search_command, bg='#C6D7FF') #Search item
searchButton.place(x=1420, y=200)

addbasketButton=Button(user_window, text="Себетке қосу",font=('Lilita', 14), width=12,  command=addbasket,  bg='#C6D7FF') #Add to basket
addbasketButton.place(x=1420, y=250)

removeButton= Button(user_window, text="Алып тастау", font=('Lilita', 14), width=12, command=removeitem, bg='#C6D7FF') #Remove item
removeButton.place(x=1000, y=750)

buyButton = Button(user_window, text="Сатып алу", font=('Lilita', 14), width=12, command=buyitem, bg='#C6D7FF') #Buy Items
buyButton.place(x=1000, y=800)

#logooo
logo = Image.open('dlogo.png')
logo = logo.resize((100, 80), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)

logo_label = Label(user_window, image=logo, borderwidth=0, highlightthickness=0)
logo_label.place(x=47, y=25)


logo1 = Image.open('dlogo.png')
logo1 = logo1.resize((170, 60), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo1)

logo_label = Label(user_window, image=logo1, borderwidth=0, highlightthickness=0)
logo_label.place(x=250, y=880)

kukukLabel=Label(user_window, text='Pharma.kz | Барлық құқықтары қорғалған | 2024', font=('Lalita', 12, 'bold'), bg='#ffffff', fg='#407BFF')
kukukLabel.place(x=450, y=910)

# buy item ----------------------------------

user_window.mainloop()