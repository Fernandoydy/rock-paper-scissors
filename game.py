#STARTING THE GAME

player1 = None
player2 = None

def playTheRound(roundWinner):
    rock, paper, scissors = 0, 1, 2
    ### PEDRA vs PAPEL
    if player1 == rock and player2 == paper:
        roundWinner = player2
    else:
        roundWinner = player1
    ### PAPEL vs Tesoura
    if player1 == paper and player2 == scissors:
        roundWinner = player2
    else:
        roundWinner = player1
    ### TESOURA vs PEDRA
    if player1 == scissors and player2 == rock:
        roundWinner = player2
    else:
        roundWinner = player1
    if player1 == player2:
          roundWinner = "DRAW, Retry!"
    if roundWinner == player1:
        roundWinner = "Player1"
    if roundWinner == player2:
        roundWinner = "Player2"

    print(f'The winner of this round is {roundWinner}')

print("THE GAME JUST START\n")
player1 = int(input("Player 1, choose your move\n"))
player2 = int(input("Player 2, choose your move\n"))
playTheRound(roundWinner=None)