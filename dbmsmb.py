from tkinter import *
import mysql.connector
import tkinter.messagebox as tm
from tkinter import ttk
from PIL import Image, ImageTk

def scrsize(window, reference_window=None):
    if reference_window:
        reference_geometry = reference_window.geometry()
        size_info, x_pos_info, y_pos_info = reference_geometry.split('+')
        width_info, height_info = size_info.split('x')

        width = int(width_info)
        height = int(height_info)
        x_pos = int(x_pos_info)
        y_pos = int(y_pos_info)

        window.geometry(f"{width}x{height}+{x_pos}+{y_pos}")

    else:
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        default_width = 900
        default_height = 650
        x_pos = (screen_width - default_width) // 2
        y_pos = (screen_height - default_height) // 2
        window.geometry(f"{default_width}x{default_height}+{x_pos}+{y_pos}")


## Button Styles ##
def button_style():
    return{'font': ('Arial', 12, 'bold'), 'bd': 3, 'width': 12, 'height': 1,'activebackground': 'purple', 'activeforeground': 'black',
                    'fg': 'white', 'bg': 'purple', 'relief': 'groove',}

def button_style1():
    return{'font': ('Arial', 12, 'bold'), 'bd': 1, 'width': 20, 'height': 8,'activebackground': 'blue', 'activeforeground': 'black',
                    'fg': 'white', 'bg': 'blue', 'relief': 'groove',}

def button_style2():
    return{'font': ('Arial', 12, 'bold'), 'bd': 1, 'width': 60, 'height': 4,'activebackground': 'lightblue', 'activeforeground': 'black',
                    'fg': 'blue', 'bg': 'lightblue', 'relief': 'groove',}
    
def button_style3():
    return{'font': ('Arial', 12, 'bold'), 'bd': 1, 'width': 25, 'height': 4,'activebackground': 'red', 'activeforeground': 'black',
                    'fg': 'black', 'bg': 'red', 'relief': 'groove',}

def button_style4():
    return{'font': ('Arial', 12, 'bold'), 'bd': 1, 'width': 25, 'height': 3, 'activebackground': 'lightblue', 'activeforeground': 'black',
                    'fg': 'blue', 'bg': 'lightblue', 'relief': 'groove',}
    
## Label Styles ##
def labeltext(x=None):
    label_font=('Gill Sans', 20, 'bold')
    if x is None:
        label_width = 500
    else:
        label_width = x.winfo_screenwidth()
    return label_font, label_width

## Registration or SignUp Setup ##    
def reg():
    global screen
    screen=Toplevel(main_screen)
    if 'screen' in globals():
        main_screen.withdraw()
    
    screen.title("REGISTER")

    scrsize(screen)
    screen.configure(bg="black")
    
    global name_entry
    global email_entry
    global password_entry
    global cid_entry

    name_entry = StringVar()
    email_entry = StringVar()
    password_entry = StringVar()
    cid_entry = StringVar()

    label_font, label_width = labeltext(main_screen)

    l1 = Label(screen, text="Customer SignUp Details", bg="royalblue", fg="black", height='2', font=label_font, width=label_width)
    l1.pack(pady=10)

    Label(screen, text='Name:', font=('Gill Sans', 14, 'bold'),bg="black", fg="white", height='2', width='30').pack()

    Entry(screen, textvariable=name_entry, width='20', font=('Gill Sans', 14)).pack()

    Label(screen, text='Email address:', font=('Gill Sans', 14, 'bold'),bg="black", fg="white", height='2', width='30').pack()

    Entry(screen, textvariable=email_entry, width='20', font=('Gill Sans', 14)).pack()

    Label(screen, text='Set Password:', font=('Gill Sans', 14, 'bold'),bg="black", fg="white", height='2', width='30').pack()

    Entry(screen, textvariable=password_entry, show='*', width='20', font=('Gill Sans', 14)).pack(pady=2)

    Label(screen, text='Customer Id:', font=('Gill Sans', 14, 'bold'),bg="black", fg="white", height='2', width='30').pack()

    Entry(screen, textvariable=cid_entry, width='20', font=('Gill Sans', 14)).pack(pady=2)

    Button(screen, text='Sign Up', **button_style(), command=signed).pack()

    reopen_button = Button(screen, text="Back", font=('Arial', 9, 'bold'), width=8, height=1, bd=1, bg='black', fg='white',activebackground='yellow', activeforeground='black', command=back1)

    reopen_button.place(relx=1.0, anchor='ne', x=-10, y=30)

