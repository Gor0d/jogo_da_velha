import tkinter as tk


class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        # Variáveis para controle
        self.turn = 'X'
        self.board = ['' for _ in range(9)]
        self.buttons = [None] * 9

        # Carregar o código HTML como texto
        html_code = """
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Jogo da Velha</title>
            <style>
                /*   body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        text-align: center;
    }

    h1 {
        color: #333;
    }

    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .board {
        background-color: #333;
        display: grid;
        grid-template-columns: repeat(3, 100px);
        grid-gap: 5px;
        padding: 10px;
        border-radius: 10px;
    }

    .cell {
        width: 100px;
        height: 100px;
        background-color: #fff;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 36px;
        color: #333;
        border-radius: 5px;
        cursor: pointer;
    }

    .cell:hover {
        background-color: #ddd;
    } */
            </style>
        </head>
        <body>
            <h1>Jogo da Velha</h1>
            <div class="container">
                <div class="board">
                    <!-- Conteúdo do tabuleiro -->
                </div>
            </div>
        </body>
        </html>
        """

        # Criar widget de navegador da web
        webview = tk.Text(root, wrap=tk.WORD)
        webview.insert(tk.INSERT, html_code)
        webview.pack()


if __name__ == '__main__':
    root = tk.Tk()
    game = JogoDaVelha(root)
    root.mainloop()
