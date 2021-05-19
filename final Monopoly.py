from random import *
from time import *

players = []
p1 = 0
p2 = 0
p3 = 0
p4 = 0

# making player unique vars
pos_1 = 0
pos_2 = 0
pos_3 = 0
pos_4 = 0
p1_props = []
p2_props = []
p3_props = []
p4_props = []
p1_wallet = 1500
p2_wallet = 1500
p3_wallet = 1500
p4_wallet = 1500
p1_jailcard = False
p2_jailcard = False
p3_jailcard = False
p4_jailcard = False
p1_injail = False
p2_injail = False
p3_injail = False
p4_injail = False
gotojail_place_1 = 0
gotojail_place_2 = 0
gotojail_place_3 = 0
gotojail_place_4 = 0
p1_bankrupt = False
p2_bankrupt = False
p3_bankrupt = False
p4_bankrupt = False
# player individual vars end here

num_of_player = 0


def rules():
    print("Hi and welcome to Virtual Monopoly. The rules are as follows.")
    sleep(1)
    print(
        "The rules are as follows.\n The players start with $1500.\n The players may buy and sell properties.\n If "
        "you don’t have money but have properties then don’t worry mortgage one of your properties to gain money.\n "
        "If you don’t have money and don’t have properties you will be automatically kicked out of the game.\n You "
        "can go to jail  if you land on ‘Go to jail’ or get a ‘Go to jail’ card.\n You can get out of jail buy using "
        "a ‘Get out of jail’ or by paying $25.\n The ‘Get out of jail’ card is applicable only once.\n If you land on "
        "an owned property you will have to pay rent.\n The rent will be automatically deducted from your account.")


def player_names():
    global p1
    global p2
    global p3
    global p4
    global num_of_player
    num_of_player = int(input("PLEASE ENTER THE NUMBER OF PLAYERS::"))
    if num_of_player == 2:
        p1 = str(input("Please Enter the name of the first player::"))
        p2 = str(input("Please Enter the name of the second player::"))
        print("THE GAME WILL BE PLAYED BETWEEN", p1, "and", p2)
        pos_1 = 1
        pos_2 = 1
    elif num_of_player == 3:
        p1 = str(input("Please Enter the name of the first player::"))
        p2 = str(input("Please Enter the name of the second player::"))
        p3 = str(input("Please Enter the name of the third player::"))
        print("THE GAME WILL BE PLAYED BETWEEN", p1, ",", p2, "and", p3)
        pos_1 = 1
        pos_2 = 1
        pos_3 = 1
    else:
        p1 = str(input("Please Enter the name of the first player::"))
        p2 = str(input("Please Enter the name of the second player::"))
        p3 = str(input("Please Enter the name of the third player::"))
        p4 = str(input("Please Enter the name of the fourth player::"))
        print("THE GAME WILL BE PLAYED BETWEEN", p1, ",", p2, ",", p3, "and", p4)
        pos_1 = 1
        pos_2 = 1
        pos_3 = 1
        pos_4 = 1


mboard = ['waste', 'GO', 'GUWAHATI', 'COMMUNITY CHEST', 'BHUBNESHWAR', 'INCOME TAX', 'Kanpur Central Station',
          'PANAJI/GOA', 'CHANCE', 'AGRA', 'VADODRA', 'JAIL/JUST VISITING', 'LUDHIANA',
          'ELECTRIC COMPANY', 'PATNA', 'BHOPAL', 'Howrah Station', 'INDORE',
          'COMMUNITY CHEST', 'NAGPUR', 'KOCHI', 'FREE PARKING', 'LUCKNOW',
          'CHANCE', 'CHANDIGARGH', 'JAIPUR', ' Ghoom Railway Station',
          'PUNE', 'HYDRABAD', 'WATER WORKS', 'AHEMDABAD', 'GO TO JAIL',
          'KOLKATA', 'CHENNAI', 'COMMUNITY CHEST', 'BANGLORE', 'Chhatrapati Shivaji Terminal Station',
          'CHANCE', 'DELHI', 'SUPER TAX', 'MUMBAI']
prices = [0, 0, 60, 0, 60, 200, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180, 0, 180, 200, 0, 220, 0,
          220, 240, 200, 260, 260, 150, 280, 0, 300, 300, 0, 320, 200, 0, 350, 100, 400]
rent = [0.0, 0.0, 9.0, 0.0, 9.0, 0, 30.0, 15.0, 0.0, 15.0,
        18.0, 0.0, 21.0, 22.5, 21.0, 24.0, 30.0, 27.0,
        0.0, 27.0, 30.0, 0.0, 33.0, 0.0, 33.0, 36.0,
        30.0, 39.0, 39.0, 22.5, 42.0, 0.0, 45.0, 45.0,
        0.0, 48.0, 30.0, 0.0, 52.5, 0, 60.0]
forced_or_not = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0,
                 0, 0, 0, 0, 1]
comc_or_ch = [0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
              0,
              0, 2, 0, 0]
utility_posList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 1, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0]
others = [0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
          0, 0, 0]
community_chest = {
    'Advance to "Go". (Collect $200)': 3,
    'Bank error in your favor. Collect $20.': 4,
    'From sale of stock you get $50.': 5,
    'Get Out of Jail Free. Can be used when needed': 6,
    'Go to Jail. Go directly to jail. Do not pass Go, Do not collect $200.': 7,
    'Grand Opera Night. Collect $50.': 8,
    'Holiday Fund matures. Receive $100': 9,
    'Income tax refund. Collect $20.': 10,
    'It is your birthday. Collect $10.': 11,
    'Life insurance matures – Collect $100': 12,
    'Hospital Fees. Pay $50.': 13,
    'School fees. Pay $50. ': 14,
    'Receive $25 consultancy fee.': 15,
    'You are assessed for street repairs: Pay $40': 16,
    'You have won second prize in a bieng ugly contest. Pay $10.': 17,
    'You loose $100. ': 18}


