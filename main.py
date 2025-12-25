# --- Python Objects & Generators ---
def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result 

my_list = make_list(100)
# print(my_list) # Commented out to focus on the game

def generator_function(num): # Fixed the "ı" character
    for i in range(num):
        yield i*2  #burada fonkyon ı yi verip duracak, taki biz devam et diyene kadar.


# --- GAME START ---
name = input("What is your name? ")
print("helloooo " + name + '!')

answer = input("    Are you ready for adventure? Y/N ").upper()

if answer == "Y":
    print("Ooo Yeaa")
else:
    print("too bad")

print('You enter the dungeon...')

Race = input('    Select your race (Human, Elf, Dwarf): ').strip()
Class = input('    Select your class (Mage, Knight, Rider): ').strip()

# Decorator for the character intro
def my_decorator(func):
    def wrap_func():
        print('\n********')
        func()
        print('********\n')
    return wrap_func 

@my_decorator
def hey():
    print(name + ' The ' + Race + " " + Class + "!! Good choice.")

hey()

# --- Adventure Logic ---
print(name + "!!!" + ' The dungeon is dark, very dark.')
print("You light your torch.")
print('There is a small hole on your right.')

hole = input("    Would you like to enter the hole? Y/N ").upper()

# Initialize variables to prevent "Variable not defined" errors
small_key = False
amulet = False

if hole == "Y":
    if Race.lower() == "dwarf":
        print('As a Dwarf, you fit into the hole.')
        print('There is a small box inside...')
        print('You find a small key!')
        small_key = True
    else:
        print('You are too tall to fit into that hole.')
else:
    print("You continue your journey into the depths of the dungeon.")

print("While continuing your journey...")

door = input('    There is a door on your right, would you like to open it? Y/N ').upper() 

if door == "Y":
    if small_key:
        print('By using the small key, the door opens!')
        print('There is a strange amulet floating in the air. You take it.')
        amulet = True
    else:
        print('The door is locked. You do not have the key.') 
else:
    print('You continue into the darkness.')

magic_door = input('   There is a strange magical door in front of you. Open it? Y/N ').upper() 

if magic_door == "Y":
    if amulet:
        print('You used the amulet to open the door! You win!')
    elif Class.lower() == 'mage':
        print('As a Mage, you used your magic powers to open the door!')
    elif Class.lower() in ['knight', 'rider']:
        print('You have neither an amulet nor magical powers to open that door!')
    else:
        print('The door remains shut.')
else:
    print('Wondering what is behind the door, you continue deep into the dungeon.')