'''
Created on 5 Sep 2018

@author: Irish
'''

# 1) user input using { input() }
print('______________________________1______________________________')
currentDay = input('What day is today? : ')
print('Today is', currentDay)

# 2) Another example, this time performing calculations on user input
print('______________________________2______________________________')
moneyGiven = input('Welcome to the doubling machine! How much money do you give? : ')
moneyGiven = int(moneyGiven)
print('You gave the machine', moneyGiven, 'euro')
print('# Making machine sounds #')
print('Cha-ching! Here is ', moneyGiven*2, ' euro')