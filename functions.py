import random
import time
from colorama import Fore, Back, Style

global stardust
global gold
global packs
stardust = 0
gold = 0
packs = 0

Commons = ["Fireball","Mini Fireballs","Pyroblast","Wizard's Apprentice","Find Overload!","Forked Lightning","Arcane Servant","A Spider","A Rake","Bomb","Chompy","Spikey","The Great Oak"]
Rares = ["Fire-Pult","Overload Totem","Stone Totem","Mana Totem","Mark of the Totem","Flaming Whelp","Loot Chest","Iron Defender","The Flag","Magic Swords","The Rooster"]
Epics = ["Green Fireball","Mage Fireball","Spare Fire","Totemic Smash","The Lock Picker","Replicating Totem","Bloodthirsty Blades","Annoying Challenger","Brewmaster Cho","Spectral Spider","Slime Boss","The Artist"]
Legendaries = ["The Mana Devourer","Flame Totem","Pyre The Red","Water Hydra"]
Quotes = ["Come on in and take a seat!","Welcome back! How's it going out there?","The tavern's always open for new visitors!","Don't tell the others, but I'm rooting for you.","Hello traveler! What have you been doing lately?","Ah, you look thirsty. Care to buy a drink?","And I told him - Hey! Welcome Back!"]

CollectionCommons = []
CollectionRares = []
CollectionEpics = []
CollectionLegendaries = []

def CollectionRoom():
  print("")
  WhatToSee = input(Fore.GREEN + "[System] You access your collection.\n     1 = Show Entire Collection \n     2 = Show Commons \n     3 = Show Rares \n     4 = Show Epics \n     5 = Show Legendaries \n > " + Style.RESET_ALL)
  print("")
  if WhatToSee == "1":
    print(Fore.GREEN + " [System] Here is your entire collection: " + Style.RESET_ALL)
    print("")
    print(Fore.WHITE + "-Commons-")
    for i in range(0,len(CollectionCommons)):
      print(CollectionCommons[i],end="")
      if CollectionCommons.count(CollectionCommons[i]) >= 2:
        print(" -(1 / 2)")
      else:
        print("")
    print("")
    print(Fore.YELLOW + "-Rares-")
    for i in range(0,len(CollectionRares)):
      print(CollectionRares[i],end="")
      if CollectionRares.count(CollectionRares[i]) >= 2:
        print(" -(1 / 2)")
      else:
        print("")
    print("")
    print(Fore.MAGENTA + "-Epics-")
    for i in range(0,len(CollectionEpics)):
      print(CollectionEpics[i],end="")
      if CollectionEpics.count(CollectionEpics[i]) >= 2:
        print(" -(1 / 2)")
      else:
        print("")
    print("")
    print(Fore.CYAN + "-Legendaries-")
    for i in range(0,len(CollectionLegendaries)):
      print(CollectionLegendaries[i])
    print("")
    totalCards = len(CollectionCommons) + len(CollectionRares) + len(CollectionEpics) + len(CollectionLegendaries)
    print(Fore.RED + "You have " + str(totalCards) + " cards!" + Style.RESET_ALL)
    print("")
  elif WhatToSee == "2":
    print(Fore.WHITE + "-Commons-")
    for i in range(0,len(CollectionCommons)):
      print(CollectionCommons[i],end="")
      if CollectionCommons.count(CollectionCommons[i]) >= 2:
        print(" -(1 / 2)")
      else:
        print("")
    print("")
  elif WhatToSee == "3":
    print(Fore.YELLOW + "-Rares-")
    for i in range(0,len(CollectionRares)):
      print(CollectionRares[i],end="")
      if CollectionRares.count(CollectionRares[i]) >= 2:
        print(" -(1 / 2)")
      else:
        print("")
    print("")
  elif WhatToSee == "4":
    print(Fore.MAGENTA + "-Epics-")
    for i in range(0,len(CollectionEpics)):
      print(CollectionEpics[i],end="")
      if CollectionEpics.count(CollectionEpics[i]) >= 2:
        print(" -(1 / 2)")
      else:
        print("")
    print("")
  elif WhatToSee == "5":
    print(Fore.CYAN + "-Legendaries-")
    for i in range(0,len(CollectionLegendaries)):
      print(CollectionLegendaries[i])
    print("")
  else:
    print("[Error 002 - Invalid Answer] Please Restart The Program To Continue.")
  print(Style.RESET_ALL)

def WhenOpened():
  Quote = random.choice(Quotes)
  print(Quote)

