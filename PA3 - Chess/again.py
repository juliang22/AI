import chess

class AGAIN():
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

    def pruning(self, board, depth, move_map, count, alpha, beta):
        if depth == self.max_depth: 
            return self.evaluation(board)

        if board.is_game_over():
            print(board.is_checkmate())
            print(board.outcome())
            # print("Checkmate: ", move_map[max(move_map.keys())] if board.turn == chess.BLACK else move_map[min(move_map.keys())])
            print("White Wins!" if board.turn == chess.BLACK else "Black Wins!") 
            exit()

        count[0] += 1
        moves = list(board.legal_moves)
        if board.turn == chess.WHITE:
            maxx = float('-inf')
            for move in moves:
                board.push(move)

                val = self.pruning(board, depth+1, move_map, count, alpha, beta)
                if depth == 0 and val >= maxx:
                    move_map[val] = move 
                board.pop()

                alpha = max(alpha, val)
                if beta <= alpha:
                    break

                maxx = max(maxx, val)
                
            return maxx
        else:
            minn = float('inf')
            for move in moves:
                board.push(move)

                val = self.pruning(board, depth+1, move_map, count, alpha, beta)
                if depth == 0 and val <= minn:
                    move_map[val] = move 
                board.pop()

                beta = min(beta, val)
                if beta <= alpha:
                    break

                minn = min(minn, val)   
                 
            return minn


    def choose_move(self, board):
        count = [0]

        move_map = {}
        self.pruning(board, 0, move_map, count, float('-inf'), float('inf'))

        print('pruningAI is recommending move ', move_map[max(move_map.keys())])
        print("pruning call count: ", count)
        for k,v in move_map.items():
            print(k,v)

        return move_map[max(move_map.keys())] if board.turn == chess.WHITE else move_map[min(move_map.keys())]