def jailfunc():
    global p1_injail
    global p2_injail
    global p3_injail
    global p4_injail
    global p1_wallet
    global p2_wallet
    global p3_wallet
    global p4_wallet
    global p1_jailcard
    global p2_jailcard
    global p3_jailcard
    global p4_jailcard
    if gotojail_place_1 == 3 or gotojail_place_2 == 3 or gotojail_place_3 == 3 or gotojail_place_4 == 3:
        print('Ohh no! Bad Luck,pay 25 bucks\nOr use a "GET OUT OF JAIL CARD"')
    if p1_injail is True or p2_injail is True or p2_injail is True or p4_injail is True:
        option_select = int(input("Type 1 for giving $25,2 to use jail card::"))
        if option_select == 1:
            if p1_injail is True:
                p1_wallet -= 25
                print("25 $ have been deducted. Your current balance is ", p1_wallet)
                p1_injail = False
            elif p2_injail is True:
                p2_wallet -= 25
                print("25 $ have been deducted. Your current balance is ", p2_wallet)
                p2_injail = False
            elif p3_injail is True:
                p3_wallet -= 25
                print("25 $ have been deducted. Your current balance is ", p3_wallet)
                p4_injail = False
            elif p4_injail is True:
                p4_wallet -= 25
                print("25 $ have been deducted. Your current balance is ", p4_wallet)
                p4_injail = False
        else:
            if option_select == 2:
                if p1_injail is True:
                    if p1_jailcard is True:
                        p1_injail = False
                        p1_jailcard = False
                        print("You are now out of jail")
                    else:
                        print("You don't have a jail card")
                elif p2_jailcard is True:
                    if p2_jailcard is True:
                        p2_injail = False
                        p2_jailcard = False
                        print("You are now out of jail")
                    else:
                        print("You don't have a jail card")
                elif p3_injail is True:
                    if p3_jailcard is True:
                        p3_injail = False
                        p3_jailcard = False
                        print("You are now out of jail")
                    else:
                        print("You don't have a jail card")
                elif p4_injail is True:
                    if p4_jailcard is True:
                        p4_injail = False
                        p4_jailcard = False
                        print("You are now out of jail")
                    else:
                        print("You don't have a jail card")


def bankrupcy1():
    global p1_bankrupt
    if p1_wallet < 0 and not p1_props:
        print(p1, "Went bankrupt he has been kicked out of the game")
        p1_bankrupt = True


def bankrupcy2():
    global p2_bankrupt
    if p2_wallet < 0 and not p2_props:
        print(p2, "Went bankrupt he has been kicked out of the game")
        p2_bankrupt = True


def bankrupcy3():
    global p3_bankrupt
    if p3_wallet < 0 and not p3_props:
        print(p3, "Went bankrupt he has been kicked out of the game")
        p3_bankrupt = True


def bankrupcy4():
    global p4_bankrupt
    if p4_wallet < 0 and not p4_props:
        print(p4, "Went bankrupt he has been kicked out of the game")
        p4_bankrupt = True


def mortgage1():
    global p1_wallet
    while True:
        print(mboard[pos_1], 'is', prices[pos_1])
        choice = int(input('Press 1 to pay. Press 2 to skip::'))
        if choice == 1:
            if p1_wallet > prices[pos_1]:
                p1_wallet -= prices[pos_1]
                p1_props.append(mboard[pos_1])
                print('You are now left with', p1_wallet)
                print('You now own', p1_props)
                break
            else:
                r = int(input('You do not have enough. Press 1 to mortgage or 2 to skip::'))
                if r == 1:
                    if not p1_props:
                        print('You have nothing to pay.')
                        break
                    else:
                        y = 0
                        for char in p1_props:
                            y += 1
                        print(y)
                        for i in range(y):
                            print('Press ', i, 'to mortgage', p1_props[i])
                        m = int(input('What do you want to mortgage::'))
                        v = 0
                        for w in range(len(mboard)):
                            if mboard[w] == p1_props[m]:
                                v = w
                        p1_props.remove(p1_props[m])
                        p1_wallet += prices[v]
                        print('You are now left with', p1_wallet)
        else:
            break


def mortgage2():
    global p2_wallet
    while True:
        print(mboard[pos_2], 'is', prices[pos_2])
        choice = int(input('Press 1 to pay. Press 2 to skip::'))
        if choice == 1:
            if p2_wallet > prices[pos_2]:
                p2_wallet -= prices[pos_2]
                p2_props.append(mboard[pos_2])
                print('You are now left with', p2_wallet)
                print('You now own', p2_props)
                break
            else:
                r = int(input('You do not have enough. Press 1 to mortgage or 2 to skip::'))
                if r == 1:
                    if not p2_props:
                        print('You have nothing to pay.')
                        break
                    else:
                        y = 0
                        for char in p2_props:
                            y += 1
                        print(y)
                        for i in range(y):
                            print('Press ', i, 'to mortgage', p2_props[i])
                        m = int(input('What do you want to mortgage::'))
                        v = 0
                        for w in range(len(mboard)):
                            if mboard[w] == p2_props[m]:
                                v = w
                        p2_props.remove(p2_props[m])
                        p2_wallet += prices[v]
                        print('You are now left with', p2_wallet)
        else:
            break


