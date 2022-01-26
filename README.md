# ChatBot (Deprecated)
A python3 based chat bot


Created by Thetvdh

Using sqlite3 database from Python

As of 10/06/2021 all information stored in said database is in plain text. DO NOT STORE ANYTHING VALUABLE IN THIS DATABASE!!!!

# How to use the bot

First clone the repo to your machine using:

git clone https://github.com/Thetvdh/ChatBot.git

install the requirements by typing

Windows:
python3 -m pip install -r requirements.txt

Linux:
pip3 install -r requirements.txt

run the bot by typing:

python3 main.py.

If the menu looks dodgy in your terminal. Go into main.py and change DEBUG to False. It is on ln10


The bot is quite thick and will ignore most things said to it but if you want here is a list of things it can do.

 - Simple greetings
 - Check weather report in your area (type weather)
 - Check a wikipedia entry for a person or thing (type what/who is <thing>)
 - Tell you the current time
 
# TODO

  - Add password hashing for the database
  - Add option to choose where you get the weather report from
  - Add ability to change account info such as name, username, and gender
  - Implement an Admin command shell where advanced database and bot commands can be executed
  - Remove all debugging

# TO FIX
 
 - For some reason using the Wikipedia search for the term "Elon Musk" breaks it.
 - what is the time no longer works due to conflict with wikipedia.

Any suggestions to make my code better will be appriciated.
