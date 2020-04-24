import random
import time
from colorama import Fore, Back, Style
from functions import *

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

WhenOpened()
OpenShop()
TavernOptions()