def mortgage3():
    global p3_wallet
    while True:
        print(mboard[pos_3], 'is', prices[pos_3])
        choice = int(input('Press 1 to pay. Press 2 to skip::'))
        if choice == 1:
            if p3_wallet > prices[pos_3]:
                p3_wallet -= prices[pos_3]
                p3_props.append(mboard[pos_3])
                print('You are now left with', p3_wallet)
                print('You now own', p3_props)
                break
            else:
                r = int(input('You do not have enough. Press 1 to mortgage or 2 to skip::'))
                if r == 1:
                    if not p3_props:
                        print('You have nothing to pay.')
                        break
                    else:
                        y = 0
                        for char in p3_props:
                            y += 1
                        print(y)
                        for i in range(y):
                            print('Press ', i, 'to mortgage', p3_props[i])
                        m = int(input('What do you want to mortgage::'))
                        v = 0
                        for w in range(len(mboard)):
                            if mboard[w] == p3_props[m]:
                                v = w
                        p3_props.remove(p3_props[m])
                        p3_wallet += prices[v]
                        print('You are now left with', p3_wallet)
        else:
            break


def mortgage4():
    global p4_wallet
    while True:
        print(mboard[pos_4], 'a', prices[pos_4])
        choice = int(input('Press 1 to pay. Press 2 to skip::'))
        if choice == 1:
            if p4_wallet > prices[pos_4]:
                p4_wallet -= prices[pos_4]
                p4_props.append(mboard[pos_4])
                print('You are now left with', p4_wallet)
                print('You now own', p4_props)
                break
            else:
                r = int(input('You do not have enough. Press 1 to mortgage or 2 to skip::'))
                if r == 1:
                    if not p4_props:
                        print('You have nothing to pay.')
                        break
                    else:
                        y = 0
                        for char in p4_props:
                            y += 1
                        print(y)
                        for i in range(y):
                            print('Press ', i, 'to mortgage', p4_props[i])
                        m = int(input('What do you want to mortgage::'))
                        v = 0
                        for w in range(len(mboard)):
                            if mboard[w] == p4_props[m]:
                                v = w
                        p4_props.remove(p4_props[m])
                        p4_wallet += prices[v]
                        print('You are now left with', p4_wallet)
        else:
            break


def mortgagerent1():
    global pos_4
    global p4_props
    global p4_cards
    global p4_wallet
    global p4_injail
    global pos_3
    global p3_props
    global p3_cards
    global p3_wallet
    global p3_injail
    global pos_2
    global p2_props
    global p2_cards
    global p2_wallet
    global p2_injail
    global pos_1
    global p1_props
    global p1_cards
    global p1_wallet
    global p1_injail
    if mboard[pos_1] in p1_props:
        print("You already own this")
        pass
    elif mboard[pos_1] in p2_props or mboard[pos_1] in p3_props or mboard[pos_1] in p4_props:
        while True:
            print(mboard[pos_1], "'s RENT IS::", rent[pos_1])
            choice = int(input('Press 1 to pay. Press 2 to skip ::'))
            if choice == 1:
                if mboard[pos_1] in p2_props and p1_wallet > rent[pos_1]:
                    print('Pay rent to ', p2)
                    p1_wallet -= rent[pos_1]
                    print(p1, "'s current wallet balance is ::", p1_wallet)
                    p2_wallet += rent[pos_1]
                    print(p2, "'s current wallet balance is ::", p2_wallet)
                    break
                elif mboard[pos_1] in p3_props and p1_wallet > rent[pos_1]:
                    print('Pay rent to ', p3)
                    p1_wallet -= rent[pos_1]
                    print(p1, "'s current wallet balance is ::", p1_wallet)
                    p3_wallet += rent[pos_1]
                    print(p3, "'s current wallet balance is ::", p3_wallet)
                    break
                elif mboard[pos_1] in p4_props and p1_wallet > rent[pos_1]:
                    print('Pay rent to ', p4)
                    p1_wallet -= rent[pos_1]
                    print(p1, "'s current wallet balance is ::", p1_wallet)
                    p4_wallet += rent[pos_1]
                    print(p1, "'s current wallet balance is ::", p4_wallet)
                    break
                else:
                    r = int(input('You do not have enough. Press 1 to mortgage or 2 to skip::'))
                    if r == 1:
                        if not p1_props:
                            print('You have nothing to pay.')
                            pos_1 = 0
                            break
                        else:
                            y = 0
                            for char in p1_props:
                                y += 1
                            print(y)
                            for i in range(y):
                                print('Press ', i, 'to mortgage', p1_props[i])
                            m = int(input('What do you want to mortgage::'))
                            v = 0
                            for w in range(len(mboard)):
                                if mboard[w] == p1_props[m]:
                                    v = w
                            p1_props.remove(p1_props[m])
                            p1_wallet += prices[v]
                            print('You are now left with', p1_wallet)


def mortgagerent2():
    global pos_4
    global p4_props
    global p4_cards
    global p4_wallet
    global p4_injail
    global pos_3
    global p3_props
    global p3_cards
    global p3_wallet
    global p3_injail
    global pos_2
    global p2_props
    global p2_cards
    global p2_wallet
    global p2_injail
    global pos_1
    global p1_props
    global p1_cards
    global p1_wallet
    global p1_injail
    if mboard[pos_2] in p2_props:
        print("You already own this")
        pass
    elif mboard[pos_2] in p1_props or mboard[pos_2] in p3_props or mboard[pos_2] in p4_props:
        while True:
            print(mboard[pos_2], "'s RENT IS::", rent[pos_2])
            choice = int(input('Press 1 to pay. ::'))
            if choice == 1:
                if mboard[pos_2] in p1_props and p2_wallet > rent[pos_2]:
                    print('Pay rent to ', p1)
                    p2_wallet -= rent[pos_2]
                    print(p2, "'s current wallet balance is ::", p2_wallet)
                    p1_wallet += rent[pos_2]
                    print(p1, "'s current wallet balance is ::", p1_wallet)
                    break
                elif mboard[pos_2] in p3_props and p2_wallet > rent[pos_2]:
                    print('Pay rent to ', p3)
                    p2_wallet -= rent[pos_2]
                    print(p2, "'s current wallet balance is ::", p2_wallet)
                    p3_wallet += rent[pos_2]
                    print(p3, "'s current wallet balance is ::", p3_wallet)
                    break
                elif mboard[pos_2] in p4_props and p2_wallet > rent[pos_2]:
                    print('Pay rent to ', p4)
                    p2_wallet -= rent[pos_2]
                    print(p2, "Your current account wallet is ::", p2_wallet)
                    p4_wallet += rent[pos_2]
                    print(p3, "Your current account wallet is ::", p4_wallet)
                    break
                else:
                    r = int(input('You do not have enough. Press 1 to mortgage or 2 to skip::'))
                    if r == 1:
                        if not p2_props:
                            print('You have nothing to pay.')
                            pos_2 = 0
                            break
                        else:
                            y = 0
                            for char in p2_props:
                                y += 1
                            print(y)
                            for i in range(y):
                                print('Press ', i, 'to mortgage', p2_props[i])
                            m = int(input('What do you want to mortgage::'))
                            v = 0
                            for w in range(len(mboard)):
                                if mboard[w] == p2_props[m]:
                                    v = w
                            p2_props.remove(p2_props[m])
                            p2_wallet += prices[v]
                            print('You are now left with', p2_wallet)


