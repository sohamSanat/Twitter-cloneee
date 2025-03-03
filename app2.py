import tkinter as tk

from pymongo.mongo_client import MongoClient


show_tweet_window = False

wrong_password = False


# !pushing data onto atlas

def push_data_onto_atlas():

    global username, password

    username = username_var.get()

    password = password_var.get()

    url = "mongodb+srv://hsohamsanat:1234@cluster0.gu2hb3z.mongodb.net/?retryWrites=true&w=majority"


    cluster = MongoClient(url)

    db = cluster["test"]

    collection = db["twitter-login"]


    post = {"username": username, "password": password}

    username_already_exists = collection.find_one({"username": username})

    if username_already_exists == None:

        collection.insert_one(post)

        print("New user detected! Account created! ")

        window.destroy()

    else:

        designated_passsword = username_already_exists["password"]

        if designated_passsword == password:

            print("Login successful")

            global show_tweet_window

            show_tweet_window = True

        else:

            print("Wrong password")

            wrong_password = True

        window.destroy()

       

        # global login

        # login = True


# !remove all content from welcome frame

def remove_all_content_from_welcome_frame():

    for widget in welcome_frame.winfo_children():

        widget.destroy()

   

# !welcome button pressed event

def welcome_button_pressed_event():

    remove_all_content_from_welcome_frame()

    push_data_onto_atlas()


# !main gui element

def gui():


    # !colors

    DARK_BACKGROUND = "#2D3250"

    LIGHT_BACKGROUND = "#424769"

    SECONDARY_TEXT = "#7077A1"

    MAIN_TEXT = "#F6B17A"


    # !window

    global window

    window = tk.Tk()

    window.geometry("1200x700+120+70")

    window.title("Twitter")

    window.config(bg=DARK_BACKGROUND)


    # //--------------------------forum poage-----------------------------

    def login_signup_page():

        # !login frame

        global login_frame

        login_frame = tk.Frame(window,bg=DARK_BACKGROUND)

        login_frame.place(anchor="center", relx=0.5, rely=0.28, relwidth=1, relheight=1.2)

       

        # ?login forum title

        login_title = tk.Label(login_frame,text="Enter your credentials", background=DARK_BACKGROUND, foreground=MAIN_TEXT, font=("Arial", 40, "bold"))

        login_title.place(anchor="center", relx=0.5, rely=0.4)


        # ?username entry

        # //username variable

        global username_var

        username_var = tk.StringVar()

        # //username variable


        username_entry = tk.Entry(login_frame, bg=LIGHT_BACKGROUND, foreground=SECONDARY_TEXT, font=("Arial", 30, "bold"), width=20, textvariable=username_var)

        username_entry.insert(0, "Username")


        username_entry.place(anchor="center", relx=0.5, rely=0.6)


        # ?password entry

        # //password variable

        global password_var

        password_var = tk.StringVar()

        # //password variable


        password_entry = tk.Entry(login_frame, bg=LIGHT_BACKGROUND, foreground=SECONDARY_TEXT, font=("Arial", 30, "bold"), width=20,textvariable=password_var)

        password_entry.insert(0, "password")


        password_entry.place(anchor="center", relx=0.5, rely=0.75)


        # ?submit button

        submit_button = tk.Button(login_frame,text="Submit", background=LIGHT_BACKGROUND, foreground=SECONDARY_TEXT, font=("Arial", 25, "bold"), width=10, command=lambda: [push_data_onto_atlas()])

        submit_button.place(anchor="center", relx=0.5, rely=0.9)

    # //------------------------forum poage-----------------------------


    # //------------------------welcome poage-----------------------------

    def main_page():

        # !welcome frame

        global welcome_frame

        welcome_frame = tk.Frame(window,bg=DARK_BACKGROUND)

        welcome_frame.place(anchor="center", relx=0.5, rely=0.38, relwidth=1, relheight=1.2)


        # ?welcome tilte

        welcome_title = tk.Label(welcome_frame,text="Welcome to Twitter", background=DARK_BACKGROUND, foreground=MAIN_TEXT, font=("Arial", 40, "bold"))

        welcome_title.place(anchor="center", relx=0.5, rely=0.4)


        # ?login button

        login_button = tk.Button(welcome_frame,text="Login", background=LIGHT_BACKGROUND, foreground=SECONDARY_TEXT, font=("Arial", 30, "bold"), width=7, command=lambda: [welcome_button_pressed_event, login_signup_page()])

        login_button.place(anchor="center", relx=0.4, rely=0.6)


        # ?signup button

        singup_button = tk.Button(welcome_frame,text="Signup", background=LIGHT_BACKGROUND, foreground=SECONDARY_TEXT, font=("Arial", 30, "bold"), width=7, command=lambda: [welcome_button_pressed_event, login_signup_page()])

        singup_button.place(anchor="center", relx=0.6, rely=0.6)

    # //------------------------welcome poage-----------------------------

       

    # !callin functions

    main_page()


    # !run

    window.mainloop()


# !callin fuctions

gui() 