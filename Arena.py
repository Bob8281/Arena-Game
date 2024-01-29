#Start Program:

advancedsetup = 0
randomizetraits = 0

def startup():
    global startupprompt
    startupprompt = int(input("Welcome to the arena! Would you like to play? (Yes=1, No=2 Advanced Setup=3)"))
    if startupprompt == 2:
        print("Too bad!")
    if startupprompt == 1:
        print("And so it begins...")
    if startupprompt == 3:
        global advancedsetup
        global numberofstartingplayers
        global randomizetraits
        advancedsetup = 1
        numberofstartingplayers = int(input("Enter a number of players: (2-7)"))
        randomizetraits = int(input("Randomize traits? (Yes = 1 No = Anything Else)"))
        input("Press 1 at any time to open stat check.")
        if numberofstartingplayers < 2 or numberofstartingplayers > 7:
            print("Enter a valid number of players.")
            advancedsetup = 0
            startup()
    if startupprompt == 42:
        print("You found easter egg number 1. (The Answer To Life)")
    if not startupprompt == 1 and not startupprompt == 2 and not startupprompt == 42:
        startup()
    print("")

startup()

#Define Player 1:

def defineplayername1():
    global player1
    player1 = input("Enter name for the first player: ")
    return

def defineplayerstrength1():
    global strength1
    strength1 = int(input("Enter a strength for the first player (1-10): "))
    return

def defineplayervigilance1():
    global vigilance1
    vigilance1 = int(input("Enter a vigilance value for the first player (1-10): "))
    return

def defineplayerspeed1():
    global speed1
    speed1 = int(input("Enter a speed value for the first player (1-10): "))
    return

def defineplayerstealth1():
    global stealth1
    stealth1 = int(input("Enter a stealth value for the first player (1-10)"))
    return

def defineplayercunning1():
    global cunning1
    cunning1 = int(input("Enter a cunning value for the first player (1-10): "))
    return

def defineplayercharisma1():
    global charisma1
    charisma1 = int(input("Enter a charisma value for the first player (1-10): "))
    return

def defineplayersanity1():
    global sanity1
    sanity1 = int(input("Enter a sanity value for the first player (1-10): "))
    return

def defineplayer1():
    defineplayername1()
    defineplayerstrength1()
    defineplayervigilance1()
    defineplayerspeed1()
    defineplayerstealth1()
    defineplayercunning1()
    defineplayercharisma1()
    defineplayersanity1()
    if strength1 < 1 or strength1 > 10:
        print("Strength must be from 1 to 10")
        defineplayer1()
    if vigilance1 < 1 or vigilance1 > 10:
        print("Vigilance must be from 1 to 10")
        defineplayer1()
    if speed1 < 1 or speed1 > 10:
        print("Speed must be from 1 to 10")
        defineplayer1()
    if stealth1 < 1 or stealth1 > 10:
        print("Stealth must be from 1 to 10")
        defineplayer1()
    if cunning1 < 1 or cunning1 > 10:
        print("Cunning must be from 1 to 10")
        defineplayer1()
    if charisma1 < 1 or charisma1 > 10:
        print("Charisma must be from 1 to 10")
        defineplayer1()
    if sanity1 < 1 or sanity1 > 10:
        print("Sanity must be from 1 to 10")
        defineplayer1()
    return

#Define Player 2:

def defineplayername2():
    global player2
    player2 = input("Enter name for the second player: ")
    return

def defineplayerstrength2():
    global strength2
    strength2 = int(input("Enter a strength for the second player (1-10): "))
    return

def defineplayervigilance2():
    global vigilance2
    vigilance2 = int(input("Enter a vigilance value for the second player (1-10): "))
    return

def defineplayerspeed2():
    global speed2
    speed2 = int(input("Enter a speed value for the second player (1-10): "))
    return

def defineplayerstealth2():
    global stealth2
    stealth2 = int(input("Enter a stealth value for the second player (1-10): "))
    return

def defineplayercunning2():
    global cunning2
    cunning2 = int(input("Enter a cunning value for the second player (1-10): "))
    return

def defineplayercharisma2():
    global charisma2
    charisma2 = int(input("Enter a charisma value for the second player (1-10): "))
    return

def defineplayersanity2():
    global sanity2
    sanity2 = int(input("Enter a sanity value for the second player (1-10): "))
    return

def defineplayer2():
    defineplayername2()
    defineplayerstrength2()
    defineplayervigilance2()
    defineplayerspeed2()
    defineplayerstealth2()
    defineplayercunning2()
    defineplayercharisma2()
    defineplayersanity2()
    if strength2 < 1 or strength2 > 10:
        print("Strength must be from 1 to 10")
        defineplayer2()
    if vigilance2 < 1 or vigilance2 > 10:
        print("Vigilance must be from 1 to 10")
        defineplayer2()
    if speed2 < 1 or speed2 > 10:
        print("Speed must be from 1 to 10")
        defineplayer2()
    if stealth2 < 1 or stealth2 > 10:
        print("Stealth must be from 1 to 10")
        defineplayer2()
    if cunning2 < 1 or cunning2 > 10:
        print("Cunning must be from 1 to 10")
        defineplayer2()
    if charisma2 < 1 or charisma2 > 10:
        print("Charisma must be from 1 to 10")
        defineplayer2()
    if sanity2 < 1 or sanity2 > 10:
        print("Sanity must be from 1 to 10")
        defineplayer2()
    return

#Define Player 3:

def defineplayername3():
    global player3
    player3 = input("Enter name for the third player: ")
    return

def defineplayerstrength3():
    global strength3
    strength3 = int(input("Enter a strength for the third player (1-10): "))
    return

def defineplayervigilance3():
    global vigilance3
    vigilance3 = int(input("Enter a vigilance value for the third player (1-10): "))
    return

def defineplayerspeed3():
    global speed3
    speed3 = int(input("Enter a speed value for the third player (1-10): "))
    return

def defineplayerstealth3():
    global stealth3
    stealth3 = int(input("Enter a stealth value for the third player (1-10): "))
    return

def defineplayercunning3():
    global cunning3
    cunning3 = int(input("Enter a cunning value for the third player (1-10): "))
    return

def defineplayercharisma3():
    global charisma3
    charisma3 = int(input("Enter a charisma value for the third player (1-10): "))
    return

def defineplayersanity3():
    global sanity3
    sanity3 = int(input("Enter a sanity value for the third player (1-10): "))
    return

def defineplayer3():
    defineplayername3()
    defineplayerstrength3()
    defineplayervigilance3()
    defineplayerspeed3()
    defineplayerstealth3()
    defineplayercunning3()
    defineplayercharisma3()
    defineplayersanity3()
    if strength3 < 1 or strength3 > 10:
        print("Strength must be from 1 to 10")
        defineplayer3()
    if vigilance3 < 1 or vigilance3 > 10:
        print("Vigilance must be from 1 to 10")
        defineplayer3()
    if speed3 < 1 or speed3 > 11:
        print("Speed must be from 1 to 10")
        defineplayer3()
    if stealth3 < 1 or stealth3 > 10:
        print("Stealth must be from 1 to 10")
        defineplayer3()
    if speed3 == 11:
        print("You found easter egg 2! (The Flash)")
    if cunning3 < 1 or cunning3 > 10:
        print("Cunning must be from 1 to 10:")
        defineplayer3()
    if charisma3 < 1 or charisma3 > 10:
        print("Charisma must be from 1 to 10:")
        defineplayer3()
    if sanity3 < 1 or sanity3 > 10:
        print("Sanity must be from 1 to 10:")
        defineplayer3()
    return

#Define Player 4

def defineplayername4():
    global player4
    player4 = input("Enter name for the fourth player: ")
    return

def defineplayerstrength4():
    global strength4
    strength4 = int(input("Enter a strength for the fourth player (1-10): "))
    return

def defineplayervigilance4():
    global vigilance4
    vigilance4 = int(input("Enter a vigilance value for the fourth player (1-10): "))
    return

def defineplayerspeed4():
    global speed4
    speed4 = int(input("Enter a speed value for the fourth player (1-10): "))
    return

def defineplayerstealth4():
    global stealth4
    stealth4 = int(input("Enter a stealth value for the fourth player (1-10): "))
    return

def defineplayercunning4():
    global cunning4
    cunning4 = int(input("Enter a cunning value for the fourth player (1-10): "))
    return

def defineplayercharisma4():
    global charisma4
    charisma4 = int(input("Enter a charisma value for the fourth player (1-10): "))
    return

def defineplayersanity4():
    global sanity4
    sanity4 = int(input("Enter a sanity value for the fourth player (1-10): "))
    return

def defineplayer4():
    defineplayername4()
    defineplayerstrength4()
    defineplayervigilance4()
    defineplayerspeed4()
    defineplayerstealth4()
    defineplayercunning4()
    defineplayercharisma4()
    defineplayersanity4()
    if strength4 < 1 or strength4 > 10:
        print("Strength must be from 1 to 10")
        defineplayer4()
    if vigilance4 < 1 or vigilance4 > 10:
        print("Vigilance must be from 1 to 10")
        defineplayer4()
    if speed4 < 1 or speed4 > 10:
        print("Speed must be from 1 to 10")
        defineplayer4()
    if stealth4 < 1 or stealth4 > 10:
        print("Stealth must be from 1 to 10")
        defineplayer4()
    if cunning4 < 1 or cunning4 > 10:
        print("Cunning must be from 1 to 10")
        defineplayer4()
    if charisma4 < 1 or charisma4 > 10:
        print("Charisma must be from 1 to 10")
        defineplayer4()
    if sanity4 < 1 or sanity4 > 10:
        print("Sanity must be from 1 to 10")
        defineplayer4()
    return

#Define Player 5:

def defineplayername5():
    global player5
    player5 = input("Enter name for the fifth player: ")
    return

def defineplayerstrength5():
    global strength5
    strength5 = int(input("Enter a strength for the fifth player (1-10): "))
    return

def defineplayervigilance5():
    global vigilance5
    vigilance5 = int(input("Enter a vigilance value for the fifth player (1-10): "))
    return

def defineplayerspeed5():
    global speed5
    speed5 = int(input("Enter a speed value for the fifth player (1-10): "))
    return

def defineplayerstealth5():
    global stealth5
    stealth5 = int(input("Enter a stealth value for the fifth player (1-10): "))
    return

def defineplayercunning5():
    global cunning5
    cunning5 = int(input("Enter a cunning value for the fifth player (1-10): "))
    return

