<<<<<<< HEAD
import random
from datetime import datetime
import requests

def greet():
    responses = [
        "Welcome, I am chatbot.Your name please",
        "Hey hello! I am your bot who helps you to do calculations.May I know your name?"
    ]
    print(random.choice(responses))


def get_greeting_time():
    time = datetime.now()
    greeting_time = "Good Morning"
    if(time.hour >= 22):
        greeting_time = "Hi, Its late"
    elif(time.hour > 17):
        greeting_time = "Good Evening"
    elif(time.hour > 12):
        greeting_time = "Good Afternoon"
    return greeting_time

def welcome(name):
    message = [
        "Nice to meet you",
        "Lets work together"
    ]
    print(f"{get_greeting_time()}, {random.choice(message)}")

greet()
name = input("Enter your name : ")
welcome(name)

=======
import datetime

def greeting():
    print("Hello there, this is bot. I'm here to help you with your health. May I know your name?")

def wish(name):
    time_now = datetime.datetime.now().hour
    if time_now < 12:
        print("Well! nice to meet you " + name + ", Good morning.")
    elif time_now > 12 and time_now < 17:
        print("Well! nice to meet you " + name + ", Good afternoon.")
    elif time_now > 18 and time_now <22:
        print("Well! nice to meet you " + name + ", Good evening.")
    else:
        print("Oh! I think it's time for bed " + name + ".")

def check():
    print("I will help you to assess your health")
    print("How are feeling now?")
    print("1. I'm feeling good and let's have some fun!!")
    print("2. I'm feeling a little ill. Can you help me?")
    print("3. End my session")
    try:
        return int(input("How are you feeling: "))
    except Exception:
        print("Enter a valid choice")

def bot():
    greeting()
    name = input()
    wish(name)
    choice = check()
    while choice != 3:
        if choice == 1:
            #place your game
        elif choice == 2:
            #covid verification
        else:
            print("Sorry! I didn't get that")
        choice = check()
    if choice == 3:
        print("Good bye "+name+" Take care :-)" )
>>>>>>> bcc7478b29c9a7f1bb68a828925a2a8a7237aa43
