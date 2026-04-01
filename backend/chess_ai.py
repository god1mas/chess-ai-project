import chess
import random

class Level2ChessAI:
    def __init__(self):
        self.piece_values = {
            chess.PAWN: 100,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.ROOK: 500,
            chess.QUEEN: 900,
            chess.KING: 20000
        }
        
        self.nodes_searched = 0

    def get_best_move(self, board, depth=2):
        """Cari langkah terbaik menggunakan Minimax dengan Alpha-Beta Pruning"""
        self.nodes_searched = 0
        
        # Validasi board state
        if board.is_game_over():
            return None
            
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            return None
        
        print(f"AI mencari dari {len(legal_moves)} legal moves")
        print(f"Current turn: {'WHITE' if board.turn else 'BLACK'}")
        
        best_move = None
        best_value = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        
        # Evaluasi setiap move
        for move in legal_moves:
            board.push(move)
            
            # Minimizing untuk lawan
            value = self.alphabeta(board, depth-1, alpha, beta, False)
            
            board.pop()
            
            self.nodes_searched += 1
            
            print(f"Move {move.uci()}: eval = {value}")
            
            if value > best_value:
                best_value = value
                best_move = move
            
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
        
        print(f"Best move chosen: {best_move.uci() if best_move else 'None'} with eval {best_value}")
        print(f"Nodes searched: {self.nodes_searched}")
        
        return best_move

    def alphabeta(self, board, depth, alpha, beta, maximizing):
        """Algoritma Minimax dengan Alpha-Beta Pruning"""
        self.nodes_searched += 1
        
        # Base case: reached depth limit or game over
        if depth == 0 or board.is_game_over():
            return self.evaluate(board)
        
        legal_moves = list(board.legal_moves)
        
        if maximizing:
            max_eval = -float('inf')
            for move in legal_moves:
                board.push(move)
                eval_score = self.alphabeta(board, depth-1, alpha, beta, False)
                board.pop()
                
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_moves:
                board.push(move)
                eval_score = self.alphabeta(board, depth-1, alpha, beta, True)
                board.pop()
                
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval

    def evaluate(self, board):
        """Evaluasi posisi papan catur dari perspektif pemain yang akan bergerak"""
        # Terminal states
        if board.is_checkmate():
            # Jika checkmate, pemain saat ini kalah
            return -100000
        
        if board.is_stalemate() or board.is_insufficient_material():
            return 0
        
        if board.is_fifty_moves() or board.is_repetition():
            return 0
        
        # Hitung material score dari perspektif WHITE
        white_score = 0
        black_score = 0
        
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                value = self.piece_values[piece.piece_type]
                if piece.color == chess.WHITE:
                    white_score += value
                else:
                    black_score += value
        
        # Tambahan evaluasi posisional sederhana
        white_score += self.positional_bonus(board, chess.WHITE)
        black_score += self.positional_bonus(board, chess.BLACK)
        
        # Hitung dari perspektif pemain yang akan bergerak
        if board.turn == chess.WHITE:
            return white_score - black_score
        else:
            return black_score - white_score

    def positional_bonus(self, board, color):
        """Bonus sederhana untuk posisi piece"""
        bonus = 0
        
        # Bonus untuk kontrol tengah
        center_squares = [chess.E4, chess.E5, chess.D4, chess.D5]
        for square in center_squares:
            piece = board.piece_at(square)
            if piece and piece.color == color:
                bonus += 10
        
        # Bonus untuk mobilitas (jumlah legal moves)
        if board.turn == color:
            bonus += len(list(board.legal_moves)) * 2
        
        return bonus