import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
from checkers.checkers import game as ch
from snake.snake import game as sn

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def sai(self):
        App = sn(700,700)
        App.on_init()



        App.ai_game(ai,True,10,None)

    def splay(self):
        App = sn(700,700)
        App.on_init()
        App.play_game(15)

    def cai(self):
        App = ch(800,800)

        App.reset(True)

        top = AI()
        bottom = AI()
        top.importAI('top')
        bottom.importAI('bottom')

        App.return_board(True)

        for turn in range(200):
            #print([y for y in top.evaluate(App.return_board(False))])
            App.make_move([y for y in top.evaluate(App.return_board(False))])

            #print([y for y in bottom.evaluate(App.return_board(False))])
            App.make_move([y for y in bottom.evaluate(App.return_board(False))])


            App.event()
            App.render_game(fps)
            print(turn, [x for x in App.return_fitness()])

    def cplay(self):
        App = ch(800,800)
        App.on_init()
        App.play_game(15)

    def main_menu(self):

        self.Saibutton = QtWidgets.QPushButton("Snake ai")
        self.Splaybutton = QtWidgets.QPushButton("play Snake")
        self.Caibutton = QtWidgets.QPushButton("Checkers ai")
        self.Cplaybutton = QtWidgets.QPushButton("play Checkers")


        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.Saibutton)
        self.layout.addWidget(self.Splaybutton)
        self.layout.addWidget(self.Caibutton)
        self.layout.addWidget(self.Cplaybutton)
        self.setLayout(self.layout)

        self.Splaybutton.clicked.connect(self.splay)
        self.Saibutton.clicked.connect(self.sai)
        self.Caibutton.clicked.connect(self.cai)
        self.Cplaybutton.clicked.connect(self.cplay)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 400)
    widget.main_menu()
    widget.show()

    sys.exit(app.exec_())
