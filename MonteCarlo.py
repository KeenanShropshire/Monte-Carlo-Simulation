import random

x = 0
y = 0
roll_win_sum = 0    #wins for current trial
trial_win_sum = 0   #wins for all trials
total_rolls = 0     #rolls for all trials
roll_count = 0      #rolls for current trial
previous_perc = 0   #previous rounds percentage of completed trials
current_perc = 0    #current percentage of completed trials

rolls = int(input('enter number of rolls per trial: '))
trials = int(input('enter number of trials: '))

def roll_dice(): #rolls random number on die
    x = random.SystemRandom()
    roll = x.randint(1,100)

    if roll == 100:
        #print(roll, 'loss')
        return False

    elif roll <= 50:
        #print(roll, 'loss')
        return False

    elif 50 < roll < 100:
        #print(roll, 'win')
        return True


while x < trials:
    while y < rolls:
        total_rolls += 1
        roll_count += 1
        result = roll_dice()
        if result:
            roll_win_sum += 1
            trial_win_sum += 1
            y += 1
            continue
        y += 1

    if trials > 100 and x > 1 and x != trials - 1:      #checks the number of trials and checks for at least 1% increase in the trial count before displaying information
        current_perc = (x / trials) * 100
        if current_perc - previous_perc >= 1:
            previous_perc = current_perc
            print('wins: ', roll_win_sum, ' Losses: ', y - roll_win_sum)
            print('win percentage this trial: ', roll_win_sum / y)
            print('current win percentage for all trials: ', trial_win_sum / roll_count)
            print('end of trial', x + 1)
            print('\n')
            roll_win_sum = 0
            y = 0
            x += 1
            continue
        else:
            roll_win_sum = 0
            y = 0
            x += 1
            continue
            #end loop

    print('wins: ', roll_win_sum, ' Losses: ', y - roll_win_sum)
    print('win percentage for this trial: ', roll_win_sum / y)
    print('win percentage for all trials: ', trial_win_sum / total_rolls)
    print('end of trial', x + 1)
    print('\n')
    roll_win_sum = 0
    y = 0
    x += 1
    #end loop