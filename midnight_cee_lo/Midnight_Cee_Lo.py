import random
import time
import bisect


def intro():

    print('{:^80}'.format('*======================*'))
    print('{:^80}'.format('|    Midnight Cee-lo   |'))
    print('{:^80}'.format('*======================*'))
    print('\n{:^80}'.format('Created By Valentin Cain'))
    print('{:^80}'.format('2018'))

    print('\n\n\nWarming Up The Dice', end='')
    time.sleep(.3)
    print('.', end='')
    time.sleep(.3)
    print('.', end='')
    time.sleep(.3)
    print('.', end='')
    time.sleep(.3)
    print('.', end='')
    time.sleep(.3)
    print('.', end='')
    time.sleep(.3)
    print('.', end='')
    time.sleep(.3)
    print('.', end='')
    time.sleep(.3)


    while True:
        instructions = input('\n\nShow Instructions? [y/n]: ').upper()
        if instructions == "Y":
            print(' \n  In this version of Cee-lo, each round involves 3 players. A bet of $100 is\n automatically put into the pot from '
                  'each player at the beginning of the\n round. Each player then will roll all three dice at once and must continue\n until a '
                  'recognized combination is rolled or they have rolled 3 times. If the\n player has not rolled a recognized combination after 3 rolls, they will\n receive a 0 for the round. Whichever player rolls the best combination\n wins the entire pot, and a '
                  'new round begins. In cases where two or more\n players tie for the best combination, the pot will be split '
                  'accordingly.\n \n The combinations are and can be ranked from best to worst as:\n\n'
                    ' 4-5-6:\n '
                    'The highest possible roll. If you roll 4-5-6, you win the pot and receive a\n bonus $100 from each player.\n\n '
                    'Trips:\n '
                    'Rolling three of the same number is known as rolling "trips". Higher trips\n beat lower trips, so 4-4-4 '
                    'is better than 3-3-3. Any trips beats any\n established point.\n\n '
                    'Point:\n '
                    'Rolling a pair, and another number, establishes the singleton as a "point".\n A higher point beats a '
                    'lower point, so 2-2-6 (6) is better than 5-5-2 (2).\n\n '
                    '1-2-3:\n '
                    'The lowest possible roll. If you roll 1-2-3, you must pay both players $100\n at the end of the round. '
                    '\n\n Any other roll is a meaningless combination and the player can re-roll until\n one of the above combinations occurs or 3 attempts have been made.')

            break
        elif instructions == 'N':
            break
        else:
            print('\nInvalid Entry')
            continue

intro()

player1_name = input("\nEnter Your Name: ").strip()
player2_name = ['Ashy Larry', 'Tron', 'Daquan', 'White Boy Rick', 'Scumbag Steve', 'Mr. Trips', 'Aiko', 'Filthy Frank', 'BBQ Becky']
player3_name = ['Mr. Peanut', 'Moneybags Miyagi', 'Fatboy Frank', 'Dirty Dick', 'Meegan', 'Shifty Charlene', 'Jasper Jr.']

random.shuffle(player2_name)
random.shuffle(player3_name)

player1 = player1_name
player2 = player2_name[0]
player3 = player3_name[0]


player1_money = 1000
player2_money = 1000
player3_money = 1000



