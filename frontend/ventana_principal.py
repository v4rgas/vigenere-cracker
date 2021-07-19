from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QVBoxLayout, QWidget, QApplication, QFileDialog, QTableWidgetItem, QHeaderView, QMessageBox

import sys

class VentanaPrincipal(QWidget):
    senal_set_file = pyqtSignal(str)
    senal_find_length = pyqtSignal()
    senal_find_key = pyqtSignal(int)
    senal_decodificar = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()
    
    def init_ui(self):
        self.main_vbox = QVBoxLayout()
        self.setLayout(self.main_vbox)
        
        top_hbox = QHBoxLayout()
        self.label0 = QLabel(self, text='PASO 1:')
        self.main_vbox.addWidget(self.label0)

        self.label1 = QLabel(self, text='Elige un archivo')
        top_hbox.addWidget(self.label1)
        
        self.button1 = QPushButton('Click Aca')
        self.button1.clicked.connect(self.browsefiles)
        top_hbox.addWidget(self.button1)
        
        self.main_vbox.addLayout(top_hbox)


        mid_hbox = QHBoxLayout()

        self.label3 = QLabel(self, text='PASO 2:')
        self.main_vbox.addWidget(self.label3)

        self.label4 = QLabel(self, text='Encuentra el largo:')
        mid_hbox.addWidget(self.label4)
        
        self.button2 = QPushButton('Click Aca')
        self.button2.clicked.connect(self.start_find_length)
        mid_hbox.addWidget(self.button2)
        self.main_vbox.addLayout(mid_hbox)

        self.tabla_largo = QTableWidget()
        self.tabla_largo.setRowCount(4)
        self.tabla_largo.setColumnCount(2)
        self.tabla_largo.setHorizontalHeaderLabels(['Distancia', 'Frecuencia'])
        self.tabla_largo.horizontalHeader().setStretchLastSection(True)
        self.tabla_largo.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.main_vbox.addWidget(self.tabla_largo)

        self.largo_box = QComboBox()
        self.main_vbox.addWidget(self.largo_box)

        low_hbox = QHBoxLayout()

        self.label5 = QLabel(self, text='PASO 3:')
        self.main_vbox.addWidget(self.label5)

        self.label6 = QLabel(self, text='Encuentra clave:')
        low_hbox.addWidget(self.label6)

        self.button3 = QPushButton('Click Aca')
        self.button3.clicked.connect(self.start_find_key)
        low_hbox.addWidget(self.button3)
        self.main_vbox.addLayout(low_hbox)

        self.entry_clave = QLineEdit('')
        self.main_vbox.addWidget(self.entry_clave)
        
        self.boton_decodificar = QPushButton('Decodificar')
        self.boton_decodificar.clicked.connect(lambda: self.senal_decodificar.emit())
        self.main_vbox.addWidget(self.boton_decodificar)


        self.message_box= QMessageBox(self)
        self.message_box.setWindowTitle('ERROR')
        self.message_box.setText("------------")
        self.message_box.setIcon(QMessageBox.Critical)

    def browsefiles(self, *args):
        fname, _ = QFileDialog.getOpenFileName(self,
            'Open file',"QFileDialog.getOpenFileName()",
            'Text (*.txt)')
        self.senal_set_file.emit(fname)
        
    def start_find_length(self, *args):
        self.button2.setEnabled(False)
        self.senal_find_length.emit()

    def start_find_key(self, *args):
        self.button3.setEnabled(False)
        self.senal_find_key.emit(int(self.largo_box.currentText()))

    def add_to_table(self, tuple_list):
        self.largo_box.clear()
        self.button2.setEnabled(True)
        for index, tupla in enumerate(tuple_list):
            distance, frec = tupla

            self.tabla_largo.setItem(index, 0, QTableWidgetItem(str(distance)))
            self.tabla_largo.setItem(index, 1, QTableWidgetItem(str(frec)))

            self.largo_box.addItem(str(distance))

    def set_text(self, text):
        self.button3.setEnabled(True)
        self.entry_clave.setText(text)

    def pop_up(self, texto):
        self.message_box.setText(texto)
        self.message_box.exec_()


            

if __name__ == "__main__":
    APP = QApplication(sys.argv)

    GUI = VentanaPrincipal()

    ret = APP.exec_()
    sys.exit(ret)
