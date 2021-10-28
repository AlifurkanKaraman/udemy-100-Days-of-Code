print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_or_right = input("You're at a cross road. Where do you want to go? Choose 'left' or 'right'\n")

if left_or_right.lower() == "left":
  swim_or_wait = input("Here we go. You see an Island across the sea. Choose 'wait' for waiting a boat or 'Swim' to swim right away to the Island\n")

  if swim_or_wait.lower() == "wait":
    door = input("You should choose a door between 3 doors. Choose 'red' for the left, 'yellow' for the middle and 'blue' for the right door\n")

    if door.lower() == "red":
      print("OMG! There is vampire waiting for you.\nGame Over.")
    elif door.lower() == "yellow":
      print("Congratulations! You find a treasure!!! Now, you're a millionare.")
    elif door.lower() == "blue":
      print("There is a fire inside. You die.\nGame Over.")  
    else:
      print("You choose a door that doesn't exist.\nGame Over!")


  else:
    print("Ohh no there is a shark that want to eat you!\nGame Over.")  

else:
  print("You fall into a hole.\nGame Over!")