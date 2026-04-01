from flask import Flask, request, jsonify
from flask_cors import CORS
import chess
from chess_ai import Level2ChessAI
import time
import random

app = Flask(__name__)
CORS(app)

ai = Level2ChessAI()

@app.route('/')
def home():
    return {
        "message": "Chess AI API - Projek Akhir AI",
        "author": "(Kelompok 8) Dimas Abdus Syukur, Jonathan, Josua Moreno Silitonga",
        "nim": "24051204101, 24051204087, 24051204091", 
        "course": "Artificial Intelligence - Semester 3",
        "algorithm": "Minimax with Alpha-Beta Pruning"
    }

@app.route('/api/move', methods=['POST'])
def get_ai_move():
    data = request.json
    fen = data.get('fen', chess.Board().fen())
    depth = data.get('depth', 3)
    
    print(f"\n=== AI Move Request ===")
    print(f"FEN: {fen}")
    print(f"Depth: {depth}")
    
    start_time = time.time()
    
    try:
        # Buat board dari FEN
        board = chess.Board(fen)
        
        print(f"Board turn: {'WHITE' if board.turn else 'BLACK'}")
        legal_moves = list(board.legal_moves)
        print(f"Legal moves count: {len(legal_moves)}")
        
        # Cek jika game sudah berakhir
        if board.is_game_over():
            print("Game is already over")
            return jsonify({
                'success': False,
                'error': 'Game is already over'
            })
        
        if not legal_moves:
            print("No legal moves available")
            return jsonify({
                'success': False,
                'error': 'No legal moves available'
            })
        
        # Dapatkan move dari AI
        ai_move = ai.get_best_move(board, depth)
        
        if ai_move is None:
            print("AI returned None, using random move")
            ai_move = random.choice(legal_moves)
        
        # CRITICAL: Validasi move sebelum apply
        if ai_move not in legal_moves:
            print(f"ERROR: AI move {ai_move.uci()} is NOT in legal moves!")
            print(f"Legal moves: {[m.uci() for m in legal_moves]}")
            ai_move = random.choice(legal_moves)
            print(f"Using fallback random move: {ai_move.uci()}")
        
        print(f"AI chosen move: {ai_move.uci()}")
        
        # Generate SAN SEBELUM push move
        san_notation = board.san(ai_move)
        
        # Push move ke board
        board.push(ai_move)
        
        move_time = time.time() - start_time
        
        print(f"Move completed in {move_time:.3f}s")
        print(f"SAN: {san_notation}")
        print(f"New FEN: {board.fen()}")
        print("=" * 40)
        
        return jsonify({
            'success': True,
            'move': ai_move.uci(),
            'san': san_notation,
            'fen': board.fen(),
            'thinking_time': round(move_time, 3),
            'depth_searched': depth,
            'nodes_searched': ai.nodes_searched
        })
        
    except Exception as e:
        print(f"ERROR in get_ai_move: {str(e)}")
        import traceback
        traceback.print_exc()
        
        # Fallback: return random legal move
        try:
            board = chess.Board(fen)
            legal_moves = list(board.legal_moves)
            if legal_moves:
                random_move = random.choice(legal_moves)
                san = board.san(random_move)
                board.push(random_move)
                
                return jsonify({
                    'success': True,
                    'move': random_move.uci(),
                    'san': san,
                    'fen': board.fen(),
                    'thinking_time': 0.01,
                    'depth_searched': 1,
                    'note': 'Fallback: used random move due to error'
                })
        except Exception as fallback_error:
            print(f"Fallback also failed: {str(fallback_error)}")
            
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/evaluate', methods=['POST'])
def evaluate_position():
    data = request.json
    fen = data.get('fen', chess.Board().fen())
    
    try:
        board = chess.Board(fen)
        evaluation = ai.evaluate(board)
        
        return jsonify({
            'success': True,
            'evaluation': evaluation,
            'turn': 'white' if board.turn else 'black',
            'score_relative': 'white' if evaluation > 0 else 'black' if evaluation < 0 else 'equal'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/board', methods=['GET'])
def get_new_board():
    board = chess.Board()
    return jsonify({
        'fen': board.fen(),
        'turn': 'white' if board.turn else 'black'
    })

if __name__ == '__main__':
    print("\n" + "="*50)
    print("Chess AI - Projek Akhir Artificial Intelligence")
    print("="*50)
    print("Server running on http://localhost:5000")
    print("\nAPI Endpoints:")
    print("  GET  /              - API Info")
    print("  GET  /api/board     - Get new board")
    print("  POST /api/move      - Get AI move")
    print("  POST /api/evaluate  - Evaluate position")
    print("="*50 + "\n")
    
    app.run(debug=True, port=5000, host='127.0.0.1')