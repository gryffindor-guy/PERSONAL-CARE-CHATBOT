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

