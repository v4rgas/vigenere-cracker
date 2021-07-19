import sys
from ntpath import basename

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class VentanaPrincipal(QWidget):
    senal_set_file = pyqtSignal(str)
    senal_find_length = pyqtSignal()
    senal_find_key = pyqtSignal(int)
    senal_decodificar = pyqtSignal()
    senal_change_lang = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

        self.show()

    def init_ui(self):
        self.setWindowTitle('Rompiendo codificación Vigenere')

        self.main_vbox = QVBoxLayout()
        self.setLayout(self.main_vbox)

        top_hbox = QHBoxLayout()
        self.label_paso1 = QLabel(self, text='PASO 1:')
        self.main_vbox.addWidget(self.label_paso1)

        self.label_elige_archivo = QLabel(self, text='Elige un archivo')
        top_hbox.addWidget(self.label_elige_archivo)

        self.boton_elige_archivo = QPushButton('Click Aca')
        self.boton_elige_archivo.clicked.connect(self.browsefiles)
        top_hbox.addWidget(self.boton_elige_archivo)

        self.main_vbox.addLayout(top_hbox)

        language_hbox = QHBoxLayout()
        self.label_idiomas = QLabel(
            self, text='Elige un idioma para intentar decodificar')
        language_hbox.addWidget(self.label_idiomas)

        self.language_box = QComboBox()
        self.language_box.addItems(['Ingles', 'Español'])
        self.language_box.currentIndexChanged.connect(self.change_lang)
        language_hbox.addWidget(self.language_box)

        self.main_vbox.addLayout(language_hbox)

        mid_hbox = QHBoxLayout()

        self.label_paso2 = QLabel(self, text='PASO 2:')
        self.main_vbox.addWidget(self.label_paso2)

        self.label_encuentra_largo = QLabel(self, text='Encuentra el largo:')
        mid_hbox.addWidget(self.label_encuentra_largo)

        self.boton_encuentra_largo = QPushButton('Click Aca')
        self.boton_encuentra_largo.clicked.connect(self.start_find_length)
        mid_hbox.addWidget(self.boton_encuentra_largo)
        self.main_vbox.addLayout(mid_hbox)

        self.tabla_largo = QTableWidget()
        self.tabla_largo.setRowCount(4)
        self.tabla_largo.setColumnCount(2)
        self.tabla_largo.setHorizontalHeaderLabels(['Distancia', 'Frecuencia'])
        self.tabla_largo.horizontalHeader().setStretchLastSection(True)
        self.tabla_largo.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.main_vbox.addWidget(self.tabla_largo)

        self.label_largo_recomendado = QLabel('Largo recomendado:', self)
        self.main_vbox.addWidget(self.label_largo_recomendado)

        self.largo_box = QComboBox()
        self.main_vbox.addWidget(self.largo_box)

        low_hbox = QHBoxLayout()

        self.label_paso3 = QLabel(self, text='PASO 3:')
        self.main_vbox.addWidget(self.label_paso3)

        self.label_encuentra_clave = QLabel(self, text='Encuentra clave:')
        low_hbox.addWidget(self.label_encuentra_clave)

        self.boton_encuentra_key = QPushButton('Click Aca')
        self.boton_encuentra_key.clicked.connect(self.start_find_key)
        low_hbox.addWidget(self.boton_encuentra_key)
        self.main_vbox.addLayout(low_hbox)

        self.entry_clave = QLineEdit('')
        self.main_vbox.addWidget(self.entry_clave)

        self.boton_decodificar = QPushButton('Decodificar')
        self.boton_decodificar.clicked.connect(
            lambda: self.senal_decodificar.emit())
        self.main_vbox.addWidget(self.boton_decodificar)

        self.message_box = QMessageBox(self)
        self.message_box.setWindowTitle('ERROR')
        self.message_box.setText("------------")
        self.message_box.setIcon(QMessageBox.Critical)

    def change_lang(self):
        langs = {'Español': 'ESP', 'Ingles': 'ENG'}
        self.senal_change_lang.emit(langs[self.language_box.currentText()])

    def browsefiles(self, *args):
        fname, _ = QFileDialog.getOpenFileName(self,
                                               'Open file', '',
                                               'Text (*.txt)')
        self.senal_set_file.emit(fname)
        self.label_elige_archivo.setText(basename(fname))
        self.label_elige_archivo.setStyleSheet('color: green;')

    def start_find_length(self, *args):
        self.senal_find_length.emit()

    def start_find_key(self, *args):
        self.senal_find_key.emit(int(self.largo_box.currentText()))

    def add_to_table(self, tuple_list):
        self.largo_box.clear()
        for index, tupla in enumerate(tuple_list):
            distance, frec = tupla

            self.tabla_largo.setItem(index, 0, QTableWidgetItem(str(distance)))
            self.tabla_largo.setItem(index, 1, QTableWidgetItem(str(frec)))

            self.largo_box.addItem(str(distance))

    def set_text(self, text):
        self.entry_clave.setText(text)

    def pop_up(self, texto):
        self.message_box.setText(texto)
        self.message_box.exec_()

    def set_recomended(self, texto):
        self.largo_box.setCurrentText(texto)


if __name__ == "__main__":
    APP = QApplication(sys.argv)

    GUI = VentanaPrincipal()

    ret = APP.exec_()
    sys.exit(ret)