def mortgagerent3():
    global pos_4
    global p4_props
    global p4_cards
    global p4_wallet
    global p4_injail
    global pos_3
    global p3_props
    global p3_cards
    global p3_wallet
    global p3_injail
    global pos_2
    global p2_props
    global p2_cards
    global p2_wallet
    global p2_injail
    global pos_1
    global p1_props
    global p1_cards
    global p1_wallet
    global p1_injail
    if mboard[pos_3] in p3_props:
        print("You already own this")
        pass
    elif mboard[pos_3] in p1_props or mboard[pos_3] in p2_props or mboard[pos_3] in p4_props:
        while True:
            print(mboard[pos_3], "'s RENT IS::", rent[pos_3])
            choice = int(input('Press 1 to pay. ::'))
            if choice == 1:
                if mboard[pos_3] in p1_props and p3_wallet > rent[pos_3]:
                    print('Pay rent to ', p1)
                    p3_wallet -= rent[pos_3]
                    print(p3, "Your current account wallet is ::", p3_wallet)
                    p1_wallet += rent[pos_3]
                    print(p1, "Your current account wallet is ::", p1_wallet)
                    break
                elif mboard[pos_3] in p2_props and p3_wallet > rent[pos_3]:
                    print('Pay rent to ', p2)
                    p3_wallet -= rent[pos_3]
                    print(p3, "Your current account wallet is ::", p3_wallet)
                    p2_wallet += rent[pos_3]
                    print(p2, "Your current account wallet is ::", p3_wallet)
                    break
                elif mboard[pos_3] in p4_props and p3_wallet > rent[pos_3]:
                    print('Pay rent to ', p4)
                    p3_wallet -= rent[pos_3]
                    print(p3, "Your current account wallet is ::", p3_wallet)
                    p4_wallet += rent[pos_3]
                    print(p4, "Your current account wallet is ::", p4_wallet)
                    break
                else:
                    r = int(input('You do not have enough. Press 1 to mortgage or 2 to skip::'))
                    if r == 1:
                        if not p3_props:
                            print('You have nothing to pay.')
                            pos_3 = 0
                            break
                        else:
                            y = 0
                            for char in p3_props:
                                y += 1
                            print(y)
                            for i in range(y):
                                print('Press ', i, 'to mortgage', p3_props[i])
                            m = int(input('What do you want to mortgage::'))
                            v = 0
                            for w in range(len(mboard)):
                                if mboard[w] == p3_props[m]:
                                    v = w
                            p3_props.remove(p3_props[m])
                            p3_wallet += prices[v]
                            print('You are now left with', p3_wallet)


def mortgagerent4():
    global pos_4
    global p4_props
    global p4_cards
    global p4_wallet
    global p4_injail
    global pos_3
    global p3_props
    global p3_cards
    global p3_wallet
    global p3_injail
    global pos_2
    global p2_props
    global p2_cards
    global p2_wallet
    global p2_injail
    global pos_1
    global p1_props
    global p1_cards
    global p1_wallet
    global p1_injail
    if mboard[pos_4] in p4_props:
        print('You own this.')
        pass
    elif mboard[pos_4] in p1_props or mboard[pos_4] in p2_props or mboard[pos_4] in p3_props:
        while True:
            print(mboard[pos_4], "'s RENT IS::", rent[pos_4])
            choice = int(input('Press 1 to pay. ::'))
            if choice == 1:
                if mboard[pos_4] in p1_props and p4_wallet > rent[pos_4]:
                    print('Pay rent to ', p1)
                    p4_wallet -= rent[pos_4]
                    print(p4, "Your current account wallet is ::", p4_wallet)
                    p1_wallet += rent[pos_4]
                    print(p1, "Your current account wallet is ::", p1_wallet)
                    break
                elif mboard[pos_4] in p2_props and p4_wallet > rent[pos_4]:
                    print('Pay rent to ', p2)
                    p4_wallet -= rent[pos_4]
                    print(p4, "Your current account wallet is ::", p4_wallet)
                    p2_wallet += rent[pos_4]
                    print(p2, "Your current account wallet is ::", p2_wallet)
                    break
                elif mboard[pos_4] in p3_props and p4_wallet > rent[pos_4]:
                    print('Pay rent to ', p3)
                    p4_wallet -= rent[pos_4]
                    print(p4, "Your current account wallet is ::", p4_wallet)
                    p3_wallet += rent[pos_4]
                    print(p3, "Your current account wallet is ::", p3_wallet)
                    break
                else:
                    r = int(input('You do not have enough. Press 1 to mortgage or 2 to skip::'))
                    if r == 1:
                        if not p4_props:
                            print('You have nothing to pay.')
                            pos_4 = 0
                            break
                    else:
                        y = 0
                        for char in p4_props:
                            y += 1
                            print(y)
                        for i in range(y):
                            print('Press ', i, 'to mortgage', p4_props[i])
                            m = int(input('What do you want to mortgage::'))
                            v = 0
                        for w in range(len(mboard)):
                            if mboard[w] == p4_props[m]:
                                v = w
                                p4_props.remove(p4_props[m])
                                p4_wallet += prices[v]
                                print('You are now left with', p4_wallet)


