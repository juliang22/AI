import chess
from collections import defaultdict 

class MinimaxAI():
    def __init__(self, max_depth):
        # Initializes algo with the max_depth allowed and the value of each piece
        self.max_depth = max_depth
        self.value_map = {
            chess.PAWN: 1,
            chess.BISHOP: 3,
            chess.KNIGHT: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 600
        }
  
    # Uses the value_map to determine how good a move is judged by the amount of pieces left and their value
    def evaluation(self, board):
        # White Total
        w_total = sum([val * len(board.pieces(piece, chess.WHITE)) for piece, val in self.value_map.items()])

        # Black Total
        b_total = sum([val * len(board.pieces(piece, chess.BLACK)) for piece, val in self.value_map.items()])
        return w_total - b_total
    
    # What to do when the game ends
    def end_game(self, board, move):
        print('Checkmate: ' + str(move))
        print(board.outcome())
        print("White Wins!" if board.turn == chess.BLACK else "Black Wins!") 
        exit()

    # Recursive minimax algorithm, exploring at depths > 1 (root of the algorithm is in choose_moves)
    def minimax(self, board, depth, count):
        # Evaluate value of the move (base case: bottom of the recursion tree)
        if depth == self.max_depth: 
            return self.evaluation(board)

        count[0] += 1 # Simple counter to track the amount of recursive calls
        moves = list(board.legal_moves)
        if board.turn == chess.WHITE:
            maxx = float('-inf')
            # Maximize the value if player is on white side
            for move in moves:
                board.push(move)
                val = self.minimax(board, depth+1, count)
                board.pop()
                maxx = max(maxx, val)
            return maxx
        else:
            minn = float('inf')
            # Minimize the value if player is on white side
            for move in moves:
                board.push(move)
                val = self.minimax(board, depth+1, count)
                board.pop()
                minn = min(val, minn)
            return minn

    # Algo to prioritize initial moves that capture (works best for alphabeta pruning minimax)
    def prioritize(self, board):
        moves = list(board.legal_moves)
        prioritized_moves = set(board.generate_legal_captures())
        sorted_moves = []
        for move in moves:
            if move in prioritized_moves: 
                sorted_moves.insert(0, move)
            else:
                sorted_moves.append(move)
        return sorted_moves

    # Root of the minimax recursion
    def choose_move(self, board):
        count = [0]
        moves = self.prioritize(board) # prioritize moves
        # moves = list(board.legal_moves)
    
        score = float('-inf') if board.turn == chess.WHITE else float('inf')
        best_move = None
        for move in moves:
            # Run minimax algo and get score for that move
            board.push(move)
            val = self.minimax(board, 1, count)
            if board.is_game_over(): self.end_game(board, move)
            board.pop()

            # Determine if that score is the best move
            if val >= score and board.turn == chess.WHITE:
                best_move = move
                score = val
            elif val <= score and board.turn == chess.BLACK:
                best_move = move
                score = val
        return best_move


