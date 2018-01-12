#Name: William Soe
#ReJane: The Game
#Ms. Thoms British Literature
#Period 7

#To sleep running statements
import time
import random
import sys
import os

name = "Jane"
cheats = False
current_time = 8
money = 100
inventory = []
devon1 = False
Ed = False
Sang = False
club = False
makeup = False

def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("ReJane: The Game")
    print("A game developed by William Soe")
    print ("Ms. Thoms's British Literature Class Period 7\n")
    sys.stdout.flush()
    time.sleep(5)
    
def naming():
    global name
    os.system('cls' if os.name == 'nt' else 'clear')
    new_name = raw_input('What would you like your name to be? ')
    if(new_name == "dev"):
        cheats = True
    print("Hello " + new_name + "! Let's begin.\n")
    name = new_name
    time.sleep(4)

def story_1():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("As the clock on your bedstand showed that it was 8:00am, the sun began to peek up over the horizon, and sunlight shined")
    print("through the windows of your ginormous floor-through apartment. The clanging of pots and pans echoed throughout the apartment, the sounds of which")
    print("wake you up. The smell of burned toast, bacon, and black coffee was pungent, and was a telltale sign that Nina was getting ready to leave.\n")
    time.sleep(10)
    print("Nina: I'm heading out %s! I don't think there's any paperwork for you today. Do what you want, I'll be back at around 10pm(22:00) for dinner!\n")%(name)
    time.sleep(3)
    response = ""
    while(response != 'yes' and response != 'no'):
        response = raw_input('Would you like to say something back? (yes/no)')
        if(response == 'yes'):
                reply = raw_input('What would you like to say?')
                print("%s: " + reply + '\n')%(name)
                time.sleep(3)
                print("Nina: What? Oh whatever, I'm late. Catch you later!\n")
                time.sleep(3)
    print("10 seconds later...")
    print("Nina: I almost forgot! Don't forget that Changhoon is arriving at the airport tomorrow! You might want to get prepared for that!\n")
    time.sleep(3)
    print("Changhoon was visiting America for the first time, and for oddly similar reasons that I moved to Seoul: He had recently filed for a divorce")
    print("with Monica, after he had found out that Monica had an affair with my old boss at the Zenith Academy. He had told me that he wanted to run away")
    print("from the chaos that was brewing back in Seoul, and wanted to catch up with me and Rachel.\n")
    time.sleep(15)
    print("You push yourself off your bed, wash up, and eat breakfast. You are finally ready to start your day.\n")
    pause = raw_input("Press Enter To Continue ")

def day1Interface():
    global current_time
    global money
    os.system('cls' if os.name == 'nt' else 'clear')
    if(current_time < 22):
        print("\nDay 1")
        print("Current Time: " + str(current_time) + ":00")
        print("Money: $" + str(money))
        print("\nWhat would you like to do?\n")
        print("Options:")
        print("Go Shopping (+2 Hours, shop)")
        print("Sort Some Files(+1 Hour, +$5, sort)")
        print("Do Some Work (+6 Hours, +$75, work)")
        print("Visit Devon (+6 Hours, devon)")
        print("Visit Ed (+6 Hours, ed)")
        print("Visit Sang (+4 Hours, sang)")
        print("Visit the Club (+4 Hours, Available between 16:00 and 18:00, club)")
        print("Go to Bed (Proceed to Next Day, bed)\n")
        choice = ''
        while(choice != 'shop' and choice != 'sort' and choice != 'work' and choice != 'devon' and choice != 'ed' and choice != 'sang' and choice != 'club' and choice != 'bed'):
            choice = raw_input("What would you like to do?(Type the word that appears at the end of your choice's parentheses) ")
        if(choice == 'shop'):
            current_time = current_time + 2
            print("\nYou make your way towards Flushing by riding the subway. A few hours later, you get off at Main Street.")
            print("Once you leave the station, you're at one of the busiest intersections in New York, right in front of a large Duane Reade.")   
            print("Equipped with your wallet, you get ready to shop.")
            time.sleep(10)
            shop(1)
        if(choice == 'sort'):
            money = money + 5
            current_time = current_time + 1
            day1Interface()
        if(choice == 'work'):
            money = money + 75
            current_time = current_time + 6
            day1Interface()
        if(choice == 'devon' and not(devon1)):
            current_time = current_time + 6
            Devon(1)
        if(choice == 'ed' and not(Ed)):
            current_time = current_time + 6
            Ed(1)
        if(choice == 'sang' and not(sang)):
            current_time = current_time + 4
            Sang(1)
        if(choice == 'club' and current_time >= 16 and current_time <= 18 and not(club)):
            current_time = current_time + 4
            club(1)
        if(choice == 'club' and (current_time <= 16 or current_time >= 18)):
            print("The club isn't open yet.")
            time.sleep(3)
            day1Interface()
        if(choice == 'bed'):
            print("For some reason, you're feeling really sleepy. You decide to go to sleep early so that you'll be refreshed by tomorrow.\n")
            time.sleep(4)
            print("As you lie in bed, you mentally prepare yourself for Changhoon's arrival. He told you over the phone that'll he'll be touching down")
            print("at JFK at around 7:00pm (19:00). It's been a couple of months since you last saw him, and the last time you saw him he was essentially")
            print("proposing to you. You only left him because of Ed. Maybe now things can change.\m")
            time.sleep(10)
            pause = raw_input("Press Enter To Continue ")
            story_2()
    else:
        print("I hear keys jingling near the front door. I'm pretty sure Nina's home.")
        time.sleep(4)
        print("Nina and I have a nice dinner while sharing about our days. Two hours later, we're off bed, getting")
        print("ready for tomorrow.\n")
        time.sleep(7)
        print("As you lie in bed, you mentally prepare yourself for Changhoon's arrival. He told you over the phone that'll he'll be touching down")
        print("at JFK at around 7:00pm (19:00). It's been a couple of months since you last saw him, and the last time you saw him he was essentially")
        print("proposing to you. You only left him because of Ed. Maybe now things can change.\m")
        time.sleep(10)
        pause = raw_input("Press Enter To Continue to Day 2 ")
        current_time = 8
        story_2()
       
