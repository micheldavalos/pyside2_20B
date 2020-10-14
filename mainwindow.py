from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from libreria_20B.libreria import Libreria
from libreria_20B.libro import Libro

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.libreria = Libreria()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.monstrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        # self.libreria.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.libreria))

    @Slot()
    def click_agregar(self):
        titulo = self.ui.titulo_lineEdit.text()
        autor = self.ui.autor_lineEdit.text()
        publicado = self.ui.publicado_spinBox.value()
        editorial = self.ui.editorial_lineEdit.text()

        libro = Libro(titulo, autor, publicado, editorial)
        self.libreria.agregar_final(libro)

        # print(titulo, autor, publicado, editorial)
        # self.ui.salida.insertPlainText(titulo + autor + str(publicado) + editorial)
    @Slot()
    def click_agregar_inicio(self):
        titulo = self.ui.titulo_lineEdit.text()
        autor = self.ui.autor_lineEdit.text()
        publicado = self.ui.publicado_spinBox.value()
        editorial = self.ui.editorial_lineEdit.text()

        libro = Libro(titulo, autor, publicado, editorial)
        self.libreria.agregar_inicio(libro)