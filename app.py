import tkinter as tk

import app2

from pymongo.mongo_client import MongoClient

from tkinter import ttk


# !setting up atlas

url = "THIS LINK CONNECTS THE APP TO ATLAS' SERVER MAKE SURE TO GET YOUR OWN LINK"


cluster = MongoClient(url)

db = cluster["test"]

collection = db["tweets"]



# !sending data on atlas

def sending_data_on_atlas(tweet):

    tweet_list = [tweet]

    username = app2.username


    post = {"username": username, "tweet": tweet_list}


    username_already_exists = collection.find_one({"username": username})

    if username_already_exists == None:

        collection.insert_one(post)

    else:

        exisiting_list_of_tweets = username_already_exists["tweet"]

        exisiting_list_of_tweets.append(tweet)

        collection.update_one({"username": username}, {"$set": {"tweet": exisiting_list_of_tweets}})


   

    print("Tweet sent!")

    quit()



# !retriving all data from atlas

list_of_all_tweets = list()

def getting_all_the_tweets():

    dict_of_name_and_all_tweets = dict()

    all_data_from_db = collection.find({})

    list_of_tweets = list(all_data_from_db)

    for person in list_of_tweets:

        username = person["username"]

        tweets = person["tweet"]

        dict_of_name_and_all_tweets[username] = tweets


    for key in dict_of_name_and_all_tweets.keys():

        list_assoicated_with_key = dict_of_name_and_all_tweets[key]

        for tweet in list_assoicated_with_key:

            pair_dict = {key: tweet}

            list_of_all_tweets.append(pair_dict)

   


# !twitter app

