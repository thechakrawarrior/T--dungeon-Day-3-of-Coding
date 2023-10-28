print('''
*******************************************************************************
    ________________________________________________________
  /|     -_-                                             _-  |\
 / |_-_- _                                         -_- _-   -| \   
   |                            _-  _--                      | 
   |                            ,                            |
   |      .-'````````'.        '(`        .-'```````'-.      |
   |    .` |           `.      `)'      .` |           `.    |          
   |   /   |   ()        \      U      /   |    ()       \   |
   |  |    |    ;         | o   T   o |    |    ;         |  |
   |  |    |     ;        |  .  |  .  |    |    ;         |  |
   |  |    |     ;        |   . | .   |    |    ;         |  |
   |  |    |     ;        |    .|.    |    |    ;         |  |
   |  |    |____;_________|     |     |    |____;_________|  |  
   |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
   |  |  / __  ()        -|        -  |  /  __--      -   |  |
   |  | /        __-- _   |   _- _ -  | /        __--_    |  |
   |__|/__________________|___________|/__________________|__|
  /                                             _ -        lc \
 /   -_- _ -             _- _---                       -_-  -_ \


*******************************************************************************
''')
print("Welcome to Dungeon Surprise.")
print("Your mission is to defeat the Monster.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print('''
*******************************************************************************

                             __.------._              _.----.____
                           .' -|  -   . `.        .--'           `--.
                          / '.' `-. `     \     .'                   `.
                         /  /      `.  ` \ \   /                       \
                        |  /         `.  \  | |                         |
                        |  |           `.   | |    *ffffffffhhhh*       |
                        |  |.---.   .---.\  | |                         |
                        | ||>< @>) (< @><|` | |                         |
                        |  |     / \     || |  \                      .'
                        |  /   `((_))'   \ _.-' `  .-.             .-'
                        | |    /     \_.-'| |   /.'.--`-._______.-'
                        | \     _.-.-'    / |_.-' ( !!! )
                        /  \     `-'     /  |      `---(
                       /    `.  '  `-._.'   \            o__
                      / / | | `-.___.-' `-._ \          __)
                     /     '|           |  \`-._         /
                    /'  /   |           |\   ` \ `-._
                   /   __.--'           `--.__  \
                  / .-' F  J `.       .' F  J `-.\
                 /.'   J   F   `.   .'   J   F   `.
                .'     F  J      `.'      F  J     `.
              .'      J   F      (_)      J   F      `.
            .'        F  J                 F  J        `.
          .'         J   \                /    F         `.
        .'           F    `--.________.--'     J           `.
       /            /                           \            \
     .'            J                             F            `.
    /            .'|                             |`.            \
  .'           .'  F                             J  `.           `.
 /           .'    |                             |    `.           \
(          .'      J                             F_     `.          )
 \       .'         \         /       \         /._`-._   `.       /
  \      \           `       '         `       '-._`-._`-._/      /
   \      \          F                         J///,-._`-._`-._  / VK

   
*******************************************************************************
''')
move = input("The monster has used Ash blow!!! will you dodge or block?\n").lower()
if move == "dodge":
  print("You barely evaded the monsters horrible fumes!!!\n But wait!!\n")
  print('''  
  *********************************
       _    ,-,    _
 ,--, /: :\/': :`\/: :\
|`;  ' `,'   `.;    `: |
|    |     |  '  |     |.
| :  |     | pb  |     ||
| :. |  :  |  :  |  :  | \
 \__/: :.. : :.. | :.. |  )
      `---',\___/,\___/ /'
           `==._ .. . /'
                `-::-'              
 **********************************
  ''')
  move2 = input("A fist suddenly approaches you will you counter or twerk!!!\n").lower()
  if move2 == "twerk":
    move3 = input("Good thinking!! Your twerking caught the monster of guard with the GYAT effect\nThe monster offers to join you in twerking contest choose a song to twerk to:\nAntiHero\nSeven\nSavage\n").lower()
    if move3 == "antihero":
      print("You twerked anti-hero and the monster fell to the ground dead from shock. You were crushed under his body!!!\Game Over\n")
    elif move3 == "cupid":
      print("The monster commends you for having good taste but kills you because the song is not for twerking")
    elif move3 == "savage":
      print("The monster joins you to twerk. You become the new Dungeon Master\n CONGRATS ON WINNING")
    else:
      print("The monster is stunned by your lack of comprehension(type one of the options)")
  else:
    print("Your counter was ineffective and the monster slayed you!!! Dumbass\Game Over")
    
  
else:
  print("You fool! Your body melted due to the acidity of the fumes.\Game Over")


