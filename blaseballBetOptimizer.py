## Blaseball Bet Odds Optimizer ##
import math
import numpy

# Manually enter the winning odds for each game, your number of coins, and your current max bet
gameOdds = [56,63,62,61,55,63,63,53,60,61] 
coins = 2147
currentMaxBet = 300
EVMode = True

# Pre-Allocating Arrays
gameOddsEV = ['0'] * len(gameOdds)
gameBetsSortedBeg = ['0'] * len(gameOdds)
gameBets = ['0'] * len(gameOdds)
totalCoins = coins
minBet = 0 # Used when EV mode set to False

# Determine game-set bet order, so high games get max bid
gameOrder = numpy.argsort(gameOdds)
gameOrder = gameOrder[::-1]
gameSorted = sorted(gameOdds)

if EVMode == False:
    HighRank = 70
    # Determining bet amounts here
    logCoEf = (1 - minBet)/(math.log1p(HighRank-50))
    print("Log Co-Efficient: " + str(logCoEf))
    for index in range(0,len(gameOdds)):
        gameBets[index] = math.floor( currentMaxBet * ((logCoEf*math.log1p(gameOdds[index] - 50)) + minBet))
        if gameBets[index] > currentMaxBet:
            gameBets[index] = currentMaxBet
    gameBetsSorted = sorted(gameBets, reverse = True)

if EVMode == True:
    EVmax = (2 - (355*10**-6)*(math.pow((100*(0.77-0.5)), 2.045)))*(0.77) - 1
    EVmin = 0
    EVrange = EVmax - EVmin
    for index in range(0,len(gameOdds)):
        gameOddsEV[index] = (2 - (355*10**-6)*(math.pow((100*(gameOdds[index]/100 - 0.5)), 2.045)))*(gameOdds[index]/100) - 1
        gameBets[index] = math.floor(currentMaxBet*(gameOddsEV[index]/EVrange))
        if gameBets[index] > currentMaxBet:
            gameBets[index] = currentMaxBet
    gameBetsSorted = sorted(gameBets, reverse = True)

for index in range(0, len(gameOdds)):
    if totalCoins < gameBetsSorted[index]:
        gameBetsSortedBeg[index] = totalCoins
        gameBetsSorted[index] = totalCoins
    if (totalCoins) <= 0:
        gameBetsSortedBeg[index] = 'Beg'
    totalCoins -= gameBetsSorted[index]
    #print('Total coins is now: ' + str(totalCoins))

# Output   
print('\nGame\tOdds\tBet')
print('|||||||||||||||||||')
for index in range(0,len(gameOdds)):
    if gameBetsSortedBeg[index] == 'Beg':
        gameBetsSorted[index] = gameBetsSortedBeg[index]
        print(f"{gameOrder[index] + 1}" +"\t"+ f"{gameOdds[gameOrder[index]]}" + '\t' + f"{gameBetsSorted[index]}")
    else:
        print(f"{gameOrder[index] + 1}" +"\t"+ f"{gameOdds[gameOrder[index]]}" + '\t' + f"{gameBetsSorted[index]}")