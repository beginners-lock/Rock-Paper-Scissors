import random

#Welcome to the Zuri Team Rock Paper Scissors game
#You play against the computer (CPU)
#You choose between three options only:
#R - Rock, P - Paper, S - Scissors

options = ["R", "P", "S"]

while True:
    player1 = input(str("Which one do you pick (R, P or S)? "))

    if player1.upper()=='R':
        player1 = 'Rock'
    elif player1.upper()=='S':
        player1 = 'Scissors'
    elif player1.upper()=='P':
        player1 = 'Paper'
    else:
        print("Invalid option chosen. Choose again")
        continue

    cpu = random.choice(options)
    if cpu.upper()=='R':
        cpu = 'Rock'
    elif cpu.upper()=='S':
        cpu = 'Scissors'
    else:
        cpu = 'Paper'

    choices = [player1, cpu]
    winner = ''
    if 'Rock' in choices and 'Scissors' in choices:
        if choices.index('Rock') == 0:
            winner = 'Player1'
        else:
            winner = 'CPU'
    elif 'Paper' in choices and 'Scissors' in choices:
        if choices.index('Scissors') == 0:
            winner = 'Player1'
        else:
            winner = 'CPU'
    elif 'Rock' in choices and 'Paper' in choices:
        if choices.index('Paper') == 0:
            winner = 'Player1'
        else:
            winner = 'CPU'
    elif player1 == cpu:
        winner = 'draw'

    print("Player1: "+player1+"\t\tCPU:"+cpu)
    if winner == 'draw':
        print('This round is a draw!!!')
    else:
        print(winner + " wins this round!!!")

    break