def back1():
    main_screen.deiconify()
    if 'screen' in globals():
        screen.withdraw()

    elif 'login_screen' in globals():
        login_screen.withdraw()

## Sign Up Window ##
def signed():
    name_info = name_entry.get()
    email_info = email_entry.get()
    pwd_info = password_entry.get()
    cid_info = cid_entry.get()

    if len(name_info) < 1 or len(email_info) < 1 or len(pwd_info) < 1 or len(cid_info) < 1:
        global error_label
        error_label = Label(screen, text="Please fill in all fields correctly",
                            bg='black', fg='red')
        error_label.pack(pady=2)
        screen.after(2500, hide_error_label)
    else:
        z = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='22bai1452',
            database='moviedetails'
        )
        mycursor = z.cursor()

        # SQL statement to insert a new customer
        sql = 'INSERT INTO customer(cname, email_id, password, cid) VALUES (%s, %s, %s, %s)'
        val = (name_info, email_info, pwd_info, cid_info)

        try:
            mycursor.execute(sql, val)
            z.commit()
            global customer_name
            customer_name=name_info
            Label(screen, text='Signed Up Successfully', bg='black', fg='Yellow').pack()
            print('\nSigned Up Successfully')
        except Exception as e:
            z.rollback()
            print("Error:", e)
        finally:
            print("\nWelcome to MOVIE WORLD\n")
            selectcity()
            mycursor.close()
            z.close()
            if 'screen' in globals():
                screen.withdraw()

## Login window ##
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    if 'screen' in globals():
        main_screen.withdraw()

    login_screen.title("LOGIN")

    scrsize(login_screen)
    login_screen.configure(bg="black")

    global cname_verify
    global password_verify
    cname_verify = StringVar()
    password_verify = StringVar()

    label_font, label_width = labeltext(main_screen)

    l1 = Label(login_screen, text="Customer Login", bg="royalblue", fg="black", 
            height='2',font=label_font, width=label_width)
    l1.pack(pady=10)

    Label(login_screen, text='Customer Name:', font=('Gill Sans', 14, 'bold'),
        bg="black", fg="white", height='2', width='30').pack()

    Entry(login_screen, textvariable=cname_verify, width='20', font=('Gill Sans', 14)).pack()

    Label(login_screen, text='Password:', font=('Gill Sans', 14, 'bold'),
        bg="black", fg="white", height='2', width='30').pack()

    Entry(login_screen, textvariable=password_verify, show='*', width='20', font=('Gill Sans', 14)).pack(pady=2)

    Button(login_screen, text='Login', **button_style(), command=login_verify).pack()

    reopen_button = Button(login_screen, text="Back", font=('Arial', 9, 'bold'), width=8, height=1, bd=1, bg='black', fg='white',
                        activebackground='yellow', activeforeground='black', command=back1)

    reopen_button.place(relx=1.0, anchor='ne', x=-10, y=30)
    
## Main Window ##    
def movie_world_screen():
    global movie_world_screen
    movie_world_screen = Toplevel(main_screen)
    scrsize(movie_world_screen)
    movie_world_screen.configure(bg="black")
    movie_world_screen.title("Movie World")

    label_font, label_width = labeltext(movie_world_screen)
    Label(movie_world_screen, text="Movie World", bg="yellow", fg="black", height='2',font=label_font, width=label_width).pack()
    Button(movie_world_screen, text='Booking History', **button_style4(), command=booking_history).pack()
    Button(movie_world_screen, text='Ticket Cancellation', **button_style4(), command=ticket_cancellation).pack()
    Button(movie_world_screen, text='New Booking', **button_style4(), command=lambda: selectcity()).pack()
    
global customer_name
## Login and Verify ##
def login_verify():
    global customer_name
    c_name = cname_verify.get()
    password = password_verify.get()

    z = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='22bai1452',
        database='moviedetails'
    )
    mycursor = z.cursor()

    sql = "SELECT * FROM customer WHERE cname = %s AND password = %s"
    val = (c_name, password)

    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    
    if result:
        customer_name = c_name  
        movie_world_screen() 
    else:
        tm.showerror("Login Error", "Invalid Credentials")
    mycursor.close()
    z.close()

