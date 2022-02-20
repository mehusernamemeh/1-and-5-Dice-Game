"""
1 AND 5 DICE GAME RULES:
Players take turns rolling 5 dice at once.
They can score points under the following conditions:

    -100 points for each roll of 1.
    -50 points for each roll of 5.
    -1500 points for a "straight" (a roll of 1,2,3,4,5 or 2,3,4,5,6).
    -If players roll 3 dice of the same value (other than 1 or 5), they score 100 times the value of the dice.
        ex. If a player rolls 4,4,4,2,6 , they score 100 * 4
    -If players roll 4 dice of the same value (other than 1 or 5), they score 100 times the value of the dice times 2.
        ex. If a player rolls 4,4,4,4,6 , they score 100 * 4 *2
    -If players roll 5 dice of the same value (other than 1 or 5), they score 100 times the value of the dice times 4.

Players may choose to continue rolling as long as they have scored on their previous roll.       
If a player scores points on a dice, that dice is removed from the next roll.
If a player scores on all remaining dice, they may continue rolling with 5 dice.
If a player chooses to continue rolling and does not score, they score 0 and their turn ends.
If a player chooses to stop rolling, they keep the points and pass the remaining dice to the next player.
If a player is passed dice from a player who stopped rolling, they may choose to roll the remaining dice
and extend the previous player's score.
    ex. Player A has 1000 points, and 1 dice remaining. They choose not to roll. They receive 1000 points
        and pass 1 dice to Player B. Player B may choose to roll the 1 die to receive 1000 points (what the
        previous player earned) + the value of the die. They may also choose to roll 5 dice as normal for 
        no extra points. Player B does not "steal" points from Player A.
        
"""

from ast import Mod
from random import randint
from collections import *
from time import *

#if there is a problem it might be because vscode is REDACTED and keeps importing random libraries ^^^
#i need randint from random and * from collections and time. thats it. 

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
moderateScore = 0
aggressiveScore = 0
cautiousScore = 0
ModeratePlayerWins = 0
AggressivePlayerWins = 0
CautiousPlayerWins = 0
PlayerWin = False
TotalModerateWins = 0
TotalAggressiveWins = 0
TotalCautiousWins = 0
ModerateRollsTaken = 0
AggressiveRollsTaken = 0
CautiousRollsTaken = 0


def resetPlayerwins():
    global CautiousPlayerWins, AggressivePlayerWins, ModeratePlayerWins
    CautiousPlayerWins = 0
    AggressivePlayerWins = 0
    ModeratePlayerWins = 0

def reset():
    global rollScore, rolls, unluckyScore, unluckyScore2, runningScore, rollsTaken, rollDecision, diceRemaining, totalScore, moderateScore,aggressiveScore, cautiousScore
    rollScore = 0
    rolls = []
    unluckyScore = 0
    unluckyScore2 = 0
    runningScore = 0
    rollsTaken = 0
    rollDecision = True
    diceRemaining = 5
    totalScore = 0
    moderateScore = 0
    aggressiveScore = 0
    cautiousScore = 0

def rollCalculation(diceRemaining, runningScore, totalScore, strategy):
    
    if strategy == 'aggressive':
        return True

    elif strategy == 'moderate':
        if ModerateRollsTaken == 0:
            return True
        elif totalScore > 8000 and diceRemaining < 5:
            return False
        elif diceRemaining >= 3:
            return True
        else: return False
        """"
        if ModerateRollsTaken == 0 and moderateScore < 10000:
            return True
        elif totalScore > 8000 and diceRemaining < 5:
            return False
        elif diceRemaining >= 3:
            return True
        elif runningScore > 1000 and (10000 - runningScore) < 1000:
            return True
        else: return False
        """

    elif strategy == 'cautious':
        return True
        """"
        if CautiousRollsTaken == 0:
            return True
        elif diceRemaining >= 4:
            return True
        elif runningScore > 500:
            return True
        else: return False
        """

print('Enter a number of games to play.')

gamestoplay = input()
gamestoplay = int(gamestoplay)

