import sys

from PyQt5.QtWidgets import QApplication

from backend.ventana_principal_backend import VentanaPrincipalBackend
from frontend.ventana_principal import VentanaPrincipal
if __name__ == "__main__":
    APP = QApplication(sys.argv)

    frontend = VentanaPrincipal()
    backend = VentanaPrincipalBackend()

    frontend.senal_set_file.connect(backend.set_file)
    frontend.senal_find_length.connect(backend.start_find_length)
    frontend.senal_find_key.connect(backend.start_find_key)
    frontend.senal_decodificar.connect(backend.decodificar)
    frontend.senal_change_lang.connect(backend.change_lang)

    backend.senal_add_to_table.connect(frontend.add_to_table)
    backend.senal_set_text.connect(frontend.set_text)
    backend.senal_set_recomended.connect(frontend.set_recomended)

    backend.senal_boton_archivo.connect(
        frontend.boton_elige_archivo.setEnabled)
    backend.senal_boton_encuentra_largo.connect(
        frontend.boton_encuentra_largo.setEnabled)
    backend.senal_boton_encuentra_key.connect(
        frontend.boton_encuentra_key.setEnabled)
    backend.senal_boton_decodificar.connect(
        frontend.boton_decodificar.setEnabled)

    ret = APP.exec_()
    sys.exit(ret)