## Booking History ##
def booking_history():
    global customer_name
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='22bai1452',
        database='moviedetails'
    )
    cursor = connection.cursor()

    query = "SELECT t_no, m_name, show_date, show_time, s_name, price FROM ticket WHERE cname = %s"
    cursor.execute(query, (customer_name,))
    tickets = cursor.fetchall()

    if not tickets:
        tm.showinfo("No Bookings Found", f"No booking history found for customer '{customer_name}'.")
        cursor.close()
        connection.close()
        return

    history_window = Toplevel(main_screen) 
    history_window.title("Booking History")
    history_window.configure(bg="black")
    scrsize(history_window) 

    Label(history_window, text="Booking History", bg="royalblue", fg="black", height='2',font=('Gill Sans', 20, 'bold')).pack(pady=10)
    
    for ticket in tickets:
        t_no, m_name, show_date, show_time, s_name, price = ticket
        ticket_info = (
            f"Ticket Number: {t_no}\nMovie: {m_name}\nShow Date: {show_date}\nShow Time: {show_time}\nSeats: {s_name}\nPrice: {price}"
        )
        Label(history_window, text=ticket_info, bg="lightyellow", fg="black", height='7',font=('Gill Sans', 14), width=25).pack(pady=5)
    Button(history_window, text="Close", command=history_window.destroy).pack(pady=5)

    cursor.close()
    connection.close()

def request_booking_history():
    if not customer_name:
        tm.showerror("Login Required", "Please log in to view booking history.")
        return
    booking_history(customer_name)

## Ticket Cancellation ##
def ticket_cancellation():
    global customer_name
    cancel_window = Toplevel(main_screen)
    cancel_window.title("Ticket Cancellation")
    cancel_window.configure(bg="black")
    match_geometry(main_screen, cancel_window)

    label_width=30
    Label(cancel_window, text="Ticket Cancellation", bg="royalblue", fg="black", height='2',font=('Gill Sans', 20, 'bold'), width=label_width).pack(pady=10)
    
    t_no_entry = Entry(cancel_window, font=('Gill Sans', 14))
    t_no_entry.pack(pady=10)

    # Cancel button
    Button(cancel_window, text="Cancel Ticket", command=lambda: cancel_ticket(t_no_entry.get()), **button_style()).pack(pady=10)
    # Close button
    Button(cancel_window, text="Close", command=cancel_window.destroy, **button_style()).pack(pady=10)

def cancel_ticket(t_no):
    if not t_no.strip():
        tm.showerror("Invalid Input", "Please enter a valid ticket number.")
        return
    global customer_name
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='22bai1452',
            database='moviedetails'
        )
        cursor = connection.cursor()

        # SQL query to delete the ticket
        query = "DELETE FROM ticket WHERE t_no = %s AND cname = %s"
        cursor.execute(query, (t_no, customer_name))
        connection.commit()

        # Check if the ticket was successfully deleted
        if cursor.rowcount > 0:
            tm.showinfo("Ticket Cancellation", "Ticket successfully cancelled.")
        else:
            tm.showerror("Ticket Cancellation", "Ticket not found or already cancelled.")

    except mysql.connector.Error as err:
        tm.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

