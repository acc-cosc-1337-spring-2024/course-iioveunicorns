#
import dictionary
inventory_dictionary={}

on = True
while on:
    print(' ')
    print('1- Add or Update Item')
    print('2 - Delete Item')
    print('3 - Exit')
    print( ' ')
    print(' Inventory: '+str(inventory_dictionary))
    print(' ')
    select = int(input(''))
    if select == 1:
        updateMenu = True
        while updateMenu == True:
            print('')
            widget_name = input('Enter widget name: ')
            print('')
            updateMenu_layer2 = True
            while updateMenu_layer2 == True:
                quantity = input('Enter quantity: ')
                print('')
                try:
                    quantity = int(quantity)
                    print(dictionary.add_inventory(inventory_dictionary,widget_name,quantity))
                    print('')
                    updateMenu = False
                    updateMenu_layer2 = False
                except:
                    print('Error: Quantity should be integer')
                    print('')
    elif select == 2:
        deleteMenu = True
        while deleteMenu == True:
            print('')
            widget_name = input('Enter widget name: ')
            print('')
            print(dictionary.remove_inventory_widget(inventory_dictionary,widget_name))
            deleteMenu = False
    elif select == 3:
        exitMenu = True
        while exitMenu == True:
            confirm = (input('Program will exit: y/n?: ').upper())
            if confirm == 'Y' or confirm == 'YES':
                on = False
                exitMenu = False
            elif confirm == 'N' or confirm == "NO":
                exitMenu = False
                