class User:
    # creates user sessions and objects for use in places
    def __init__(self, firstname, lastname, age, gender, username, password, bot_name, first_time):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.username = username
        self.password = password
        self.pronouns = ()
        self.bot_name = bot_name
        self.first_time = first_time

    def establish_pronouns(self): # not sure if this will be used but its a feature I guess
        if self.gender == "male":
            self.pronouns = ("he", "him")
        elif self.gender == "female":
            self.pronouns = ("she", "her")
        else:
            self.pronouns = ("they", "them")