## Select City ##
def selectcity():
    global sc, lbl_text, city_screen, movie_frame
    city_screen = Toplevel(main_screen)  
    scrsize(city_screen)
    city_screen.configure(bg="black")
    city_screen.title("Choose Theater and Movie!!")

    label_font, label_width = labeltext(city_screen)

    lbl_text = StringVar()
    lbl_text.set("Select Your City")

    # Title label
    label = Label(city_screen, textvariable=lbl_text, height=1, width=label_width,font=label_font, bg='skyblue', fg='black')
    label.pack()

    # Dropdown menu for city selection
    cities = ["Velachery", "Annanagar", "Thoraipakkam", "Vadapalani", "Ashokpillar","T Nagar", "Saidapet", "Adyar"]

    sc = StringVar()
    sc.set("Cities")

    font_config = ('bold', 14)
    width_config = 15
    height_config = 1

    menubutton = Menubutton(city_screen, textvariable=sc, font=font_config, width=width_config, height=height_config, bd=0, bg="azure", fg="black", activebackground="yellow",
                            activeforeground='black')
    menubutton.menu = Menu(menubutton, tearoff=0, bd=0, bg="white", fg="black",activebackground="yellow", activeforeground='black', font=font_config)
    menubutton["menu"] = menubutton.menu

    # Adding city selection options
    for city_name in cities:
        menubutton.menu.add_radiobutton(
            label=city_name,
            variable=sc,
            value=city_name,
            command=update_movies)
    menubutton.pack()
    movie_frame = Frame(city_screen, bg="black")
    movie_frame.pack(fill=BOTH, expand=TRUE, padx=10, pady=10)

    # Sign-out button to return to main screen
    reopen_button2 = Button(city_screen, text="Sign Out", font=('Arial', 9, 'bold'), width=8, height=1,bd=1, bg='dimgrey', fg='white', activebackground='yellow', 
                            activeforeground='black', command=lambda: signout(city_screen))
    
    reopen_button2.place(relx=1.0, anchor='ne', x=-10, y=8)
    reopen_button2.lift()
    
def signout(city):
    main_screen.deiconify()
    if 'screen' in globals():
        screen.withdraw()

    elif 'login_screen' in globals():
        login_screen.destroy()
    city.withdraw()

## Movies Display ##
def update_movies():
    for widget in movie_frame.winfo_children():
        widget.destroy()
    movies_list(city_screen)

tid = None
def movies_list(city_screen):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='22bai1452',
            database='moviedetails'
        )
        cursor = connection.cursor()
        
        selected_city = sc.get()  
        query = "SELECT m_name, duration, ratings, tid FROM movie WHERE location = %s"
        cursor.execute(query, (selected_city,))
        movies = cursor.fetchall() 
        
        # Ensure previous widgets are removed to avoid overlap
        for widget in movie_frame.winfo_children():
            if isinstance(widget, Button):
                widget.destroy()

        if movies:
            for movie in movies:
                movie_name, duration, ratings, tid = movie
                button_text = f"{movie_name}\nDuration: {duration} min\nRating: {ratings}/10"

                # Create a button to show movie details
                btn = Button(movie_frame, text=button_text, **button_style1(),command=lambda mn=movie_name, t=tid: show_shows(city_screen, mn, t)) 
                btn.pack(side=LEFT, padx=10, pady=10)  
        else:
            Label(movie_frame, text="No movies found for the selected city.", bg="black",fg="white", font=('Gill Sans', 14)).pack(pady=10)

    except mysql.connector.Error as e:
        print("Error:", e) 
    finally:
        cursor.close()
        connection.close()

def show_shows(city, movie_name, tid):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='22bai1452',
            database='moviedetails'
        )
        cursor = connection.cursor()

        # SQL query to fetch shows for the selected movie and theater
        query = "SELECT show_date, show_time, show_day, language FROM `show` WHERE m_name = %s AND tid_s = %s"
        cursor.execute(query, (movie_name, tid))
        shows = cursor.fetchall() 
        
        # Clear previous widgets in the city frame to prevent overlap
        for widget in city.winfo_children():
            widget.destroy() 
        movie_label = Label(city, text=f"Movie: {movie_name}", **button_style3())
        movie_label.pack(pady=10, anchor=CENTER)  
        
        if shows:
            # Display shows for the selected movie
            for show in shows:
                show_info = f"Date: {show[0]}, Time: {show[1]}, Day: {show[2]}, Language: {show[3]}"
                # Create a button for each show
                btn = Button(
                    city, 
                    text=show_info, 
                    **button_style2(),  
                    command=lambda: seat_selection(city, movie_name, show[1], show[0])  
                )
                btn.pack(pady=5, anchor=W)  

    except mysql.connector.Error as e:
        print("Database Error:", e)  
    finally:
        cursor.close()
        connection.close()

def match_geometry(parent_window, new_window):
    geometry = parent_window.geometry()  
    new_window.geometry(geometry)  
    
import tkinter as tk
import random
import time