def player_1_rent():
    global p1_wallet
    global p2_wallet
    global p3_wallet
    global p4_wallet
    mortgagerent1()


def player_2_rent():
    global p1_wallet
    global p2_wallet
    global p3_wallet
    global p4_wallet
    mortgagerent2()


def player_3_rent():
    global p1_wallet
    global p2_wallet
    global p3_wallet
    global p4_wallet
    mortgagerent3()


def player_4_rent():
    global p1_wallet
    global p2_wallet
    global p3_wallet
    global p4_wallet
    mortgagerent4()


def chance1():
    global pos_1
    global p1_props
    global p1_cards
    global p1_wallet
    global p1_injail
    print('rolling....')
    sleep(1)
    dice1 = choice(range(1, 6))
    dice2 = choice(range(1, 6))
    dice = dice2 + dice1
    print('You got ', dice1, ',', dice2, 'with a total of', dice)
    print('IT OFFERS::')
    for i in community_chest:
        if community_chest[i] == dice:
            sleep(1)
            print(i)
            print("Your current wallet balance is ::", p1_wallet)
            if dice == 3:
                pos_1 = 1
                print("You have passed GO, You now recieve $200")
                p1_wallet += 200
            elif dice == 4:
                p1_wallet += 20
            elif dice == 5:
                p1_wallet += 50
            elif dice == 6:
                p1_jailcard = True
                print("YOU now have a go to jail card, YOU may use it whenever needed")
            elif dice == 7:
                p1_injail = True
                print("You are now in jail")
                jailfunc()
            elif dice == 8:
                p1_wallet += 150
            elif dice == 9:
                p1_wallet += 100
            elif i == 10:
                p1_wallet += 20
            elif dice == 11:
                print("HAPPY BIRTHDAY")
                p1_wallet += 30
            elif dice == 12:
                p1_wallet += 100
            elif dice == 13:
                p1_wallet -= 50
            elif dice == 14:
                p1_wallet -= 50
            elif dice == 15:
                p1_wallet += 25
            elif dice == 16:
                p1_wallet -= 40
            elif dice == 17:
                p1_wallet -= 10
            elif dice == 18:
                p1_wallet -= 100
            else:
                pass
    print("Your new wallet balance is ::", p1_wallet)


def chance2():
    global pos_2
    global p2_props
    global p2_cards
    global p2_wallet
    global p2_injail
    print('rolling....')
    sleep(1)
    dice1 = choice(range(1, 6))
    dice2 = choice(range(1, 6))
    dice = dice2 + dice1
    print('You got ', dice1, ',', dice2, 'with a total of', dice)
    print('IT OFFERS::')
    for i in community_chest:
        if community_chest[i] == dice:
            sleep(1)
            print(i)
            print("Your current wallet balance is ::", p2_wallet)
            if dice == 3:
                pos_2 = 0
                print("You have passed GO, You now recieve $200")
                p2_wallet += 200
            elif dice == 4:
                p2_wallet += 20
            elif dice == 5:
                p2_wallet += 50
            elif dice == 6:
                p2_jailcard = True
                print("YOU now have a go to jail card, YOU may use it whenever needed")
            elif dice == 7:
                p2_injail = True
                print("You are now in jail")
                jailfunc()
            elif dice == 8:
                p2_wallet += 150
            elif dice == 9:
                p2_wallet += 100
            elif dice == 10:
                p2_wallet += 20
            elif dice == 11:
                print("HAPPY BIRTHDAY")
                p2_wallet += 30
            elif dice == 12:
                p2_wallet += 100
            elif dice == 13:
                p2_wallet -= 50
            elif dice == 14:
                p2_wallet -= 50
            elif dice == 15:
                p2_wallet += 25
            elif dice == 16:
                p2_wallet -= 40
            elif dice == 17:
                p2_wallet -= 10
            elif dice == 18:
                p2_wallet -= 100
            else:
                pass
    print("Your new wallet balance is ::", p2_wallet)


def chance3():
    global pos_3
    global p3_props
    global p3_cards
    global p3_wallet
    global p3_injail
    print('rolling....')
    sleep(1)
    dice1 = choice(range(1, 6))
    dice2 = choice(range(1, 6))
    dice = dice2 + dice1
    print('You got ', dice1, ',', dice2, 'with a total of', dice)
    print('IT OFFERS::')
    for i in community_chest:
        if community_chest[i] == dice:
            sleep(1)
            print(i)
            print("Your current wallet balance is ::", p3_wallet)
            if dice == 3:
                pos_3 = 0
                print("You have passed GO, You now recieve $200")
                p3_wallet += 200
            elif dice == 4:
                p3_wallet += 20
            elif dice == 5:
                p3_wallet += 50
            elif dice == 6:
                p3_jailcard = True
                print("YOU now have a go to jail card, YOU may use it whenever needed")
            elif dice == 7:
                p3_injail = True
                print("You are now in jail")
                jailfunc()
            elif dice == 8:
                p3_wallet += 150
            elif dice == 9:
                p3_wallet += 100
            elif dice == 10:
                p3_wallet += 20
            elif dice == 11:
                print("HAPPY BIRTHDAY")
                p3_wallet += 30
            elif dice == 12:
                p3_wallet += 100
            elif dice == 13:
                p3_wallet -= 50
            elif dice == 14:
                p3_wallet -= 50
            elif dice == 15:
                p3_wallet += 25
            elif dice == 16:
                p3_wallet -= 40
            elif dice == 17:
                p3_wallet -= 10
            elif dice == 18:
                p3_wallet -= 100
            else:
                pass
    print("Your new wallet balance is ::", p3_wallet)


