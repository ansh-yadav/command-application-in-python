# Kreek's Adventures
# Kreek is a troubling guy who himself get into an troublesome situation but soon realizes this wants to get out and you would you like to help

''' We want some scences :- Store Room Scence, Corridor Scence '''

# this is our start where our program starts
def on_start():
    print("*" * 25)
    print("Welcome to Kreek's Adventures")
    print("*" * 25)
    play()

# Here all playing things we regulated
def play(): 
    print(" Press RETURN to start the game and CTRL - C to exit")
    input("> ")
    store_room()
    

# It is our Store Room Scence where we would start our game
def store_room():
    print("Your mouth been taped How would you escape ?")

    choice = input("> ")

    if choice == "struggle":
        print(" Oh Bad choice tap is electrified which get trigger by your movement")
        print("Oh Shame On you fool")
    elif choice == "walk":
        print("Good going Your mouth was bounded not your legs")
        print("Go ahead")
        corridor()

# This is a corridor 
def corridor():
    
    print("There is a monster which don't have eyes ")

    choice = input("> ")

    if choice == "fight":
        print("You are a fool and always remain a fool")
        print(" Don't you watch movies, those don't have eyes they got ears and powers")
    elif choice == "silent":
        print("Woah You escape from the corridor now you are free")
        print("Don't mess with for this short story, I am black belt holder in the arguments and the budget was smalllllllllllllllllllllllllllllll opposite to this spelling ")
        print("Get lost now.")

on_start()