def seat_selection(city, movie_name, show_time, show_date):
    global seat, movie_name_global, show_time_global, show_date_global, seat_vars
    seat = tk.Toplevel(city)  
    movie_name_global = movie_name
    show_time_global = show_time
    show_date_global = show_date
    
    match_geometry(city, seat)
    
    if 'city' in globals():
        city.withdraw()

    seat.title("Seat Selection")
    seat.configure(bg="black")
    
    label_font, label_width = ("Arial", 25), 30
    tk.Label(seat, text="SELECT YOUR SEATS", width=label_width, font=label_font).pack()

    # Back and logout buttons
    back_button = tk.Button(
        seat,
        text="Back",
        font=('Arial', 9, 'bold'),
        width=7,
        height=1,
        command=back_1,
        bg='black',
        fg='white',
        activebackground='yellow',
        activeforeground='black'
    )
    back_button.place(relx=1.0, anchor='ne', x=-10, y=8)

    logout_button = tk.Button(
        seat,
        text="LogOut",
        font=('Arial', 9, 'bold'),
        width=8,
        height=1,
        command=signout_1,
        bg='black',
        fg='white',
        activebackground='yellow',
        activeforeground='black'
    )
    logout_button.place(relx=0.0, anchor='nw', x=10, y=8)

    # Dynamic seat checkboxes
    seat_vars = [tk.IntVar() for _ in range(96)]
    seat_positions = {"A": 65, "B": 95, "C": 125, "D": 155, "E": 185, "F": 215}

    for row, y_pos in seat_positions.items():
        for i in range(1, 17):
            seat_idx = (ord(row) - ord("A")) * 16 + i - 1
            tk.Checkbutton(
                seat,
                text="",
                onvalue=1,
                offvalue=0,
                height=2,
                variable=seat_vars[seat_idx],
                bg="grey",
                fg="black",
                activebackground="darkviolet",
                activeforeground="black"
            ).place(x=50 + (30 * (i - 1)), y=y_pos)

    # Screen label
    tk.Label(
        seat,
        text="Screen",
        bg="black",
        fg="darkviolet",
        font=('Gill Sans', 15, 'bold')
    ).place(x=255, y=260)

    # Confirm booking button
    confirm_button = tk.Button(
        seat,
        text="Confirm Booking",
        font=('Arial', 15, 'bold'),
        bg='lightgreen',
        fg='green',
        command=confirm_seat_selection
    )
    confirm_button.pack(side=tk.BOTTOM)
    
def back_1():
    if 'city' in globals():
        city.deiconify()  
        seat.withdraw()  

def signout_1():
    if 'main_screen' in globals():
        main_screen.deiconify()  
    if 'city' in globals():
        city.withdraw()
    if 'seat' in globals():
        seat.withdraw()

# generate a unique payment ID
def generate_payment_id():
    random.seed(time.time())
    return random.randint(10000, 99999)  

# generate a unique ticket number
def generate_ticket_number():
    return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))  


