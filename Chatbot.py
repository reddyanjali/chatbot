#Created By : Anjali Deepak
#Name of the Project : Simple Chatbot - Anj

#Function to greet the user
def greet(bot_name, year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + year + 'by Anjali.')

#Function to ask the user details
def user_name():
    print('How would you like me to call you?')
    name = input()
    print('That is a sweet name. It is a pleasure meeting you '+ name + '!')

#Function to get the users' favorite musician details
def user_fav_singer():
    print('Who is your favorite musician?')
    print(' 1. BTS \n 2. Taylor Swift \n 3. One Direction')
    fav_singer = int(input())

    if fav_singer == 1:
        print('Hey ARMY! Borahae! Let me recommend a song')
        song_rec(1)
        quit()
    elif(fav_singer == 2):
        print('Oh hey Swiftie! Nice to meet you! Let me recommend a song')
        quit()
    elif(fav_singer == 3):
        print('Hello Directioner! Nice to meet you! Let me recommend a song')
        quit()
    else:
        print("Enter a correct value")

def song_rec(selection):
    if selection == 1:
        text = "Listen to the latest song Take Two <3!"
        print("\x1B[3m" + text + "\x1B[0m")
    elif selection == 2:
        text = "Let's listen to August!"
        print("\x1B[3m" + text + "\x1B[0m")
    elif selection == 3:
        text = "Let's listen to What makes you beautiful!"
        print("\x1B[3m" + text + "\x1B[0m")

def quit():
    print("Seeya! Bye!")

greet('Anj','2023')
user_name()
user_fav_singer()