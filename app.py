import tkinter as tk

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def jogo_da_velha():
    return render_template('jogo_da_velha.html')


class JogoDaVelha:


# O restante do código do jogo da velha

if __name__ == "__main__":
    root = tk.Tk()
    game = JogoDaVelha(root)
    root.mainloop()
