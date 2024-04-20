#
from class_a import die
power = 1
dice = die()

def selectMenu(select):
    try:
        (int(select)==1 or int(select)==2)
        if int(select)==1:
            return(2)
        elif int(select)==2:
            return(3)
        else:
            print('Invalid selection')
            return(1)
        
    except:
        print('Invalid selection')
        return(1)
    
def quitMenu(select):
    try:
        if select.upper()=='Y' or select.upper()=='N' or select=='1' or select=='2':
            if(select=='1' or select.upper()=='Y'):
                return(0)
            elif(select=='2' or str(select).upper()=='N'):
                return(1)
            else:
                print('Invalid Selection')
                return(1)
        else:
            print('Invalid Selection')
            return(1)
    except:
        print('Invalid selection')
        return(1)
    
while power ==1:
    print('DICE ROLL MENU')
    print('')
    print('1 - Roll Dice')
    print('2 = Quit')
    print('_____')
    print('')
    select = input('')
    power = selectMenu(select)
    while power ==2:
        print('')
        dice.roll()
        print(dice)
        print('')
        print('1 to re-roll, 2 to exit')
        print('_____')
        print('')
        select =input('')
        power = selectMenu(select)

    while power == 3:
        print('')
        print('Would you like to exit?')
        print('Confirm = Y or 1, to cancel N or 2')
        print('')
        select = input('')
        power = quitMenu(select)