def shop(dayNumber):
    global money
    global inventory
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Your Money: $"+str(money))
    print("Your Inventory: "+str(inventory))
    print("\nThings you can buy:\n")
    print("Bouquet of Roses (-$15, Roses)")
    print("2 Pounds of Beef (-$25, Beef)")
    print("Random Vegetables (-$10, Veges)")
    print("Camera (-$100, Camera)")
    print("Gold Ring (-$250, Gold Ring)")
    print("Wine (-$45, Wine)")
    print("6-pack of Beer (-$25, Beer)")
    print("Red Dress (-$80, Dress)")
    print("Blouse and Pleated Pants (-$80, Blouse and Pants)")
    print("Go Home (Return Home, Home)\n")
    choice = ""
    while(choice != 'Roses' and choice != 'Beef' and choice != 'Veges' and choice != 'Camera' and choice != 'Gold Ring' and choice != 'Wine' and choice != 'Beer' and choice != 'Dress' and choice != 'Blouse and Pants' and choice != 'Home' and money > 0):
        choice = raw_input('What do you want to do? ')
        if(choice == 'Roses' and money >= 15 and 'Roses' not in inventory):
            print("You bought: "+choice)
            time.sleep(3)
            inventory.append('Roses')
            money = money - 15
            shop(dayNumber)
        if(choice == 'Roses' and money < 15):
            print("You don't have enough money to buy that")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Roses' and ('Roses' in inventory)):
            print("You already have that item")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Beef' and money >= 25 and 'Beef' not in inventory):
            print("You bought: " + choice)
            time.sleep(3)
            inventory.append('Beef')
            money = money - 25
            shop(dayNumber)
        if(choice == 'Beef' and money < 25):
            print("You don't have enough money to buy that")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Beef' and ('Beef' in inventory)):
            print("You already have that item")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Veges' and money >= 10 and 'Veges' not in inventory):
            print("You bought: " +choice)
            time.sleep(3)
            inventory.append('Veges')
            money = money - 10
            shop(dayNumber)
        if(choice == 'Veges' and money < 10):
            print("You don't have enough money to buy that")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Veges' and ('Veges' in inventory)):
            print("You already have that item")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Camera' and money >= 100 and 'Camera' not in inventory):
            print('You bought: '+choice)
            time.sleep(3)
            inventory.append('Camera')
            money = money - 100
            shop(dayNumber)
        if(choice == 'Camera' and money < 100):
            print("You don't have enough money to buy that")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Camera' and ('Camera' in inventory)):
            print("You already have that item")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Gold Ring' and money >= 250 and 'Gold Ring' not in inventory):
            print("You bought: "+choice)
            time.sleep(3)
            inventory.append('Gold Ring')
            money = money - 250
            shopReturn(dayNumber)
        if(choice == 'Gold Ring' and money < 250):
            print("You don't have enough money to buy that")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Gold Ring' and ('Gold Ring' in inventory)):
            print("You already have that item")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Wine' and money >= 45 and 'Wine' not in inventory):
            print('You bought: '+choice)
            time.sleep(3)
            inventory.append('Wine')
            money = money - 45
            shop(dayNumber)
        if(choice == 'Wine' and money < 45):
            print("You don't have enough money to buy that")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Wine' and ('Wine' in inventory)):
            print("You already have that item")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Beer' and money >= 25 and 'Beer' not in inventory):
            print('You bought: '+choice)
            time.sleep(3)
            inventory.append('Beer')
            money = money - 25
            shop(dayNumber)
        if(choice == 'Beer' and money < 25):
            print("You don't have enough money to buy that")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Beer' and ('Beer' in inventory)):
            print("You already have that item")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Dress' and money >= 80 and 'Dress' not in inventory):
            print('You bought: '+choice)
            time.sleep(3)
            inventory.append('Dress')
            money = money - 80
            shop(dayNumber)
        if(choice == 'Dress' and money < 80):
            print("You don't have enough money to buy that")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Dress' and ('Dress' in inventory)):
            print("You already have that item")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Blouse and Pants' and money >= 80 and 'Blouse and Pants' not in inventory):
            print('You bought: '+choice)
            time.sleep(3)
            inventory.append('Blouse and Pants')
            money = money - 80
            shop(dayNumber)
        if(choice == 'Blouse and Pants' and money < 80):
            print("You don't have enough money to buy that")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Blouse and Pants' and ('Blouse and Pants' in inventory)):
            print("You already have that item")
            time.sleep(3)
            shop(dayNumber)
        if(choice == 'Home'):
            if(dayNumber == 1):
                day1Interface()
            if(dayNumber == 2):
                day2Interface()

