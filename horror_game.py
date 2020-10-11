#Horror House

def start():
    print("You are stucked in a haunted house.. you need to get out from here!! \nChoose one scare:\n1.scare1\n2.scare2")
    choice = int(input('> '))
    if choice == 1:
        scare1()
    elif choice == 2:
        scare2()
    
def scare1():
    print('You just heard someone walking...\nWhat you gonna do now...\nChoose one:\n1.go check it\n2.run away')
    choice = int(input('> '))
    run_away = 'You should not have ran without checking.'
    if choice == 1:
        go_check_it()
    elif choice == 2:
        dead(run_away)   
    exit()    

def scare2():
    print('Damn! You are just seeing a ghost, staring at you...\nWhat you gonna do now...\nChoose one:\n1.checking ghost\n2.run away')
    run_away = 'You should not have ran without checking.'
    choice = int(input('> '))
    if choice == 1:
        checking_ghost()
    elif choice == 2:
        dead(run_away) 
    exit()    

def go_check_it():
    print('So you decided to have a check...\nChoose one possibility:\n1.woman\n2.No one')
    choice = int(input('> '))
    if choice == 1:
        woman()
    elif choice == 2:
        no_one()   
    exit()    


def dead(why):
    print(why,'\nYou are Dead!!')

def victory(why_victory):    
    print(why_victory, "\nYou are saved!\nHope you liked the game.")

def woman():
    print('This woman is hot as fuck...but scarier at the same time\nWhat will you do now..\n1.run away\n2.ask her')
    choice = int(input('> '))
    run_away = 'Atleast you should have guts to ask something out.'
    if choice == 1:
        dead(run_away)
    elif choice == 2:
        ask_her()
    exit()        

def no_one():
    print('You saw nothing and had gone where you started that is \nscare2')

def ask_her():
    print(f'you are brave!\nSo you decided to ask.\nShe tells {woman_wiki}\nWhat you gonna do now:\n1.help her\n2.run away')
    choice = int(input('> '))
    run_away = 'You ran and she becomes the ghost.'
    if choice == 1:
        help_her()
    elif choice == 2:
        dead(run_away)
    exit()    

woman_wiki = "\"I too got stucked in this haunted house,i've also been finding the exit too.\""   

def help_her():
    print('You are brave and helpful...\nand you both got reached where you started that is \nscare2')

def checking_ghost():
    print('You just saw a slight presence of a someone standing right in front of you\n...\n...\n...\nFuck man! he is real.\nyou are scared as hell\nYou have three things near you\nOnly one of these thing can end that mfs career...\nChoose one:\n1.torch\n2.mirror\n3.matchstick') 
    choice = int(input('> '))
    if choice == 1:
        reason = 'Using torch smh!..u should have checked its battery!'
        dead(reason)
    elif choice == 2:
        reason2 = 'this ghost seen his own image in the mirror\nThat was the only way of defeating him.'
        victory(reason2)
    else:
        reason3 = 'while you were lighting the matchstick..\nHe just vanished'  
        dead(reason3)  



start()