def chance4():
    global pos_4
    global p4_props
    global p4_cards
    global p4_wallet
    global p4_injail
    print('rolling....')
    sleep(1)
    dice1 = choice(range(1, 6))
    dice2 = choice(range(1, 6))
    dice = dice2 + dice1
    print('You got ', dice1, ',', dice2, 'with a total of', dice)
    print('IT OFFERS::')
    for i in community_chest:
        if community_chest[i] == dice:
            sleep(1)
            print(i)
            print("Your current wallet balance is ::", p4_wallet)
            if dice == 3:
                pos_4 = 0
                print("You have passed GO, You now recieve $200")
                p4_wallet += 200
            elif dice == 4:
                p4_wallet += 20
            elif dice == 5:
                p4_wallet += 50
            elif dice == 6:
                p4_jailcard = True
                print("YOU now have a go to jail card, YOU may use it whenever needed")
            elif dice == 7:
                p4_injail = True
                print("You are now in jail")
                jailfunc()
            elif dice == 8:
                p4_wallet += 150
            elif dice == 9:
                p4_wallet += 100
            elif dice == 10:
                p4_wallet += 20
            elif dice == 11:
                print("HAPPY BIRTHDAY")
                p4_wallet += 30
            elif dice == 12:
                p4_wallet += 100
            elif dice == 13:
                p4_wallet -= 50
            elif dice == 14:
                p4_wallet -= 50
            elif dice == 15:
                p4_wallet += 25
            elif dice == 16:
                p4_wallet -= 40
            elif dice == 17:
                p4_wallet -= 10
            elif dice == 18:
                p4_wallet -= 100
            else:
                pass
    print("Your new wallet balance is ::", p1_wallet)


dice1 = 0
dice2 = 0
dicef = 0


def dice():
    global dice1
    global dice2
    global dicef
    global gotojail_place
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print("Rolling..")
    sleep(1)
    print("First dice shows", dice1)
    print("Second dice shows", dice2)
    dicef = dice1 + dice2


# from here the players start moving
def player_1_moves():
    global pos_1
    global p1_props
    global p1_cards
    global p1_wallet
    global p1_injail
    global gotojail_place_1
    if p1_injail == False and gotojail_place_1 < 3:
        print("It's", p1, "'s Turn")
        input("Please Press ENTER to Roll the DICE")
        dice()
        pos_1 += dicef
        if pos_1 > 39:
            pos_1 -= 39
            print("You passed go, You get $200")
            p1_wallet += 200
            print("Your current account wallet is now ::", p1_wallet)
        print("YOU are now on", mboard[pos_1])
        if mboard[pos_1] in p1_props:
            print("You already own this")
            pass
        elif mboard[pos_1] in p2_props or mboard[pos_1] in p3_props or mboard[pos_1] in p4_props:
            player_1_rent()
        elif others[pos_1] == 1:
            print("You landed on", mboard[pos_1])
        elif others[pos_1] == 2:
            print("You landed on", mboard[pos_1], "You are now in jail")
            p1_injail = True
            jailfunc()
        elif forced_or_not[pos_1] == 1:
            if p1_wallet > prices[pos_1]:
                print("YOU are forced to pay here since this is", mboard[pos_1])
                print("WE are deducting", prices[pos_1], "from your wallet")
                p1_wallet -= prices[pos_1]
                print("Your current account wallet is ::", p1_wallet)
            else:
                mortgage1()
        elif utility_posList[pos_1] == 1:
            print("This is a utility", mboard[pos_1], "do you want to purchase this ?")
            p_or_not = int(
                input("Press 1. to buy else\n Press 2. to ignore and move on !\nPress 3. To view all your owned "
                      "Properties"))
            if p_or_not == 1:
                if p1_wallet > prices[pos_1]:
                    print("Congratulations on purchasing", mboard[pos_1], "\n We have deducted", prices[pos_1],
                          "From your wallet")
                    p1_wallet -= prices[pos_1]
                    print("Your current account wallet is ::", p1_wallet)
                    p1_props.append(mboard[pos_1])
                else:
                    mortgage1()
            elif p_or_not == 2:
                pass
            elif p_or_not == 3:
                print(p1_props)
        elif comc_or_ch[pos_1] == 1:
            print("You landed on", mboard[pos_1])
            chance1()
        elif comc_or_ch[pos_1] == 2:
            print("You landed on", mboard[pos_1])
            chance1()
        else:
            if pos_1 > 1:
                print("Press 1. to purchase", mboard[pos_1], "It Costs $", prices[pos_1],
                      "\nElse press 2. to ignore\nPress 3. to view all your properties.")
                p_or_not = int(input("Please Enter you Choice"))
                if p_or_not == 1:
                    if p1_wallet > prices[pos_1]:
                        print("Congratulations on purchasing", mboard[pos_1], "\nWe have deducted", prices[pos_1],
                              "From your wallet")
                        p1_wallet -= prices[pos_1]
                        print("Your current account wallet is ::", p1_wallet)
                        p1_props.append(mboard[pos_1])
                    else:
                        mortgage1()
                elif p_or_not == 2:
                    pass
                elif p_or_not == 3:
                    print(p1_props)
            else:
                print('You landed on GO')
    else:
        print('Sorry you are in jail')
        gotojail_place_1 += 1
        if gotojail_place_1 >= 3:
            p1_injail = False
            gotojail_place_1 = 0


