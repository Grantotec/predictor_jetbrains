from copy import copy
from random import choice


general = ''

print('''Please give AI some data to learn...
The current data length is 0, 100 symbols left''')

while len(general) < 100:
    print('Print a random string containing 0 or 1:\n')
    digits = [x for x in input() if (x == '0' or x == '1')]
    general += ''.join(digits)
    if len(general) < 100:
        print('Current data length is {}, {} symbols left'.format(len(general), 100 - len(general)))

print('\nFinal data string:\n{}\n'.format(general))
searches = ['000', '001', '010', '011', '100', '101', '110', '111']
diction = dict.fromkeys(searches)

for i in searches:
    s = copy(general)
    count_of_zero = 0
    count_of_one = 0
    while s.find(i) != -1 and 3 < len(s) != s.find(i) + 3:
        if s[s.find(i) + 3] == '1':
            count_of_one += 1
        else:
            count_of_zero += 1
        s = s[(s.find(i) + 1):]
    diction[i] = [count_of_zero, count_of_one]

print('''You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!\n''')
capital = 1000

test_string = input('Print a random string containing 0 or 1:\n')

while test_string != 'enough':
    mistake = 0
    for i in test_string:
        if i not in ['0', '1']:
            mistake += 1
    if mistake > 0:
        print('> some wrong input')
        test_string = input('\nPrint a random string containing 0 or 1:\n')
        continue
    # prediction first three characters
    max_of_triads = []
    for i in searches:
        max_of_triads.append(diction[i][0] + diction[i][1])

    # predicting whole test string
    prediction = str(searches[max_of_triads.index(max(max_of_triads))])

    k = 0  # counter for index

    # predicting
    while k < len(test_string) - 3:
        if diction[test_string[k:k + 3]][0] > diction[test_string[k:k + 3]][1]:
            prediction += '0'
        elif diction[test_string[k:k + 3]][0] < diction[test_string[k:k + 3]][1]:
            prediction += '1'
        else:
            prediction += str(choice([0, 1]))
        k += 1

    print('prediction:\n{}\n'.format(prediction))

    # checking
    n = 0  # count of right predicting
    for i in range(3, len(test_string)):
        if test_string[i] == prediction[i]:
            n += 1

    print('Computer guessed right {} out of {} symbols ({} %)'.format(n, len(prediction) - 3, round(((n / (len(prediction) - 3)) * 100), 2)))
    capital = capital - n + (len(prediction) - 3 - n)
    print('Your capital is now ${}'.format(capital))
    test_string = input('\nPrint a random string containing 0 or 1:\n')

print('Game over!')
