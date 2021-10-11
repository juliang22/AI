import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from again import AGAIN
import sys



# player1 = HumanPlayer()
# player2 = MinimaxAI(3)
player2 = AlphaBetaAI(3)
# player1 = AGAIN(3)
player1 = RandomAI()



game = ChessGame(player1, player2)


while not game.is_game_over():
    print(game)
    game.make_move()


#print(hash(str(game.board)))
