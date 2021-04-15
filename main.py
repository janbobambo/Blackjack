koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

import random
random.shuffle(koloda)

print('Play Blackjack?')
count = 0

while True:
    choice = input('Select card? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Your card %d' %current)
        count += current
        if count > 21:
            print('You lose')
            break
        elif count == 21:
            print('Congratulation, your card 21!')
            break
        else:
            print('You score %d.' %count)
    elif choice == 'n':
        print('You have %d score and you select game end.' %count)
        break
print('See you later')
