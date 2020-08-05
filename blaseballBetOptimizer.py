## Blaseball Bet Odds Optimizer ##
import math
import numpy

# Manually enter the winning odds for each game, your number of coins, and your current max bet
gameOdds = [61,66, 68, 57, 63, 54, 58, 50, 59, 62] 
coins = 546
currentMaxBet = 60 

# Favor games between high, med , low
gameRank = ["Unranked"] * len(gameOdds)
for game in range(0,len(gameOdds)):
    if gameOdds[game] >= 65:
        gameRank[game] = "High"
    elif 55 < gameOdds[game] < 65:
        gameRank[game] = "Mid"
    elif 50 <= gameOdds[game] <= 55:
        gameRank[game] = "Low"
numberHighRanks = gameRank.count('High')
# if numberHighRanks == 1:
#     print('There is {0} high favor game'.format(numberHighRanks))
# elif numberHighRanks > 1:
#     print('There are {0} high favor games'.format(numberHighRanks))

# Determine game-set bet order, so high games get max bid
gameOrder = numpy.argsort(gameOdds)
gameOrder = gameOrder[::-1]
# print('Bet in this order: ' + str(gameOrder + 1))
gameSorted = sorted(gameOdds)

# Now we decide how much to put in each game
gameBets = ['0'] * len(gameOdds)
totalCoins = coins
for game in range(0,len(gameOdds)):
    gameBets[game] = math.floor( currentMaxBet * ((0.3065*math.log1p(gameOdds[game] - 50)) + 0.15))
    if gameBets[game] > currentMaxBet:
        gameBets[game] = currentMaxBet
gameBetsSorted = sorted(gameBets, reverse = True)

for game in range(0, len(gameOdds)):
    totalCoins -= gameBetsSorted[game]
    if totalCoins <= 0:
        gameBetsSorted[game] = 'Beg'
# print('With these amounts: ' + str(gameBetsSorted))

print("\nIn order, bet these amounts: " + str(gameBets))