def Devon(dayNumber):
    global current_time
    global name
    global devon1 
    os.system('cls' if os.name == 'nt' else 'clear')
    print("It's about time that I go and see Devon. Let's go see how she's doing.\n")
    time.sleep(3)
    print("About an hour later, I arrived at the front of the Mazer's home. It's been a couple of months since")
    print("I last came here. I want to say that Devon and I are better now, and that my relationship with Beth")
    print("isn't in complete shambles, but after destroying their family, I can't say that they'll magically")
    print("forgive me. I still don't forgive myself for what I have done. I still want to see Devon, though. I")
    print("press the button on the door labelled B.MAZER, and wait for a response.\n")
    time.sleep(17)
    print("Brrrrring...Brrrrring...Brrrrring...\n")
    time.sleep(5)
    if(current_time <= 14):
        print("I guess no one is home. I might come back later.")
        time.sleep(4)
        day1Interface()
    elif(dayNumber == 1):
        devon1 = True
        print("Devon: Who's there? Leave the package on the front door if you have it!\n")
        time.sleep(4)
        print("%s: It's %s, Devon. Open the door.\n")%(name, name)
        time.sleep(3)
        print("Devon: I'm coming!\n")
        time.sleep(3)
        print("Devon opens the door. She's wearing her usual black clothing, with a shirt a size or two too big")
        print("on her. Her body is still very slim, but she's grown quite a bit taller. She's approaching my eye level.\n")
        time.sleep(7)
        print("%s: Hey Devon! Were you expecting something?\n")%(name)
        time.sleep(4)
        print("Devon: Only the newest Evv-R-Blu album! Apparently it's going to be the last one they're")
        print("releasing before the group disbands, so I had to get my hands on it.\n")
        time.sleep(7)
        print("%s: That's pretty cool. We should listen to it sometime.\n")%(name)
        time.sleep(4)
        print("Devon: Why not now? Come on in! I'll go get my CD player, and we'll listen to it together!\n")
        time.sleep(4)
        print("I walk in, and walk towards the living room.\n")
        time.sleep(3)
        print("%s: But your mother probably doesn't want me hanging around here. I just wanted to see how you were doing.")%(name)
        print("I haven't seen you in a while, and wanted to ask you about Hunter and some other things.\n")
        time.sleep(4)
        print("Devon: Don't worry, my mom isn't coming home in...\n")
        time.sleep(3)
        print("BAM\n")
        time.sleep(3)
        print("We could hear the front door slam open.\n")
        time.sleep(3)
        print("Beth: Devon? I'm home! Devon? DEVON WHERE ARE YOU?\n")
        time.sleep(4)
        print("Devon: God... she's home early? I thought she had work today. What are you going to do?\n")
        decision = ""
        while(decision != "Confront Beth" and decision != "Try to Run"):
            decision = raw_input("What are you going to do? (Confront Beth/Try to Run)\n")
            if(decision == "Try to Run"):
                print("%s: Devon, I have to go now. Maybe we'll catch up later?\n")%(name)
                time.sleep(4)
                print("Devon: I understand. Just wait for her to pass by.\n")
                time.sleep(4)
                print("You wait a few seconds for Beth to start walking by. You peer out through the living room door and spot Beth.")
                print("Beth looks frantic. She must think that Devon left the house. I wait for her footsteps to pass though the")
                print("living room door. I hear pass the living room. She's still screaming for Devon.")
                time.sleep(10)
                print("Devon: Now's your chance! Go!\n")
                time.sleep(4)
                print("I made my way to the door. Beth forgot to close it. I first walk out, then I race to the train station.\n")
                time.sleep(5)
                print("What a mess.")
                time.sleep(4)
                day1Interface()
            if(decision == "Confront Beth"):
                print("%s: I'm going to talk to her.\n")%(name)
                time.sleep(4)
                print("Devon: What?!?\n")
                time.sleep(3)
                print("I step out of the living room and into the hallway. In front of me is Beth Mazer.") 
                print("She looks skinnier than usual. However, there is the faint, yet lingering smell of onions coming from")
                print("her direction.\n")
                time.sleep(5)
                print("Beth: %s? What are you doing here? What the hell did you do with Devon? Where is she? Where the f--- is")%(name)
                print("my daughter?\n")
                time.sleep(5)
                if('Veges' in inventory):
                    print("%s: Oh, I just came to give you some organic vegetables. As an apology for coming in last time.\n")%(name)
                    time.sleep(4)
                    print("Beth: Oh, so you think you can come in before you apologized?\n")
                    time.sleep(3)
                    print("She had a point.\n")
                    time.sleep(3)
                    print("Beth: But thank you. I appreciate the gift. But still, is Devon here?\n")
                    time.sleep(4)
                    print("%s: Yea, she's still here. She's in her room. She wasn't answering because she was trying to hide me.\n")%(name)
                    time.sleep(5)
                    print("Devon: Well thanks for ratting me out. Welcome home, mom.\n")
                    time.sleep(4)
                    print("Beth: Thank god you're ok. You're all that I have left.\n")
                    time.sleep(3)
                    print("Beth goes in for an embrace, but Devon quickly shuffles back and hides behind me.\n")
                    time.sleep(4)
                    print("Devon: Mom, not in front of %s.\n")%(name)
                    time.sleep(3)
                    print("Beth: She's still fond of you, %s. I have to admit, you and my daughter are quite a pair.\n")%(name)
                    time.sleep(4)
                    print("%s: Maybe because I was her au pair, huh?\n")%(name)
                    time.sleep(4)
                    print("Beth: Maybe you two were meant to be. But I'll have you know that I can still never forgive you for Ed.\n")
                    time.sleep(5)
                    print("%s: I understand, Ms. Mazer.\n")%(name)
                    time.sleep(3)
                    print("Beth: Please, call me Beth. And if Devon is happy with you, you're free to see her when you want.")
                    print("Just keep your activities within this house, please.\n")
                    time.sleep(7)
                    print("%s: Thank you, Beth. I'll make sure to take care of Devon when I do.\n")%(name)
                    time.sleep(4)
                    print("Devon: We'll listen the next time you come, ok? Promise me!\n")
                    time.sleep(4)
                    print("%s: I promise. I have to get going now, but it was great meeting you two. Thanks for having me.\n")%(name)
                    time.sleep(5)
                    print("This is a promise I will not break.\n")
                    time.sleep(4)
                    print("Beth: See you around, %s. Say hi to Sang for me, will you?\n")%(name)
                    time.sleep(4)
                    print("%s: I will. Bye Beth. Bye Devon. See you around.\n")%(name)
                    time.sleep(5)
                    devon1 = True
                    print("You have completed the Devon storyline!\n")
                    cont = ""
                    while(cont != "continue"):
                        cont = raw_input("Type 'continue' to continue.")
                    if(cont == 'continue'):
                        day1Interface()
                else:
                    print("%s: Your daughter is in her room. Calm down, Beth.\n")%(name)
                    time.sleep(4)
                    print("Beth: Calm down? I thought I just lost my daughter, the one person I have left! And now you're in my house?")
                    print("I told you before, and now before I call the cops, get the f--- out of my home.\n")
                    time.sleep(7)
                    print("As soon as she said those words, I scrambled out of her home, and rushed towards the exit.\n")
                    time.sleep(5)
                    print("What a mess.\n")
                    print("Hint: Try to get Beth a gift.")
                    pause = raw_input("Press Enter To Continue ")
                    day1Interface()