def player_2_moves():
    global pos_2
    global p2_props
    global p2_cards
    global p2_wallet
    global p2_injail
    global gotojail_place_2
    if p2_injail == False and gotojail_place_2 < 3:
        print("It's", p2, "'s Turn")
        input("Please Press ENTER to Roll the DICE")
        dice()
        pos_2 += dicef
        if pos_2 > 39:
            pos_2 = 1
            print("You passed go, You get $200")
            p2_wallet += 200
            print("Your current account wallet is ::", p2_wallet)
        print("YOU are now on", mboard[pos_2])
        if mboard[pos_2] in p2_props:
            print("You already own this")
            pass
        elif mboard[pos_2] in p1_props or mboard[pos_2] in p3_props or mboard[pos_2] in p4_props:
            player_2_rent()
        elif others[pos_2] == 1:
            print("You landed on", mboard[pos_2])
        elif others[pos_2] == 2:
            print("You landed on", mboard[pos_2], "You are now in jail")
            p2_injail = True
            jailfunc()
        elif forced_or_not[pos_2] == 1:
            if p2_wallet > prices[pos_2]:
                print("YOU are forced to pay here since this is", mboard[pos_2])
                print("WE are deducting", prices[pos_2], "from your wallet")
                p2_wallet -= prices[pos_2]
                print("Your current account wallet is ::", p2_wallet)
            else:
                mortgage2()
        elif utility_posList[pos_2] == 1:
            print("This is a utility", mboard[pos_2], "do you want to purchase this ?")
            p_or_not = int(input("Press 1. to buy else\n Press 2. to ignore and move on !\nPress 3. To view all your "
                                 "owned "
                                 "Properties"))
            if p_or_not == 1:
                if p2_wallet > prices[pos_2]:
                    print("Congratulations on purchasing", mboard[pos_2], "\n We have deducted", prices[pos_2],
                          "From your wallet")
                    p2_wallet -= prices[pos_2]
                    print("Your current account wallet is ::", p2_wallet)
                    p2_props.append(mboard[pos_2])
                else:
                    mortgage2()
            elif p_or_not == 2:
                pass
            elif p_or_not == 3:
                print(p2_props)
        elif comc_or_ch[pos_2] == 1:
            print("You landed on", mboard[pos_2])
            chance2()
        elif comc_or_ch[pos_2] == 2:
            print("You landed on", mboard[pos_2])
            chance2()
        else:
            if pos_2 > 1:
                print("Press 1. to purchase", mboard[pos_2], "It Costs $", prices[pos_2],
                      "\nElse press 2. to ignore\nPress 3. to view all your properties.")
                p_or_not = int(input("Please Enter you Choice"))
                if p_or_not == 1:
                    if p2_wallet > prices[pos_2]:
                        print("Congratulations on purchasing", mboard[pos_2], "\nWe have deducted", prices[pos_2],
                              "From your wallet")
                        p2_wallet -= prices[pos_2]
                        print("Your current account wallet is ::", p2_wallet)
                        p2_props.append(mboard[pos_2])
                    else:
                        mortgage2()
                elif p_or_not == 2:
                    pass
                elif p_or_not == 3:
                    print(p2_props)
            else:
                print('You landed on GO')
    else:
        print('Sorry you are in jail')
        gotojail_place_2 += 1
        if gotojail_place_2 >= 3:
            p2_injail = False
            gotojail_place_2 = 0


def player_3_moves():
    global pos_3
    global p3_props
    global p3_cards
    global p3_wallet
    global p3_injail
    global gotojail_place_3
    if p3_injail == False and gotojail_place_3 < 3:
        print("It's", p3, "'s Turn")
        input("Please Press ENTER to Roll the DICE")
        dice()
        pos_3 += dicef
        if pos_3 > 39:
            pos_3 = 1
            print("You passed go, You get $200")
            p3_wallet += 200
            print("Your current account wallet is ::", p3_wallet)
        print("YOU are now on", mboard[pos_3])
        if mboard[pos_3] in p3_props:
            print("You already own this")
            pass
        elif mboard[pos_3] in p1_props or mboard[pos_3] in p2_props or mboard[pos_3] in p4_props:
            player_3_rent()
        elif others[pos_3] == 1:
            print("You landed on", mboard[pos_3])
        elif others[pos_3] == 2:
            print("You landed on", mboard[pos_3], "You are now in jail")
            p3_injail = True
            jailfunc()
        elif forced_or_not[pos_3] == 1:
            if p3_wallet > prices[pos_3]:
                print("YOU are forced to pay here since this is", mboard[pos_3])
                print("WE are deducting", prices[pos_3], "from your wallet")
                p3_wallet -= prices[pos_3]
                print("Your current account wallet is ::", p3_wallet)
            else:
                mortgage3()
        elif utility_posList[pos_3] == 1:
            print("This is a utility", mboard[pos_3], "do you want to purchase this ?")
            p_or_not = int(
                input("Press 1. to buy else\n Press 2. to ignore and move on !\n Press 3. To view your owned "
                      "properties"))
            if p_or_not == 1:
                if p3_wallet > prices[pos_3]:
                    print("Congratulations on purchasing", mboard[pos_3], "\n We have deducted", prices[pos_3],
                          "From your wallet")
                    p3_wallet -= prices[pos_3]
                    print("Your current account wallet is ::", p3_wallet)
                    p3_props.append(mboard[pos_3])
                else:
                    mortgage3()
            elif p_or_not == 2:
                pass
            elif p_or_not == 3:
                print(p3_props)
        elif comc_or_ch[pos_3] == 1:
            print("You landed on", mboard[pos_3])
            chance3()
        elif comc_or_ch[pos_3] == 2:
            print("You landed on", mboard[pos_3])
            chance3()
        else:
            if pos_3 > 1:
                print("Press 1. to purchase", mboard[pos_3], "It Costs $", prices[pos_3],
                      "\nElse press 2. to ignore\nPress 3. to view all your properties.")
                p_or_not = int(input("Please Enter you Choice"))
                if p_or_not == 1:
                    if p3_wallet > prices[pos_3]:
                        print("Congratulations on purchasing", mboard[pos_3], "\nWe have deducted", prices[pos_3],
                              "From your wallet")
                        p3_wallet -= prices[pos_3]
                        print("Your current account wallet is ::", p3_wallet)
                        p3_props.append(mboard[pos_3])
                    else:
                        mortgage3()
                elif p_or_not == 2:
                    pass
                elif p_or_not == 3:
                    print(p3_props)
            else:
                print('You are on GO')
    else:
        print('Sorry you are in jail')
        gotojail_place_3 += 1
        if gotojail_place_3 >= 3:
            p3_injail = False
            gotojail_place_3 = 0