def calculate_total_cost():
    price_per_seat = 180  
    selected_seats = []
    for i, var in enumerate(seat_vars):
        if var.get() == 1:  
            row = chr(ord("A") + i // 16)  
            seat_number = (i % 16) + 1  
            seat_name = f"{row}{seat_number}"
            selected_seats.append(seat_name)

    return len(selected_seats) * price_per_seat

# Function to select seats and confirm booking
def seat_selection(city, movie_name, show_time, show_date):
    global seat, movie_name_global, show_time_global, show_date_global, seat_vars, seat_positions,t_no
    seat = tk.Toplevel(city)  
    movie_name_global = movie_name
    show_time_global = show_time
    show_date_global = show_date
    
    match_geometry(city, seat)  # Adjust the geometry

    if 'city' in globals():
        city.withdraw()  # Hide the city window

    seat.title("Seat Selection")
    seat.configure(bg="black")
    
    t_no = generate_ticket_number()
    
    label_font, label_width = ("Arial", 25), 30
    tk.Label(seat, text="SELECT YOUR SEATS", width=label_width, font=label_font).pack()

    # Back and logout buttons
    back_button = tk.Button(
        seat,
        text="Back",
        font=('Arial', 9, 'bold'),
        width=7,
        height=1,
        command=back_1,
        bg='black',
        fg='white',
        activebackground='yellow',
        activeforeground='black'
    )
    back_button.place(relx=1.0, anchor='ne', x=-10, y=8)

    logout_button = tk.Button(
        seat,
        text="LogOut",
        font=('Arial', 9, 'bold'),
        width=8,
        height=1,
        command=signout_1,
        bg='black',
        fg='white',
        activebackground='yellow',
        activeforeground='black'
    )
    logout_button.place(relx=0.0, anchor='nw', x=10, y=8)

    # Define seat positions
    seat_positions = {
        "A": 65,
        "B": 95,
        "C": 125,
        "D": 155,
        "E": 185,
        "F": 215
    }

    # Dynamic seat checkboxes
    seat_vars = [tk.IntVar() for _ in range(96)]

    # Fetch booked seats from the database
    booked_seats = get_booked_seats(movie_name, show_time, show_date)

    for row, y_pos in seat_positions.items():
        for i in range(1, 17):
            seat_idx = (ord(row) - ord("A")) * 16 + i - 1
            seat_name = f"{row}{i}"

            # Check if the seat is already booked
            if seat_name in booked_seats:
                seat_vars[seat_idx].set(1)  # Mark the seat as booked
                check_btn = tk.Checkbutton(
                    seat,
                    text=seat_name,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    variable=seat_vars[seat_idx],
                    bg="red",  # Indicate that the seat is booked
                    fg="white",
                    state=tk.DISABLED  # Disable the checkbox
                )
            else:
                check_btn = tk.Checkbutton(
                    seat,
                    text=seat_name,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    variable=seat_vars[seat_idx],
                    bg="grey",
                    fg="black",
                    activebackground="darkviolet",
                    activeforeground="black"
                )

            check_btn.place(x=50 + (30 * (i - 1)), y=y_pos)
    Label(
        seat,
        text="Screen",
        bg="black",
        fg="darkviolet",
        font=('Gill Sans', 15, 'bold')
    ).place(x=255, y=260)

    canvas = Canvas(seat, width=350, height=20, bg="lightcyan")
    canvas.place(x=120, y=290)
    
    # Confirm booking button
    confirm_button = tk.Button(
        seat,
        text="Confirm Booking",
        font=('Arial', 15, 'bold'),
        bg='lightgreen',
        fg='green',
        command=confirm_seat_selection
    )
    confirm_button.pack(side=tk.BOTTOM)

def get_booked_seats(movie_name, show_time, show_date):
    z = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='22bai1452',
        database='moviedetails'
    )
    mycursor = z.cursor()
    sql = "SELECT s_name FROM ticket WHERE m_name = %s AND show_time = %s AND show_date = %s"
    val = (movie_name, show_time, show_date)
    mycursor.execute(sql, val)
    booked_seats = mycursor.fetchall()  

    # Convert the fetched results to a list of seat names
    booked_seats = [seat[0] for seat in booked_seats]

    mycursor.close()
    z.close()
    return booked_seats

def confirm_seat_selection():
    total_cost = calculate_total_cost() 
    if total_cost == 0:
        tm.showerror("Error", "Please select at least one seat.") 
        return
    seat.withdraw()  # Close the seat selection window

    payment_window(total_cost)

def payment_window(total_cost):
    pay_id = generate_payment_id()  

    payment = tk.Toplevel()
    payment.title("Payment")
    payment.configure(bg="black")
    
    label_font = ("Arial", 12)
    label_width = 35
    
    match_geometry(seat, payment)  
    
    heading_label = tk.Label(
        payment,
        text="Proceed to Payment",  
        bg="red",  
        fg="black",  
        height=3,  
        font=label_font,  
        width=label_width  
    )
    heading_label.pack()
    tk.Label(
        payment,
        text=f"Payment ID: {pay_id}\nTotal Cost: {total_cost}",
        bg="lightyellow",
        fg="black",
        height='15',
        font=label_font,
        width=label_width
    ).pack()

    def proceed_payment():
        print("Payment Successful")
        update_payment_table(pay_id, total_cost, t_no)  
        
        # Generate ticket information
        ticket_info = {
            "cname": customer_name,
            "tid_t": movie_name_global,
            "t_no": t_no,
            "m_name": movie_name_global,
            "show_date":show_date_global,
            "show_time": show_time_global,  
            "seat_names": [f"{chr(ord('A') + i // 16)}{(i % 16) + 1}" for i, var in enumerate(seat_vars) if var.get() == 1],
            "price": total_cost, 
        }
        
        update_ticket_table(ticket_info)
        display_ticket(ticket_info) 
        
    payment_button = tk.Button(
        payment,
        text="Proceed to Payment",
        font=('Arial', 15, 'bold'),
        bg='lightgreen',
        fg='green',
        command=proceed_payment
    )
    payment_button.pack(side=tk.BOTTOM)
    exit_button = tk.Button(
    payment,
    text="Exit",
    font=('Arial', 15, 'bold'),
    bg='lightgreen',
    fg='green',
    command=payment.destroy  
    )
    exit_button.pack(side=tk.BOTTOM)
    