def Ed(dayNumber):
    global Ed
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sorry, this option is not available yet.")
    time.sleep(4)
    if(dayNumber == 1):
        day1Interface()
    if(dayNumber == 2):
        day2Interface()

def Sang(dayNumber):
    global sang
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sorry, this option is not available yet.")
    time.sleep(4)
    if(dayNumber == 1):
        day1Interface()
    if(dayNumber == 2):
        day2Interface()

def club(dayNumber):
    global club
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sorry, this option is not available yet.")
    time.sleep(4)
    if(dayNumber == 1):
        day1Interface()
    if(dayNumber == 2):
        day2Interface()

def story_2():
    global name
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The morning was filled with a light drizzle that blanketed New York with rain. The clouds completely blocked at the sun, where")
    print("you could only see the soft glow of light emananting from behind the clouds. Aside from the light, the rest of the city was pitch")
    print("black, although it was 8am already. Nina was already gone, and she had left a note on my bedstand. It read:\n")
    time.sleep(14)
    print("%s, I had to leave early today because someone called with a plumbing problem. Remember that Changhoon's coming at 7pm!")%(name)
    print("If you want, you can head out and buy some gifts for him to welcome him. I'll be at the airport around then, so dont be late!\n")
    print("Nina\n")
    time.sleep(10)
    print("I guess it's time for me to get up and get ready to meet Changhoon.\n")
    pause = raw_input("Press Enter To Continue ")
    day2Interface()
    
