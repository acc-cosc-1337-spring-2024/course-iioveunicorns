#

import repetition

print('Homework 3 Menu\n'
      '1-Factorial\n'
      '2-Sum Odd Numbers\n'
      '3-Exit\n')

menu_select = int(input('Select one of the options: '))

while menu_select == 1 or menu_select == 2 or menu_select == 3:

    if menu_select == 1:
        factorial = int(input('Please enter a number to receive the factorial of (between 0-10): '))
        if factorial < 0 or factorial > 10:
            while factorial <0 or factorial >10:
                factorial = int(input('Invalid Number selected, use 1-10: '))
        result = repetition.get_factorial(factorial)
        print('The Factorial of the number is: ', result)
        menu_cont = input('Would you like to choose another option? (Y or N) ' )
        if menu_cont == 'y':
            menu_select = int(input('Please select another number from Homework Menu: '))
        else:
            menu_select = 'Exit'
    
    elif menu_select == 2:
        total_sum = int(input('Please enter a number to receive the sum of the odd factors (between 0-100): '))
        if total_sum < 0 or total_sum > 100:
            while total_sum < 0 or total_sum > 100:
                total_sum = int(input('Invalid number selected, use 1-100: '))

        result = repetition.sum_odd_numbers(total_sum)
        print('The sum of all odd factors is: ', result)

        menu_cont = input("Would you like to choose another option? (Y or N): ")
        if menu_cont == 'y':
            menu_select = int(input('Please select another number from Homework Menu: '))
        else: 
            menu_select = 'Exit'
        
    else: 
        menu_cont = input('Are you sure you would like to exit? (Y or N): ')
        if menu_cont == 'n':
            menu_select = int(input('Please select another number from Homework Menu'))
        else:
            menu_select = 'Exit'

print("Thank you, Goodbye.")