for i in range(gamestoplay):
#while ModeratePlayerWins and AggressivePlayerWins and CautiousPlayerWins == 0:
    while ModeratePlayerWins == 0 and AggressivePlayerWins == 0 and CautiousPlayerWins == 0:
    #while PlayerWin == False:
    #Continue running until total score reaches 10,000.
        while moderateScore < 10000 and moderateScore != 10000:
            if diceRemaining > 0:
                totalScore = moderateScore
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

                    print('MODERATE PLAYER:')
                    #sleep(1)

                    if rolls == straightRoll1:                     #If the dice lands in either straight combination, the player scores 1500.
                        rollScore = 1500
                        #diceRemaining = 0
                    elif rolls == straightRoll2:
                        rollScore = 1500
                        #diceRemaining = 0
                    elif sameNumbercheck[2] == 3:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2
                        print('I rolled 3 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[2] == 4:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2 *2
                        print('I rolled 4 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[2] == 5:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2 * 4
                        print('I rolled 5 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[2] == 6:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2 * 8
                        print('I rolled 6 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[3] == 3:
                        rollScore = 100 * 3
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 3 3s!')
                    elif sameNumbercheck[3] == 4:
                        rollScore = 100 * 3 * 2
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 4 3s!')
                    elif sameNumbercheck[3] == 5:
                        rollScore = 100 * 3 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 5 3s!')
                    elif sameNumbercheck[3] == 6:
                        rollScore = 100 * 3 * 8
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 6 3s!')
                    elif sameNumbercheck[4] == 3:
                        rollScore = 100 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 3 4s!')
                    elif sameNumbercheck[4] == 4:
                        rollScore = 100 * 4 * 2
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 4 4s!')
                    elif sameNumbercheck[4] == 5:
                        rollScore = 100 * 4 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 5 4s!')
                    elif sameNumbercheck[4] == 6:
                        rollScore = 100 * 4 * 8
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 6 4s!')
                    elif sameNumbercheck[6] == 3:
                        rollScore = 100 * 6
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 3 6s!')
                    elif sameNumbercheck[6] == 4:
                        rollScore = 100 * 6 * 2
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 4 6s!')
                    elif sameNumbercheck[6] == 5:
                        rollScore = 100 * 6 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 5 6s!')
                    elif sameNumbercheck[6] == 6:
                        rollScore = 100 * 6 * 8
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 6 6s!')
                    else:
                        rollScore = unluckyScore              #If no straight combinations or multiples are rolled, the score will be equal to "unlucky score".
                        diceRemaining = diceRemaining - sameNumbercheck[1] - sameNumbercheck[5]

                    print('My rolls were ' + str(rolls))
                    print('My score for the roll was: ' + str(rollScore))

                    ModerateRollsTaken = ModerateRollsTaken + 1                   #Increment # of rolls taken.
                    
                    rolls = []

                    if runningScore + totalScore + rollScore > 10000:          #If total score would go over 10000, do not add to score.
                        runningScore = 0
                        diceRemaining = 5
                        print('Almost! Your turn.')
                        ModerateRollsTaken = 0
                        break
                    elif rollScore == 0:
                        diceRemaining = 5
                        runningScore = 0
                        ModerateRollsTaken = 0
                        break
                    else: runningScore = runningScore + rollScore

                    print('My score this round is: ' + str(runningScore))
                    print('My total score so far is still ' + str(totalScore))
                    #print('I have taken ' + str(rollsTaken) + ' rolls total.')
                    print('There are ' + str(diceRemaining) + ' dice to throw.')
                    print()

                    rolls = []
                    rollScore = 0                               #Reset player scores for next roll.
                    unluckyScore = 0  

                    if totalScore == 10000:
                        print('I won')
                        print('I took ' + str(rollsTaken) + ' rolls to reach 10000')
                        ModeratePlayerWins = ModeratePlayerWins + 1
                        #PlayerWin = True
                        reset()
                        ModerateRollsTaken = 0
                        break

                    rollCalculation(diceRemaining, runningScore, totalScore, 'moderate')

                else:
                    #diceRemaining = 5
                    totalScore = totalScore + runningScore
                    moderateScore = totalScore
                    #runningScore = 0
                    print('I wont roll again on this one.')
                    print('That brings my total score to ' + str(moderateScore))
                    print()
                    totalScore = 0
                    rolls = []
                    ModerateRollsTaken = 0

                    if moderateScore == 10000:
                        ModeratePlayerWins = ModeratePlayerWins + 1
                        ModerateRollsTaken = 0
                        #PlayerWin = True
                    break

                    rollCalculation(diceRemaining, runningScore, totalScore, 'moderate')

            elif diceRemaining == 0 and runningScore != 0:
                    diceRemaining = 5

            elif diceRemaining == 0 and runningScore == 0:
                    print('hellothere')

            else: break

        #print('I took ' + str(rollsTaken) + ' rolls to hit 10000.')
        print('The running score is ' + str(runningScore))
        print('My total score is ' + str(moderateScore))
        print('There are ' + str(diceRemaining) + ' dice for the next player to roll')
        print()

        while aggressiveScore < 10000 and aggressiveScore != 10000:
            if diceRemaining > 0:
                totalScore = aggressiveScore
                rollCalculation(diceRemaining, runningScore, totalScore, 'aggressive')
                if rollCalculation(diceRemaining, runningScore, totalScore, 'aggressive') == True:

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

                    print('AGGRESSIVE PLAYER:')
                    #sleep(1)

                    if rolls == straightRoll1:                     #If the dice lands in either straight combination, the player scores 1500.
                        rollScore = 1500
                        #diceRemaining = 0
                    elif rolls == straightRoll2:
                        rollScore = 1500
                        #diceRemaining = 0
                    elif sameNumbercheck[2] == 3:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2
                        print('I rolled 3 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[2] == 4:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2 *2
                        print('I rolled 4 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[2] == 5:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2 * 4
                        print('I rolled 5 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[2] == 6:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2 * 8
                        print('I rolled 6 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[3] == 3:
                        rollScore = 100 * 3
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 3 3s!')
                    elif sameNumbercheck[3] == 4:
                        rollScore = 100 * 3 * 2
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 4 3s!')
                    elif sameNumbercheck[3] == 5:
                        rollScore = 100 * 3 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 5 3s!')
                    elif sameNumbercheck[3] == 6:
                        rollScore = 100 * 3 * 8
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 6 3s!')
                    elif sameNumbercheck[4] == 3:
                        rollScore = 100 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 3 4s!')
                    elif sameNumbercheck[4] == 4:
                        rollScore = 100 * 4 * 2
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 4 4s!')
                    elif sameNumbercheck[4] == 5:
                        rollScore = 100 * 4 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 5 4s!')
                    elif sameNumbercheck[4] == 6:
                        rollScore = 100 * 4 * 8
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 6 4s!')
                    elif sameNumbercheck[6] == 3:
                        rollScore = 100 * 6
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 3 6s!')
                    elif sameNumbercheck[6] == 4:
                        rollScore = 100 * 6 * 2
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 4 6s!')
                    elif sameNumbercheck[6] == 5:
                        rollScore = 100 * 6 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 5 6s!')
                    elif sameNumbercheck[6] == 6:
                        rollScore = 100 * 6 * 8
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 6 6s!')
                    else:
                        rollScore = unluckyScore              #If no straight combinations or multiples are rolled, the score will be equal to "unlucky score".
                        diceRemaining = diceRemaining - sameNumbercheck[1] - sameNumbercheck[5]

                    print('My rolls were ' + str(rolls))
                    print('My score for the roll was: ' + str(rollScore))

                    AggressiveRollsTaken = AggressiveRollsTaken + 1                   #Increment # of rolls taken.
                    
                    rolls = []
                    
                    if runningScore + totalScore + rollScore > 10000:          #If total score would go over 10000, do not add to score.
                        runningScore = 0
                        diceRemaining = 5
                        print('Almost! Your turn.')
                    elif rollScore == 0:
                        diceRemaining = 5
                        runningScore = 0
                        break
                    else: runningScore = runningScore + rollScore

                    print('My score this round is: ' + str(runningScore))
                    print('My total score so far is still ' + str(aggressiveScore))
                    #print('I have taken ' + str(rollsTaken) + ' rolls total.')
                    print('There are ' + str(diceRemaining) + ' dice to throw.')
                    print()

                    rolls = []
                    rollScore = 0                               #Reset player scores for next roll.
                    unluckyScore = 0  

                    if totalScore == 10000:
                        print('I won')
                        print('I took ' + str(rollsTaken) + ' rolls to reach 10000')
                        AggressivePlayerWins = AggressivePlayerWins + 1
                        #PlayerWin = True
                        break

                    rollCalculation(diceRemaining, runningScore, totalScore, 'moderate')

                    if diceRemaining == 0 and runningScore != 0:
                        diceRemaining = 5
                        break

                    elif diceRemaining == 0 and runningScore == 0:
                        print('hellothere')
                        break

                else:
                    #diceRemaining = 5
                    totalScore = totalScore + runningScore
                    aggressiveScore = totalScore
                    #runningScore = 0
                    print('I wont roll again on this one.')
                    print('That brings my total score to ' + str(aggressiveScore))
                    print()
                    totalScore = 0
                    rolls = []
                    if aggressiveScore == 10000:
                        AggressivePlayerWins = AggressivePlayerWins + 1
                        #PlayerWin = True
                        break

                    rollCalculation(diceRemaining, runningScore, totalScore, 'moderate')

            """"
            elif diceRemaining == 0 and runningScore != 0:
                    diceRemaining = 5
                    break

            elif diceRemaining == 0 and runningScore == 0:
                    print('hellothere')
                    break
            """

        #print('I took ' + str(rollsTaken) + ' rolls to hit 10000.')
        print('The running score is ' + str(runningScore))
        print('My total score is ' + str(aggressiveScore))
        print('There are ' + str(diceRemaining) + ' dice for the next player to roll')
        print()

        while cautiousScore < 10000 and cautiousScore != 10000:
            if diceRemaining > 0:
                totalScore = cautiousScore
                rollCalculation(diceRemaining, runningScore, totalScore, 'cautious')
                if rollCalculation(diceRemaining, runningScore, totalScore, 'cautious') == True:

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

                    print('CAUTIOUS PLAYER:')
                    #sleep(1)

                    if rolls == straightRoll1:                     #If the dice lands in either straight combination, the player scores 1500.
                        rollScore = 1500
                        #diceRemaining = 0
                    elif rolls == straightRoll2:
                        rollScore = 1500
                        #diceRemaining = 0
                    elif sameNumbercheck[2] == 3:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2
                        print('I rolled 3 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[2] == 4:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2 *2
                        print('I rolled 4 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[2] == 5:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2 * 4
                        print('I rolled 5 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[2] == 6:                  #If the number 2 is rolled 3 times or more, the player score is 200 * the # of occurences of 2.
                        rollScore = 100 * 2 * 8
                        print('I rolled 6 2s!')
                        diceRemaining = diceRemaining - sameNumbercheck[2]
                    elif sameNumbercheck[3] == 3:
                        rollScore = 100 * 3
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 3 3s!')
                    elif sameNumbercheck[3] == 4:
                        rollScore = 100 * 3 * 2
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 4 3s!')
                    elif sameNumbercheck[3] == 5:
                        rollScore = 100 * 3 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 5 3s!')
                    elif sameNumbercheck[3] == 6:
                        rollScore = 100 * 3 * 8
                        diceRemaining = diceRemaining - sameNumbercheck[3]
                        print('I rolled 6 3s!')
                    elif sameNumbercheck[4] == 3:
                        rollScore = 100 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 3 4s!')
                    elif sameNumbercheck[4] == 4:
                        rollScore = 100 * 4 * 2
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 4 4s!')
                    elif sameNumbercheck[4] == 5:
                        rollScore = 100 * 4 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 5 4s!')
                    elif sameNumbercheck[4] == 6:
                        rollScore = 100 * 4 * 8
                        diceRemaining = diceRemaining - sameNumbercheck[4]
                        print('I rolled 6 4s!')
                    elif sameNumbercheck[6] == 3:
                        rollScore = 100 * 6
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 3 6s!')
                    elif sameNumbercheck[6] == 4:
                        rollScore = 100 * 6 * 2
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 4 6s!')
                    elif sameNumbercheck[6] == 5:
                        rollScore = 100 * 6 * 4
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 5 6s!')
                    elif sameNumbercheck[6] == 6:
                        rollScore = 100 * 6 * 8
                        diceRemaining = diceRemaining - sameNumbercheck[6]
                        print('I rolled 6 6s!')
                    else:
                        rollScore = unluckyScore              #If no straight combinations or multiples are rolled, the score will be equal to "unlucky score".
                        diceRemaining = diceRemaining - sameNumbercheck[1] - sameNumbercheck[5]

                    print('My rolls were ' + str(rolls))
                    print('My score for the roll was: ' + str(rollScore))

                    CautiousRollsTaken = CautiousRollsTaken + 1                   #Increment # of rolls taken.
                    
                    rolls = []

                    if runningScore + totalScore + rollScore > 10000:          #If total score would go over 10000, do not add to score.
                        runningScore = 0
                        diceRemaining = 5
                        print('Almost! Your turn.')
                        CautiousRollsTaken = 0
                        break
                    elif rollScore == 0:
                        diceRemaining = 5
                        runningScore = 0
                        break
                    else: runningScore = runningScore + rollScore

                    print('My score this round is: ' + str(runningScore))
                    print('My total score so far is still ' + str(cautiousScore))
                    #print('I have taken ' + str(rollsTaken) + ' rolls total.')
                    print('There are ' + str(diceRemaining) + ' dice to throw.')
                    print()

                    rolls = []
                    rollScore = 0                               #Reset player scores for next roll.
                    unluckyScore = 0  

                    if totalScore == 10000:
                        print('I won')
                        print('I took ' + str(rollsTaken) + ' rolls to reach 10000')
                        CautiousPlayerWins = CautiousPlayerWins + 1
                        #PlayerWin = True
                        break

                    rollCalculation(diceRemaining, runningScore, totalScore, 'moderate')

                else:
                    #diceRemaining = 5
                    totalScore = totalScore + runningScore
                    cautiousScore = totalScore
                    #runningScore = 0
                    print('I wont roll again on this one.')
                    print('That brings my total score to ' + str(cautiousScore))
                    print()
                    totalScore = 0
                    if cautiousScore == 10000:
                        CautiousPlayerWins = CautiousPlayerWins + 1
                        CautiousRollsTaken = 0
                        #PlayerWin = True
                    break

                    rollCalculation(diceRemaining, runningScore, totalScore, 'moderate')

            elif diceRemaining == 0 and runningScore != 0:
                    diceRemaining = 5
                    break

            elif diceRemaining == 0 and runningScore == 0:
                    print('hellothere')
                    break

            else: break

        #print('I took ' + str(rollsTaken) + ' rolls to hit 10000.')
        print('The running score is ' + str(runningScore))
        print('My total score is ' + str(cautiousScore))
        print('There are ' + str(diceRemaining) + ' dice for the next player to roll')
        print()

    print('There was a winner')

    TotalAggressiveWins = TotalAggressiveWins + AggressivePlayerWins
    TotalCautiousWins = TotalCautiousWins + CautiousPlayerWins
    TotalModerateWins = TotalModerateWins + ModeratePlayerWins
    resetPlayerwins()
    reset()
    print('The cautious player has won ' + str(TotalCautiousWins) + 'times.')
    print('The aggressive player has won ' + str(TotalAggressiveWins) + 'times.')
    print('The moderate player has won ' + str(TotalModerateWins) + 'times.')
    sleep(5)