def player_4_moves():
    global pos_4
    global p4_props
    global p4_cards
    global p4_wallet
    global p4_injail
    global gotojail_place_4
    if p4_injail == False and gotojail_place_4 < 3:
        print("It's", p4, "'s Turn")
        input("Please Press ENTER to Roll the DICE")
        dice()
        pos_4 += dicef
        if pos_4 > 39:
            pos_4 = 1
            print("You passed go, You get $200")
            p4_wallet += 200
            print("Your current account wallet is ::", p4_wallet)
        print("YOU are now on", mboard[pos_4])
        if mboard[pos_4] in p4_props:
            print('You own this.')
            pass
        elif mboard[pos_4] in p1_props or mboard[pos_4] in p2_props or mboard[pos_4] in p3_props:
            player_4_rent()
        elif others[pos_4] == 1:
            print("You landed on", mboard[pos_4])
        elif others[pos_4] == 2:
            print("You landed on", mboard[pos_4], "You are now in jail")
            p4_injail = True
            jailfunc()
        elif forced_or_not[pos_4] == 1:
            if p4_wallet > prices[pos_4]:
                print("YOU are forced to pay here since this is", mboard[pos_4])
                print("WE are deducting", prices[pos_4], "from your wallet")
                p4_wallet -= prices[pos_4]
                print("Your current account wallet is ::", p4_wallet)
            else:
                mortgage4()
        elif utility_posList[pos_4] == 1:
            print("This is a utility", mboard[pos_4], "do you want to purchase this ?")
            p_or_not = int(
                input("Press 1. to buy else\n Press 2. to ignore and move on !\nPress 3. To view all Your owned "
                      "Properties"))
            if p_or_not == 1:
                if p4_wallet > prices[pos_4]:
                    print("Congratulations on purchasing", mboard[pos_4], "\n We have deducted", prices[pos_4],
                          "From your wallet")
                    p4_wallet -= prices[pos_4]
                    print("Your current account wallet is ::", p4_wallet)
                    p4_props.append(mboard[pos_4])
                else:
                    mortgage4()
            elif p_or_not == 2:
                pass
            elif p_or_not == 3:
                print(p4_props)
        elif comc_or_ch[pos_4] == 1:
            print("You landed on", mboard[pos_4])
            chance4()
        elif comc_or_ch[pos_4] == 2:
            print("You landed on", mboard[pos_4])
            chance4()
        else:
            if pos_4 > 1:
                print("Press 1. to purchase", mboard[pos_4], "It Costs $", prices[pos_4],
                      "\nElse press 2. to ignore\nPress 3. to view all your properties.")
                p_or_not = int(input("Please Enter you Choice"))
                if p_or_not == 1:
                    if p4_wallet > prices[pos_4]:
                        print("Congratulations on purchasing", mboard[pos_4], "\nWe have deducted", prices[pos_4],
                              "From your wallet")
                        p4_wallet -= prices[pos_4]
                        print("Your current account wallet is ::", p4_wallet)
                        p4_props.append(mboard[pos_4])
                    else:
                        mortgage4()
                elif p_or_not == 2:
                    pass
                elif p_or_not == 3:
                    print(p4_props)
            else:
                print('You are on GO')
    else:
        print('Sorry you are in jail')
        gotojail_place_4 += 1
        if gotojail_place_4 >= 3:
            gotojail_place_4 = 0
            p4_injail = False


def main():
    rules()
    sleep(1)
    player_names()
    while True:
        if num_of_player == 2:
            if p1_bankrupt is False:
                player_1_moves()
                print('_______________________________________________________________________________________________')
            if p2_bankrupt is False:
                player_2_moves()
                print('_______________________________________________________________________________________________')
        elif num_of_player == 3:
            if p1_bankrupt is False:
                player_1_moves()
                print('_______________________________________________________________________________________________')
            if p2_bankrupt is False:
                player_2_moves()
                print('_______________________________________________________________________________________________')
            if p3_bankrupt is False:
                player_3_moves()
                print('_______________________________________________________________________________________________')
        else:
            if p1_bankrupt is False:
                player_1_moves()
                print('_______________________________________________________________________________________________')
            if p2_bankrupt is False:
                player_2_moves()
                print('_______________________________________________________________________________________________')
            if p3_bankrupt is False:
                player_3_moves()
                print('_______________________________________________________________________________________________')
            if p4_bankrupt is False:
                player_4_moves()
                print('_______________________________________________________________________________________________')
        if p2_bankrupt is True and p3_bankrupt is True and p4_bankrupt is True:
            print(p1, ' IS THE WINNER')
            break
        elif p1_bankrupt is True and p3_bankrupt is True and p4_bankrupt is True:
            print(p2, ' IS THE WINNER')
            break
        elif p2_bankrupt is True and p1_bankrupt is True and p4_bankrupt is True:
            print(p3, ' IS THE WINNER')
            break
        elif p2_bankrupt is True and p3_bankrupt is True and p1_bankrupt is True:
            print(p4, ' IS THE WINNER')
            break


main()















