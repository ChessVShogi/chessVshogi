tester = False
if tester:
    from ingame_chess import *
    ui_item = Ui_IngameChess
else:
    from ingame_shogi import *
    ui_item = Ui_IngameShogi

Piece_Resource_Corresp = {
    "C_WP":":/Chess/resources/chess_48/Chess_plt48.png",
    "C_WR":":/Chess/resources/chess_48/Chess_rlt48.png",
    "C_WN":":/Chess/resources/chess_48/Chess_nlt48.png",
    "C_WB":":/Chess/resources/chess_48/Chess_blt48.png",
    "C_WQ":":/Chess/resources/chess_48/Chess_qlt48.png",
    "C_WK":":/Chess/resources/chess_48/Chess_klt48.png",
    "C_BP":":/Chess/resources/chess_48/Chess_pdt48.png",
    "C_BR":":/Chess/resources/chess_48/Chess_rdt48.png",
    "C_BN":":/Chess/resources/chess_48/Chess_ndt48.png",
    "C_BB":":/Chess/resources/chess_48/Chess_bdt48.png",
    "C_BQ":":/Chess/resources/chess_48/Chess_qdt48.png",
    "C_BK":":/Chess/resources/chess_48/Chess_kdt48.png",
    "S_BP":":/Ichiji/resources/Ichiji/Gfu.png",
    "S_BL":":/Ichiji/resources/Ichiji/Gkyo.png",
    "S_BN":":/Ichiji/resources/Ichiji/Gkei.png",
    "S_BS":":/Ichiji/resources/Ichiji/Ggin.png",
    "S_BG":":/Ichiji/resources/Ichiji/Gkin.png",
    "S_BK":":/Ichiji/resources/Ichiji/Ggyoku.png",
    "S_BB":":/Ichiji/resources/Ichiji/Gkaku.png",
    "S_BR":":/Ichiji/resources/Ichiji/Ghi.png",
    "S_WP":":/Ichiji/resources/Ichiji/Sfu.png",
    "S_WL":":/Ichiji/resources/Ichiji/Skyo.png",
    "S_WN":":/Ichiji/resources/Ichiji/Skei.png",
    "S_WS":":/Ichiji/resources/Ichiji/Sgin.png",
    "S_WG":":/Ichiji/resources/Ichiji/Skin.png",
    "S_WK":":/Ichiji/resources/Ichiji/Sou.png",
    "S_WB":":/Ichiji/resources/Ichiji/Skaku.png",
    "S_WR":":/Ichiji/resources/Ichiji/Shi.png",
}

class Window(QtWidgets.QWidget, ui_item):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.tiles = []
        for i in range(11, 100):
            try:
                tile = getattr(self, "Tile_{}".format(i))
                self.tiles.append(tile)
                tile.installEventFilter(self)
                if tile.property("Piece") != '':
                    tile.setPixmap(QtGui.QPixmap(Piece_Resource_Corresp[tile.property("Piece")]))
            except AttributeError:
                pass

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and source in self.tiles:
            if event.button() == 1:
                self.clicked_tile = source
                print("Coordinates:", self.clicked_tile.objectName()[-2], self.clicked_tile.objectName()[-1])
                if source.pixmap() is not None:
                    print("You are trying to move a piece!")
                    print("It is coded as:", source.property("Piece"))
        return super(Window, self).eventFilter(source, event)


import sys

app = QtWidgets.QApplication([])
w = Window()
sys.exit(app.exec_())