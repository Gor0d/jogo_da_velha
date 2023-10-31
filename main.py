from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def jogo_da_velha():
    return render_template('jogo_da_velha.html')

class JogoDaVelha:
    def __init__(self):
        self.turn = 'X'
        self.board = ['' for _ in range(9)]

    def click(self, i):
        if self.board[i] == '' and not self.check_winner():
            self.board[i] = self.turn
            if self.check_winner():
                return f"Jogador {self.turn} venceu!"
            elif all(cell != '' for cell in self.board):
                return "Empate!"
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in win_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != '':
                return True
        return False

if __name__ == "__main__":
    app.run()
