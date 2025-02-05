from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class JogoDaVelha(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.jogador = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.botoes = []

        for linha in range(3):
            for coluna in range(3):
                botao = Button(font_size=32)
                botao.bind(on_release=self.jogar)
                self.add_widget(botao)
                self.botoes.append(botao)

    def jogar(self, botao):
        if botao.text == '':
            botao.text = self.jogador
            linha, coluna = divmod(self.botoes.index(botao), 3)
            self.tabuleiro[linha][coluna] = self.jogador

            if self.verificar():
                print(f"Jogador {self.jogador} é o vencedor!")
                self.reset()
                return

            self.alternar()

    def alternar(self):
        self.jogador = 'O' if self.jogador == 'X' else 'X'

    def verificar(self):
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] and linha[0] != '':
                return True

        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] and self.tabuleiro[0][coluna] != '':
                return True

        if (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] and self.tabuleiro[0][0] != '') or \
           (self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] and self.tabuleiro[0][2] != ''):
            return True

        return False

    def reset(self):
        for botao in self.botoes:
            botao.text = ''
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.jogador = 'X'

class JogoApp(App):
    def build(self):
        return JogoDaVelha()

if __name__ == '__main__':
    JogoApp().run()
