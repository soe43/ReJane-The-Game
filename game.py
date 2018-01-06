#Name: William Soe
#ReJane: The Game
#Ms. Thoms British Literature
#Period 7

#To sleep running statements
import time
import random
import sys
import os

name = ""
cheats = False
current_time = 8
money = 100
inventory = []

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
    time.sleep(3)

def story_1():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("As the clock on your bedstand showed that it was 8:00am, the sun began to peek up over the horizon, and sunlight shined")
    print("through the windows of your ginormous floor-through apartment. The clanging of pots and pans echoed throughout the apartment, the sounds of which")
    print("wake you up. The smell of burned toast, bacon, and black coffee was pungent, and was a telltale sign that Nina was getting ready to leave.\n")
    time.sleep(10)
    print("Nina: I'm heading out %s! I don't think there's any paperwork for you today. Do what you want, I'll be back for dinner!\n")%(name)
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
    time.sleep(7)

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
        if(choice == 'devon'):
            current_time = current_time + 6
            Devon(1)
        if(choice == 'ed'):
            current_time = current_time + 6
            Ed(1)
        if(choice == 'sang'):
            current_time = current_time + 4
            Sang(1)
        if(choice == 'club' and current_time >= 16 and current_time <= 18):
            current_time = current_time + 4
            club(1)
            if(choice == 'club' and (current_time <= 16 or current_time >= 18)):
                print("The club isn't open yet.")
        if(choice == 'bed'):
            story_2()
    else:
        print("I hear keys jingling near the front door. I'm pretty sure Nina's home.")
       
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
        if(choice == 'Beer' and money >= 25 and 'Beer' in inventory):
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
            shop(1)
        if(choice == 'Dress' and money >= 80 and 'Dress' in inventory):
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

def Devon(dayNumber):
    os.system('cls' if os.name == 'nt' else 'clear')
    return
def Ed(dayNumber):
    os.system('cls' if os.name == 'nt' else 'clear')
    return
def Sang(dayNumber):
    os.system('cls' if os.name == 'nt' else 'clear')
    return
def club(dayNumber):
    os.system('cls' if os.name == 'nt' else 'clear')
    return
def story_2():
    os.system('cls' if os.name == 'nt' else 'clear')
    return
def day2Interface():
    os.system('cls' if os.name == 'nt' else 'clear')

def runGame():
    intro()
    naming()
    story_1()
    day1Interface()

#Run the Game
runGame()

#Stuff for debugging
#intro()
#naming()
#story_1()
#day1Interface()
          
    
    