def defineplayercharisma5():
    global charisma5
    charisma5 = int(input("Enter a charisma value for the fifth player (1-10): "))
    return

def defineplayersanity5():
    global sanity5
    sanity5 = int(input("Enter a sanity value for the fifth player (1-10): "))
    return

def defineplayer5():
    defineplayername5()
    defineplayerstrength5()
    defineplayervigilance5()
    defineplayerspeed5()
    defineplayerstealth5()
    defineplayercunning5()
    defineplayercharisma5()
    defineplayersanity5()
    if strength5 < 1 or strength5 > 11:
        print("Strength must be from 1 to 10")
        defineplayer5()
    if vigilance5 < 1 or vigilance5 > 10:
        print("Vigilance must be from 1 to 10")
        defineplayer5()
    if speed5 < 1 or speed5 > 11:
        print("Speed must be from 1 to 10")
        defineplayer5()
    if strength5 == 11 and speed5 ==11:
        print("You found easter egg 3! (The Terminator)")
    if stealth5 < 1 or stealth5 > 10:
        print("Stealth must be from 1 to 10")
        defineplayer5()
    if cunning5 < 1 or cunning5 > 10:
        print("Cunning must be from 1 to 10")
        defineplayer5()
    if charisma5 < 1 or charisma5 > 10:
        print("Cunning must be from 1 to 10")
        defineplayer5()
    if sanity5 < 1 or sanity5 > 10:
        print("Sanity must be from 1 to 10")
        defineplayer5()
    return

#Define Player 6:

def defineplayername6():
    global player6
    player6 = input("Enter name for the sixth player: ")
    return

def defineplayerstrength6():
    global strength6
    strength6 = int(input("Enter a strength for the sixth player (1-10): "))
    return

def defineplayervigilance6():
    global vigilance6
    vigilance6 = int(input("Enter a vigilance value for the sixth player (1-10): "))
    return

def defineplayerspeed6():
    global speed6
    speed6 = int(input("Enter a speed value for the sixth player (1-10): "))
    return

def defineplayerstealth6():
    global stealth6
    stealth6 = int(input("Enter a stealth value for the sixth player (1-10): "))
    return

def defineplayercunning6():
    global cunning6
    cunning6 = int(input("Enter a cunning value for the sixth player (1-10): "))
    return

def defineplayercharisma6():
    global charisma6
    charisma6 = int(input("Enter a charisma value for the sixth player (1-10): "))
    return

def defineplayersanity6():
    global sanity6
    sanity6 = int(input("Enter a sanity value for the sixth player (1-10): "))
    return

def defineplayer6():
    defineplayername6()
    defineplayerstrength6()
    defineplayervigilance6()
    defineplayerspeed6()
    defineplayerstealth6()
    defineplayercunning6()
    defineplayercharisma6()
    defineplayersanity6()
    if strength6 < 1 or strength6 > 10:
        print("Strength must be from 1 to 10")
        defineplayer6()
    if vigilance6 < 1 or vigilance6 > 10:
        print("Vigilance must be from 1 to 10")
        defineplayer6()
    if speed6 < 1 or speed6 > 10:
        print("Speed must be from 1 to 10")
        defineplayer6()
    if stealth6 < 1 or stealth6 > 10:
        print("Stealth must be from 1 to 10")
        defineplayer6()
    if cunning6 < 1 or cunning6 > 10:
        print("Cunning must be from 1 to 10")
        defineplayer6()
    if charisma6 < 1 or charisma6 > 10:
        print("Charisma must be from 1 to 10")
        defineplayer6()
    if sanity6 < 1 or sanity6 > 10:
        print("Sanity must be from 1 to 10")
        defineplayer6()
    return

#Define Player 7:

def defineplayername7():
    global player7
    player7 = input("Enter name for the seventh player: ")
    return

def defineplayerstrength7():
    global strength7
    strength7 = int(input("Enter a strength for the seventh player (1-10): "))
    return

def defineplayervigilance7():
    global vigilance7
    vigilance7 = int(input("Enter a vigilance value for the seventh player (1-10): "))
    return

def defineplayerspeed7():
    global speed7
    speed7 = int(input("Enter a speed value for the seventh player (1-10): "))
    return

def defineplayerstealth7():
    global stealth7
    stealth7 = int(input("Enter a stealth value for the seventh player (1-10): "))
    return

def defineplayercunning7():
    global cunning7
    cunning7 = int(input("Enter a cunning value for the seventh player (1-10): "))
    return

def defineplayercharisma7():
    global charisma7
    charisma7 = int(input("Enter a charisma value for the seventh player (1-10): "))
    return

def defineplayersanity7():
    global sanity7
    sanity7 = int(input("Enter a sanity value for the seventh player (1-10): "))
    return

def defineplayer7():
    defineplayername7()
    defineplayerstrength7()
    defineplayervigilance7()
    defineplayerspeed7()
    defineplayerstealth7()
    defineplayercunning7()
    defineplayercharisma7()
    defineplayersanity7()
    if strength7 < 1 or strength7 > 10:
        print("Strength must be from 1 to 10")
        defineplayer7()
    if vigilance7 < 1 or vigilance7 > 10:
        print("Vigilance must be from 1 to 10")
        defineplayer7()
    if speed7 < 1 or speed7 > 10:
        print("Speed must be from 1 to 10")
        defineplayer7()
    if stealth7 < 1 or stealth7 > 10:
        print("Stealth must be from 1 to 10")
        defineplayer7()
    if cunning7 < 1 or cunning7 > 10:
        print("Cunning must be from 1 to 10")
        defineplayer7()
    if charisma7 < 1 or charisma7 > 10:
        print("Charisma must be from 1 to 10")
        defineplayer7()
    if sanity7 < 1 or sanity7 > 10:
        print("Sanity must be from 1 to 10")
    return

#Begin Game:

if advancedsetup == 0:
    numberofstartingplayers = 7

import random

global strength1
global strength2
global strength3
global strength4
global strength5
global strength6
global strength7
global vigilance1
global vigilance2
global vigilance3
global vigilance4
global vigilance5
global vigilance6
global vigilance7
global speed1
global speed2
global speed3
global speed4
global speed5
global speed6
global speed7
global stealth1
global stealth2
global stealth3
global stealth4
global stealth5
global stealth6
global stealth7
global cunning1
global cunning2
global cunning3
global cunning4
global cunning5
global cunning6
global cunning7
global charisma1
global charisma2
global charisma3
global charisma4
global charisma5
global charisma6
global charisma7
global sanity1
global sanity2
global sanity3
global sanity4
global sanity5
global sanity6
global sanity7

if numberofstartingplayers > 0:
    if randomizetraits == 1:
        defineplayername1()
        strength1 = random.randint(1,10)
        vigilance1 = random.randint(1,10)
        speed1 = random.randint(1,10)
        stealth1 = random.randint(1,10)
        cunning1 = random.randint(1,10)
        charisma1 = random.randint(1,10)
        sanity1 = random.randint(1,10)
    else:
        defineplayer1()
        print("")
if numberofstartingplayers > 1:
    if randomizetraits == 1:
        defineplayername2()
        strength2 = random.randint(1,10)
        vigilance2 = random.randint(1,10)
        speed2 = random.randint(1,10)
        stealth2 = random.randint(1,10)
        cunning2 = random.randint(1,10)
        charisma2 = random.randint(1,10)
        sanity2 = random.randint(1,10)
    else:
        defineplayer2()
        print("")
if numberofstartingplayers > 2:
    if randomizetraits == 1:
        defineplayername3()
        strength3 = random.randint(1,10)
        vigilance3 = random.randint(1,10)
        speed3 = random.randint(1,10)
        stealth3 = random.randint(1,10)
        cunning3 = random.randint(1,10)
        charisma3 = random.randint(1,10)
        sanity3 = random.randint(1,10)
    else:
        defineplayer3()
        print("")
if numberofstartingplayers > 3:
    if randomizetraits == 1:
        defineplayername4()
        strength4 = random.randint(1,10)
        vigilance4 = random.randint(1,10)
        speed4 = random.randint(1,10)
        stealth4 = random.randint(1,10)
        cunning4 = random.randint(1,10)
        charisma4 = random.randint(1,10)
        sanity4 = random.randint(1,10)
    else:
        defineplayer4()
        print("")
if numberofstartingplayers > 4:
    if randomizetraits == 1:
        defineplayername5()
        strength5 = random.randint(1,10)
        vigilance5 = random.randint(1,10)
        speed5 = random.randint(1,10)
        stealth5 = random.randint(1,10)
        cunning5 = random.randint(1,10)
        charisma5 = random.randint(1,10)
        sanity5 = random.randint(1,10)
    else:
        defineplayer5()
        print("")
if numberofstartingplayers > 5:
    if randomizetraits == 1:
        defineplayername6()
        strength6 = random.randint(1,10)
        vigilance6 = random.randint(1,10)
        speed6 = random.randint(1,10)
        stealth6 = random.randint(1,10)
        cunning6 = random.randint(1,10)
        charisma6 = random.randint(1,10)
        sanity6 = random.randint(1,10)
    else:
        defineplayer6()
        print("")
if numberofstartingplayers > 6:
    if randomizetraits == 1:
        defineplayername7()
        strength7 = random.randint(1,10)
        vigilance7 = random.randint(1,10)
        speed7 = random.randint(1,10)
        stealth7 = random.randint(1,10)
        cunning7 = random.randint(1,10)
        charisma7 = random.randint(1,10)
        sanity7 = random.randint(1,10)
    else:
        defineplayer7()
        print("")

numberofaliveplayers = numberofstartingplayers

print("The game begins...")
input("")

