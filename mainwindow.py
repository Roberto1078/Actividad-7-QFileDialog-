from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from administrador.particula import Particula
from administrador.particulas import Particulas


class Mainwindow(QMainWindow) :
    def __init__(self) :
        super(Mainwindow, self).__init__()
        self.particulas = Particulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.action_guardar.triggered.connect(self.guardar_archivo)
        self.ui.action_abrir.triggered.connect(self.abrir_archivo)

    @Slot()
    def abrir_archivo(self) :
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        if self.particulas.abrir(ubicacion) :
            QMessageBox.information(
                self,
                'Exito',
                'Se abrio el archivo ' + ubicacion
            )
        else :
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo abrir el archivo'
            )

    @Slot()
    def guardar_archivo(self) :
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        
        if self.particulas.guardar(ubicacion) :
            QMessageBox.information(
                self,
                'Exito',
                'Guardado correctamente en ' + ubicacion
            )
        else :
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo guardar el archivo'
            )

    @Slot()
    def click_mostrar(self) :
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))

    @Slot()
    def click_agregar_final(self) :
        i_d = self.ui.id_lineEdit.text()
        origen_x  = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(i_d, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self) :
        print("Agregado Correctamente :)")
        id = self.ui.id_lineEdit.text()
        origen_x  = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)
