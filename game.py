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
sang = False
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
    new_name = raw_input('What would you like your name to be? (Press Enter to Keep Default Name)')
    if(new_name == "dev"):
        cheats = True
    print("Hello " + name + "! Let's begin.\n")
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
            time.sleep(8)
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
            print("\nThe club isn't open yet.")
            time.sleep(3)
            day1Interface()
        if(choice == 'bed'):
            print("\nFor some reason, you're feeling really sleepy. You decide to go to sleep early so that you'll be refreshed by tomorrow.\n")
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
    global inventory
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
                time.sleep(8)
                shop(2)
            if(choice == 'sort'):
                money = money + 5
                current_time = current_time + 1
                day2Interface()
            if(choice == 'work'):
                money = money + 75
                current_time = current_time + 6
                day2Interface()
            if(choice == 'makeup' and not(makeup)):
                makeup = True
                money = money - 10
                current_time = current_time + 1
                print("\nIf you're headed out, you have to tidy up a little bit. You put on some foundation, blush,")
                print("and lipstick. You look similar to the Korean version of %s.")%(name)
                pause = raw_input("Press Enter To Continue ")
                day2Interface()
            if(choice == 'makeup' and makeup):
                print("You already put your makeup on.\n")
                time.sleep(4)
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
                print("\nThe club isn't open yet.")
                time.sleep(3)
                day2Interface()
            if(choice == 'chill'):
                current_time = current_time + 11
                print("\nYou chilled out and waited for Changhoon's arrival time.")
                time.sleep(4)
                day2Interface()
    else:
        print("It's time to go and pick up Changhoon from the airport. I hope he still remembers what I look like.\n")
        time.sleep(4)
        if('Blouse and Pants' in inventory):
            print("I put on the stylish blouse and pants that I bought when I went out shopping. After trying it on, I looked at myself in the mirror.\n")
            time.sleep(5)
            print("I'm definitely going to get some head turns with this outfit.\n")
            ChanghoonEnding()
        elif('Blouse and Pants' not in inventory):
            print("I look around through the house, but I realized I forgot to do the laundry. In a panic, I scramble around looking for any spare clothes")
            print("around the apartment. I end up finding my old 1999 Disney World t-shirt and a pair of flared blue jeans. After putting it on, I look")
            print("at myself in the mirror.\n")
            time.sleep(10)
            print("Changhoon is going to get right back on the plane back to Korea after seeing me.\n")
            pause = raw_input("Press Enter To Continue ")
            ChanghoonEnding()

