import datetime
import random
import webbrowser
from ROCK_PAPER_SCISSORS import rock_paper_scissors
import covid_checker
from TIC_TAC_TOE import tic_tac_toe_gui

def greeting():
    responses = [
        "Welcome, I am a personal chatbot. I can take care of you :). Your name please : ",
        "Hey hello! I am your personal bot who helps you to do your things. May I know your name? : "
    ]
    print(random.choice(responses))

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
    print("I can make you more comfortable :)")
    print("How are feeling now?")
    print("1. I'm feeling good and let's have some fun!!")
    print("2. I'm Not Feeling well :( Can you help me?")
    print("3. I want to watch movies and webseries")
    print("4. I want to buy some things")
    print("5. End my session")
    try:
        return int(input("How are you feeling now: "))
    except Exception:
        print("Enter a valid choice")

def bot():
    greeting()
    name = input()
    wish(name)
    choice = check()
    while choice != 5:
        if choice == 1:
            print("Why don't we play some exciting games :)")
            print("Avialable Games")
            print("1. Tic Tac Toe")
            print("2. Rock Paper Scissors")
            print("3. Why don't we have some Excitement!!!*Let me Guess your Age*")
            try:
                game = int(input("Choose A Game : "))
            except:
                print("Invalid Input")
                continue
            if game == 1:
                tic_tac_toe_gui.ttt()
            elif game == 2:
                rock_paper_scissors.rps()
            elif game == 3:
                pass
            else:
                print("Invalid Input :( ")
        elif choice == 2:
            print("1 : I am Physically Not well, Can you help me")
            print("2 : I am Mentally Disturbed, Can you help me")
            try:
                game = int(input("Choose your choice: "))
            except:
                print("Invalid Input")
                continue
            if game == 1:
                print("Oh!, I am worried about you")
                print("Trending Health Assessment tests....")
                print("1 : Covid-19 Health Assessment Test")
                print("2 : Health Condition Checker using Symptoms")
                try:
                    choose = int(input("Choose your Choice : "))
                except:
                    print("Invalid Input")
                    continue
                if choose == 1:
                    covid_checker.check_me()
                elif choose == 2:
                    print("Redirecting you.......")
                    webbrowser.open("https://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075", new = 1)
                else:
                    print("Sorry! I didn't get that")
            elif game == 2:
                print("Redirecting you.......")
                webbrowser.open("https://www.happify.com/", new = 1)
            else:
                print("Sorry! I didn't get that")
        elif choice == 3:
            print("Redirecting you.......")
            webbrowser.open("https://www.netflix.com/in/", new = 1)
        elif choice == 4:
            print("Redirecting you.......")
            webbrowser.open("https://www.amazon.in/", new = 1)
        else:
            print("Sorry! I didn't get that")
        choice = check()
    if choice == 3:
        print("Good bye "+name+" Take care :-)" )
bot()