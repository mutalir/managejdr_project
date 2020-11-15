from gui import Main, caracs
from pnj import pnj
from PyQt5 import QtCore, QtGui, QtWidgets
import breeze_resources

class StatsTableModel(QtCore.QAbstractTableModel):
    #Permet de donner la forme du tableau et comment il doit être rempli.
    def __init__(self, caracs):
        super(StatsTableModel, self).__init__()

        self.stats = list(caracs.keys())
        self._data = [[caracs[key]] for key in self.stats]

    def data(self, index, role):
        #Donne la manière dont doit être choisi les données du tableau.
        #index.row donne la ligne actuellement considérée par l'application et index.column, la colonne.
        #Tous les rôles permettent à l'application de savoir quoi regarder.
        if role == QtCore.Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignVCenter + QtCore.Qt.AlignHCenter

        # if role == QtCore.Qt.BackgroundRole:
        #     return QtGui.QColor('black')
        #
        # if role == QtCore.Qt.ForegroundRole:
        #     return QtGui.QColor('orange')

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Vertical:
                return str(self.stats[section])

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The length of the sub-list (columns)
        return 1

class CaracsWin(caracs.Ui_MainWindow, QtWidgets.QMainWindow):
    #c'est la deuxième fenêtre. Le "parent" dans super et init permet d'en faire une fenêtre secondaire par rapport
    #à la fenêtre principale.
    def __init__(self, parent, PNJ):
        super(CaracsWin, self).__init__(parent)
        self.setupUi(self)

        self.StatsModel = StatsTableModel(PNJ.AfficherCaracs())
        self.CaracsTable.setModel(self.StatsModel)
        #Permet de rendre la taille de la première colonne adaptée à ce qu'il y a dedans.
        header = self.CaracsTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

class MainGUI(Main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        self.setupUi(self)
        #Connecte le bouton à la fonction CreatePNJ.
        self.CreateButton.clicked.connect(self.CreatePNJ)
        #Connecte les items de la liste à la fonction DisplayCaracs.
        self.PNJList.itemClicked.connect(self.DisplayCaracs)
        self.PNJs = {}

    def CreatePNJ(self):
        #Créer le PNJ et le garde dans self.PNJs sous forme de dictionnaire
        if self.PaysanButton.isChecked():
            paysan = pnj.Pnj('Paysan')
            self.PNJs[paysan.name] = paysan
            self.PNJList.addItem(paysan.name)

    def DisplayCaracs(self, name):
        #Lance la deuxième fenêtre.
        CARACSWINDOW = CaracsWin(self, self.PNJs[name.text()])
        CARACSWINDOW.show()



if __name__ ==  '__main__':
    app = QtWidgets.QApplication([])
    qt_app = MainGUI()
    qt_app.show()
    qt_app.setAttribute(QtCore.Qt.WA_StyledBackground)
    # set stylesheet
    file = QtCore.QFile(":/dark.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    app.setStyle("plastique")
    app.exec_()