global statcheckcounter
statcheckcounter = 0
def dostatcheck():
    global statcheckcounter
    if player1dead == 0 and numberofstartingplayers > 0:
        print(player1, "strength:", strength1)
        print(player1, "vigilance:", vigilance1)
        print(player1, "speed:", speed1)
        print(player1, "stealth:", stealth1)
        print(player1, "cunning:", cunning1)
        print(player1, "charisma:", charisma1)
        print(player1, "sanity:", sanity1)
    if player2dead == 0 and numberofstartingplayers > 1:
        print(player2, "strength:", strength2)
        print(player2, "vigilance:", vigilance2)
        print(player2, "speed:", speed2)
        print(player2, "stealth:", stealth2)
        print(player2, "cunning:", cunning2)
        print(player2, "charisma:", charisma2)
        print(player2, "sanity:", sanity2)
    if player3dead == 0 and numberofstartingplayers > 2:
        print(player3, "strength:", strength3)
        print(player3, "vigilance:", vigilance3)
        print(player3, "speed:", speed3)
        print(player3, "stealth:", stealth3)
        print(player3, "cunning:", cunning3)
        print(player3, "charisma:", charisma3)
        print(player3, "sanity:", sanity3)
    if player4dead == 0 and numberofstartingplayers > 3:
        print(player4, "strength:", strength4)
        print(player4, "vigilance:", vigilance4)
        print(player4, "speed:", speed4)
        print(player4, "stealth:", stealth4)
        print(player4, "cunning:", cunning4)
        print(player4, "charisma:", charisma4)
        print(player4, "sanity:", sanity4)
    if player5dead == 0 and numberofstartingplayers > 4:
        print(player5, "strength:", strength5)
        print(player5, "vigilance:", vigilance5)
        print(player5, "speed:", speed5)
        print(player5, "stealth:", stealth5)
        print(player5, "cunning:", cunning5)
        print(player5, "charisma:", charisma5)
        print(player5, "sanity:", sanity5)
    if player6dead == 0 and numberofstartingplayers > 5:
        print(player6, "strength:", strength6)
        print(player6, "vigilance:", vigilance6)
        print(player6, "speed:", speed6)
        print(player6, "stealth:", stealth6)
        print(player6, "cunning:", cunning6)
        print(player6, "charisma:", charisma6)
        print(player6, "sanity:", sanity6)
    if player7dead == 0 and numberofstartingplayers > 6:
        print(player7, "strength:", strength7)
        print(player7, "vigilance:", vigilance7)
        print(player7, "speed:", speed7)
        print(player7, "stealth:", stealth7)
        print(player7, "cunning:", cunning7)
        print(player7, "charisma:", charisma7)
        print(player7, "sanity:", sanity7)
    input("Press any key to continue.")
    print("")
    statcheckcounter = statcheckcounter + 1
    if statcheckcounter == 91:
        print("You found easter egg 5! (Statistician)")
    return

#Encounter List:

def createrumor():
    global rumornumber
    global rumor
    rumornumber = random.randint(0,13)
    if rumornumber == 0:
        rumor = "is a possessed demon that eats puppies"
    if rumornumber == 1:
        rumor = "is secretly a doppelganger"
    if rumornumber == 2:
        rumor = "is the dictator of Bulgaria"
    if rumornumber == 3:
        rumor = "is an alien"
    if rumornumber == 4:
        rumor = "doesn't like pinapple on pizza"
    if rumornumber == 5:
        rumor = "is only a figment of the collective imagination"
    if rumornumber == 6:
        rumor = "ISN'T REAL"
    if rumornumber == 7:
        rumor = "is represented by a bianary number"
    if rumornumber == 8:
        rumor = "owns a dragon named Gus who burned down an entire village"
    if rumornumber == 9:
        rumor = "has never eaten cookies, and must therefore be a terrible person"
    if rumornumber == 10:
        rumor = "killed someone"
    if rumornumber == 11:
        rumor = "knew Ghengis Khan personally"
    if rumornumber == 12:
        rumor = "is a weakling"
    if rumornumber == 13:
        rumor = "is actually a halfway decent person"

def createalliancename():
    global alliancenumber
    global alliancename
    alliancenumber = random.randint(0, 13)
    if alliancenumber == 0:
        alliancename = "THE CULT OF THE RABBIT"
    if alliancenumber == 1:
        alliancename = "THE SYNDICATE"
    if alliancenumber == 2:
        alliancename = "THE BULGARIAN ARMY"
    if alliancenumber == 3:
        alliancename = "THE PIZZA DELIVERY-MEN"
    if alliancenumber == 4:
        alliancename = "THE JELLY BEANS"
    if alliancenumber == 5:
        alliancename = "THE ALLIANCE THAT REALLY NEEDED TO COME UP WITH A BETTER NAME"
    if alliancenumber == 6:
        alliancename = "THE ILLUMINATI"
    if alliancenumber == 7:
        alliancename = "THE DERANGED FISHERMEN"
    if alliancenumber == 8:
        alliancename = "THE JUSTICE LEAGUE"
    if alliancenumber == 9:
        alliancename = "THE FERRETS"
    if alliancenumber == 10:
        alliancename = "THE AVENGERS OF THE FALLEN TURTLE"
    if alliancenumber == 11:
        alliancename = "THE CULT OF SPAGHETTI"
    if alliancenumber == 12:
        alliancename = "THE FORKMEN"
    if alliancenumber == 13:
        alliancename = "THE DRAGON-RIDERS"