while True:

    win1 = 0
    win2 = 0
    win3 = 0

    if player1_money < 100:
        print('Go Home ' + player1_name + ', You\'re Broke! ')
        break
    if player2_money < 100:
        if len(player2_name) > 1:
            print(player2 + ' Left The Game!\n')
            del player2_name[0]
            player2 = player2_name[0]
            player2_money = 1000
        elif len(player2_name) <= 1:
            print(player2 + ' Left The Game!\n')
            print('No More Players Around. Come Back Later ' + player1 + '!')
            break
    if player3_money < 100:
        if len(player3_name) > 1:
            print(player3 + ' Left The Game!\n')
            del player3_name[0]
            player3 = player3_name[0]
            player3_money = 1000
        elif len(player3_name) <= 1:
            print(player3 + ' Left The Game!\n')
            print('No More Players Around. Come Back Later ' + player1 + '!')
            break




    print('\n')
    print(player1 + ":${}".format(player1_money), end=" | ")
    print(player2 + ":${}".format(player2_money),end=" | ")
    print(player3 + ":${}".format(player3_money) + "\n")




    def bet():
      # input('Press Enter To Place Bet: ')
        global player1_money
        global player2_money
        global player3_money
        player1_money -= 100
        player2_money -= 100
        player3_money -= 100


    bet()
    print('Collecting $100 Bet From Each Player...\n')
    time.sleep(1)




    player1_dice = []
    player2_dice = []
    player3_dice = []



    def player1_roll():
        rolls = 3
        success = False
        while rolls > 0 and success is False:
            rolls -= 1
            d1 = (random.randint(1, 6))
            d2 = (random.randint(1, 6))
            d3 = (random.randint(1, 6))
            dice = d1, d2, d3
            input("Hit 'Enter' Key To Roll Dice: ")
            bisect.insort(player1_dice, d1)
            bisect.insort(player1_dice, d2)
            bisect.insort(player1_dice, d3)

            for number in dice:
                print(number, end=' ')
                time.sleep(.25)

            #return d1, d2, d3

            if player1_dice[0] == player1_dice[1] == player1_dice[2]:
                print(
                    "\n" + player1 + ' Rolled: Trips {}!!'.format(player1_dice[0]))
                success = True
                return int(str(player1_dice[0]) + str(player1_dice[1]) + str(player1_dice[2]))

            elif player1_dice[0] == player1_dice[1] or player1_dice[1] \
                    == player1_dice[2]:
                if player1_dice[0] == player1_dice[1]:
                    print('\n' + player1 + ' Rolled: {}'.format(player1_dice[2]))
                    return player1_dice[2]
                elif player1_dice[1] == player1_dice[2]:
                    print('\n' + player1 + ' Rolled: {}'.format(player1_dice[0]))
                    return player1_dice[0]
                success = True


            elif player1_dice == [4, 5, 6]:
                print("\n" + player1 + " Rolled: 4 - 5 - 6!!!")
                success = True
                return 777

            elif player1_dice == [1, 2, 3]:
                print("\n" + player1 + " Rolled: 1 - 2 - 3, Ouch!!")
                success = True
                return 888
            else:
                del player1_dice[:]
                print('\n\nNo Point Roll\n')


        if rolls == 0:
            print(player1 + ' Is Out Of Rolls')
            return 0


    def player2_roll():
        rolls = 3
        success = False
        while rolls > 0 and success is False:
            rolls -= 1
            d1 = (random.randint(1, 6))
            d2 = (random.randint(1, 6))
            d3 = (random.randint(1, 6))
            dice = d1, d2, d3
            print(player2 + " Rolling Dice... ")
            bisect.insort(player2_dice, d1)
            bisect.insort(player2_dice, d2)
            bisect.insort(player2_dice, d3)

            for number in dice:
                print(number, end=' ')
                time.sleep(.25)

            #return d1, d2, d3

            if player2_dice[0] == player2_dice[1] == player2_dice[2]:
                print("\n" + player2 + ' Rolled: Trips {}!!'.format(player2_dice[0]))
                success = True
                return int(str(player2_dice[0]) + str(player2_dice[1]) + str(player2_dice[2]))

            elif player2_dice[0] == player2_dice[1] or player2_dice[1] \
                    == player2_dice[2]:
                if player2_dice[0] == player2_dice[1]:
                    print('\n' + player2 + ' Rolled: {}'.format(player2_dice[2]))
                    return player2_dice[2]
                elif player2_dice[1] == player2_dice[2]:
                    print('\n' + player2 + ' Rolled: {}'.format(player2_dice[0]))
                    return player2_dice[0]
                success = True


            elif player2_dice == [4, 5, 6]:
                print("\n" + player2 + " Rolled: 4 - 5 - 6!!!")
                success = True
                return 777

            elif player2_dice == [1, 2, 3]:
                print("\n" + player2 + " Rolled: 1 - 2 - 3, Ouch!!")
                success = True
                return 888

            else:
                del player2_dice[:]
                print('\n\nNo Point Roll\n')
                time.sleep(1)
        if rolls == 0:
            print(player2 + ' Is Out Of Rolls')
            return 0

    def player3_roll():
        rolls = 3
        success = False
        while rolls > 0 and success is False:
            rolls -= 1
            d1 = (random.randint(1, 6))
            d2 = (random.randint(1, 6))
            d3 = (random.randint(1, 6))
            dice = d1, d2, d3
            print(player3 + " Rolling Dice... ")
            bisect.insort(player3_dice, d1)
            bisect.insort(player3_dice, d2)
            bisect.insort(player3_dice, d3)

            for number in dice:
                print(number, end=' ')
                time.sleep(.25)

            #return d1, d2, d3

            if player3_dice[0] == player3_dice[1] == player3_dice[2]:
                print("\n" + player3 + ' Rolled: Trips {}!!'.format(player3_dice[0]))
                success = True
                return int(str(player3_dice[0]) + str(player3_dice[1]) + str(player3_dice[2]))

            elif player3_dice[0] == player3_dice[1] or player3_dice[1] \
                    == player3_dice[2]:
                if player3_dice[0] == player3_dice[1]:
                    print('\n' + player3 + ' Rolled: {}'.format(player3_dice[2]))
                    return player3_dice[2]
                elif player3_dice[1] == player3_dice[2]:
                    print('\n' + player3 + ' Rolled: {}'.format(player3_dice[0]))
                    return player3_dice[0]
                success = True


            elif player3_dice == [4, 5, 6]:
                print("\n" + player3 + " Rolled: 4 - 5 - 6!!!")
                success = True
                return 777

            elif player3_dice == [1, 2, 3]:
                print("\n" + player3 + " Rolled: 1 - 2 - 3, Ouch!!")
                success = True
                return 888

            else:
                del player3_dice[:]
                print('\n\nNo Point Roll\n')
                time.sleep(1)
        if rolls == 0:
            print(player3 + ' Is Out Of Rolls')
            return 0


    while True:


        roll1 = player1_roll()
        time.sleep(2)
        print('\n')


        roll2 = player2_roll()
        time.sleep(2)
        print('\n')

        roll3 = player3_roll()
        time.sleep(2)
        print('\n')
        break


    if roll1 != 777 and roll1 != 888:
        if roll1 > roll2 and roll1 > roll3:
            win1 += 300
            win2 -= 0
            win3 -= 0
        elif roll1 > roll3 and roll1 == roll2:
            win1 += 150
            win3 -= 0
            win2 += 150

    if roll2 != 777 and roll2 != 888:
        if roll2 > roll1 and roll2 > roll3:
            win2 += 300
            win1 -= 0
            win3 -= 0
        elif roll2 > roll1 and roll2 == roll3:
            win2 += 150
            win3 += 150
            win1 += 0

    if roll3 != 777 and roll3 != 888:
        if roll3 > roll2 and roll3 > roll1:
            win3 += 300
            win1 -= 0
            win2 -= 0
        elif roll3 > roll2 and roll3 == roll1:
            win3 += 150
            win1 += 150
            win2 += 0

    if roll1 == roll2 and roll2 == roll3:
        win3 += 100
        win1 += 100
        win2 += 100



    elif roll1 == 777:
        win1 += 500
        win2 -= 100
        win3 -= 100
        if roll2 == 777:
            win1 -= 250
            win2 += 350
            win3 -= 100
        elif roll3 == 777:
            win1 -= 250
            win3 += 350
            win2 -= 100
        if roll2 == 888:
            win3 += 100
            win1 += 100
            win2 -= 200
            if roll3 == 888:
                win3 -= 200
                win1 += 100
                win2 += 100
        elif roll3 == 888:
            win1 += 100
            win3 -= 200
            win2 += 100

    elif roll2 == 777:
        win2 += 500
        win1 -= 100
        win3 -= 100
        if roll3 == 777:
            win1 -= 100
            win3 += 350
            win2 -= 250
        if roll1 == 888:
            win3 += 100
            win2 += 100
            win1 -= 200
            if roll3 == 888:
                win3 -= 200
                win1 += 100
                win2 += 100
        elif roll3 == 888:
            win2 += 100
            win3 -= 200
            win1 += 100

    elif roll3 == 777:
        win3 += 500
        win1 -= 100
        win2 -= 100
        if roll2 == 888:
            win3 += 100
            win1 += 100
            win2 -= 200
            if roll1 == 888:
                win1 -= 200
                win3 += 100
                win2 += 100
        elif roll1 == 888:
            win2 += 100
            win1 -= 200
            win3 += 100



    elif roll1 == 888:
        if roll2 == 888:
            win1 -= 100
            win3 += 100
            win2 -= 100
            if roll3 == 0:
                win1 += 100
                win3 += 200
                win2 += 100
            elif roll3 < 667:
                win3 += 400
                win1 -= 0
                win2 -= 0

        elif roll2 > roll3 and roll2 != 888:
            win1 -= 200
            win2 += 400
            win3 += 100
        elif roll3 > roll2 and roll3 != 888:
            win1 -= 200
            win3 += 400
            win2 += 100
        elif roll2 == 0 and roll3 == 0:
            win1 -= 100
            win2 += 200
            win3 += 200
        elif roll2 == roll3:
            win1 -= 200
            win2 += 250
            win3 += 250

    elif roll2 == 888:
        if roll3 == 888:
            win2 -= 100
            win1 += 100
            win3 -= 100
            if roll1 == 0:
                win3 += 100
                win1 += 200
                win2 += 100
            elif roll1 < 667:
                    win1 += 400
                    win3 -= 0
                    win2 -= 0

        if roll1 > roll3 and roll1 != 888:
            win2 -= 200
            win1 += 400
            win3 += 100
        elif roll3 > roll1 and roll3 != 888:
            win2 -= 200
            win3 += 400
            win1 += 100
        elif roll1 == 0 and roll3 == 0:
            win2 -= 100
            win1 += 200
            win3 += 200
        elif roll1 == roll3:
            win2 -= 200
            win1 += 250
            win3 += 250


    elif roll3 == 888:
        if roll1 == 888:
            win3 -= 100
            win2 += 100
            win1 -= 100
            if roll2 == 0:
                win1 += 100
                win2 += 200
                win3 += 100
            elif roll2 < 667:
                    win2 += 400
                    win1 -= 0
                    win3 -= 0
        if roll1 > roll2 and roll1 != 888:
            win3 -= 200
            win1 += 400
            win2 += 100
        elif roll2 > roll1 and roll2 != 888:
            win3 -= 200
            win2 += 400
            win1 += 100
        elif roll1 == 0 and roll2 == 0:
            win3 -= 100
            win1 += 200
            win2 += 200
        elif roll1 == roll2:
            win3 -= 200
            win2 += 250
            win1 += 250

    print("Round Winnings/Losses:\n")

    player1_money += win1
    player2_money += win2
    player3_money += win3

    print(player1 + ": ${}".format(win1))
    print(player2 + ": ${}".format(win2))
    print(player3 + ": ${}".format(win3) + "\n")
