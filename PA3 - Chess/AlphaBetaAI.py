import chess

class AlphaBetaAI():
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
    
    def end_game(self, board, move):
        print('Checkmate: ' + str(move))
        board.push(move)
        print(board.outcome())
        print("White Wins!" if board.turn == chess.BLACK else "Black Wins!") 
        exit()

    def ab_minimax(self, board, depth, count, alpha, beta):
        if depth == self.max_depth: 
            return self.evaluation(board)

        if board.is_game_over():
            return 'end'

        count[0] += 1
        moves = list(board.legal_moves)
        if board.turn == chess.WHITE:
            maxx = float('-inf')
            for move in moves:
                board.push(move)
                val = self.ab_minimax(board, depth+1, count, alpha, beta)
                board.pop()
                maxx = max(maxx, val)

                alpha = max(alpha, val)
                if beta < alpha:
                    return val
            return maxx
        else:
            minn = float('inf')
            for move in moves:
                board.push(move)
                val = self.ab_minimax(board, depth+1, count, alpha, beta)
                board.pop()
                minn = min(val, minn)

                beta = min(alpha, val)
                if beta < alpha:
                    return val
            return minn


    def choose_move(self, board):
        count = [0]
        moves = list(board.legal_moves)
        score = float('-inf') if board.turn == chess.WHITE else float('inf')
        best_move = None
        for move in moves:
            board.push(move)
            val = self.ab_minimax(board, 1, count, float('-inf'), float('inf'))
            board.pop()

            if val == 'end':
                self.end_game(board, move)

            if val >= score and board.turn == chess.WHITE:
                best_move = move
                score = val
            elif val <= score and board.turn == chess.BLACK:
                best_move = move
                score = val
            # print(best_move, val)
        return best_move