def encounter0():
    global activestrength1
    print(activeplayer1 + " finds a medical kit hidden in the arena.")
    activestrength1 = activestrength1 + 1
    statcheck = input("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter1():
    global activestrength1
    global numberofaliveplayers
    global activeplayer1dead
    print(activeplayer1 + " runs into a prickly thorn bush.")
    activestrength1 = activestrength1 - 1
    if activestrength1 < 1:
        print (activeplayer1 + " bleeds out from his wounds.")
        numberofaliveplayers = numberofaliveplayers - 1
        activeplayer1dead = 1
        print ("Remaining players:", numberofaliveplayers)
    statcheck = input("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter2():                                                
    global activestrength2
    global activeplayer2dead
    global numberofaliveplayers
    print(activeplayer1 + " and " + activeplayer2 + " meet one another in the forest. " + activeplayer1 + " attacks " + activeplayer2 +
          ", assaulting him with a large stick he finds on the ground.")
    activestrength2 = activestrength2 - 2
    if activestrength2 < 1:
        print (activeplayer2 + " dies from a concussion caused by the attack.")
        numberofaliveplayers = numberofaliveplayers - 1
        activeplayer2dead = 1
        print ("Remaining players:", numberofaliveplayers)
    statcheck = input("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return


def encounter3():
    global activevigilance1
    print(activeplayer1, "has a near miss with a steep cliff edge. He vows to be more careful in the future.")
    activevigilance1 = activevigilance1 + 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter4():
    global activevigilance1
    print ("The bright sun glares in ", activeplayer1, "'s eyes.", sep="")
    activevigilance1 = activevigilance1 - 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter5():
    global activevigilance1
    print(activeplayer1, " hides in a sandy depression and ambushes ", activeplayer2,
          ". They tussle, and ", activeplayer2, " manages to escape by throwing sand into ", activeplayer1, "'s eyes, blinding him.", sep="")
    activevigilance1 = activevigilance1 - 2
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter6():
    global activevigilance1
    global activestrength1
    global numberofaliveplayers
    global activeplayer1dead
    if activevigilance1 < 1:
        print (activeplayer1, " unknowingly stumbles upon a bear's cave. The bear attacks, mauling and killing", activeplayer1, ".", sep="")
        numberofaliveplayers = numberofaliveplayers - 1
        activeplayer1dead = 1
        print ("Remaining players:", numberofaliveplayers)
    else:
        print (activeplayer1, "finds a cave. However, after noticing the large bear tracks nearby, he decides not to enter.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter7():
    global activevigilance1
    global activestrength1
    global numberofaliveplayers
    global activeplayer1dead
    if activevigilance1 < 4:
        print (activeplayer1, "takes a tumble off of a steep hill, hitting his head on a rock.")
        activestrength1 = activestrength1 - 3
        if activestrength1 < 1:
            print ("He does not get up.")
            numberofaliveplayers = numberofaliveplayers - 1
            activeplayer1dead = 1
            print ("Remaining players:", numberofaliveplayers)
    else:
        print (activeplayer1, "very nearly falls down a steep hill, barely catching himself.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter8():
    global activevigilance1
    global activestrength1
    global numberofaliveplayers
    global activeplayer1dead
    if activevigilance1 < 7:
        print (activeplayer1, "traipses through the forest, oblivious to his surroundings. He accidentally disturbs a beehive, and is swarmed by bees.")
        activestrength1 = activestrength1 - 1
        if activestrength1 < 1:
            print (activeplayer1, "is evidentally allergic to bee stings.")
            numberofaliveplayers = numberofaliveplayers - 1
            activeplayer1dead = 1
            print("Remaining players:", numberofaliveplayers)
    else:
        print (activeplayer1, "notices a beehive, and gives it a wide berth.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter9():
    global activevigilance1
    global activestrength1
    global numberofaliveplayers
    global activeplayer1dead
    if activevigilance1 < 10:
        print (activeplayer1, "unknowingly consumes poisonous berries. He spends the next hour vomiting the contents of his stomach.")
        activestrength1 = activestrength1 - 1
        if activestrength1 < 1:
            print (activeplayer1, "is too weak to continue, and eventually dies.")
            numberofaliveplayers = numberofaliveplayers - 1
            activeplayer1dead = 1
            print("Remaining players:", numberofaliveplayers)
    else:
        print (activeplayer1, "searches for food. He carefully sorts out which barries are poisonous so that he doesn't get sick.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter10():
    global activespeed1
    print (activeplayer1, "finds a pair of sturdy boots hidden in the arena.")
    activespeed1 = activespeed1 + 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter11():
    global activespeed1
    print (activeplayer1, "trips on an exposed tree root and twists his ankle.")
    activespeed1 = activespeed1 - 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter12():
    global activespeed2
    print (activeplayer1, " smashes ", activeplayer2, "'s leg with a large rock.", sep="")
    activespeed2 = activespeed2 - 2
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter13():
    global activespeed1
    global numberofaliveplayers
    global activeplayer1dead
    if activespeed1 < 1:
        print (activeplayer1, "is chased by a pack of wolves."
               " He is not quick enough to escape, and is hunted down and torn to shreds by the hungry pack.")
        numberofaliveplayers = numberofaliveplayers - 1
        activeplayer1dead = 1
        print ("Remaining players:",numberofaliveplayers)

    else:
        print (activeplayer1, "is chased by a pack of wolves."
               " He barely escapes by sprinting to climb a tall tree and waiting for the wolves to move on.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter14():
    global activespeed1
    global activestrength1
    global activeplayer1dead
    global numberofaliveplayers
    print(activeplayer1, "is chased through the forest by a wild boar.")
    if activespeed1 < 4:
        print("The boar gores", activeplayer1, "with its tusks.")
        activestrength1 = activestrength1 - 3
        if activestrength1 < 1:
            print(activeplayer1, "dies from his wounds.")
            activeplayer1dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter15():
    global activespeed1
    global activestrength1
    global numberofaliveplayers
    global activeplayer1dead
    if activespeed1 < 7:
        print (activeplayer1, "sees", activeplayer2, "and runs away in fear.", activeplayer2, "chases him down and attacks him with a large stick.")
        activestrength1 = activestrength1 - 3
        if activestrength1 < 1:
            print (activeplayer1, " dies to the onslaught of ", activeplayer2, ".", sep="")
            numberofaliveplayers = numberofaliveplayers - 1
            activeplayer1dead = 1
            print ("Remaining players:", numberofaliveplayers)
    else:
        print (activeplayer2, "chases", activeplayer1, "intending to kill him.", activeplayer1, "is fast enough to escape.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter16():
    global activespeed1
    global activestrength1
    global activeplayer1dead
    global numberofaliveplayers
    print(activeplayer1, "is walking through the forest, when suddenly he hears a loud snapping sound. He looks up to see the branch of a dead tree",
          "plummeting towards him.")
    if activespeed1 < 10:
        activestrength1 = activestrength1 - 1
        if activestrength1 > 1:
            print(activeplayer1, "leaps to the side to narrowly avoid getting clobbered by the branch. However, he badly scrapes his arm in the process.")
        else:
            print(activeplayer1, "is crushed into a fine pulp by the falling branch.")
            activeplayer1dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
    else:
        print(activeplayer1, "rolls under the branch into a flying somersault, expertly twisting between two tree limbs and landing in a perfect crouch.",
              "He calmly stands, brushes a bit of dust off of the collar of his cloak, and continues on.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter17():
    global activestealth1
    print (activeplayer1, "smudges his clothes and face with dirt, leaves, and grime, so that he blends in with the undergrowth.")
    activestealth1 = activestealth1 + 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter18():
    global activestealth1
    print(activeplayer1, "steps in a mud puddle. Now, his boots make loud shlopping noises every time he takes a step.")
    activestealth1 = activestealth1 - 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter19():
    global activestealth1
    print(activeplayer1, "'s favorite hiding spot is discovered by the other players.", sep= "")
    activestealth1 = activestealth1 - 2
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter20():
    global activestealth1
    global activeplayer1dead
    global numberofaliveplayers
    if activestealth1 < 1:
        print(activeplayer1, " attempts to sneak into ", activeplayer2, "'s camp in the night. ", activeplayer2,
              ", however, was only pretending to be asleep. He leaps up and tackles ", activeplayer1, " strangling him to death.", sep= "")
        activeplayer1dead = 1
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
    else:
        print(activeplayer1, "quietly slips past", activeplayer2, "while he is sleeping.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter21():
    global activestealth1
    global activestrength2
    global activeplayer2dead
    global numberofaliveplayers
    if activestealth1 < 4:
        print(activeplayer1, "attempts to steal from", activeplayer2, "in the night. However,", activeplayer2, "wakes up, and", activeplayer1,
            "is forced to flee.")
    else:
        activestrength2 = activestrength2 - 1
        if activestrength2 < 1:
            print(activeplayer1, "slits the throat of", activeplayer2, "in the dead of night.")
            activeplayer2dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        else:
            print(activeplayer1, "steals medical supplies from", activeplayer2)
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter22():
    global activestealth1
    global activestrength2
    global activeplayer2dead
    global numberofaliveplayers
    if activestealth1 < 7:
        print(activeplayer1, "attempts to ambush", activeplayer2, "but is unsuccessful.")
    else:
        activestrength2 = activestrength2 - 1
        if activestrength2 < 1:
            print(activeplayer1, " leaps out from behind a bush and attacks ", activeplayer2, ". ", activeplayer2, " dies from sheer surprise.", sep="")
            activeplayer2dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        else:
            print(activeplayer1, "ambushes", activeplayer2, "by leaping from a tree and tackling him.", activeplayer2, "is wounded, but escapes.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter23():
    global activestealth1
    global activestrength2
    global activeplayer2dead
    global numberofaliveplayers
    if activestealth1 < 10:
        print(activeplayer1, "falls down a hole.")
    else:
        activestrength2 = activestrength2 - 3
        if activestrength2 < 1:
            print(activeplayer1, "spends five hours hiding in the tall grass near the edge of a rocky incline.",
                  "Finally, someone appears;", activeplayer2,
                  "emerges from the trees nearby and stands near the edge of the slope, looking out at the lake below.",
                  activeplayer1, "leaps forward, shoving", activeplayer2, "over the edge.", activeplayer2, "drowns.")
            activeplayer2dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        else:
            print(activeplayer1, "sneaks up on", activeplayer2, "and slaps him in the face with a dead fish.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter24():
    global activecunning1
    print (activeplayer1, "sits down on a rock to scheme. He begins to draw a complex diagram with a stick in the dirt, and laughs quietly to himself.")
    activecunning1 = activecunning1 + 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter25():
    global activecunning1
    print (activeplayer1, "has not been able to find water for quite some time. He begins to go delerious from dehydration.")
    activecunning1 = activecunning1 - 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter26():
    global activecunning1
    global activestrength2
    global numberofaliveplayers
    global activeplayer2dead
    if activecunning1 > 1:
        print(activeplayer1, "carefully constructs a pit trap. The manuever is successful;", activeplayer2, "falls into the trap and is seriously wounded.")
        activecunning1 = activecunning1 - 2
        activestrength2 = activestrength2 - 3
        if activestrength2 < 1:
            print(activeplayer1, "finds", activeplayer2, "stuck in the trap and finishes the job.")
            numberofaliveplayers = numberofaliveplayers - 1
            activeplayer2dead = 1
            print("Remaining players:", numberofaliveplayers)
    else:
        print(activeplayer1, "wants to make a pit trap, but can't figure out how to dig a hole.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter27():
    global activecunning1
    global activestrength2
    global numberofaliveplayers
    global activeplayer2dead
    if activecunning1 > 1:
        print(activeplayer1, "lures", activeplayer2, "into a pirhanna-infested lake.")
        activecunning1 = activecunning1 - 2
        activestrength2 = activestrength2 - 3
        if activestrength2 < 1:
            print(activeplayer2, "is very tasty.")
            numberofaliveplayers = numberofaliveplayers - 1
            activeplayer2dead = 1
            print("Remaining players:", numberofaliveplayers)
    else:
        print(activeplayer1, "tries to lure", activeplayer2, "into a pirhanna-infested lake, but fails.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter28():
    global activecunning1
    global activestrength2
    global numberofaliveplayers
    global activeplayer2dead
    if activecunning1 > 1:
        print(activeplayer1, "intentionally harvests poisoned barries, then leaves them in a basket.",
              activeplayer2, "finds the barries and eats them, then falls extremely ill.")
        activecunning1 = activecunning1 - 2
        activestrength2 = activestrength2 - 3
        if activestrength2 < 1:
            print(activeplayer2, "dies from poisoning.")
            numberofaliveplayers = numberofaliveplayers - 1
            activeplayer2dead = 1
            print("Remaining players:", numberofaliveplayers)
    else:
        print(activeplayer1, "thought of a really cool idea, but then forgot it.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print ("")
    return

def encounter29():
    global activecharisma1
    print(activeplayer1, "stands on a hilltop, silhouetted by the setting sun, as his long, gorgeous hair billows in the wind.")
    activecharisma1 = activecharisma1 + 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter30():
    global activecharisma1
    print(activeplayer1, "steps on a baby rabbit, crushing it.", activeplayer2, "witnesses the tragedy, and shakes his head in disgust.")
    activecharisma1 = activecharisma1 - 1
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter31():
    global activecharisma1
    global activestrength1
    if activecharisma1 > 1:
        print(activeplayer1, "recieves a gift from an unknown benefactor. Inside he finds clean bandages.")
        activestrength1 = activestrength1 + 1
        activecharisma1 = activecharisma1 - 2
    else:
        print(activeplayer1, "recieves a gift from an unknown benefactor. Inside he finds a dirty sock.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter32():
    global activecharisma1
    global activevigilance1
    if activecharisma1 > 1:
        print(activeplayer1, "recieves a wrapped package from an unknown benefactor. Inside he finds a walking stick, a device",
              "useful for regaining one's footing and poking mysterious objects from a safe distance.")
        activevigilance1 = activevigilance1 + 1
        activecharisma1 = activecharisma1 - 2
    else:
        print(activeplayer1, "recieves a wrapped package from an unkown benefactor. Inside he finds half a dozen rotten, putrid-smelling potatoes.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter33():
    global activecharisma1
    global activespeed1
    if activecharisma1 > 1:
        print(activeplayer1, "recieves a small parcel from an unknown benefactor. Inside he finds a pair of running shoes.")
        activespeed1 = activespeed1 + 1
        activecharisma1 = activecharisma1 - 2
    else:
        print(activeplayer1, "recieves a small parcel from an unknown benefactor. Inside he finds a curved stone with the words \"R.I.P.",
              activeplayer1, "\"")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter34():
    global activecharisma1
    global activestealth1
    if activecharisma1 > 1:
        print(activeplayer1, "recieves a wooden box from an unknown benefactor. Inside he finds a dark cloak, which makes him harder to spot at night.")
        activestealth1 = activestealth1 + 1
        activecharisma1 = activecharisma1 - 2
    else:
        print(activeplayer1, "recieves a wooden box from an unknown benefactor. Inside he finds a live snake, which he runs away from in terror.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter35():
    global activecharisma1
    global activecunning1
    if activecharisma1 > 1:
        print(activeplayer1, "recieves a small box from an unknown benefactor. Inside he finds a sealed envelope, which he opens and reads.",
              "He glances furitively around, then chuckles ominously, slipping the envelope into his belt and slinking off into the woods.")
        activecunning1 = activecunning1 + 1
        activecharisma1 = activecharisma1 - 2
    else:
        print(activeplayer1, "recieves a small box from an unknown benefactor. Inside he finds... absolutely nothing.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter36():
    global activecharisma1
    global activesanity1
    if activecharisma1 > 1:
        print(activeplayer1, "recieves an envelope containing a slip of paper from an unknown benefactor.",
              "Inside he finds a photo of someone very dear to him.")
        activesanity1 = activesanity1 + 1
        activecharisma1 = activecharisma1 -2
    else:
        print(activeplayer1, "recieves an envelope containing a slip of paper from an unknown benefactor.",
              "Inside he finds a note informing him that his house has been confiscated because his payment is two weeks overdue.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter37():
    global activesanity1
    print(activeplayer1, "is convinced that someone is following him. He is becoming more and more paranoid.")
    activesanity1 = activesanity1 - 1
    if activesanity1 < 1:
        print(activeplayer1, "has been driven INSANE...")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter38():
    global activesanity1
    print(activeplayer1, "comes frighteningly close to stepping on a snake. His nerves are badly shaken.")
    activesanity1 = activesanity1 - 2
    if activesanity1 < 1:
        print(activeplayer1, "has been driven INSANE...")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter39():
    global activedeadplayer
    global activesanity1
    if activedeadplayer == 1:
        print("As a cold wind blows through the trees, ", activeplayer1, " swears he can hear laughter. It almost sounds like ", activedeadplayername,
              "...", sep="")
        activesanity1 = activesanity1 - 1
        if activesanity1 < 1:
            print(activeplayer1, "has been driven INSANE...")
    else:
        print(activeplayer1, "listens to birds chirping in the trees. It makes him smile.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter40():
    global activedeadplayer
    global activesanity1
    if activedeadplayer == 1:
        print(activeplayer1, "stumbles upon the rotting corpse of", activedeadplayername)
        activesanity1 = activesanity1 - 2
        if activesanity1 < 1:
            print(activeplayer1, "has been driven INSANE...")
    else:
        print(activeplayer1, "stumbles upon a bunch of bright red tulips growing in a grassy field. He stops to pick one up, and gently tucks it into",
              "his shirt.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter41():
    global activedeadplayer
    global activesanity1
    if activedeadplayer == 1:
        print(activeplayer1, "is haunted by the ghost of", activedeadplayername, "and is slowly being driven mad.")
        activesanity1 = activesanity1 - 3
        if activesanity1 < 1:
            print(activeplayer1, "has been driven INSANE...")
    else:
        print(activeplayer1, "remembers his family at home. The thought of them drives him onward as he continues to search for food and supplies.")
    statcheck = input ("Press any key to continue.")
    if statcheck == "1":
        dostatcheck()
    print("")
    return

def encounter42through48():
    global activesanity1
    global activestrength1
    global activestrength2
    global activeplayer1dead
    global activeplayer2dead
    global numberofaliveplayers
    if activesanity1 < 1:
        print(activeplayer1, "is INSANE. He madly rushes at", activeplayer2, "wildly punching, kicking, and screaming at the top of his lungs.")
        activestrength1 = activestrength1 - 2
        activestrength2 = activestrength2 - 2
        if activestrength1 < 1 and activestrength2 > 0:
            print(activeplayer2, " manages to fend off ", activeplayer1, ". ", activeplayer1, " dies soon after from his wounds.", sep="")
            activeplayer1dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        if activestrength1 > 0 and activestrength2 < 1:
            print(activeplayer2, "is strangled to death.")
            activeplayer2dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        if activestrength1 < 1 and activestrength2 < 1:
            print(activeplayer1, "beats", activeplayer2, "to death, but sustains so many wounds that he dies soon afterwards.")
            activeplayer1dead = 1
            activeplayer2dead = 1
            numberofaliveplayers = numberofaliveplayers - 2
            print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter49through55():
    global activesanity1
    global activevigilance1
    global activevigilance2
    global activeplayer1dead
    global activeplayer2dead
    global numberofaliveplayers
    if activesanity1 < 1:
        print(activeplayer1, " is INSANE. He tackles " , activeplayer2,
              ", picking him up, lifting him over his head, and running toward a nearby cliff edge.", sep="")
        activevigilance1 = activevigilance1 - 2
        activevigilance2 = activevigilance2 - 2
        if activevigilance1 < 1 and activevigilance2 > 0:
            print(activeplayer2, "barely scrambles free of", activeplayer1, "who continues running right over the edge of the cliff.")
            activeplayer1dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        if activevigilance1 > 0 and activevigilance2 < 1:
            print(activeplayer1, "throws", activeplayer2, "over the edge of the cliff.")
            activeplayer2dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        if activevigilance1 < 1 and activevigilance2 < 1:
            print(activeplayer2, "can't get free in time. Both", activeplayer1, "and", activeplayer2, "go tumbling over the edge of the cliff.")
            activeplayer1dead = 1
            activeplayer2dead = 1
            numberofaliveplayers = numberofaliveplayers - 2
            print("Remaining players:", numberofaliveplayers)
        if activevigilance1 > 0 and activevigilance2 > 0:
            print(activeplayer2, " escapes from ", activeplayer1, "'s grip. ", activeplayer1,
                  " skids to a stop, looking around in confusion as ", activeplayer2, " escapes.", sep="")
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter56through62():
    global activesanity1
    global activespeed1
    global activespeed2
    global activeplayer1dead
    global activeplayer2dead
    global numberofaliveplayers
    if activesanity1 < 1:
        print(activeplayer1, "is INSANE. He runs screaming after", activeplayer2, "and both of them tumble into a raging river.")
        activespeed1 = activespeed1 - 2
        activespeed2 = activespeed2 - 2
        if activespeed1 < 1:
            print(activeplayer1, "drowns.")
            activeplayer1dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        else:
            print(activeplayer1, "escapes the current.")
        if activespeed2 < 1:
            print(activeplayer2, "drowns.")
            activeplayer2dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        else:
            print(activeplayer2, "escapes the current.")
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter63():
    global activedeadplayer
    global randomdeadplayer
    global strength1
    global strength2
    global strength3
    global strength4
    global strength5
    global strength6
    global strength7
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if activedeadplayer == 1:
        if randomdeadplayer == 1:
            print(player1, "was only faking his death! He has returned, and is hunting his enemies...")
            player1dead = 0
            strength1 = 1
            numberofaliveplayers = numberofaliveplayers + 1
            print("Remaining players:", numberofaliveplayers)
        if randomdeadplayer == 2:
            print(player2, "was only faking his death! He has returned, and is hunting his enemies...")
            player2dead = 0
            strength2 = 1
            numberofaliveplayers = numberofaliveplayers + 1
            print("Remaining players:", numberofaliveplayers)
        if randomdeadplayer == 3:
            print(player3, "was only faking his death! He has returned, and is hunting his enemies...")
            player3dead = 0
            strength3 = 1
            numberofaliveplayers = numberofaliveplayers + 1
            print("Remaining players:", numberofaliveplayers)
        if randomdeadplayer == 4:
            print(player4, "was only faking his death! He has returned, and is hunting his enemies...")
            player4dead = 0
            strength4 = 1
            numberofaliveplayers = numberofaliveplayers + 1
            print("Remaining players:", numberofaliveplayers)
        if randomdeadplayer == 5:
            print(player5, "was only faking his death! He has returned, and is hunting his enemies...")
            player5dead = 0
            strength5 = 1
            numberofaliveplayers = numberofaliveplayers + 1
            print("Remaining players:", numberofaliveplayers)
        if randomdeadplayer == 6:
            print(player6, "was only faking his death! He has returned, and is hunting his enemies...")
            player6dead = 0
            strength6 = 1
            numberofaliveplayers = numberofaliveplayers + 1
            print("Remaining players:", numberofaliveplayers)
        if randomdeadplayer == 7:
            print(player7, "was only faking his death! He has returned, and is hunting his enemies...")
            player7dead = 0
            strength7 = 1
            numberofaliveplayers = numberofaliveplayers + 1
            print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
    return

def encounter64():
    global revengeplot
    global strength1
    global activeplayer1dead
    global numberofaliveplayers
    if revengeplot == 0:
        print(activeplayer1, "challenges", activeplayer2, "to a duel.", activeplayer2, "accepts, and easily bests", activeplayer1, "in the fight.")
        strength1 = strength1 - 3
        if strength1 < 1:
            print(activeplayer1, "'s wounds get infected, and he dies soon afterward.", sep="")
            activeplayer1dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        else:
            print(activeplayer2, "leaves", activeplayer1, "to die.")
            revengeplot = 1
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter65():
    global revengeplot
    global vigilance1
    if revengeplot == 0:
        print(activeplayer2, " slashes ", activeplayer1, "'s eye out. ", activeplayer1, " slinks off, badly wounded, yet already planning his revenge...",
              sep="")
        vigilance1 = vigilance1 - 3
        revengeplot = 1
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter66():
    global revengeplot
    global speed1
    if revengeplot == 0:
        print(activeplayer1, "chases", activeplayer2, "through the forest. He almost catches his quarry, but he stubs his foot on a tree root and falls.",
              activeplayer1, "blames", activeplayer2, "for his stubbed toe, and begins to plot his revenge...")
        speed1 = speed1 - 3
        revengeplot = 1
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter67():
    global revengeplot
    global stealth1
    if revengeplot == 0:
        print(activeplayer1, "finds a cave, and decides to wait in it so that he can ambush the other players.",
              "However, before he can execute his plan,", activeplayer2, "spots him and warns the other players of his plot.",
              activeplayer1, "does not plan to let this insult go unpunished...")
        stealth1 = stealth1 - 3
        revengeplot = 1
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter68():
    global revengeplot
    global cunning1
    if revengeplot == 0:
        print(activeplayer1, "designs a set of explosive mines, and buries them throughout the arena. However,", activeplayer2,
              "learns of his plot, and deactivates the mines by throwing rocks at them from a safe distance.", activeplayer1, "is furious.")
        cunning1 = cunning1 - 3
        revengeplot = 1
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter69():
    global revengeplot
    global charisma1
    if revengeplot == 0:
        print(activeplayer2, " spreads a rumor that ", activeplayer1, " ", rumor, ", turning the other players against him.", sep="")
        charisma1 = charisma1 - 3
        revengeplot = 1
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter70():
    global revengeplot
    global sanity1
    if revengeplot == 0:
        print(activeplayer2, " insults ", activeplayer1, "'s mother.", sep="")
        sanity1 = sanity1 - 3
        revengeplot = 1
        if sanity1 < 1:
            print(activeplayer1, "has been driven INSANE...")
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter71():
    global revengeplot
    global avengername
    global avengeename
    global avengee
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if revengeplot == 2:
        print(avengername, "stabs", avengeename, "in the back, claiming his revenge.")
        if avengee == 1:
            player1dead = 1
        if avengee == 2:
            player2dead = 1
        if avengee == 3:
            player3dead = 1
        if avengee == 4:
            player4dead = 1
        if avengee == 5:
            player5dead = 1
        if avengee == 6:
            player6dead = 1
        if avengee == 7:
            player7dead = 1
        revengeplot = 0
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter72():
    global revengeplot
    global avengername
    global avengeename
    global avengee
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if revengeplot == 2:
        print(avengername, "sneaks up behind", avengeename, "and pushes him off of a cliff, claiming his revenge.")
        if avengee == 1:
            player1dead = 1
        if avengee == 2:
            player2dead = 1
        if avengee == 3:
            player3dead = 1
        if avengee == 4:
            player4dead = 1
        if avengee == 5:
            player5dead = 1
        if avengee == 6:
            player6dead = 1
        if avengee == 7:
            player7dead = 1
        revengeplot = 0
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter73():
    global revengeplot
    global avengername
    global avengeename
    global avengee
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if revengeplot == 2:
        print(avengername, " strangles ", avengeename, ", claiming his revenge.", sep="")
        if avengee == 1:
            player1dead = 1
        if avengee == 2:
            player2dead = 1
        if avengee == 3:
            player3dead = 1
        if avengee == 4:
            player4dead = 1
        if avengee == 5:
            player5dead = 1
        if avengee == 6:
            player6dead = 1
        if avengee == 7:
            player7dead = 1
        revengeplot = 0
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return
    
def encounter74():
    global revengeplot
    global avengername
    global avengeename
    global avengee
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if revengeplot == 2:
        print(avengername, "pushes a boulder down a hill right as", avengeename, "is walking underneath it.",
              avengeename, "is crushed, and", avengername, "claims his revenge.")
        if avengee == 1:
            player1dead = 1
        if avengee == 2:
            player2dead = 1
        if avengee == 3:
            player3dead = 1
        if avengee == 4:
            player4dead = 1
        if avengee == 5:
            player5dead = 1
        if avengee == 6:
            player6dead = 1
        if avengee == 7:
            player7dead = 1
        revengeplot = 0
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter75():
    global revengeplot
    global avengername
    global avengeename
    global avengee
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if revengeplot == 2:
        print(avengername, "is chased through a field by a pack of hyeenas. He leads the hyeenas to",
              avengeename, "then trips him.", avengername, "escapes as he is devoured.")
        if avengee == 1:
            player1dead = 1
        if avengee == 2:
            player2dead = 1
        if avengee == 3:
            player3dead = 1
        if avengee == 4:
            player4dead = 1
        if avengee == 5:
            player5dead = 1
        if avengee == 6:
            player6dead = 1
        if avengee == 7:
            player7dead = 1
        revengeplot = 0
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter76():
    global revengeplot
    global avengername
    global avengeename
    global avengee
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if revengeplot == 2:
        print(avengername, " intends to claim his revenge on ", avengeename, ". He challenges ", avengeename,
              " to a duel. ", avengeename, " accepts; after all, he beat ", avengername, " the first time. He runs towards ",
              avengername, " a large stick brandished high above his head- and promptly explodes as he steps on the land mine ",
              avengername, " secretly planted.", sep="")
        if avengee == 1:
            player1dead = 1
        if avengee == 2:
            player2dead = 1
        if avengee == 3:
            player3dead = 1
        if avengee == 4:
            player4dead = 1
        if avengee == 5:
            player5dead = 1
        if avengee == 6:
            player6dead = 1
        if avengee == 7:
            player7dead = 1
        revengeplot = 0
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter77():
    global revengeplot
    global avengername
    global avengeename
    global avenger
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if revengeplot == 2:
        print(avengername, "stabs", avengeename, "in the back, claiming his revenge. Or so he thought.", avengeename,
              "rises, removing the protective leather vest he had hidden under his shirt. Before", avengername,
              "can defend himself,", avengeename, "kills him.")
        if avenger == 1:
            player1dead = 1
        if avenger == 2:
            player2dead = 1
        if avenger == 3:
            player3dead = 1
        if avenger == 4:
            player4dead = 1
        if avenger == 5:
            player5dead = 1
        if avenger == 6:
            player6dead = 1
        if avenger == 7:
            player7dead = 1
        revengeplot = 0
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter78():
    global alliance
    global activeplayer1dead
    global activeplayer2dead
    if numberofaliveplayers > 2:
        if alliance == 0:
            print(activeplayer1, "and", activeplayer2, "band together to form an alliance! They decide to call themselves...", alliancename)
            activeplayer1dead = 1
            activeplayer2dead = 1
            alliance = 1
            statcheck = input ("Press any key to continue.")
            if statcheck == "1":
                dostatcheck()
            print("")
            return

def encounter79():
    global activestrength1
    global activeplayer1dead
    global numberofaliveplayers
    if alliance == 2:
        print(alliancename, " band together to attack ", activeplayer1, "!", sep="")
        activestrength1 = activestrength1 - 2
        if activestrength1 < 1:
            print(activeplayer1, "cannot fend off both players at once, and dies to the attack!")
            activeplayer1dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        else:
            print(activeplayer1, "barely escapes", alliancename, "but is badly wounded.")
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter80():
    global alliance
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if alliance == 2:
        print(alliancemembername1, "betrays", alliancemembername2, "by stabbing him in the back!", "The alliance called", alliancename, "is broken!")
        alliance = 0
        if alliancemember1 == 1:
            player1dead = 0
        if alliancemember1 == 2:
            player2dead = 0
        if alliancemember1 == 3:
            player3dead = 0
        if alliancemember1 == 4:
            player4dead = 0
        if alliancemember1 == 5:
            player5dead = 0
        if alliancemember1 == 6:
            player6dead = 0
        if alliancemember1 == 7:
            player7dead = 0
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter81():
    global alliance
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global numberofaliveplayers
    if alliance == 2:
        print(alliancemembername2, "betrays", alliancemembername1, "by stabbing him in the back!", "The alliance called", alliancename, "is broken!")
        alliance = 0
        if alliancemember2 == 1:
            player1dead = 0
        if alliancemember2 == 2:
            player2dead = 0
        if alliancemember2 == 3:
            player3dead = 0
        if alliancemember2 == 4:
            player4dead = 0
        if alliancemember2 == 5:
            player5dead = 0
        if alliancemember2 == 6:
            player6dead = 0
        if alliancemember2 == 7:
            player7dead = 0
        numberofaliveplayers = numberofaliveplayers - 1
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter82():
    global activecharisma1
    if alliance == 2:
        print(alliancename, " has been spreading rumors about ", activeplayer1, ", claiming that he ", rumor, ".", sep="")
        activecharisma1 = activecharisma1 - 2
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter83():
    global activecunning1
    if alliance == 2:
        print(alliancename, "seems to be up to something...")
        activecunning1 = activecunning1 - 2
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter84():
    global activesanity1
    if alliance == 2:
        print(alliancename, "has been leaving threatening messages, such as", alliancename, "IS COMING FOR YOU.",
              activeplayer1, "is deeply troubled.")
        activesanity1 = activesanity1 - 1
        if activesanity1 < 1:
            print(activeplayer1, "has been driven INSANE...")
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter85():
    global activestrength1
    global activestrength2
    global activeplayer1dead
    global activeplayer2dead
    global numberofaliveplayers
    if alliance == 2:
        print(alliancename, "secretly plants a bomb in the arena. Their timing is perfect;", activeplayer1, "and", activeplayer2,
              "are caught in the blast.")
        activestrength1 = activestrength1 - 5
        activestrength2 = activestrength2 - 5
        if activestrength1 < 1:
            print(activeplayer1, "dies to the explosion.")
            activeplayer1dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        if activestrength2 < 1:
            print(activeplayer2, "dies to the explosion.")
            activeplayer2dead = 1
            numberofaliveplayers = numberofaliveplayers - 1
            print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter86():
    global alliance
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global activeplayer1dead
    global numberofaliveplayers
    if alliance == 2:
        print(alliancename, " are growing more and more in power. The remaining players realize that they must do something to stop this ",
              "terrible force, before it is too late. They band together and attack ", alliancename, ". ", activeplayer1,
              " heroically sacrifices himself to kill ", alliancemembername1, ". ", alliancemembername2, " escapes.")
        activeplayer1dead = 1
        alliance = 0
        if alliancemember2 == 1:
            player1dead = 0
        if alliancemember2 == 2:
            player2dead = 0
        if alliancemember2 == 3:
            player3dead = 0
        if alliancemember2 == 4:
            player4dead = 0
        if alliancemember2 == 5:
            player5dead = 0
        if alliancemember2 == 6:
            player6dead = 0
        if alliancemember2 == 7:
            player7dead = 0
        numberofaliveplayers = numberofaliveplayers - 2
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return

def encounter87():
    global alliance
    global player1dead
    global player2dead
    global player3dead
    global player4dead
    global player5dead
    global player6dead
    global player7dead
    global activeplayer1dead
    global numberofaliveplayers
    if alliance == 2:
        print(alliancename, " are growing more and more in power. The remaining players realize that they must do something to stop this ",
              "terrible force, before it is too late. They band together and attack ", alliancename, ". ", activeplayer1,
              " heroically sacrifices himself to kill ", alliancemembername2, ". ", alliancemembername1, " escapes.")
        activeplayer1dead = 1
        alliance = 0
        if alliancemember1 == 1:
            player1dead = 0
        if alliancemember1 == 2:
            player2dead = 0
        if alliancemember1 == 3:
            player3dead = 0
        if alliancemember1 == 4:
            player4dead = 0
        if alliancemember1 == 5:
            player5dead = 0
        if alliancemember1 == 6:
            player6dead = 0
        if alliancemember1 == 7:
            player7dead = 0
        numberofaliveplayers = numberofaliveplayers - 2
        print("Remaining players:", numberofaliveplayers)
        statcheck = input ("Press any key to continue.")
        if statcheck == "1":
            dostatcheck()
        print("")
        return
        
#Run Encounters Until Winner

global activeplayer1dead
activeplayer1dead = 0
global activeplayer2dead
activeplayer2dead = 0
global player1dead
player1dead = 0
global player2dead
player2dead = 0
global player3dead
player3dead = 0
global player4dead
player4dead = 0
global player5dead
player5dead = 0
global player6dead
player6dead = 0
global player7dead
player7dead = 0
global activedeadplayer
activedeadplayer = 0

global activeplayer1
global activestrength1
global activevigilance1
global activespeed1
global activestealth1
global activecunning1
global activecharisma1
global activesanity1
global activeplayer2
global activestrength2
global activestealth2
global activevigilance2
global activespeed2
global activecunning2
global activecharisma2
global activesanity2

global revengeplot
global avengername
global avengeename
global avengee
global avenger
revengeplot = 0

global alliance
global alliancemember1name
global alliancemember2name
global alliancemember1
global alliancemember2
alliance = 0
alliancemember1 = 0
alliancemember2 = 0

while numberofaliveplayers > 1 and not (alliance == 2 and numberofaliveplayers == 2):
    def chooseactivedeadplayer():
        global randomdeadplayer
        global activedeadplayer
        global activedeadplayername
        randomdeadplayer = random.randint(1,numberofstartingplayers)
        if randomdeadplayer == 1:
            if player1dead == 1:
                if not alliancemember1 == 1:
                    if not alliancemember2 == 1:
                        activedeadplayer = 1
                        activedeadplayername = player1
        if randomdeadplayer == 2:
            if player2dead == 1:
                if not alliancemember1 == 2:
                    if not alliancemember2 == 2:
                        activedeadplayer = 1
                        activedeadplayername = player2
        if randomdeadplayer == 3:
            if player3dead == 1:
                if not alliancemember1 == 3:
                    if not alliancemember2 == 3:
                        activedeadplayer = 1
                        activedeadplayername = player3
        if randomdeadplayer == 4:
            if player4dead == 1:
                if not alliancemember1 == 4:
                    if not alliancemember2 == 4:
                        activedeadplayer = 1
                        activedeadplayername= player4
        if randomdeadplayer == 5:
            if player5dead == 1:
                if not alliancemember1 == 5:
                    if not alliancemember2 == 5:
                        activedeadplayer = 1
                        activedeadplayername = player5
        if randomdeadplayer == 6:
            if player6dead == 1:
                if not alliancemember1 == 6:
                    if not alliancemember2 == 6:
                        activedeadplayer = 1
                        activedeadplayername = player6
        if randomdeadplayer == 7:
            if player7dead == 1:
                if not alliancemember1 == 7:
                    if not alliancemember2 == 7:
                        activedeadplayer = 1
                        activedeadplayername = player7
                
    def chooseactiveplayer1():
        global randomplayer1
        global activeplayer1
        global activestrength1
        global activevigilance1
        global activespeed1
        global activestealth1
        global activecunning1
        global activecharisma1
        global activesanity1
        randomplayer1 = random.randint(1,numberofstartingplayers)
        if randomplayer1 == 1:
            if player1dead == 0:
                activeplayer1 = player1
                activestrength1 = strength1
                activevigilance1 = vigilance1
                activespeed1 = speed1
                activestealth1 = stealth1
                activecunning1 = cunning1
                activecharisma1 = charisma1
                activesanity1 = sanity1
            else:
                chooseactiveplayer1()
        if randomplayer1 == 2:
            if player2dead == 0:
                activeplayer1 = player2
                activestrength1 = strength2
                activevigilance1 = vigilance2
                activespeed1 = speed2
                activestealth1 = stealth2
                activecunning1 = cunning2
                activecharisma1 = charisma2
                activesanity1 = sanity2
            else:
                chooseactiveplayer1()
        if randomplayer1 == 3:
            if player3dead == 0:
                activeplayer1 = player3
                activestrength1 = strength3
                activevigilance1 = vigilance3
                activespeed1 = speed3
                activestealth1 = stealth3
                activecunning1 = cunning3
                activecharisma1 = charisma3
                activesanity1 = sanity3
            else:
                chooseactiveplayer1()
        if randomplayer1 == 4:
            if player4dead == 0:
                activeplayer1 = player4
                activestrength1 = strength4
                activevigilance1 = vigilance4
                activespeed1 = speed4
                activestealth1 = stealth4
                activecunning1 = cunning4
                activecharisma1 = charisma4
                activesanity1 = sanity4
            else:
                chooseactiveplayer1()
        if randomplayer1 == 5:
            if player5dead == 0:
                activeplayer1 = player5
                activestrength1 = strength5
                activevigilance1 = vigilance5
                activespeed1 = speed5
                activestealth1 = stealth5
                activecunning1 = cunning5
                activecharisma1 = charisma5
                activesanity1 = sanity5
            else:
                chooseactiveplayer1()
        if randomplayer1 == 6:
            if player6dead == 0:
                activeplayer1 = player6
                activestrength1 = strength6
                activevigilance1 = vigilance6
                activespeed1 = speed6
                activestealth1 = stealth6
                activecunning1 = cunning6
                activecharisma1 = charisma6
                activesanity1 = sanity6
            else:
                chooseactiveplayer1()
        if randomplayer1 == 7:
            if player7dead == 0:
                activeplayer1 = player7
                activestrength1 = strength7
                activevigilance1 = vigilance7
                activespeed1 = speed7
                activestealth1 = stealth7
                activecunning1 = cunning7
                activecharisma1 = charisma7
                activesanity1 = sanity7
            else:
                chooseactiveplayer1()

    def chooseactiveplayer2():
        global randomplayer2
        global activeplayer2
        global activestrength2
        global activevigilance2
        global activespeed2
        global activestealth2
        global activecunning2
        global activecharisma2
        global activesanity2
        global randomplayer1
        randomplayer2 = random.randint(1,numberofstartingplayers)
        if randomplayer2 == 1:
            if not randomplayer1 == 1:
                if player1dead == 0:
                    activeplayer2 = player1
                    activestrength2 = strength1
                    activevigilance2 = vigilance1
                    activespeed2 = speed1
                    activestealth2 = stealth1
                    activecunning2 = cunning1
                    activecharisma2 = charisma1
                    activesanity2 = sanity1
                else:
                    chooseactiveplayer2()
            else:
                chooseactiveplayer2()
        if randomplayer2 == 2:
            if not randomplayer1 == 2:
                if player2dead == 0:
                    activeplayer2 = player2
                    activestrength2 = strength2
                    activevigilance2 = vigilance2
                    activespeed2 = speed2
                    activestealth2 = stealth2
                    activecunning2 = cunning2
                    activecharisma2 = charisma2
                    activesanity2 = sanity2
                else:
                    chooseactiveplayer2()
            else:
                chooseactiveplayer2()
        if randomplayer2 == 3:
            if not randomplayer1 == 3:
                if player3dead == 0:
                    activeplayer2 = player3
                    activestrength2 = strength3
                    activevigilance2 = vigilance3
                    activespeed2 = speed3
                    activestealth2 = stealth3
                    activecunning2 = cunning3
                    activecharisma2 = charisma3
                    activesanity2 = sanity3
                else:
                    chooseactiveplayer2()
            else:
                chooseactiveplayer2()
        if randomplayer2 == 4:
            if not randomplayer1 == 4:
                if player4dead == 0:
                    activeplayer2 = player4
                    activestrength2 = strength4
                    activevigilance2 = vigilance4
                    activespeed2 = speed4
                    activestealth2 = stealth4
                    activecunning2 = cunning4
                    activecharisma2 = charisma4
                    activesanity2 = sanity4
                else:
                    chooseactiveplayer2()
            else:
                chooseactiveplayer2()
        if randomplayer2 == 5:
            if not randomplayer1 == 5:
                if player5dead == 0:
                    activeplayer2 = player5
                    activestrength2 = strength5
                    activevigilance2 = vigilance5
                    activespeed2 = speed5
                    activestealth2 = stealth5
                    activecunning2 = cunning5
                    activecharisma2 = charisma5
                    activesanity2 = sanity5
                else:
                    chooseactiveplayer2()
            else:
                chooseactiveplayer2()
        if randomplayer2 == 6:
            if not randomplayer1 == 6:
                if player6dead == 0:
                    activeplayer2 = player6
                    activestrength2 = strength6
                    activevigilance2 = vigilance6
                    activespeed2 = speed6
                    activestealth2 = stealth6
                    activecunning2 = cunning6
                    activecharisma2 = charisma6
                    activesanity2 = sanity6
                else:
                    chooseactiveplayer2()
            else:
                chooseactiveplayer2()
        if randomplayer2 == 7:
            if not randomplayer1 == 7:
                if player7dead == 0:
                    activeplayer2 = player7
                    activestrength2 = strength7
                    activevigilance2 = vigilance7
                    activespeed2 = speed7
                    activestealth2 = stealth7
                    activecunning2 = cunning7
                    activecharisma2 = charisma7
                    activesanity2 = sanity7
                else:
                    chooseactiveplayer2()
            else:
                chooseactiveplayer2()
    if alliance == 0 or numberofaliveplayers > 3:
        chooseactiveplayer1()
        chooseactiveplayer2()
        chooseactivedeadplayer()
    else:
        if numberofaliveplayers == 3:
            randomencounter = random.randint(0,1)
            if randomencounter == 0:
                encounter80()
            if randomencounter == 1:
                encounter81()
            
    randomencounter = random.randint(0,87)
    createrumor()
    if alliance == 0:
        createalliancename()
    if randomencounter == 0:
        encounter0()
    if randomencounter == 1:
        encounter1()
    if randomencounter == 2:
        encounter2()
    if randomencounter == 3:
        encounter3()
    if randomencounter == 4:
        encounter4()
    if randomencounter == 5:
        encounter5()
    if randomencounter == 6:
        encounter6()
    if randomencounter == 7:
        encounter7()
    if randomencounter == 8:
        encounter8()
    if randomencounter == 9:
        encounter9()
    if randomencounter == 10:
        encounter10()
    if randomencounter == 11:
        encounter11()
    if randomencounter == 12:
        encounter12()
    if randomencounter == 13:
        encounter13()
    if randomencounter == 14:
        encounter14()
    if randomencounter == 15:
        encounter15()
    if randomencounter == 16:
        encounter16()
    if randomencounter == 17:
        encounter17()
    if randomencounter == 18:
        encounter18()
    if randomencounter == 19:
        encounter19()
    if randomencounter == 20:
        encounter20()
    if randomencounter == 21:
        encounter21()
    if randomencounter == 22:
        encounter22()
    if randomencounter == 23:
        encounter23()
    if randomencounter == 24:
        encounter24()
    if randomencounter == 25:
        encounter25()
    if randomencounter == 26:
        encounter26()
    if randomencounter == 27:
        encounter27()
    if randomencounter == 28:
        encounter28()
    if randomencounter == 29:
        encounter29()
    if randomencounter == 30:
        encounter30()
    if randomencounter == 31:
        encounter31()
    if randomencounter == 32:
        encounter32()
    if randomencounter == 33:
        encounter33()
    if randomencounter == 34:
        encounter34()
    if randomencounter == 35:
        encounter35()
    if randomencounter == 36:
        encounter36()
    if randomencounter == 37:
        encounter37()
    if randomencounter == 38:
        encounter38()
    if randomencounter == 39:
        encounter39()
    if randomencounter == 40:
        encounter40()
    if randomencounter == 41:
        encounter41()
    if randomencounter == 42:
        encounter42through48()
    if randomencounter == 43:
        encounter42through48()
    if randomencounter == 44:
        encounter42through48()
    if randomencounter == 45:
        encounter42through48()
    if randomencounter == 46:
        encounter42through48()
    if randomencounter == 47:
        encounter42through48()
    if randomencounter == 48:
        encounter42through48()
    if randomencounter == 49:
        encounter49through55()
    if randomencounter == 50:
        encounter49through55()
    if randomencounter == 51:
        encounter49through55()
    if randomencounter == 52:
        encounter49through55()
    if randomencounter == 53:
        encounter49through55()
    if randomencounter == 54:
        encounter49through55()
    if randomencounter == 55:
        encounter49through55()
    if randomencounter == 56:
        encounter56through62()
    if randomencounter == 57:
        encounter56through62()
    if randomencounter == 58:
        encounter56through62()
    if randomencounter == 59:
        encounter56through62()
    if randomencounter == 60:
        encounter56through62()
    if randomencounter == 61:
        encounter56through62()
    if randomencounter == 62:
        encounter56through62()
    if randomencounter == 63:
        encounter63()
    if randomencounter == 64:
        encounter64()
    if randomencounter == 65:
        encounter65()
    if randomencounter == 66:
        encounter66()
    if randomencounter == 67:
        encounter67()
    if randomencounter == 68:
        encounter68()
    if randomencounter == 69:
        encounter69()
    if randomencounter == 70:
        encounter70()
    if randomencounter == 71:
        encounter71()
    if randomencounter == 72:
        encounter72()
    if randomencounter == 73:
        encounter73()
    if randomencounter == 74:
        encounter74()
    if randomencounter == 75:
        encounter75()
    if randomencounter == 76:
        encounter76()
    if randomencounter == 77:
        encounter77()
    if randomencounter == 78:
        encounter78()
    if randomencounter == 79:
        encounter79()
    if randomencounter == 80:
        encounter80()
    if randomencounter == 81:
        encounter81()
    if randomencounter == 82:
        encounter82()
    if randomencounter == 83:
        encounter83()
    if randomencounter == 84:
        encounter84()
    if randomencounter == 85:
        encounter85
    if randomencounter == 86:
        encounter86
    if randomencounter == 87:
        encounter87

    if activeplayer1dead == 1 or activeplayer2dead == 1:
        revengeplot = 0
    if randomplayer1 == 1:
        strength1 = activestrength1
        vigilance1 = activevigilance1
        speed1 = activespeed1
        stealth1 = activestealth1
        cunning1 = activecunning1
        charisma1 = activecharisma1
        sanity1 = activesanity1
        if activeplayer1dead == 1:
            player1dead = 1
            activeplayer1dead = 0
    if randomplayer1 == 2:
        strength2 = activestrength1
        vigilance2 = activevigilance1
        speed2 = activespeed1
        stealth2 = activestealth1
        cunning2 = activecunning1
        charisma2 = activecharisma1
        sanity2 = activesanity1
        if activeplayer1dead == 1:
            player2dead = 1
            activeplayer1dead = 0
    if randomplayer1 == 3:
        strength3 = activestrength1
        vigilance3 = activevigilance1
        speed3 = activespeed1
        stealth3 = activestealth1
        cunning3 = activecunning1
        charisma3 = activecharisma1
        sanity3 = activesanity1
        if activeplayer1dead == 1:
            player3dead = 1
            activeplayer1dead = 0
    if randomplayer1 == 4:
        strength4 = activestrength1
        vigilance4 = activevigilance1
        speed4 = activespeed1
        stealth4 = activestealth1
        cunning4 = activecunning1
        charisma4 = activecharisma1
        sanity4 = activesanity1
        if activeplayer1dead == 1:
            player4dead = 1
            activeplayer1dead = 0
    if randomplayer1 == 5:
        strength5 = activestrength1
        vigilance5 = activevigilance1
        speed5 = activespeed1
        stealth5 = activestealth1
        cunning5 = activecunning1
        charisma5 = activecharisma1
        sanity5 = activesanity1
        if activeplayer1dead == 1:
            player5dead = 1
            activeplayer1dead = 0
    if randomplayer1 == 6:
        strength6 = activestrength1
        vigilance6 = activevigilance1
        speed6 = activespeed1
        stealth6 = activestealth1
        cunning6 = activecunning1
        charisma6 = activecharisma1
        sanity6 = activesanity1
        if activeplayer1dead == 1:
            player6dead = 1
            activeplayer1dead = 0
    if randomplayer1 == 7:
        strength7 = activestrength1
        vigilance7 = activevigilance1
        speed7 = activespeed1
        stealth7 = activestealth1
        cunning7 = activecunning1
        charisma7 = activecharisma1
        sanity7 = activesanity1
        if activeplayer1dead == 1:
            player7dead = 1
            activeplayer1dead = 0
    if randomplayer2 == 1:
        strength1 = activestrength2
        vigilance1 = activevigilance2
        speed1 = activespeed2
        stealth1 = activestealth2
        cunning1 = activecunning2
        charisma1 = activecharisma2
        sanity1 = activesanity2
        if activeplayer2dead == 1:
            player1dead = 1
            activeplayer2dead = 0
    if randomplayer2 == 2:
        strength2 = activestrength2
        vigilance2 = activevigilance2
        speed2 = activespeed2
        stealth2 = activestealth2
        cunning2 = activecunning2
        charisma2 = activecharisma2
        sanity2 = activesanity2
        if activeplayer2dead == 1:
            player2dead = 1
            activeplayer2dead = 0
    if randomplayer2 == 3:
        strength3 = activestrength2
        vigilance3 = activevigilance2
        speed3 = activespeed2
        stealth3 = activestealth2
        cunning3 = activecunning2
        charisma3 = activecharisma2
        sanity3 = activesanity2
        if activeplayer2dead == 1:
            player3dead = 1
            activeplayer2dead = 0
    if randomplayer2 == 4:
        strength4 = activestrength2
        vigilance4 = activevigilance2
        speed4 = activespeed2
        stealth4 = activestealth2
        cunning4 = activecunning2
        charisma4 = activecharisma2
        sanity4 = activesanity2
        if activeplayer2dead ==1:
            player4dead = 1
            activeplayer2dead = 0
    if randomplayer2 == 5:
        strength5 = activestrength2
        vigilance5 = activevigilance2
        speed5 = activespeed2
        stealth5 = activestealth2
        cunning5 = activecunning2
        charisma5 = activecharisma2
        sanity5 = activesanity2
        if activeplayer2dead == 1:
            player5dead = 1
            activeplayer2dead = 0
    if randomplayer2 == 6:
        strength6 = activestrength2
        vigilance6 = activevigilance2
        speed6 = activespeed2
        stealth6 = activestealth2
        cunning6 = activecunning2
        charisma6 = activecharisma2
        sanity6 = activesanity2
        if activeplayer2dead == 1:
            player6dead = 1
            activeplayer2dead = 0
    if randomplayer2 == 7:
        strength7 = activestrength2
        vigilance7 = activevigilance2
        speed7 = activespeed2
        stealth7 = activestealth2
        cunning7 = activecunning2
        charisma7 = activecharisma2
        sanity7 = activesanity2
        if activeplayer2dead == 1:
            player7dead = 1
            activeplayer2dead = 0
    if revengeplot == 1:
        avengername = activeplayer1
        avengeename = activeplayer2
        if randomplayer1 == 1:
            avenger = 1
        if randomplayer1 == 2:
            avenger = 2
        if randomplayer1 == 3:
            avenger = 3
        if randomplayer1 == 4:
            avenger = 4
        if randomplayer1 == 5:
            avenger = 5
        if randomplayer1 == 6:
            avenger = 6
        if randomplayer1 == 7:
            avenger = 7
        if randomplayer2 == 1:
            avengee = 1
        if randomplayer2 == 2:
            avengee = 2
        if randomplayer2 == 3:
            avengee = 3
        if randomplayer2 == 4:
            avengee = 4
        if randomplayer2 == 5:
            avengee = 5
        if randomplayer2 == 6:
            avengee = 6
        if randomplayer2 == 7:
            avengee = 7
        revengeplot = 2
    if alliance == 1:
        alliancemembername1 = activeplayer1
        alliancemembername2 = activeplayer2
        if randomplayer1 == 1:
            alliancemember1 = 1
        if randomplayer1 == 2:
            alliancemember1 = 2
        if randomplayer1 == 3:
            alliancemember1 = 3
        if randomplayer1 == 4:
            alliancemember1 = 4
        if randomplayer1 == 5:
            alliancemember1 = 5
        if randomplayer1 == 6:
            alliancemember1 = 6
        if randomplayer1 == 7:
            alliancemember1 = 7
        if randomplayer2 == 1:
            alliancemember2 = 1
        if randomplayer2 == 2:
            alliancemember2 = 2
        if randomplayer2 == 3:
            alliancemember2 = 3
        if randomplayer2 == 4:
            alliancemember2 = 4
        if randomplayer2 == 5:
            alliancemember2 = 5
        if randomplayer2 == 6:
            alliancemember2 = 6
        if randomplayer2 == 7:
            alliancemember2 = 7
        alliance = 2
    activedeadplayer = 0 

#Win Declaration

if numberofaliveplayers == 1:
    if player1dead == 0 and numberofstartingplayers > 0:
        print(player1 + " wins!")
    if player2dead == 0 and numberofstartingplayers > 1:
        print(player2 + " wins!")
    if player3dead == 0 and numberofstartingplayers > 2:
        print(player3 + " wins!")
    if player4dead == 0 and numberofstartingplayers > 3:
        print(player4 + " wins!")
    if player5dead == 0 and numberofstartingplayers > 4:
        print(player5 + " wins!")
    if player6dead == 0 and numberofstartingplayers > 5:
        print(player6 + " wins!")
        if vigilance6 < 1 and speed6 < 1 and stealth6 < 1 and cunning6 < 1 and charisma6 < 1 and sanity6 < 1:
            print("You found easter egg 4! (The Survivor)")
    if player7dead == 0 and numberofstartingplayers > 6:
        print(player7 + " wins!")

if numberofaliveplayers < 1:
    print("There is no winner. Everyone died!")

if numberofaliveplayers == 2:
    print(alliancename, " win!")

#Idea List:

#Weapon Delta: Each trait (or most) can get you a weapon in a different way, randomly chosen from weapon pool, unlocks new encounters
#Add to alliance delta
#More encounters that actually effect traits
#Trap Setting