def ChanghoonEnding():
    global name
    global inventory
    global makeup
    os.system('cls' if os.name == 'nt' else 'clear')
    print("I hailed a cab outside of my apartment and told the driver to take me JFK. He nodded, and I travelled through Astoria to the airport.")
    print("I hope I make it in time.\n")
    time.sleep(5)
    print("2 Hours Later\n")
    time.sleep(3)
    print("In classic fashion, I was an hour late to Changhoon's arrival. We got caught up in some traffic on the Van Wyck Expressway, with the driver yelling")
    print("at the car in front of him the entire time. When the taxi finally pulled up to the arrivals entrance of Terminal 1, where Korean Air lands.")
    print("I hastily paid the driver and ran inside.")
    print("The space was gigantic. There were people bustling left and right, but the only person I cared about wasn't in sight.")
    print("I looked through the entire gate area, but he was no where in sight.\n")
    time.sleep(14)
    print("?: %s? I'm here!\n")%(name)
    time.sleep(4)
    print("I recognized that voice instantly. I turned around, and about 5 inches away from my face was Changhoon. He looked a little bit different from")
    print("before. His hair was longer, and he was starting to grow some stubble on his chin. He smiled at me, and it was the same Park Ji-Sung smile")
    print("from before.\n")
    print("Man, was he handsome.\n")
    time.sleep(8)
    print("%s: Oh, welcome to America! I haven't seen you in months!\n")%(name)
    time.sleep(4)
    print("Real smooth there.\n")
    time.sleep(4)
    if('Blouse and Pants' in inventory):
        print("Changhoon: Gomahwuh(thank you), %s. You look really good today. You still have good style.\n")%(name)
        time.sleep(4)
        print("%s: Thanks, Changhoon. I bought it just for you.\n")%(name)
        time.sleep(4)
        print("I had to buy it if I didn't want to wear some less attractive pieces of clothing.\n")
        time.sleep(4)
        pause = raw_input("Press Enter To Continue \n")
    else:
        print("Changhoon: Gamsa(thank you), %s. Is that the fashion trend here in America?\n")%(name)
        time.sleep(4)
        print("%s: Yeah, yeah, this shirt is very popular in the U.S. nowadays.\n")%(name)
        time.sleep(4)
        #print("Congratulations! You made it to the last tree of this beta mode. to start the game over, ")
        #print("press enter and run the game again.")
        print("Changhoon: Are you sure? You look like you just came out of 1999.\n")
        time.sleep(4)
        print("I really regret not buying that cute outfit that I saw earlier in Flushing.\n")
        time.sleep(4)
        pause = raw_input("Press Enter To Continue \n")
    print("Changhoon: Anyways, how have you been, Jane? It's been quite a while.\n")
    time.sleep(4)
    print("His English skills have definitely gotten better from when I last saw him. The Korean accent was inevitably present, but he had stronger control")
    print("over his speech and wasn't as shaky as he was before.\n")
    time.sleep(6)
    print("<What would you like to say to Changhoon?>\n")
    print("Option 1: I'm really sorry about what happened between you and Monica.")
    print("Option 2: I've been pretty busy lately, with my new job and everything.\n")
    while(response != 'option 1' and response != 'option 2'):
        response = raw_input("What would you like to say?(Type 'option' and the number of the option you want ex. option 1)")
        if(response == 'option 1'):
            print("%s: \nI'm really sorry about what happened between you and Monica.\n")%(name)
            time.sleep(3)
            print("Changhoon: Oh Monica? That cheat? I should have known that she could not stay loyal. She flirts with everyone. It's just her nature.\n")
            time.sleep(5)
            print("%s: Is everything going alright? Is there any way I can help?")%(name)
            time.sleep(4)
            print("Changhoon: Everything is doing pretty well, considering this is the second time a woman has left me for another man.\n")
            time.sleep(5)
            print("Ouch.\n")
            time.sleep(4)
            print("%s: How did you find out?...")%(name)
            time.sleep(4)
            print("Changhoon: I asked your aunt. She told me why you ran away.\n")
            time.sleep(4)
            print("%s: I didn't run away, Changhoon. I just had to leave because it was time to leave.\n")%(name)
            time.sleep(4)
            print("Changhoon: And the time was right before you came to meet my parents? How do you think I felt? I feel the same way now.\n")
            time.sleep(5)
            print("%s: I couldn't be with you, Changhoon. You knew that all along. You never dated %s. You dated some picturesque version of me.\n")%(name)
            time.sleep(4)
            print("Changhoon: But I can still love you for who you were, Jane. Do you think it was just the looks I was after? My motives should be pretty apparent after")
            print("I got married to Monica.\n")
            time.sleep(6)
            print("Did he just call her ugly? Damn.\n")
            time.sleep(3)
            print("%s: You married for the sake of getting married? That's why you rushed in with Monica? That's a pretty bad reason, if you ask anyone.\n")%(name)
            time.sleep(4)
            print("%s: If you are looking for love, Changhoon, you were looking in the wrong places.")%(name)
            time.sleep(4)
            print("Changhoon: I'm looking at my love, Jane.\n")%(name)
            time.sleep(3)
            print("Huh?\n")
            time.sleep(2)
            print("Changhoon: I missed you so much %s. I missed you so much since you left. Monica was me being reckless, to try to fix my sadness. I miss everything")
            print("we went through together. I know I made mistakes, but please don't run away from me again. I'm here, and I want to be with you.\n")%(name)
            time.sleep(4)
            print("<What do you want to say back?>\n")
            print("Option 1: I've thought about it for a while. I think I want to be with you, too.")
            print("Option 2: I've thought about it for some time. And I think we should stay apart. I don't know for how long, but I much rather stay where we are now.\n")
            while(response != 'option 1' and response != 'option 2'):
                response = raw_input("How do you respond? (Choose the number of the option you want in the same way)")
                if(response == 'option 1'):
                    print("\n%s: I've thought about it for a while. I think I want to be with you, too.\n")%(name)
                    time.sleep(4)
                    print("Reader, I told him I loved him. He treated me with so much love and respect, and I completely ignored it. He is perfect for me,")
                    print("and I can't believe I didn't see that earlier.\n")
                    time.sleep(6)
                    print("I brought him to Flushing, and we had some soju and Korean barbeque together. We got to my apartment at around 1am. He wished me a goodnight,")
                    print("and before I went in he gave me a kiss. Reader, we were on. Again.\n")
                    time.sleep(7)
                    print("Congratulations! You have completed the Changhoon ending! To discover more endings, play through the game again.\n")
                    print("Thanks for playing!")
                    response = raw_input("Press Enter To Exit")
                    return
                if(response == 'option 2'):
                    print("\n%s: I've thought about it for some time. And I think we should stay apart. I don't know for how long, but I much rather stay where we are now.\n")%(name)
                    time.sleep(4)
                    print("Reader, I told him that I couldn't be with him. I didn't deserve him, not after what I had done to him. I never loved him like he loved me,")
                    print("and I don't expect that to change.\n")
                    time.sleep(6)
                    print("Changhoon was visibly sad, but he knew he had to accept the situation. I brought him around New York, and showed him places like Ground Zero.")
                    print("I then went with him to his hotel, where I gave him a hug and wished him goodnight. Afterwards, I went home, where Nina was already asleep.")
                    print("I changed, got back into bed, and fell asleep peacefully.\n")
                    time.sleep(9)
                    print("Congratulations! You have completed the Solo ending! To discover more endings, play through the game again.\n")
                    print("Thanks for playing!")
                    response = raw_input("Press Enter To Exit")
                    return
        if(response == 'option 2'):
            print("%s: I've been pretty busy lately, with my new job and everything.\n")%(name)
            time.sleep(4)
            print("Changhoon: New job? What do you do now?\n")
            time.sleep(4)
            print("%s: I work as a manager for a business me and Nina run. You remember Nina, right?\n")%(name)
            time.sleep(4)
            print("Changhoon: Yea, the American girl who came to Korea to see you? She was ok. You working together now?\n")
            time.sleep(4)
            print("%s: Yea, yea, she's a really good mechanic, and I'm good with accounting, so we work well together.\n")%(name)
            time.sleep(4)
            print("God, this is so awkward. I haven't seen him in such a long time, and I barely know what's going on in his life. Maybe I should get this over with quickly.\n")
            time.sleep(4)
            print("%s: So, uh, do you want to go to see Ground Zero?\n")%(name)
            tmie.sleep(3)
            print("Changhoon: Yea, that is good.\n")
            time.sleep(3)
            print("Reader, I took him on the most boring trip I could have possibly taken him on. We visited a couple of tourist attractions, but most of the time in complete")
            print("silence. At the end of the day, it was time to see him to his hotel.\n")
            time.sleep(4)
            print("Changhoon: So, uh, thanks for bringing me around. I'll take myself to see some friends tomorrow, so don't worry about me.\n")
            time.sleep(5)
            print("%s: Oh, ok. Enjoy the rest of your time in New York! Have fun!.\n")%(name)
            time.sleep(4)
            print("I went home right after. It was around 12am. I was exhausted, and as soon as I entered the apartment I threw myself onto my bed. In bed, I began to chuckle.")
            print("Today was a mess.\n")
            time.sleep(6)
            print("Congratulations! You have completed the Mess ending! To discover more endings, play through the game again.\n")
            print("Thanks for playing!")
            response = raw_input("Press Enter To Exit")
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
#story_2()
day2Interface()   
#ChanghoonEnding()      
    
    