def OpenPack():
  global packs
  global stardust
  print(Fore.GREEN + "[System] Opening Pack..." + Style.RESET_ALL)
  print("")
  for i in range(0,4):
    CREL = random.randint(0,100)
    List = ""
    if CREL <= 75:
      List = Commons
      print(Fore.WHITE + "Common.",end=" ")
    elif CREL <= 90:
      List = Rares
      print(Fore.YELLOW + "Rare!",end=" ")
    elif CREL <= 99:
      List = Epics
      print(Fore.MAGENTA + "EPIC!",end=" ")
    else:
      List = Legendaries
      print(Fore.CYAN + "OOH! LEGENDARY!",end=" ")
    card = random.choice(List)
    print("You got the card '" + card + "'!" + Style.RESET_ALL)
    if CREL <= 75 and CollectionCommons.count(card) >= 2:
      stardust += 10
      print(Fore.WHITE + "     DISENCHANTED - You already have 2 of these. You get 10 stardust." + Style.RESET_ALL)
    elif CREL <= 75:
      CollectionCommons.append(card)
    elif CREL <= 90 and CollectionRares.count(card) >= 2:
      stardust += 20
      print(Fore.YELLOW + "     DISENCHANTED - You already have 2 of these. You get 20 stardust." + Style.RESET_ALL)
    elif CREL <= 90:
      CollectionRares.append(card)
    elif CREL <= 99 and CollectionEpics.count(card) >= 2:
      stardust += 40
      print(Fore.MAGENTA + "     DISENCHANTED - You already have 2 of these. You get 40 stardust." + Style.RESET_ALL)
    elif CREL <= 99:
      CollectionEpics.append(card)
    else:
      if CollectionLegendaries.count(card) >= 1:
        stardust += 250
        print(Fore.CYAN + "     DISENCHANTED - You already have 1 of these. You get 250 stardust." + Style.RESET_ALL)
      else:
        CollectionLegendaries.append(card)
  List = Rares
  print(Fore.YELLOW + "Rare!",end=" ")
  card = random.choice(List)
  print("You got the card '" + card + "'!" + Style.RESET_ALL)
  if CollectionRares.count(card) >= 2:
      stardust += 20
      print(Fore.YELLOW + "     DISENCHANTED - You already have 2 of these. You get 20 stardust." + Style.RESET_ALL)
  else:
    CollectionRares.append(card)
  print("")
  packs -= 1

