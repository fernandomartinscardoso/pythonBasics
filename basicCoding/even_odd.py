from random import randint
print('\033[32m-=-\033[m'*9)
print("\033[31mLet's play odds and evens\033[m")
print('\033[32m-=-\033[m'*9)
ch = str(input('Type your choice (odd or even): '))
choice = ch.lower()

if choice == 'odd':
    fingers = int(input('How many fingers will you extend? '))
    if fingers > 5:
        print('Invalid option! Maximum of fingers allowed is 5.')
    else:
        comp = randint(0, 5)
        print('Computer extended {} fingers.'.format(comp))
        comb = fingers + comp
        if comb % 2 == 0:
            print('Sorry! You lose!')
        else:
            print('Congrats! You win!')
elif choice == 'even':
    fingers = int(input('How many fingers will you extend? '))
    if fingers > 5:
        print('Invalid option! Maximum of fingers allowed is 5.')
    else:
        comp = randint(0, 5)
        print('Computer extended {} fingers.'.format(comp))
        comb = fingers + comp
        if comb % 2 == 1:
            print('Sorry! You lose!')
        else:
            print('Congrats! You win!')
else:
    print('Invalid choice.')
