#Emily Rusch - Project 2
import time
import random
out = []
element = ""

def prt_list(list):
    for x in list:
        print(x, flush=True)
        if len(x) < 70:
            time.sleep(2)
        else:
            time.sleep(3)

def prt_single(sentence, num):
    print(sentence, flush=True)
    time.sleep(num)

#Intro to the story
def intro():
    global element
    element = random.choice(["valley","forest","mountains","river"])
    story = [
        "You are driving in the late night trying to make it home.",
        "As your drive continues your phone battery is getting closer and closer to 0%.",
        "The next thing you know it dies and you have lost your only form of directions.",
        "You decide the best thing to do is continue straight as long as you can.",
        "Your plan is working until you find yourself approaching a fork in the raod.",
        f"To your left is a {element} and to your right is a corn field.",
        "Now you are left to choose which direction to turn.\n"
    ]
    prt_list(story)

#Choosing which direction to turn
def choice_1():
    act = [
        "Enter 1 to turn to the left.",
        "Enter 2 to turn to the right."
    ]
    prt_list(act)
    response = str(input("Which direction will you turn?\n"))
    return response

#The player decides to turn to the left in choice_1
def choice_left():
    act11 = [
        f"You decide to turn left towards the {element}.",
        "You continue on your journey home when you see a sign up ahead.\n"
        ]
    act1 = [
        f"You decide to turn left towards the {element}.",
        "You continue on your journey home when you see a sign up ahead.",
        "You are hoping the sign will point you home.",
        "Once you finally get close enough to read the sign it tells you there is a dirt path labeled shortcut.\n"
        ]
    if "gauge" in out:
        prt_list(act11)
    else:
        prt_list(act1)
    response1 = str(input("Do you decide to continue straight (3) or take the shortcut (4)?\n"))
    return response1

#Related to the response to choice_11 to either continue straight or take the short cut
def choice_straight():
    response1 = choice_left()
    if response1 == "3":
        act3 = [
            f"You decide to continue straight towards the {element}.",
            "Soon you hear putter putter from your car until it slows to a stop.",
            "You are now out of gas and officially lost!\n"
            ]
        act4 = [
            f"You continue straight through the {element} for miles and miles.",
            "You start to feel like you are never going to make it home.",
            "You glance down at the gauge measuring the gas left in your tank.",
            f"Eventually you make it out of the {element} and after many more miles of driving you finally see your house.",
            "You have made it home!\n"
            ]
        if "gauge" in out:
            prt_list(act4)
            play_again()
        else:
            prt_list(act3)
            play_again()
    elif response1 == "4":
        act5 = ["You turn down the shortcut and everything is looking okay.",
            "That is, until you come across another fork in the road.\n"
            ]
        if "gauge" in out:
            prt_single("The road ahead of you looks promising that it will lead you home.",
                "You glance down to check the gauge measuring the amount of gas left in the tank.",
                "You have a about a quarter tank left and are hoping that will be enough.",
                "You continue to drive towards the corn field.",
                "Soon you realize that you are going in a big circle around the corn field.",
                "So, you decide to go the other direction at the fork in the road.\n"
                )
        else:
            prt_list(act5)
            out.append("gauge")
            choice_1
    else:
        prt_single("Choose wisely!", 2)
        choice_straight()

#The player decides to turn to the right in choice_1
def choice_right():
    prt_single("You turn right and continue on towards a corn field.", 2)
    act2 = [
        "We are at another fork in the road. Now which way will we go?", 2
        ]
    if "gauge" in out:
        prt_single(
            "You know the path towards the corn field will not get you home.",
            "It is just a path circling the corn field", 1
            )
        prt_single("You are back at the original fork in the road", 2)
    else:
        prt_list(act2)
        out.append("gauge")

def game():
    response = choice_1()
    if response == "1":
        choice_straight()
    elif response == "2":
        choice_right()
    else:
        game()
    game()

# Adventure game
def word_game():
    intro()
    game()
    play_again()

# Playing play_again
def play_again():
    global about
    prt_single("Would you like to play again?", 2)
    response2 = str(input("Please enter 'y' for yes and 'n' for no.\n").lower())
    if response2 == "y":
        out = []
        word_game()
    elif response2 == "n":
        exit()
    else:
        play_again()

word_game()