def CraftingRoom():
  global stardust
  choice = 0
  while choice == 0:
    print("")
    print(Fore.GREEN + "[System] You have " + str(stardust) + " stardust. A Common costs 100, Rare is 200, Epic is 400, and Legendary is 1000" + Style.RESET_ALL)
    print("")
    whatToCraft = input(Fore.GREEN + "[System] What would you like to do? \n     1 = Craft Common \n     2 = Craft Rares \n     3 = Craft Epics \n     4 = Craft Legendaries. \n     5 = Leave \n > " + Style.RESET_ALL)
    print("")
    if stardust >= 100 and whatToCraft == "1":
      secondchoice = 0
      while secondchoice == 0:
        do = input(Fore.GREEN + "[System] What would you like to do? \n     1 = Craft \n     2 = Check Commons \n     3 = Exit Craft Commons \n > " + Style.RESET_ALL)
        print("")
        if stardust >= 100 and do == "1":
          craft = input(Fore.GREEN + "[System]  What would you like to craft? Specify the Card Name Below. \n > " + Style.RESET_ALL)
          if craft in Commons and CollectionCommons.count(craft) <= 1:
            print("[Magic] Your Card is Being Created...")
            print("")
            stardust -= 100
            print(craft + " has been added to your collection!")
            CollectionCommons.append(craft)
            print("")
          else:
            print("[Error 003] That card does not exist.")
            print("[Problem Solver] Make sure that you have everything spelled correctly. Spelling and capitalization count! If you already have two of the card, you can't craft it!")
            print("")
        elif do == "2":
          print(Fore.WHITE + "-Commons-")
          for i in range(0,len(Commons)):
            print(Commons[i] + " x" + str(CollectionCommons.count(Commons[i])))
          print(Style.RESET_ALL)
        elif do == "3":
          secondchoice = 1
        else:
          print("[Error 004] Invalid Command. Or you don't have enough stardust.")
          print("")
    elif stardust >= 200 and whatToCraft == "2":
      secondchoice = 0
      while secondchoice == 0:
        do = input(Fore.GREEN + "[System] What would you like to do? \n     1 = Craft \n     2 = Check Rares \n     3 = Exit Craft Rares \n > " + Style.RESET_ALL)
        print("")
        if stardust >= 200 and do == "1":
          craft = input(Fore.GREEN + "[System]  What would you like to craft? Specify the Card Name Below. \n > " + Style.RESET_ALL)
          if craft in Rares and CollectionRares.count(craft) <= 1:
            print("[Magic] Your Card is Being Created...")
            print("")
            stardust -= 200
            print(craft + " has been added to your collection!")
            CollectionRares.append(craft)
            print("")
          else:
            print("[Error 005] That card does not exist.")
            print("[Problem Solver] Make sure that you have everything spelled correctly. Spelling and capitalization count! If you already have two of the card, you can't craft it!")
            print("")
        elif do == "2":
          print(Fore.YELLOW + "-Rares-")
          for i in range(0,len(Rares)):
            print(Rares[i] + " x" + str(CollectionRares.count(Rares[i])))
          print(Style.RESET_ALL)
        elif do == "3":
          secondchoice = 1
        else:
          print("[Error 006] Invalid Command. Or you don't have enough stardust.")
          print("")
    elif stardust >= 400 and whatToCraft == "3":
      secondchoice = 0
      while secondchoice == 0:
        do = input(Fore.GREEN + "[System] What would you like to do? \n     1 = Craft \n     2 = Check Epics \n     3 = Exit Craft Epics \n > " + Style.RESET_ALL)
        print("")
        if stardust >= 400 and do == "1":
          craft = input(Fore.GREEN + "[System]  What would you like to craft? Specify the Card Name Below. \n > " + Style.RESET_ALL)
          if craft in Epics and CollectionEpics.count(craft) <= 1:
            print("[Magic] Your Card is Being Created...")
            print("")
            stardust -= 400
            print(craft + " has been added to your collection!")
            CollectionEpics.append(craft)
            print("")
          else:
            print("[Error 007] That card does not exist.")
            print("[Problem Solver] Make sure that you have everything spelled correctly. Spelling and capitalization count! If you already have two of the card, you can't craft it!")
            print("")
        elif do == "2":
          print(Fore.MAGENTA + "-Epics-")
          for i in range(0,len(Epics)):
            print(Epics[i] + " x" + str(CollectionEpics.count(Epics[i])))
          print(Style.RESET_ALL)
        elif do == "3":
          secondchoice = 1
        else:
          print("[Error 008] Invalid Command. Or you don't have enough stardust.")
          print("")
    elif stardust >= 1000 and whatToCraft == "4":
      secondchoice = 0
      while secondchoice == 0:
        do = input(Fore.GREEN + "[System] What would you like to do? \n     1 = Craft \n     2 = Check Legendaries \n     3 = Exit Craft Legendaries \n > " + Style.RESET_ALL)
        print("")
        if stardust >= 1000 and do == "1":
          craft = input(Fore.GREEN + "[System]  What would you like to craft? Specify the Card Name Below. \n > " + Style.RESET_ALL)
          if craft in Legendaries and CollectionLegendaries.count(craft) <= 1:
            print("[Magic] Your Card is Being Created...")
            print("")
            stardust -= 1000
            print(craft + " has been added to your collection!")
            CollectionLegendaries.append(craft)
            print("")
          else:
            print("[Error 009] That card does not exist.")
            print("[Problem Solver] Make sure that you have everything spelled correctly. Spelling and capitalization count! If you already have one of the card, you can't craft it!")
            print("")
        elif do == "2":
          print(Fore.CYAN + "-Legendaries-")
          for i in range(0,len(Legendaries)):
            print(Legendaries[i] + " x" + str(CollectionLegendaries.count(Legendaries[i])))
          print(Style.RESET_ALL)
        elif do == "3":
          secondchoice = 1
        else:
          print("[Error 010] Invalid Command. Or you don't have enough stardust.")
          print("")
    elif whatToCraft == "5":
      choice = 1
    else:
      print("[Error 011] Either you do not have enough stardust or that is an invalid command.")
      print("")


