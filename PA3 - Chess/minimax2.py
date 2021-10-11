import chess

class Mini():
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.value_map = {
            chess.PAWN: 1,
            chess.BISHOP: 3,
            chess.KNIGHT: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 600
        }
  
    def evaluation(self, board):
        # White Total
        w_total = sum([val * len(board.pieces(piece, chess.WHITE)) for piece, val in self.value_map.items()])

        # Black Total
        b_total = sum([val * len(board.pieces(piece, chess.BLACK)) for piece, val in self.value_map.items()])
        return w_total - b_total

    def minimax(self, board, depth, move_map, origin, count):
        if depth == self.max_depth: 
            return self.evaluation(board)

        if board.is_game_over():
            print("Checkmate: ", origin)
            print("White Wins!" if board.turn == chess.BLACK else "Black Wins!") 
            exit()

        moves = list(board.legal_moves)
        max_val, min_val = float('-inf'), float('inf')
        for move in moves:
            board.push(move)

            # Only the next move is actually submitted, have to keep track of origin moves
            backtracked = move if depth == 0 else origin
            count[0] += 1
            val = self.minimax(board, depth+1, move_map, backtracked, count)
            if val > max_val and board.turn == chess.WHITE: 
                # if max_val != float('-inf'): del move_map[max_val]
                max_val = max(max_val, val)
                move_map[max_val] = backtracked
            elif val < min_val and board.turn == chess.BLACK: 
                # if min_val != float('inf'): del move_map[min_val]
                min_val = min(min_val, val)
                move_map[min_val] = backtracked
            board.pop()
        return max_val if board.turn == chess.WHITE else min_val

        
    def choose_move(self, board):
        move_map = {}
        count = [0]
        self.minimax(board, 0, move_map, None, count)
        print('MinimaxAI is recommending move ',move_map[max(move_map.keys())] if board.turn == chess.WHITE else move_map[min(move_map.keys())])
        print("minimax call count: ", count)
        print(min(move_map.keys()))
        return move_map[max(move_map.keys())] if board.turn == chess.WHITE else move_map[min(move_map.keys())]


