import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from iterative_deepening_abminimax import Iterative_AlphaBetaAI
from ChessGame import ChessGame
import sys



# player1 = MinimaxAI(3)
player1 = HumanPlayer()
player2 = AlphaBetaAI(4)
# player1 = Iterative_AlphaBetaAI(6)
# player2 = RandomAI()



game = ChessGame(player1, player2)


while not game.is_game_over():
    print(game)
    game.make_move()


