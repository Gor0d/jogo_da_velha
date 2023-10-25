import tkinter as tk
from tkinter import messagebox


class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        # Variáveis para controle
        self.turn = 'X'
        self.board = ['' for _ in range(9)]
        self.buttons = [None] * 9


        for i in range(9):
            row, col = divmod(i, 3)
            self.buttons[i] = tk.Button(root, text='', width=10, height=3, command=lambda i=i: self.click(i))
            self.buttons[i].grid(row=row, column=col)

    def click(self, i):
        if self.board[i] == '' and not self.check_winner():
            self.board[i] = self.turn
            self.buttons[i]['text'] = self.turn
            if self.check_winner():
                messagebox.showinfo("Fim do Jogo", f"Jogador {self.turn} venceu!")
            elif all(cell != '' for cell in self.board):
                messagebox.showinfo("Fim do Jogo", "Empate!")
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
    root = tk.Tk()
    game = JogoDaVelha(root)
    root.mainloop()
