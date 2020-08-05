## Blaseball Bet Odds Optimizer ##
import math
import numpy

# Manually enter the winning odds for each game, your number of coins, and your current max bet
gameOdds = [63, 55, 59, 55, 51, 69, 72, 53, 60, 72] 
coins = 1414
currentMaxBet = 200
minBet = 0.05

# Determine game-set bet order, so high games get max bid
gameOrder = numpy.argsort(gameOdds)
gameOrder = gameOrder[::-1]
gameSorted = sorted(gameOdds)
#print("\nGame order is: " + str(gameOrder + 1))

# Now we decide how much to put in each game
gameBets = ['0'] * len(gameOdds)
totalCoins = coins
gameBetsSortedBeg = ['0'] * len(gameOdds)
# Determining bet amounts here
logCoEf = (1 - minBet)/(math.log1p(65-49))
for index in range(0,len(gameOdds)):
    gameBets[index] = math.floor( currentMaxBet * ((logCoEf*math.log1p(gameOdds[index] - 50)) + minBet))
    if gameBets[index] > currentMaxBet:
        gameBets[index] = currentMaxBet
gameBetsSorted = sorted(gameBets, reverse = True)

#print('Total coins starts at: ' + str(totalCoins))
for index in range(0, len(gameOdds)):
    if totalCoins < gameBetsSorted[index]:
        gameBetsSortedBeg[index] = totalCoins
        gameBetsSorted[index] = totalCoins
    if (totalCoins) <= 0:
        gameBetsSortedBeg[index] = 'Beg'
    totalCoins -= gameBetsSorted[index]
    #print('Total coins is now: ' + str(totalCoins))
   

# print('Sorted game bets are: ' + str(gameBetsSorted))
# print('Sorted games with begging are: ' + str(gameBetsSortedBeg))
# print("In order, bet these amounts: " + str(gameBets))

print('\nGame\tOdds\tBet')
print('|||||||||||||||||||')
for index in range(0,len(gameOdds)):
    if gameBetsSortedBeg[index] == 'Beg':
        gameBetsSorted[index] = gameBetsSortedBeg[index]
        print(f"{gameOrder[index] + 1}" +"\t"+ f"{gameOdds[gameOrder[index]]}" + '\t' + f"{gameBetsSorted[index]}")
    else:
        print(f"{gameOrder[index] + 1}" +"\t"+ f"{gameOdds[gameOrder[index]]}" + '\t' + f"{gameBetsSorted[index]}")