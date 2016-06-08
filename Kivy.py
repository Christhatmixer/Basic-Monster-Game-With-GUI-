


__author__ = 'Christian Farley'

import random
import os


try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *   #

import sys
import time
import csv

'''Set up main window and loop
   create dice roll function,main variables,and character stats
   simulate basic game'''
# Items
# Monsters
monster = {"health":100,"expGiven":10}


# Player = {"health":100,"Exp":0,"Lvl":1,"Weapon":"hands","Armour":"Robe"} # Player health
inventory = []


reader = csv.reader(open("saveFile.csv"))
Player = {}
for row in reader:
    key = row[0]
    if key in Player:
        # implement your duplicate row handling here
        pass
    Player[key] = row[1]
    print(Player[key])
    
Player["health"] = 100
Player["Lvl"] = int(Player["Lvl"])
Player["Exp"] = int(Player["Exp"])
Player["Atk"] = 0


# main Window
root = Tk()
root.geometry("200x200")
root.resizable(width=False,height=False)
root.title("Monster Game")
pHealth = StringVar(root)
mHealth = StringVar(root)

pHealth.set(Player["health"])
mHealth.set(monster["health"])



# Item drops
def itemDrop():
    chance = random.randint(0,100)
    if "sword" not in inventory:
        if chance <= 9:
            inventory.append("Sword")
            print("You have found a sword!")
        else:
            pass
    if "shield" not in inventory:
        if 10 >= chance <= 29:
            inventory.append("shield")
            print("You have found")
        else:
            pass
    if "shiny dagger" not in inventory:
        if 30 >= chance <= 49:
            inventory.append("shiny dagger")
            print("You have found a shiny dagger!")
        else:
            pass
    else:
        print(" ")








def Press(): #callback for button. simulates Die roll
      die = random.randrange(1,20)
      if die == 1:
          Player["health"] = Player["health"] - 20
          pHealth.set(Player["health"])
          print("The monster hits you for 20 points of damage!")
          if Player["health"] <= 0:
            Die.config(state=DISABLED)
            print("YOU WERE SLAIN")
      elif die == 20:
          monster["health"] = monster["health"] - 20
          mHealth.set(monster["health"])
          print("Perfect Hit! The monster can not attack and you do 20 damage!")
          if monster["health"] <= 0:
            Die.config(state=DISABLED)
            print("YOU HAVE SLAIN THE MONSTER")
      else:
          monster["health"] = monster["health"] - die
          mHealth.set(monster["health"])
          returnDamage = 20-die
          Player["health"] = Player["health"] - returnDamage
          pHealth.set(Player["health"])
          print("You hit the monster for" + " " + str(die) +" "+ "Points of damage")
          print("The monster hits you for" + " " + str(returnDamage)+ " " + "points of damage")
          if Player["health"] <= 0: #Player death
            Die.config(state=DISABLED)
            print("YOU WERE SLAIN")
          elif monster["health"] <= 0: #Monster death
            Die.config(state=DISABLED)
            print("YOU HAVE SLAIN THE MONSTER")
            print(itemDrop())
            Player["health"] = 100
            monster["health"] = 100
            root.destroy()
            print(statusWindow())
          elif monster["health"] and Player["health"] <= 0:
              print("YOU BOTH FALL")

def Save():
    saveFile = csv.writer(open("saveFile.csv", "w"))
    for key, val in Player.items():
        saveFile.writerow([key, val])





#Player health
PlayerName = Label(root, text="Player Health",underline=0)
PlayerName.grid(row=1, column=1)
PlayerHealth = Label(root, textvariable=pHealth, fg="green", bg="white")
PlayerHealth.grid(row=2, column=1)


#Monster Health
MonsterName = Label(root, text="Monster Health",underline=0)
MonsterName.grid(row=1,column=6)
MonsterHealth = Label(root, textvariable=mHealth, fg="green",padx=38)
MonsterHealth.grid(row=2, column=6)

#Die button
Die = Button(root, text="Roll", command=Press)
Die.grid(row=3, column=2)

if Player["health"] <= 0:
    Die.config(state=DISABLED)
    print("YOU WERE SLAIN")



