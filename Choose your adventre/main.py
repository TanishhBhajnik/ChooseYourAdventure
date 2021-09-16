# This is an choose adventure game! You will be given in a certain situation you have to find your way out alive!
import time
def main():
    #Asking user's name 
    name = input("Enter your name: ")
    print(f"Welcome {name} to this adventure!")
    time.sleep(1)
    print("WARNING! This game is very dangerous! Play wisely!")
    time.sleep(1)

    print("Its a dark, cold night..")
    time.sleep(1)
    print("You are walking on a dirt road alone, it comes to an end, there are two ways...")
    time.sleep(1)
    answer = input("LEFT or RIGHT? Which way would you go..??").lower()
    time.sleep(1)   

    #Using If else statement for the questions if they choose the right question they go ahead or else they die.
    if answer == "left":
        print('You come across a bridge. It looks Whacky! Do you walk on the bridge or go back?')
        time.sleep(1)
        answer2 = input("(Type walk to cross the bridge or Type back to go back..)")
        time.sleep(1)



        if answer2 == "walk":
            print("You start walking on the bridge..The bridge starts to wobble and breaks down.. You fall down and Die!")
            time.sleep(1)

        elif answer2 == "back":
            print("You are afraid and start going back..But suddendly a Demon appears, he eats you up. You Die! ")
            time.sleep(1)

        else:
            print("Not a valid option! You lose... ")
            time.sleep(1)


    elif answer == "right":
        print("You go ahead, and find a sword... Do you pick it up or go ahead? ")
        time.sleep(1)
        answer3 = input("(Type pick if you want to pick the sword or Type ahead to walk ahead)")
        time.sleep(1)

        if answer3 == "pick":
            print("You find a huge demon coming towards you...you slay him with the sword. You Win! ")
            time.sleep(1)
        elif answer3 == "ahead":
            print("You ignore the sword and walk ahead..A huge demon comes towards you and eats you.You lose! ")
            time.sleep(1)

        else:
            print("Not a valid option! You lose...") 
            time.sleep(1)  

main()



    
