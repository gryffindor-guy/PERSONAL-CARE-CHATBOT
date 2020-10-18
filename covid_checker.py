import pyfiglet #Install this module using command --> pip install pyfiglet
import webbrowser
def symptoms():
    print("Are you experiencing any of the following Symptoms")
    print("1 : Cough")
    print("2 : Fever")
    print("3 : Difficulty in breathing")
    print("4 : Loss of senses of smell and taste")
    print("5 : None of the above")
    print("__________________________________")
    try:
        score = int(input("Enter the number of symptoms that you are experiencing. Enter 0 if your choice is 'None of the Above' : "))
    except:
        print("please enter a valid number of symptoms that you are experiencing")
        score = 10
        return score
    finally:
        if (score < 0 or score > 4):
            print("please enter a valid number of symptoms that you are experiencing")
            score = 10
        return score
def health_problems():
    score = 0
    print("Have you ever had any of the following?")
    print("1 : Diabetes")
    print("2 : Hypertension")
    print("3 : Lung disease")
    print("4 : Heart Diesease")
    print("5 : Kidney Disorder")
    print("0 : None of the above")
    print("__________________________________")
    try:
        score = int(input("Enter the number of Health Problems that you are experiencing. Enter 0 if your choice is 'None of the Above' : "))
    except:
        print("please enter a valid number of Health Problems that you are experiencing")
        score = 10;
        return score
    finally:
        if (score < 0 or score > 5):
            print("please enter a valid number of Health Problems that you are experiencing")
            score = 10
        return score
def isTravelled():
    score = 0
    print("Have you traveled anywhere internationally in the last 28-45 days?")
    print("1 : Yes")
    print("0 : No")
    try:
        score = int(input("Enter your Response : "))
    except:
        print("please enter a valid number of symptoms that you are experiencing")
        score = 10;
        return score
    finally:
        if (score < 0 or score > 1):
            print("please enter a valid number of symptoms that you are experiencing")
            score = 10
        return score

def interaction():
    score = 0
    print("Which of the following apply to you?")
    print("1 : I have recently interacted or lived with someone who has tested covid-19 positive ")
    print("2 : I am a Healthcare Worker and I examined a covid-19 confirmed case without protective gear")
    print("0 : None of the above")
    print("__________________________________")
    try:
        score = int(input("Enter the number of above conditions that you are applicable. Enter 0 if your choice is 'None of the Above' : "))
    except:
        print("please enter a valid number of symptoms that you are experiencing")
        score = 10
        return score
    finally:
        if (score < 0 or score > 4):
            print("please enter a valid number of symptoms that you are experiencing")
            score = 10
        return score

def covid_checkup_score():
    total_score = 0
    # Symptoms
    score = symptoms()
    if (score == 10): return "something went wrong"
    elif (score > 2): total_score += (score + 2)
    else: total_score += score
    # Health Condition
    score = health_problems()
    if (score == 10): return "something went wrong"
    elif (score > 2): total_score += (score + 2)
    else: total_score += score
    # Recently Travelled or not
    score = isTravelled()
    if (score == 10): return "something went wrong"
    elif (score == 1): total_score += 3
    else: total_score += score
    # Interaction
    score = interaction()
    if (score == 10): return "something went wrong"
    elif (score > 1): total_score += 5
    else: total_score += score * 2
    return total_score

def covid_checkup(value):
    status = True
    try:
        if (value >= 15):
            print("!!!!!!!!!")
            print("If the information provided by you is accurate, It indicates that you are either unwell or at Risk.")
            print("we recommand you to get tested for covid-19 near your local hospital!,Please put on a mask!")
            print("CHOOSE YOUR INTEREST OF CONSULTATION")
            print("1 : I want an Hospital appointment")
            print("2 : I want an video appointment with a doctor")
            print("3 : I will take care of it")
            try:
                response = int(input())
                if response == 1:
                    print("Redirecting you........")
                    webbrowser.open("https://www.askapollo.com/online-doctors-consultation/", new=1)
                elif response == 2:
                    print("Redirecting you........")
                    webbrowser.open("https://www.practo.com/", new=1)
            except:
                print("Invalid input, please choose carefully.")
            
            status = False
        elif (value < 15):
            result = pyfiglet.figlet_format("HEALTH REPORT")
            print(result)
            print("Your infection risk is low :) :) :)")
            print("May be its just climate change ,we recommend you to stay at home for a couple of days to avoid any chance of exposure to the Novel Coronavirus and get this sample test done again.")
            print("Thank you! For your patience there isn't anything you should be worried about now, get this test done again when you dont feel well")
            print("----------------------------------------------------------------------------------------------------")
            status = False
    except:
        print("Invalid details are provided :(")

def check_me():
    value = covid_checkup_score()
    covid_checkup(value)