def update_payment_table(pay_id, total_cost, t_no):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='22bai1452',
            database='moviedetails'
        )
        cursor = connection.cursor()
        
        payment_query = """
            INSERT INTO payment (pay_id, t_amount, t_no)
            VALUES (%s, %s, %s)
        """
        cursor.execute(payment_query, (pay_id, total_cost, t_no))     
        connection.commit()  
    except mysql.connector.Error as error:
        print("Error updating payment table:", error)
    finally:
        cursor.close() 

def update_ticket_table(ticket_info):
    global customer_name
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='22bai1452',
            database='moviedetails'
        )
        cursor = connection.cursor()
        ticket_query = """
            INSERT INTO ticket (cname, tid_t, t_no, m_name, show_date, show_time, s_name, price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(ticket_query, (
            ticket_info["cname"],  
            ticket_info["tid_t"],  
            ticket_info["t_no"],  
            ticket_info["m_name"],  
            ticket_info["show_date"],  
            ticket_info["show_time"],  
            ",".join(ticket_info["seat_names"]),  
            ticket_info["price"],  
        ))
        connection.commit()
    except mysql.connector.Error as error:
        print("Error updating ticket table:", error) 
    finally:
        cursor.close()

def display_ticket(ticket_info):
    ticket_screen = tk.Toplevel()
    ticket_screen.title("Ticket Details")
    ticket_screen.configure(bg="black")
    match_geometry(seat, ticket_screen)
    
    label_font = ("Arial", 15, "bold")  
    label_width = 35  
    heading_label = tk.Label(
        ticket_screen,
        text="Tickets Booked Successfully",  
        bg="red",  
        fg="black", 
        height=3,  
        font=label_font, 
        width=label_width  
    )
    heading_label.pack()
    
    ticket_label = tk.Label(
        ticket_screen,
        text=f"Ticket Number: {ticket_info['t_no']}\n"
            f"Movie Name: {ticket_info['m_name']}\n"
            f"Show Date: {ticket_info['show_date']}\n"
            f"Show Time: {ticket_info['show_time']}\n"
            f"Seats: {', '.join(ticket_info['seat_names'])}\n"
            f"Total Cost: {ticket_info['price']}",
        bg="lightyellow",
        fg="black",
        font=("Arial", 12),
        width=35,
        height=15
    )
    ticket_label.pack()
    
    exit_button = tk.Button(
        ticket_screen,
        text="Exit",
        font=('Arial', 15, 'bold'),
        bg='lightgreen',
        fg='green',
        command=lambda: return_to_main(ticket_screen) 
    )
    exit_button.pack(side=tk.BOTTOM)
    
# Function to return to the main screen and close the current window
def return_to_main(current_screen):
    main_screen.deiconify()  
    current_screen.destroy()
    
##Main Screen for All windows##
def main_account_screen():
    global main_screen
    main_screen = Tk()
    scrsize(main_screen)
    main_screen.configure(bg="black")
    label_font, label_width = labeltext(main_screen)
    main_screen.title('Movie World')
    
    new_font = ("Comic Sans MS",28 , "bold underline")  # Change font family, size, and style
    Label(main_screen, text="MOVIE WORLD!!", bg="#D8BFD8", fg="purple", height='3', font=new_font, width=label_width).pack()
    
    Label(main_screen, text='', bg="black").pack()
    btn = Button(text='New User', command=reg, **button_style()) 
    btn.place(relx=0.5, rely=0.5, anchor=CENTER)
    btn1 = Button(text='Login', command=login, **button_style()) 
    btn1.place(relx=0.5, rely=0.6, anchor=N)

    # Run the application
    main_screen.mainloop()

# Define main screen
main_account_screen()