def ShowTheTavern():
  global stardust
  global gold
  global packs
  print("")
  print(Fore.GREEN + "[System] You have entered the tavern." + Style.RESET_ALL)
  print("")
  print("Hello Visitor! This is our tavern room. Here we sell drinks of all kinds - and other things as well.")
  for i in range(0,3):
    time.sleep(1)
    print(".",end="")
  time.sleep(0.5)
  print("")
  print("Oh! I almost forgot! Have your first pack, complement of the tavern!")
  packs = 1
  OpenPack()
  print("Well, now that you got your first cards, we should show you the collection room!")
  print("")
  time.sleep(2)
  print(Fore.GREEN + "[System] You enter the collection room." + Style.RESET_ALL)
  CollectionRoom()
  print("Now time for the final room! Time to view the crafting room!")
  print("")
  print(Fore.GREEN + "[System] You enter the crafting room." + Style.RESET_ALL)
  stardust = 100
  CraftingRoom()
  print("")
  print("Well, the student becomes the master! Am I right?")
  print("")
  print("I only have to tell you a few more things: \n \n     1) Remember to Save When You Exit\n     2) Extra Commons, Rares, Epics, and Legendaries will be automatically disenchanted.\n          2.5) You can only have 2 of every card in your deck. For Legendaries, only 1.\n     3) The Maximum deck size is 30 cards.\n     4) I will be giving you 15 more packs to start off.")
  packs = 15
  gold = 50
  print("")
  print("Good Luck Traveler, and make sure to stop by now and then!")
  print("")

def Save():
  Code = "" + str(gold) + ";" + str(stardust) + ";" + str(packs) + ";"
  for i in range(0,len(CollectionCommons)):
    neededCard = CollectionCommons[i]
    spotFound = ""
    for i in range(0,len(Commons)):
      if Commons[i] == neededCard:
        spotFound = i
        break
    Code = Code + str(spotFound) + ","
  Code = Code + ";"
  for i in range(0,len(CollectionRares)):
    neededCard = CollectionRares[i]
    spotFound = ""
    for i in range(0,len(Rares)):
      if Rares[i] == neededCard:
        spotFound = i
        break
    Code = Code + str(spotFound) + ","
  Code = Code + ";"
  for i in range(0,len(CollectionEpics)):
    neededCard = CollectionEpics[i]
    spotFound = ""
    for i in range(0,len(Epics)):
      if Epics[i] == neededCard:
        spotFound = i
        break
    Code = Code + str(spotFound) + ","
  Code = Code + ";"
  for i in range(0,len(CollectionLegendaries)):
    neededCard = CollectionLegendaries[i]
    spotFound = ""
    for i in range(0,len(Legendaries)):
      if Legendaries[i] == neededCard:
        spotFound = i
        break
    Code = Code + str(spotFound) + ","
  Code = Code + ";"
  Code = Code + "!"
  return Code

def LoadCode(Code):
  global gold
  global stardust
  global packs
  character = 0
  Index = ""
  while Code[character] != ";":
    Index += str(Code[character])
    character += 1
  gold = int(Index)
  character += 1
  Index = ""
  while Code[character] != ";":
    Index += str(Code[character])
    character += 1
  stardust = int(Index)
  character += 1
  Index = ""
  while Code[character] != ";":
    Index += str(Code[character])
    character += 1
  packs = int(Index)
  character += 1
  while Code[character] != ";":
    Index = ""
    while Code[character] != ",":
      Index += str(Code[character])
      character += 1
    CollectionCommons.append(Commons[int(Index)])
    character += 1
  character += 1
  while Code[character] != ";":
    Index = ""
    while Code[character] != ",":
      Index += str(Code[character])
      character += 1
    CollectionRares.append(Rares[int(Index)])
    character += 1
  character += 1
  while Code[character] != ";":
    Index = ""
    while Code[character] != ",":
      Index += str(Code[character])
      character += 1
    CollectionEpics.append(Epics[int(Index)])
    character += 1
  character += 1
  while Code[character] != ";":
    Index = ""
    while Code[character] != ",":
      Index += str(Code[character])
      character += 1
    CollectionLegendaries.append(Legendaries[int(Index)])
    character += 1
  character += 1

def OpenShop():
  print("")
  print("")
  print("")
  Load = input(Fore.GREEN + "[System] Hello. Do you have a save code?\n     1 = No\n     2 = Yes\n > " + Style.RESET_ALL)
  print("")
  if Load == "2":
    Code = input(Fore.GREEN + "[System] Please enter your save code.\n > " + Style.RESET_ALL)
    LoadCode(Code)
  elif Load == "1":
    print("Ah, a new visitor! Welcome. Let Me show you around.")
    ShowTheTavern()
  else:
    print("[Error 001 - Invalid Answer] Please Restart The Program To Continue.")

def runValidationTech(validationNumber):
  if validationNumber%2 == 0:
    return 2
  if validationNumber%1 == 1:
    return 1


