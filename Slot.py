import random
import math

x = 0   # counter
reel1 = 0   # made for accessing reels, 0 is inactive, 1 is accessing roll_dice()
reel2 = 0
index1 = 0  # tracks segments of large 8 in reel 1
index2 = 0
previous_perc = 0  # previous rounds percentage of completed trials
current_perc = 0  # current percentage of completed trials

coins = int(input('enter number of coins held (1 coin used per play): '))
trials = int(input('enter number of trials: '))


def roll_dice():
    global index1
    global index2
    r = random.SystemRandom()
    if reel1 == 1:
        roll = r.randint(1,9)
        if roll == 8 and index1 < 9:
            index1 += 1
            return True
        else:
            return False
    elif reel2 == 1:
        roll = r.randint(1,10)
        if roll == 8 and index2 < 9:
            index2 += 1
            return True
        else:
            return False
#end function


def slot_machine(funds, play_cost):
    global reel1, reel2, index1, index2, previous_perc, current_perc
    full_win1 = 0
    full_win2 = 0
    value = funds * 2   #value subtracts 2 per turn so double the amount
    wager = play_cost
    turn_total = 0
    avg_turn_total = 0
    play_count = x


    while index1 < 9 and index2 < 9:
        reel1 += 1
        if roll_dice():
            value += wager
        else:
            value -= wager
        reel1 -= 1  #return reel accessor to 0

        reel2 += 1
        if roll_dice():
            value += wager
        else:
            value -= wager
        reel2 -= 1      #return reel accessor to 0

        if index1 == 8:     # award payout coins
            value += 10
            index1 = 0
            full_win1 = 1
            continue
        elif index2 == 8:
            value += 20
            index2 = 0
            full_win2 = 1
            continue

        if full_win1 == 1 and full_win2 == 1:
            value += 100
            break

        turn_total += 1

        if value <= 0:
            break
    #end loop
    avg_turn_total += turn_total
    if trials > 100 and x > 1 and x != trials - 1:  #only display every 1% and the final trial if there are more than 100
        current_perc = (x / trials) * 100
        diff = current_perc - previous_perc
        if diff >= 1:
            previous_perc = current_perc
            value /= 2                      #return value to the approx. original amount and floor it to get true amount
            value = math.floor(value)
            print('funds: ', value)
            print('plays (coins used)', turn_total)
            print('reel 1 segments: ', index1)
            print('reel 2 segments: ', index2)
            print('end trial ', play_count + 1, '\n')
    else:
        value /= 2                      #return value to the approx. original amount and floor it to get true amount
        value = math.floor(value)
        print('funds remaining: ', value)
        print('plays', turn_total)
        print('reel 1 segments: ', index1)
        print('reel 2 segments: ' , index2)
        print('end trial ', play_count + 1, '\n')

#end function


while x < trials:
    slot_machine(coins, 1)
    index1 = 0
    index2 = 0
    x += 1


