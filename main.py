# /usr/bin/env python3

import sys
import databasemgmt
import usermgmt

# user = usermgmt.User("Test", "Acc", 17, "male", "TestAcc", "TestAcc") SYNTAX FOR CREATING USER OBJECT
version = 2
capabilities = ['Conversation', 'Commands', 'Searching']
stand_greetings = {}


def add_new_user():
    valid = False
    firstname = input("What is your first name? ")
    lastname = input("What is your last name? ")
    age = input("What is your age? ")
    gender = input("What is your gender? ")
    username = ""
    while not valid:  # checks for duplicates and assigns stuff
        username = input("Please create a username: ")
        if manager.check_duplicate_users(username):
            print("Username is already taken. Please enter a different username.")
            valid = False
        else:
            valid = True
    password = input("Please create a password: ")

    user = usermgmt.User(firstname, lastname, age, gender, username, password, None, 1)  # creates user object to pass
    return user


def login(): # basic login system
    username_valid = False
    password_valid = False
    username = ""
    while not username_valid:
        username = input("Please enter your username!! ")
        if manager.check_duplicate_users(username):
            username_valid = True
        else:
            print("Username incorrect. Please try again.")
    while not password_valid:
        password = input("Please enter your password!! ")
        valid, userobj = manager.verify_login_details(username, password)
        if valid:
            return userobj
        else:
            print("Invalid password!!")


def print_menu():
    print(f"#############################\n"
          f"#\t\t CHATBOT V{version} \t\t#\n"
          f"#############################\n"
          f"# (1)\t Add User\t\t\t#\n"
          f"# (2)\t Login \t\t\t\t#\n"
          f"# (3)\t Admin \t\t\t\t#\n"
          f"# (4)\t Exit \t\t\t\t#\n"
          f"#############################\n")


def main(session):
    session.establish_pronouns()
    if session.bot_name is None: # runs if no bot name
        print(f"Hello {session.firstname}, I am Chatbot V1! However, I understand that is quite formal so...")
        refer_name = input("What would you like to call me? ")
        session.bot_name = refer_name
        choice = input("Would you like to save that for future chats? Y/N ")
        if choice.lower() == 'y':
            if manager.write_bot_name(session.username, refer_name):
                print("My name has been remembered!")
        else:
            print(f"Ok then. I will be called {session.bot_name} for just this chat!")
    # runs if first time
    if session.first_time == 1:
        print(f"Hello {session.firstname}, I am {session.bot_name}. As it's your first time\n"
              f"I thought it might be good to walk you through a list of my capabilities!")
        for capability in capabilities:
            print(capability)
        print("To see what advanced features I have, type help and I will tell you what to do next!")
        print("Well then. Looks like your introduction has finished! To replay this intro, type show introduction\not7"
              "and I will replay it for you!")
        session.first_time = 0
        manager.first_time_complete(session.username) # sets first time to false
    print(f"Welcome, {session.firstname}")
    while True: # game loop
        user_input = input().lower()
        user_input_list = user_input.split(" ")
        if user_input_list[0] == "help" or user_input_list[0] == "show" or user_input_list[0] == "set":
            # TODO add the commands in here
            pass
        elif user_input in stand_greetings.keys():
            # TODO Do logic to do response
            pass
        else:
            print("Sorry I am not too sure what you mean. Try rephrasing it and maybe I can help you!")


def menu():
    valid = False
    while not valid:
        print_menu()
        choice = int(input("Enter a choice "))
        if choice == 1:
            new_user = add_new_user()
            if manager.insert_user(new_user):
                print("New user has been successfully created. Please login!")
        elif choice == 2:
            session = login()
            print("Logged in successfully")
            main(session)
            print("Main Ended")  # TODO remove debugging
            manager.close_connection()
            sys.exit(0)
        elif choice == 3:
            valid = True
        elif choice == 4:
            print("Goodbye!!")
            sys.exit(0)
        elif choice == 5:
            print("Well done you discovered the secret!!")
            sys.exit(0)
        else:
            print("Invalid option. Please choose an option from the menu")


if __name__ == '__main__':
    manager = databasemgmt.DatabaseManager("project.db")
    menu()