def TavernOptions():
  global stardust
  global gold
  global packs
  while 1 < 2:
    print("")
    print("You have " + str(packs) + " packs.")
    print("You have " + str(stardust) + " stardust.")
    print("You have " + str(gold) + " gold.")
    print("")
    options = input(Fore.GREEN + "[System] What would you like to do? \n     1 = Open Packs \n     2 = Buy Packs \n     3 = Craft \n     4 = View Collection \n     5 = Talk to Bob, The Tavern Owner\n     6 = Redeem Gold\n     7 = Get Save Code\n     8 = Trade Gold For Stardust \n > " + Style.RESET_ALL)
    print("")
    if options == "1" and packs >= 1:
      ask = int(input(Fore.GREEN + "[System] How many packs would you like to open?\n > " + Style.RESET_ALL))
      print("")
      if ask > packs:
        print(Fore.GREEN + "[System] Sorry, but you don't have that many packs." + Style.RESET_ALL)
      elif packs >= ask:
        print(Fore.GREEN + "[System] Opening Packs..." + Style.RESET_ALL)
        print("")
        for i in range(0,ask):
          OpenPack()
          print("")
        print(Fore.GREEN + "[System] You have completed opening the packs." + Style.RESET_ALL)
      else:
        print("[Error 012] That is not a valid option.")
      print("")
    elif options == "2":
      ask = input(Fore.GREEN + "[System] Each pack costs you 100 gold. You have " + str(gold) + " gold. What would you like to do?\n     1 = Buy a Pack\n     2 = Exit Pack Buyer.\n > " + Style.RESET_ALL)
      print("")
      if ask == "1" and gold >= 100:
        count = int(input(Fore.GREEN + "[System] How many packs would you like to buy? \n > " + Style.RESET_ALL))
        if count * 100 > gold or count < 0:
          print(Fore.GREEN + "[System] You don't have enough gold to buy that." + Style.RESET_ALL)
        elif count * 100 <= gold and count >= 0:
          print(Fore.GREEN + "[System] Buying packs..." + Style.RESET_ALL)
          print("")
          for i in range(0,count):
            gold -= 100
            packs += 1
          print(Fore.GREEN + "[System] You bought " + str(count) + " packs!" + Style.RESET_ALL)
        else:
          print("[Error 013] That is not a valid number." + Style.RESET_ALL)
      elif ask == "2":
        print("", end="")
      else:
        print("[Error 014] That is not a valid option. Or you don't have enough gold." + Style.RESET_ALL)
      print("")
    elif options == "3":
      print(Fore.GREEN + "[System] Entering the crafting module..." + Style.RESET_ALL)
      print("")
      CraftingRoom()
      print(Fore.GREEN + "[System] Exiting the crafting module..." + Style.RESET_ALL)
      print("")
    elif options == "4":
      print(Fore.GREEN + "[System] Entering the collection module..." + Style.RESET_ALL)
      print("")
      CollectionRoom()
      print(Fore.GREEN + "[System] Exiting the collection module..." + Style.RESET_ALL)
      print("")
    elif options == "5":
      print("Oh! Hi! Thanks for Talking to me!")
      print("")
    elif options == "6":
      goldBonus = 0
      code = input(Fore.GREEN + "[System] Enter your gold code here:\n > " + Style.RESET_ALL)
      validationNumber = ""
      if "vd" in code:
        if "evd" in code:
          if "fevd" in code:
            if "aa129" in code:
              validationNumber = 1
            elif "aa118" in code:
              validationNumber = 2
          elif "tevd" in code:
            validationNumber = 3
        elif "vde" in code:
          validationNumber = 4
      Validating = runValidationTech(validationNumber)
      if Validating == 2:
        if "vde" in code:
          goldBonus = code.replace("vde","")
          print(Fore.GREEN + "[System] Validation Successful. You gained " + goldBonus + " gold!" + Style.RESET_ALL)
          gold += int(goldBonus)
        else:
          print(Fore.GREEN + "[Frustrated System] Stop Trying to Cheat." + Style.RESET_ALL)
    elif options == "7":
      print(Fore.GREEN + "[System] Retrieving your Save Code..." + Style.RESET_ALL)
      SaveCode = Save()
      print(Fore.GREEN + "[System] Here is your save code:" + Style.RESET_ALL)
      print("")
      print(str(SaveCode))
      print("")
    elif options == "8":
      spend = int(input(Fore.GREEN + "[System] How much would gold would you like to spend? Each 1 gold = 5 stardust.\n > " + Style.RESET_ALL))
      print("")
      if spend > gold * 5 or spend < 0:
        print("[Error 206] You don't have enough money for that.")
      elif spend <= gold * 5 and spend >= 0:
        print(Fore.GREEN + "[System] Buying stardust..." + Style.RESET_ALL)
        gold -= spend
        stardust += spend * 5