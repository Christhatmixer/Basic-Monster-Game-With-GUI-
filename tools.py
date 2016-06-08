import random
import time
from tkinter import *
import os


def GameInit():
    root = Tk()
    root.geometry("200x200")
    root.resizable(width=False,height=False)
    root.title("Monster Game")
    pHealth = StringVar(root)
    mHealth = StringVar(root)

    pHealth.set(Player["health"])
    mHealth.set(monster["health"])

    #Player stat handling
    if Player["Exp"] >= 20:
        Player["Lvl"] = Player["Lvl"] + 1

    #Item drops
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
                root.destroy()
              elif monster["health"] and Player["health"] <= 0:
                  print("YOU BOTH FALL")

    def Save():
        saveFile = open("saveFile","W")





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
               
               
          
          
     
          
def statusWindow():
    info = Tk()
    info.geometry("300x300")
    info.resizable(width=False,height=False)
    info.title("Status")
    LevelGUI = StringVar(info)
    WeaponGUI = StringVar(info)
    ArmourGUI = StringVar(info)

    LevelGUI.set(Player["Lvl"])

    Level = Label(info, text="Level",underline=0)
    Level.grid(row=1, column=2)
    currentLevel = Label(info, textvariable=LevelGUI,)
    currentLevel.grid(row=2, column=2)


    Weapon = Label(info, textvariable=WeaponGUI, fg="green", bg="white")
    Weapon.grid(row=3, column=1)








