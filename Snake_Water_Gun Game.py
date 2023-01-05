import random

def win_game(comp, plyr):
    if(comp == plyr):
        return None
    elif(comp == 's'):
        if(plyr == 'g'):
            return True
        elif(plyr == 'w'):
            return False
    elif(comp == 'w'):
        if(plyr == 's'):
            return True
        elif(plyr == 'g'):
            return False
    elif(comp == 'g'):
        if(plyr == 'w'):
            return True
        elif(plyr == 's'):
            return False

# comp_turn = ("Computer's turn: Snake('s'), Water('w'), Gun('g')")
comp_no = random.randint(1,3)
if comp_no == 1:
    comp = 's'
elif comp_no == 2:
    comp = 'w'
elif comp_no == 3:
    comp = 'g'

plyr = input("Player's turn [Snake('s'), Water('w'), Gun('g')]: ")

win = win_game(comp, plyr)

print(f"Computer's Choice: {comp}")
print(f"Player's Choice: {plyr}")

# Winner selection:
if (win == None):
    print("The game is Tie!")
elif (win == True):
    print("Player Won!")
else:
    print("Computer Won!")