import pyttsx3 as TTs
engine = TTs.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 145)

def TTS(Text):
    engine.say(Text)
    engine.runAndWait()

def Adjust_Pace(Rate):
    engine.setProperty('rate', Rate)

def Voice_Change(Num):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[Num].id)

TTS("Greetings")
TTS("Kindly Choose One of the following")
i = 100
while i == 100:
    user = input("\nChoose one:\n 1. TTS\n2. Change voice\n3. Adjust Pace\n4.Exit\n")
    user.lower()
    if user == "1" or user == "TTS":
        while i == 100:
            TTS("Type 1 to continue or 2 to exit")
            choice = input("Choose if\n 1. Continue\n2. Exit")
            choice.lower()
            if choice == "1" or choice == "continue":
                TTS("What do you want to say??")
                print("What do you want to say??")
                TTS("Please type:")
                print("Please type:\n")
                Say = input()
                TTS(Say)
            else:
                break

    elif user == "2" or user == "change voice":
        Voice_ID = int(input("Enter '0' or '1':  "))
        Voice_Change(Voice_ID)
        TTS("Voice Changed")

    elif user == "3" or user == "adjust pace":
        Rate = int(input("Enter the Pace: "))
        Adjust_Pace(Rate)
        TTS("Pace Adjusted")

    elif user == "4" or user == "exit":
        print("Thank You")
        TTS("Thank You")
        exit()

    else:
        print("Command not Understood")
        TTS("Command not Understood")
