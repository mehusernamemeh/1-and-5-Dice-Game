from random import randint
from collections import *

from numpy import roll

rollScore = 0
rolls = []
straightRoll1 = [1,2,3,4,5]  #One of two possible "straight" combinations
unluckyScore = 0
unluckyScore2 = 0
straightRoll2 = [2,3,4,5,6]  #The other possible straight combination
runningScore = 0
rollsTaken = 0
rollDecision = True
diceRemaining = 5
totalScore = 0

def rollCalculation(diceRemaining, runningScore, totalScore, strategy):
    if strategy == 'aggressive':
        return True
    elif strategy == 'moderate':
        if totalScore > 8000 and diceRemaining < 5:
            return False
        elif diceRemaining >= 3:
            return True
        elif runningScore > 1000 and (10000 - runningScore) < 1000:
            return True
        else: return False
    elif strategy == 'cautious':
        if diceRemaining >= 4:
            return True
        elif runningScore > 500:
            return True
        else: return False

#python is so fucking gay fuck indentations fuck yourself fuck you fuck python
#Continue running until total score reaches 10,000.
while totalScore < 10000:
    if diceRemaining > 0:
        rollCalculation(diceRemaining, runningScore, totalScore, 'moderate')
        if rollCalculation(diceRemaining, runningScore, totalScore, 'moderate') == True:

            for i in range(diceRemaining):                 #Roll 5 Dice. Store the values of the rolls in a list called rolls for later. Store the values of the 1s and 5s scores in unluckyScore.
                diceRoll = randint(1,6)
                rolls.append(diceRoll)
                
                if diceRoll == 1:                          #If the dice lands on 1, add 100 to the "unlucky" score.
                    unluckyScore = unluckyScore + 100
                elif diceRoll == 5:
                    unluckyScore = unluckyScore + 50       #If the dice lands on 5, add 50 to the "unlucky" score.
                else: unluckyScore = unluckyScore

            rolls.sort()                                   #Sort the values of the dice to be compared to the straight combinations.
            sameNumbercheck = Counter(rolls)               #Check the number of occurences of each number in the list.

            if rolls == straightRoll1:                     #If the dice lands in either straight combination, the player scores 1500.
                rollScore = 1500
                diceRemaining = 0
            elif rolls == straightRoll2:
                rollScore = 1500
                diceRemaining = 0
            elif sameNumbercheck[2] >= 3:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                rollScore = 200 * sameNumbercheck[2]
                print('Multiple 2s!')
                diceRemaining = diceRemaining - sameNumbercheck[2]
            elif sameNumbercheck[3] >= 3:
                rollScore = 300 * sameNumbercheck[3]
                diceRemaining = diceRemaining - sameNumbercheck[3]
                print('Multiple 3s!')
            elif sameNumbercheck[4] >= 3:
                rollScore = 400 * sameNumbercheck[4]
                diceRemaining = diceRemaining - sameNumbercheck[4]
                print('Multiple 4s!')
            elif sameNumbercheck[6] >= 3:
                rollScore = 600 * sameNumbercheck[6]
                diceRemaining = diceRemaining - sameNumbercheck[6]
                print('Multiple 6s!')
            else:
                rollScore = unluckyScore              #If no straight combinations or multiples are rolled, the score will be equal to "unlucky score".
                diceRemaining = diceRemaining - sameNumbercheck[1] - sameNumbercheck[5]


            print('My rolls were ' + str(rolls))
            print('My score for the roll was: ' + str(rollScore))

            rollsTaken = rollsTaken + 1                   #Increment # of rolls taken.
                   
            if runningScore + totalScore + rollScore > 10000:          #If total score would go over 10000, do not add to score.
                runningScore = 0
                diceRemaining = 5
                print('Almost! Your turn.')
            elif rollScore == 0:
                diceRemaining = 5
                runningScore = 0
            else: runningScore = runningScore + rollScore

            print('My score this round is: ' + str(runningScore))
            print('My total score so far is still ' + str(totalScore))
            #print('I have taken ' + str(rollsTaken) + ' rolls total.')
            print('I have ' + str(diceRemaining) + ' dice to throw.')
            print()

            rolls = []
            rollScore = 0                               #Reset player scores for next roll.
            unluckyScore = 0  

            if totalScore == 10000:
                print('I won')
                print('I took ' + str(rollsTaken) + ' rolls to reach 10000')
                break
        else:
            diceRemaining = 5
            totalScore = totalScore + runningScore
            runningScore = 0
            print('I wont roll again on this one.')
            print('That brings my total score to ' + str(totalScore))
            print()

            rollCalculation(diceRemaining, runningScore, totalScore, 'moderate')

    elif diceRemaining == 0 and runningScore != 0:
            diceRemaining = 5

    elif diceRemaining == 0 and runningScore == 0:
            print('hellothere')

    else: break

print('I took ' + str(rollsTaken) + ' rolls to hit 10000.')