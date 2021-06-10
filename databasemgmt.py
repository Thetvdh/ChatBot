import sqlite3
import usermgmt


class DatabaseManager:
    def __init__(self, name):
        self.name = str(name)
        self.connection = None
        self.cursor = None
        self.establish_connection()

    def establish_connection(self):  # connects to db and creates cursor
        try:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()
            print("[INFO] Established Connection with the database")
        except Exception:
            print("[ERROR] Failed to establish connection with the database")

    def close_connection(self):  # closes connection
        self.connection.close()

    def create_table(self, tbl_name, **kwargs):  # method to create a table. Most likely will not be used again.
        magic = ""
        for key, value in kwargs.items():
            # print(f"Key is {key} Value is {value}")
            magic = magic + key + " " + value + ","
        magic = magic[:-1]
        # print(magic)
        sql = f'''CREATE TABLE {tbl_name} 
                ({magic})'''
        self.cursor.execute(sql)
        self.cursor.commit()

    def insert_user(self, user):  # adds a user to the db
        params = (user.firstname, user.lastname, user.age, user.gender, user.username, user.password)
        sql = "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)"
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return True
        except sqlite3.OperationalError:
            print("The database is experiencing an issue currently. Please try again later. (Operational Error)")
            return False

    def read_data(self, *args):  # reads all data from the users table. Usable by admins when implemented TODO
        params = tuple(args)
        print(params)  # TODO remove debugging
        sql = "SELECT * FROM users"
        self.cursor.execute(sql, params)
        print("[DB]", self.cursor.fetchall())

    def check_duplicate_users(self, username):  # checks for duplicate users in the db
        sql = "SELECT username FROM users"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for name in data:
            test_name = name[0].lower()
            if username.lower() == test_name:
                return True
        return False

    def verify_login_details(self, username, password):  # checks if the login details are correct
        # TODO check if any password in the db can log into any account
        sql = "SELECT username, password FROM users WHERE username=:username"
        self.cursor.execute(sql, {"username": username})
        data = self.cursor.fetchone()
        if data[1] == password:
            sql = "SELECT * FROM users WHERE username=:username"
            self.cursor.execute(sql, {"username": username})
            data = self.cursor.fetchone()
            print(data)  # TODO remove debugging
            userobj = usermgmt.User(data[1], data[2], data[3], data[4].lower(), data[5], data[6], data[7], data[8])
            # ^ creates a user object to be established in a session
            return True, userobj
        return False

    def write_bot_name(self, username, bot_name):  # adds the bot name to the db when created
        sql = "UPDATE users SET botname=:botname WHERE username=:username"
        self.cursor.execute(sql, {"botname": bot_name, "username": username})
        self.connection.commit()
        # Check to see if it has written
        sql = "SELECT botname FROM users WHERE username=:username"
        self.cursor.execute(sql, {"username": username})
        data = self.cursor.fetchone()
        if data[0] == bot_name:
            return True

    def first_time_complete(self, username):  # sets first time to false in db
        sql = "UPDATE users SET firsttime=0 WHERE username=:username"
        self.cursor.execute(sql, {"username": username})
        self.connection.commit()