def day2Interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    global current_time
    global money
    global makeup
    global name
    os.system('cls' if os.name == 'nt' else 'clear')
    if(current_time < 19):
        print("\nDay 2")
        print("Current Time: " + str(current_time) + ":00")
        print("Money: $" + str(money))
        print("\nWhat would you like to do?\n")
        print("Options:")
        print("Go Shopping (+2 Hours, shop)")
        print("Sort Some Files(+1 Hour, +$5, sort)")
        print("Do Some Work (+6 Hours, +$75, work)")
        print("Put Makeup On (+1 Hour, -$10, makeup)")
        print("Visit Ed (+6 Hours, ed)")
        print("Visit Sang (+4 Hours, sang)")
        print("Visit the Club (+4 Hours, Available between 16:00 and 18:00, club)")
        print("Just Chill (+ 11 Hours, chill)")
        choice = ''
        while(choice != 'shop' and choice != 'sort' and choice != 'work' and choice != 'makeup' and choice != 'ed' and choice != 'chill' and choice != 'sang' and choice != 'club'):
            choice = raw_input("What would you like to do?(Type the word that appears at the end of your choice's parentheses) ")
            if(choice == 'shop'):
                current_time = current_time + 2
                print("\nYou make your way towards Flushing by riding the subway. A few hours later, you get off at Main Street.")
                print("Once you leave the station, you're at one of the busiest intersections in New York, right in front of a large Duane Reade.")   
                print("Equipped with your wallet, you get ready to shop.")
                time.sleep(10)
                shop(2)
            if(choice == 'sort'):
                money = money + 5
                current_time = current_time + 1
                day2Interface()
            if(choice == 'work'):
                money = money + 75
                current_time = current_time + 6
                day2Interface()
            if(choice == 'makeup'):
                makeup = True
                money = money - 10
                current_time = current_time + 1
                print("\nIf you're headed out, you have to tidy up a little bit. You put on some foundation, blush,")
                print("and lipstick. You look similar to the Korean version of %s.")%(name)
                pause = raw_input("Press Enter To Continue ")
                day2Interface()
            if(choice == 'ed' and not(Ed)):
                current_time = current_time + 6
                Ed(2)
            if(choice == 'sang' and not(sang)):
                current_time = current_time + 4
                Sang(2)
            if(choice == 'club' and current_time >= 16 and current_time <= 18 and not(club)):
                current_time = current_time + 4
                club(2)
            if(choice == 'club' and (current_time <= 16 or current_time >= 18)):
                print("The club isn't open yet.")
                time.sleep(3)
                day2Interface()
        else:
            print("It's time to go and pick up Changhoon from the airport. I hope he still remembers what I look like.\n")
            pause = raw_input("Press Enter To Continue ")
            ChanghoonEnding()

def ChanghoonEnding():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def runGame():
    intro()
    naming()
    story_1()
    day1Interface()

#Run the Game
#runGame()

#Stuff for debugging
#intro()
#naming()
#story_1()
#day1Interface()
story_2()
          
    
    
