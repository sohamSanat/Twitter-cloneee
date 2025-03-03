Detailed Features
1. User Authentication (app2.py)

    Users can sign up by entering a username and password.
    If the username is new, it creates an account in MongoDB Atlas.
    If the username already exists, it checks if the password is correct:
        If correct, the user logs in.
        If incorrect, an error message is displayed.

2. Tweet Management (app.py)

    Users can compose and submit tweets, which are stored in MongoDB Atlas under their username.
    Tweets are appended to the user’s existing tweet history if they have tweeted before.
    The app retrieves and displays all tweets from all users in a scrollable interface.

3. GUI (Graphical User Interface)

    Uses Tkinter to create a visually appealing Twitter-like interface.
    Three main pages:
        Welcome Page – Users choose to log in or sign up.
        Compose Page – Logged-in users can write and submit tweets.
        Read Tweets Page – Displays all tweets from all users in a scrollable window.

4. Database Integration (MongoDB Atlas)

    Uses MongoClient to connect to MongoDB Atlas.
    Stores user data (username & password) in the "twitter-login" collection.
    Stores tweets in the "tweets" collection, structured as:

    {
      "username": "exampleUser",
      "tweet": ["First tweet!", "Another tweet!"]
    }

    Retrieves all stored tweets when needed.

How It Works

    User opens the app.
    Chooses to log in or sign up.
    If login is successful, they can:
        Compose & submit tweets.
        Read all tweets from all users.
    Tweets are saved and displayed in a scrollable list.