def main_gui():


    # !colors

    DARK_BACKGROUND = "#2D3250"

    LIGHT_BACKGROUND = "#424769"

    SECONDARY_TEXT = "#7077A1"

    MAIN_TEXT = "#F6B17A"


    # !window

    window = tk.Tk()

    window.geometry("1200x700+120+70")

    window.title("Twitter")

    window.config(bg=DARK_BACKGROUND)

    # //--------------------reading page-----------------------------

    def reading_tweets_page():

        # !reading frame

        reading_frame = tk.Frame(window, bg=DARK_BACKGROUND)

        reading_frame.place(anchor="center", relx=0.5, rely=0.5, relwidth=1, relheight=1.2)


        # ?reading tweets title

        tweet_composing_title = tk.Label(reading_frame, text="All tweets", background=DARK_BACKGROUND, foreground=MAIN_TEXT, font=("Arial", 40, "bold"))

        tweet_composing_title.place(anchor="center", relx=0.5, rely=0.15)


        # !craete a main frame


        main_frame = tk.Frame(window, bg=DARK_BACKGROUND)

        main_frame.place(anchor="center", relx=0.5, rely=0.57, relwidth=1, relheight=0.85)


        # !create a canvas


        my_canvas = tk.Canvas(main_frame, bg=DARK_BACKGROUND, border=0, highlightthickness=0)

        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=20, pady=20)


        # !add a scrollbar to canvas


        my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)

        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


        # !configure the canvas


        my_canvas.configure(yscrollcommand=my_scrollbar.set)

        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))


        # !another frame inside canvas


        text_holder = tk.Frame(my_canvas, background=DARK_BACKGROUND)


        # !add new frame to a window in canvas


        my_canvas.create_window((0, 0), window=text_holder, anchor="nw")


        for i in range(len(list_of_all_tweets)):

            user_who_tweeted = list(list_of_all_tweets[i].keys())[0].capitalize()


            respective_tweets = list(list_of_all_tweets[i].values())[0]


            # //displaying tweeter name variable

            tweeter_name = tk.StringVar()

            tweeter_name.set(user_who_tweeted)

            # //displaying tweeter name variable


            # //displaying tweeter's tweet

            tweeter_tweet = tk.StringVar()

            tweeter_tweet.set(respective_tweets)

            # //displaying tweeter's tweet


            tk.Label(text_holder, textvariable=tweeter_name, bg=DARK_BACKGROUND, fg=MAIN_TEXT, font=("Arial", 30) ).pack(anchor="w")


            tk.Label(text_holder, textvariable=tweeter_tweet, bg=DARK_BACKGROUND, fg=SECONDARY_TEXT, font=("Arial", 15), pady=10).pack(anchor="w")

           

    # //--------------------reading page-----------------------------


    # //--------------------choosing page-----------------------------

    def choosing_page():

        # !choosing frame

        choosing_frame = tk.Frame(window, bg=DARK_BACKGROUND)

        choosing_frame.place(anchor="center", relx=0.5, rely=0.4, relwidth=1, relheight=1.2)


        # ?choosing tilte

        welcome_title = tk.Label(choosing_frame,text="Choose one", background=DARK_BACKGROUND, foreground=MAIN_TEXT, font=("Arial", 40, "bold"))

        welcome_title.place(anchor="center", relx=0.5, rely=0.4)


        # ?compose button

        login_button = tk.Button(choosing_frame,text="Compose", background=LIGHT_BACKGROUND, foreground=SECONDARY_TEXT, font=("Arial", 30, "bold"), width=10, command=compose_tweet)

        login_button.place(anchor="center", relx=0.3, rely=0.6)


        # ?read button

        singup_button = tk.Button(choosing_frame,text="Read", background=LIGHT_BACKGROUND, foreground=SECONDARY_TEXT, font=("Arial", 30, "bold"), width=10, command=lambda:[getting_all_the_tweets(), reading_tweets_page()])

        singup_button.place(anchor="center", relx=0.7, rely=0.6)

    # //--------------------choosing page-----------------------------


    # //--------------------tweet composing---------------------------

    def compose_tweet():

        # !tweet composing frame

        tweet_compose_frame = tk.Frame(window, bg=DARK_BACKGROUND)

        tweet_compose_frame.place(anchor="center", relx=0.5, rely=0.28, relwidth=1, relheight=1.2)


        # ?username displaying

        # //username variable

        username_variable = tk.StringVar()

        typed_username = app2.username

        username_variable.set(f"username: {typed_username}")

        # //username variable


        displaying_username = tk.Label(tweet_compose_frame, text="Username", background=DARK_BACKGROUND, foreground=SECONDARY_TEXT, font=("Arial", 25, "bold"), textvariable=username_variable)

        displaying_username.place(anchor="w", relx=0.14, rely=0.3)


        # ?tweet compose title

        tweet_composing_title = tk.Label(tweet_compose_frame, text="Compose Tweet", background=DARK_BACKGROUND, foreground=MAIN_TEXT, font=("Arial", 40, "bold"))

        tweet_composing_title.place(anchor="center", relx=0.5, rely=0.4)


        # ?tweet composing text box

        tweet_composing_text_box = tk.Text(tweet_compose_frame, height=10, width=60, bg=LIGHT_BACKGROUND, foreground=SECONDARY_TEXT,font=("Arial", 20, "bold"))

        tweet_composing_text_box.place(anchor="center", relx=0.53, rely=0.67)


        # ?submiting tweet button

        tweet_submit_button = tk.Button(tweet_compose_frame,font=("Arial", 20, "bold"), text="Submit", bg=LIGHT_BACKGROUND, foreground=SECONDARY_TEXT, width=30, command=lambda: sending_data_on_atlas(tweet_composing_text_box.get("1.0", "end-1c")))

        tweet_submit_button.place(anchor="center", relx=0.53, rely=0.96)

    # //--------------------tweet composing---------------------------


    # !calling func

    choosing_page()


    # !run

    window.mainloop()



# !calling main function

def main():

    if app2.show_tweet_window == True:

        main_gui()

    else:

        if app2.wrong_password == True:

            print("Wrong password mate")


if __name__ == "__main__":

    main() 
