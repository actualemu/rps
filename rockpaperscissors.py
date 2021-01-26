#rock paper scissors

while True:
    pOne = input('Welcome to Rock, Paper, Scissors! Player one, please input rock, paper, or scissors.\n').lower()
    pTwo = input('Player two, please input rock, paper, or scissors.\n').lower()

    if (pOne == 'rock'.lower() and pTwo == 'scissors'.lower()) or (pOne == 'paper'.lower() and pTwo == 'rock'.lower()) or (pOne == 'scissors'.lower()) and (pTwo == 'paper'.lower()):
        print('Player one wins!!')
    elif (pTwo == 'rock'.lower() and pOne == 'scissors'.lower()) or (pTwo == 'scissors'.lower() and pOne =='paper'.lower()) or (pTwo == 'paper'.lower() and pOne == 'rock'.lower()):
        print('Player two wins!!')
    elif pOne == pTwo:
        print('It\'s a draw!!')
    else:
        print('Please type a valid entry.')
    replay = input('Would you like to play again? Type y for yes, n for no.\n').lower()
    if replay == 'y':
        continue
    elif replay == 'n':
        print('Thanks for playing.')
        break
