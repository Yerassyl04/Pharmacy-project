from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import tkinter as tk
import psycopg2 as pg

bgPic = None
#funct part
def forget_pass():
    global bgPic
    def change_password():
        if email_entry.get()=='' or password_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error', 'All Fields Are Required', parent=windows)
        elif password_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'Passwords arent matching', parent=windows)
        else:
            conn = pg.connect(host='localhost', database='EliteMarket', port='5432', user='postgres', password='1234560')
            mycursor = conn.cursor()

            query = 'select * from userdata where email=%s'
            mycursor.execute(query, (email_entry.get(),))
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'User with this email doesnt exist', parent=windows)
            else:
                query='update userdata set password=%s where email=%s'
                mycursor.execute(query, (password_entry.get(), email_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Succes', 'Password is reset', parent=windows)
                windows.destroy()


    windows = Toplevel()
    windows.title('Change Password')

    bgPic= ImageTk.PhotoImage(file='Дизайн без названия (6).png')
    bg2Label = Label(windows, image=bgPic)
    bg2Label.grid()

    heading_label = Label(windows, text='RESET PASSWORD', font=('Times New Roman', 23, 'bold'), bg='white', fg='#57a1f8')
    heading_label.place(x=900, y=120)

    emailLabel = Label(windows, text='Email', font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    emailLabel.place(x=900, y=170)

    email_entry = Entry(windows, width=25, font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    email_entry.place(x=900, y=170)

    Frame(windows, width=900, height=3, bg='#40e0d0').place(x=900, y=160)

    passwordLabel = Label(windows, text='New Password', font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    passwordLabel.place(x=900, y=210)

    password_entry = Entry(windows, width=25, font=('Times New Roman', 18), bd=0,bg='white', fg='#57a1f8')
    password_entry.place(x=900, y=210)

    Frame(windows, width=900, height=3, bg='#40e0d0').place(x=900, y=200)

    confirmpassLabel = Label(windows, text='Confirm Password', font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    confirmpassLabel.place(x=900, y=250)

    confirmpass_entry=Entry(windows, width=25, font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
    confirmpass_entry.place(x=900, y=250)

    Frame(windows, width=350, height=3, bg='#40e0d0').place(x=850, y=260)

    submitButton = Button(windows, text='Submit',font=('Times New Roman', 20),
                        bg='white', fg='#57a1f8', cursor='hand2', bd=0, width=15, command=change_password)
    submitButton.place(x=900, y=290)

def login_user():
    if usernameEntry.get() == 'saya.juz40@gmail.com' and passwordEntry.get() == '1234':
        root()
    else:
        if usernameEntry.get()=='' or passwordEntry.get()=='':
             messagebox.showerror('Error', 'All fields are required to fill')

        else:
         try:
             conn = pg.connect(host='localhost', database='Pharmacy', port='5432', user='postgres', password='admin')
             mycursor=conn.cursor()
             pass
         except:
             messagebox.showerror('Error', 'Connection is not established')
             return

         mycursor = conn.cursor()
         query='Select * from userdata where username=%s and password=%s'
         mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
         row=mycursor.fetchone()
         if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
         else:
            root()


def root():
    login_window.destroy()
    import root

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
login_window.geometry('1900x1000+50+50')
login_window.resizable(1,1)
login_window.title('Login page')

bgImage = ImageTk.PhotoImage(file='login.png')

bgLabel=Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)


heading=Label(login_window, text='User login', font=('Times New Roman',40, 'bold'), bg='white', fg='#57a1f8')
heading.place(x=900,y=100)

usernameEntry = Entry(login_window, width=25, font=('Times New Roman', 18), bd=0, bg='white', fg='#57a1f8')
usernameEntry.place(x=900, y=180)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

frame1 =Frame(login_window, width=300, height=3, bg='#40e0d0')
frame1.place(x=900, y=180)

passwordEntry = Entry(login_window, width=25, font=('Times New Roman', 18), bd=0 ,bg='white', fg='#57a1f8')
passwordEntry.place(x=900, y=230)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)


frame2 =Frame(login_window, width=300, height=3, bg='#40e0d0')
frame2.place(x=900, y=230)

forgetButton =Button(login_window,text='Forget password?', bd=0, bg='white', fg='#57a1f8',
                      cursor='hand2', font=('Times New Roman', 14, 'underline'), command=forget_pass)
forgetButton.place(x=1000, y=260)

loginButton= Button(login_window, text='Login', font=('Times New Roman Sans', 20, 'bold'),
                    bg='white', fg='#57a1f8', cursor='hand2', bd=0, width=15, command=login_user)
loginButton.place(x=900 , y=300)

newaccountButton=Button(login_window, text='Create an account',font=('Times New Roman', 14, 'underline'),
                    bg='white', fg='#57a1f8', cursor='hand2', bd=0, width=20, command=signup_page)
newaccountButton.place(x=920, y=360)


login_window.mainloop()

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All fields should be filled')
    elif  passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password doesnt match')
    else:
        try:
            conn=pg.connect(host='localhost',database='EliteMarket', port='5432', user='postgres', password='1234560')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established')
            return

        mycursor = conn.cursor()
        query='Select * from userdata where email = %s'
        mycursor.execute(query, (emailEntry.get(),))
        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Email Already Exists')
        else:
            query = 'INSERT INTO userdata(email, username, password) VALUES (%s, %s, %s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Succes', 'Registration is successful')
            clear()
            signup_window.destroy()
            import signin

def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()
signup_window.geometry('1900x1000+50+50')
signup_window.title('Signin Window')


background=ImageTk.PhotoImage(file='login.png')

bgLabel=Label(signup_window, image=background)
bgLabel.grid()

frame=Frame(signup_window, width=50, height=20, bg='#40e0d0')
frame.place(x=850, y=200)

heading=Label(signup_window, text='Create an account', font=('Times New Roman', 23, 'bold'), bg='white', fg='#57a1f8')
heading.place(x=900, y=120)

emailLabel=Label(frame, text='Email', font=('Times New Roman', 16, 'bold'), bg='white', fg='#57a1f8')
emailLabel.grid(row=1, column=0, sticky='w', padx=10)

emailEntry=Entry(frame, width=30,  font=('Times New Roman', 16, 'bold'))
emailEntry.grid(row=2, column=0, sticky='w', padx=10)

usernameLabel=Label(frame, text='Username', font=('Times New Roman', 16, 'bold'), bg='white', fg='#57a1f8')
usernameLabel.grid(row=3, column=0, sticky='w',  padx=10)

usernameEntry=Entry(frame, width=30,  font=('Times New Roman', 16, 'bold'))
usernameEntry.grid(row=4, column=0, sticky='w',  padx=10)

passwordLabel=Label(frame, text='Password', font=('Times New Roman', 16, 'bold'), bg='white', fg='#57a1f8')
passwordLabel.grid(row=5, column=0, sticky='w',  padx=10)

passwordEntry=Entry(frame, width=30,  font=('Times New Roman', 16, 'bold'))
passwordEntry.grid(row=6, column=0, sticky='w',  padx=10)

confirmLabel=Label(frame, text='Confirm Password', font=('Times New Roman', 16, 'bold'), bg='white', fg='#57a1f8')
confirmLabel.grid(row=7, column=0, sticky='w',  padx=10)

confirmEntry=Entry(frame, width=30,  font=('Times New Roman', 16, 'bold'))
confirmEntry.grid(row=8, column=0, sticky='w',  padx=10)

signupButton=Button(frame, width=20,  text='Signup',font=('Times New Roman',15, 'bold'), bg='white', fg='#57a1f8', command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount= Label(frame,text='Already have an account?', font=('Times New Roman',14,), bg='white', fg='#57a1f8')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=20, pady=10)

loginButton=Button(frame, text='Login', font=('Times New Roman',12),
                   command=login_page, bg='white', fg='#57a1f8')
loginButton.place(x=280, y=300)

signup_window.mainloop()

basket = []  # To store selected products

# Establish connection to the database
def create_connection():
    conn = pg.connect(
        host='localhost',
        database='EliteMarket',
        port='5432',
        user='postgres',
        password='1234560'
    )
    return conn

def signin_page():
    root.destroy()
    import signin

def fetch_product_prices():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT p_name, price_in_$ FROM products")
    prices = {row[0]: row[1] for row in cursor.fetchall()}

    conn.close()
    return prices

# Function to calculate the total price of the products in the basket
def calculate_total_price(prices):
    total_price = sum(prices.get(item[1], 0) for item in basket)
    return total_price

# Search products based on user input
def search_products():
    search_term = entry_search.get()
    conn = create_connection()
    cursor = conn.cursor()

    query = "SELECT product_id, p_name, price_in_$, quantity, p_categories FROM products WHERE p_name ILIKE %s"
    cursor.execute(query, ('%' + search_term + '%',))
    rows = cursor.fetchall()

    conn.close()

    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row)

# Add selected product to basket
def add_to_basket():
    selected = listbox.curselection()
    if selected:
        selected_product = listbox.get(selected)
        basket.append(selected_product)
        messagebox.showinfo("Added to Basket", f"{selected_product[1]} added to your basket.")

# Display items in the basket
def view_basket():
    basket_window = tk.Toplevel(root)
    basket_window.title("My Basket")

    basket_listbox = tk.Listbox(basket_window, width=400, height=500, bg = '#40e0d0', fg = 'black', font=("Arial", 24))
    basket_listbox.pack(padx=20, pady=20)

    for item in basket:
        basket_listbox.insert(tk.END, item)

# Buy selected product from the basket
def buy_product():
    selected = listbox.curselection()
    if selected:
        selected_product = listbox.get(selected)
        # Perform action to buy the product
        messagebox.showinfo("Purchase", f"You have bought: {selected_product[1]}")
        listbox.delete(selected)  # Remove item from the listbox
    else:
        messagebox.showwarning("No Selection", "Please select a product to buy.")

def buy_product():
    selected = listbox.curselection()
    if selected:
        selected_product = listbox.get(selected)
        basket.remove(selected_product)
        prices = fetch_product_prices()
        total_price = calculate_total_price(prices)
        messagebox.showinfo("Purchase", f"You have bought: {selected_product[1]}\nTotal Price: ${total_price}")
        listbox.delete(selected)  # Remove item from the listbox
    else:
        messagebox.showwarning("No Selection", "Please select a product to buy.")



# Log out function
def log_out():
    # Perform any necessary log out actions
    messagebox.showinfo("Logged Out", "You have been logged out.")
    root.destroy()  # Close the window or redirect to login screen

# About Us function
def about_us():
    aboutus_window = tk.Toplevel() #new windowww
    aboutus_window.title("About Us")

    img = Image.open("About us (2).png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(aboutus_window, image=photo)
    label.image = photo
    label.pack()

def contacts():
    aboutus_window = tk.Toplevel() #new windowww
    aboutus_window.title("Contacts")

    img = Image.open("Contact (1).png")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(aboutus_window, image=photo)
    label.image = photo
    label.pack()

# Tkinter setup
root = tk.Tk()
root.title("Elite Market")
root.geometry("1900x1000+50+50")

# Background colors
frame_bg_color = "#40e0d0"
button_bg_color = "#f2faf2"
button_fg_color = "black"
button_hover_bg_color = "#f2faf2"
button_hover_fg_color = "black"
root.config(bg=frame_bg_color)

frame_search = tk.Frame(root, bg=frame_bg_color)
frame_search.place(x=500, y=20)

label_search = tk.Label(frame_search, text="Search Product:", font=("Times New Roman", 25), bg=frame_bg_color)
label_search.pack(side=tk.LEFT)

entry_search = tk.Entry(frame_search, font=("Times New Roman", 25))
entry_search.pack(side=tk.LEFT, padx=10)

button_search = tk.Button(frame_search, text="Search", command=search_products, font=("Times New Roman", 25),
                          bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                          activeforeground=button_hover_fg_color)
button_search.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=30, font=("Times New Roman", 25))
listbox.place(x=500, y=150)

img = tk.PhotoImage(file='Дизайн без названия (2).png')
save = tk.Canvas(root, width=400, height=500)
save.place(x=20, y=20)
save.create_image(200, 200, image=img)

button_add_to_basket = tk.Button(root, text="Add to Basket", command=add_to_basket, font=("Times New Roman", 25),
                                 bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                                 activeforeground=button_hover_fg_color)
button_add_to_basket.place(x=1100, y=150)

button_view_basket = tk.Button(root, text="My Basket", command=view_basket, font=("Times New Roman", 25),
                               bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                               activeforeground='black')
button_view_basket.place(x=1100, y=250)

button_buy = tk.Button(root, text="Buy", command=buy_product, font=("Times New Roman", 25),
                       bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                       activeforeground=button_hover_fg_color)
button_buy.place(x=1100, y=350)

button_about_us = tk.Button(root, text="About Us", command=about_us, font=("Times New Roman", 25),
                            bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                            activeforeground=button_hover_fg_color)
button_about_us.place(x=700, y=550)

button_contacts=tk.Button(root, text="Contacts", command=contacts, font=("Times New Roman", 25),
                            bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                            activeforeground=button_hover_fg_color)
button_contacts.place(x=900, y=550)

button_log_out = tk.Button(root, text="Log Out", command=log_out, font=("Times New Roman", 25),
                           bg=button_bg_color, fg=button_fg_color, activebackground=button_hover_bg_color,
                           activeforeground=button_hover_fg_color)
button_log_out.place(x=1100, y=550)

root.mainloop()