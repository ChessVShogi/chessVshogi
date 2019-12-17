# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GamemodeWindow(object):
    def setupUi(self, GamemodeWindow):
        GamemodeWindow.setObjectName("GamemodeWindow")
        GamemodeWindow.resize(640, 480)
        GamemodeWindow.setMinimumSize(QtCore.QSize(640, 480))
        GamemodeWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.verticalLayout = QtWidgets.QVBoxLayout(GamemodeWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(GamemodeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonChess = QtWidgets.QPushButton(GamemodeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonChess.sizePolicy().hasHeightForWidth())
        self.buttonChess.setSizePolicy(sizePolicy)
        self.buttonChess.setMinimumSize(QtCore.QSize(90, 30))
        self.buttonChess.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonChess.setFont(font)
        self.buttonChess.setObjectName("buttonChess")
        self.horizontalLayout.addWidget(self.buttonChess)
        self.buttonHybrid = QtWidgets.QPushButton(GamemodeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonHybrid.sizePolicy().hasHeightForWidth())
        self.buttonHybrid.setSizePolicy(sizePolicy)
        self.buttonHybrid.setMinimumSize(QtCore.QSize(90, 30))
        self.buttonHybrid.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonHybrid.setFont(font)
        self.buttonHybrid.setObjectName("buttonHybrid")
        self.horizontalLayout.addWidget(self.buttonHybrid)
        self.buttonShogi = QtWidgets.QPushButton(GamemodeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonShogi.sizePolicy().hasHeightForWidth())
        self.buttonShogi.setSizePolicy(sizePolicy)
        self.buttonShogi.setMinimumSize(QtCore.QSize(90, 30))
        self.buttonShogi.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonShogi.setFont(font)
        self.buttonShogi.setObjectName("buttonShogi")
        self.horizontalLayout.addWidget(self.buttonShogi)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.buttonCustom = QtWidgets.QPushButton(GamemodeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCustom.sizePolicy().hasHeightForWidth())
        self.buttonCustom.setSizePolicy(sizePolicy)
        self.buttonCustom.setMinimumSize(QtCore.QSize(90, 30))
        self.buttonCustom.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonCustom.setFont(font)
        self.buttonCustom.setObjectName("buttonCustom")
        self.horizontalLayout_2.addWidget(self.buttonCustom)
        self.buttonVersus = QtWidgets.QPushButton(GamemodeWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonVersus.sizePolicy().hasHeightForWidth())
        self.buttonVersus.setSizePolicy(sizePolicy)
        self.buttonVersus.setMinimumSize(QtCore.QSize(90, 30))
        self.buttonVersus.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonVersus.setFont(font)
        self.buttonVersus.setObjectName("buttonVersus")
        self.horizontalLayout_2.addWidget(self.buttonVersus)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

        self.retranslateUi(GamemodeWindow)
        QtCore.QMetaObject.connectSlotsByName(GamemodeWindow)

    def retranslateUi(self, GamemodeWindow):
        _translate = QtCore.QCoreApplication.translate
        GamemodeWindow.setWindowTitle(_translate("GamemodeWindow", "Form"))
        self.label.setText(_translate("GamemodeWindow", "Choose a Game Mode"))
        self.buttonChess.setText(_translate("GamemodeWindow", "Chess"))
        self.buttonHybrid.setText(_translate("GamemodeWindow", "Hybrid"))
        self.buttonShogi.setText(_translate("GamemodeWindow", "Shogi"))
        self.buttonCustom.setText(_translate("GamemodeWindow", "Custom"))
        self.buttonVersus.setText(_translate("GamemodeWindow", "Versus"))