def statusWindow():
    print("Use Equip(item) to equip different items")
    info = Tk()
    info.geometry("300x350")
    info.resizable(width=False,height=False)
    info.title("Status")
    LevelGUI = StringVar(info)
    WeaponGUI = StringVar(info)
    ArmourGUI = StringVar(info)

    LevelGUI.set(Player["Lvl"])
    WeaponGUI.set(Player["Weapon"])
    ArmourGUI.set(Player["Armour"])

    Level = Label(info, text="Level",underline=0)
    Level.grid(row=1, column=2)
    currentLevel = Label(info, textvariable=LevelGUI,)
    currentLevel.grid(row=2, column=2)

    Weapon = Label(info, text="Weapon")
    Weapon.grid(row=3,column=1)
    currentWeapon = Label(info, textvariable=WeaponGUI, fg="green", bg="white")
    currentWeapon.grid(row=4, column=1)

    Armour = Label(info, text="Armour")
    Armour.grid(row=5,column=1)
    currentArmour = Label(info, textvariable=ArmourGUI, fg="green", bg="white")
    currentArmour.grid(row=6, column=1)

    Items = Listbox(info)
    Items.grid(row=8,column=1)


    for item in inventory:
        Items.insert(END,item)

    print("inventory")
    print(inventory)

    saveButton = Button(info, text="Save", command=Save)
    saveButton.grid(row=3, column=3)


    def Again():
        info.destroy()
        fightSetup()

    def Equip(item):
        if item in inventory:
            if item == "sword":
                Player["Weapon"] = "sword"
                Player["Atk"] = Player["Atk"] + 10
            elif item == "shiny dagger":
                Player["Weapon"] = "shiny dagger"
                Player["Atk"] = Player["Atk"] + 1
            elif item == "shield":
                Player["Armour"] = "shield"
                Player["Def"] = 1





    Battle = Button(info,text="Fight!",command=Again)
    Battle.grid(row=3,column=4)









def fightSetup():
    root = Tk()
    root.geometry("200x200")
    root.resizable(width=False,height=False)
    root.title("Monster Game")
    pHealth = StringVar(root)
    mHealth = StringVar(root)

    pHealth.set(Player["health"])
    mHealth.set(monster["health"])

    # Player stat handling
    if Player["Exp"] >= 20:
        Player["Lvl"] = Player["Lvl"] + 1

    # Item drops
    def itemDrop():
        chance = random.randrange(100)
        if "sword" not in inventory:
            if chance <= 9:
                inventory.append("Sword")
                print("You have found a sword!")
        if "shield" not in inventory:
            if 10 >= chance <=29:
                inventory.append("shield")
                print("You have found")
        if "shiny dagger" not in inventory:
            if 30 >= chance <= 49:
                inventory.append("shiny dagger")
                print("You have found a shiny dagger!")
        else:
            print(" ")








    def Press(): #callback for button. simulates Die roll
          die = random.randrange(1,20)
          if die == 1:
              Player["health"] = Player["health"] - 20
              pHealth.set(Player["health"])
              print("The monster hits you for 20 points of damage!")
              if Player["health"] <= 0:
                Die.config(state=DISABLED)
                print("YOU WERE SLAIN")
          elif die == 20:
              monster["health"] = monster["health"] - 20
              mHealth.set(monster["health"])
              print("Perfect Hit! The monster can not attack and you do 20 damage!")
              if monster["health"] <= 0:
                Die.config(state=DISABLED)
                print("YOU HAVE SLAIN THE MONSTER")
          else:
              monster["health"] = monster["health"] - (die + Player["Atk"])
              mHealth.set(monster["health"])
              returnDamage = 20-die
              Player["health"] = Player["health"] - (returnDamage - Player["Def"])
              pHealth.set(Player["health"])
              print("You hit the monster for" + " " + str(die) +" "+ "Points of damage")
              print("The monster hits you for" + " " + str(returnDamage)+ " " + "points of damage")
              if Player["health"] <= 0: #Player death
                Die.config(state=DISABLED)
                print("YOU WERE SLAIN")
              elif monster["health"] <= 0: #Monster death
                Die.config(state=DISABLED)
                print("YOU HAVE SLAIN THE MONSTER")
                print(itemDrop())
                Player["health"] = 100
                monster["health"] = 100
                Player["Exp"] = Player["Exp"] + 10
                print(statusWindow())
                root.destroy()
              elif monster["health"] and Player["health"] <= 0:
                  print("YOU BOTH FALL")







    #Player health
    PlayerName = Label(root, text="Player Health",underline=0)
    PlayerName.grid(row=1, column=1)
    PlayerHealth = Label(root, textvariable=pHealth, fg="green", bg="white")
    PlayerHealth.grid(row=2, column=1)


    #Monster Health
    MonsterName = Label(root, text="Monster Health",underline=0)
    MonsterName.grid(row=1,column=6)
    MonsterHealth = Label(root, textvariable=mHealth, fg="green",padx=38)
    MonsterHealth.grid(row=2, column=6)

    #Die button
    Die = Button(root, text="Roll", command=Press)
    Die.grid(row=3, column=2)

    if Player["health"] <= 0:
        Die.config(state=DISABLED)
        print("YOU WERE SLAIN")

    root.mainloop()




root.mainloop()
