import datetime
import pyfiglet
from ROCK_PAPER_SCISSORS import rock_paper_scissors
import covid_checker
from TIC_TAC_TOE import tic_tac_toe_gui

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
            print(pyfiglet.figlet_format("GAMES"))
            print("Avialable Games")
            print("1. Tic Tac Toe")
            print("2. Rock Paper Scissors")
            print("3. Why don't we have some Excitement!!!*Let me Guess your Age*")
            try:
                game = int(input("Choose A Game"))
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
            covid_checker.check_me()
        else:
            print("Sorry! I didn't get that")
        choice = check()
    if choice == 3:
        print("Good bye "+name+" Take care :-)" )
bot()