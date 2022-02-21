import json
from PySide2.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from views.Ui_main import Ui_MainWindow
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.columnasTabla()
        self.productos = []
        self.ubicacion = "./respaldo.json"
        self.input = "./input.json"
        self.guardado = True

        self.abrir()

        self.ui.registrar_pushButton.clicked.connect(self.registrar)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar)

        self.ui.actionGuardar.triggered.connect(self.action_guardar)
        self.ui.actionCargar.triggered.connect(self.action_abrir)
    
    def __del__(self):
        if not self.guardado:
            self.guardar()

    def columnasTabla(self):
        self.ui.registros_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    
    def llenarTabla(self):
        self.ui.registros_tableWidget.setRowCount(len(self.productos))

        for (index_row, row) in enumerate(self.productos):
            for(index_cell, cell) in enumerate(row):
                self.ui.registros_tableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def guardar(self):
        try:
            with open(self.ubicacion, 'w') as archivo:
                lista = []
                for producto in self.productos:
                    lista.append(
                        {
                            "codigo": producto[0],
                            "nombre": producto[1],
                            "marca": producto[2],
                            "precio": producto[3],
                            "categoria": producto[4],
                            "cantidad": producto[5]
                        }
                    )
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self):
        try:
            with open(self.ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                for producto in lista:
                    valores = producto.values()
                    self.productos.append(list(valores))
                self.llenarTabla()
                return 1
        except:
            return 0
    
    @Slot()
    def registrar(self):
        nombre = self.ui.nombre_lineEdit.text()
        marca = self.ui.marca_lineEdit.text()
        precio = self.ui.precio_doubleSpinBox.value()
        categoria = self.ui.categoria_lineEdit.text()
        cantidad = self.ui.cantidad_spinBox.value()
        codigo = categoria[0] + categoria[1] + marca[0] + marca[1] + marca[2] + nombre[0] + nombre[1]
        self.productos.append([codigo, nombre, marca, precio, categoria, cantidad])
        self.guardado = False
        self.llenarTabla()
    
    @Slot()
    def limpiar(self):
        self.productos.clear()
        self.llenarTabla()
    
    @Slot()
    def action_guardar(self):
        if self.guardar():
            QMessageBox.information(self, "Exito", "Se pudo crear el archivo")
            self.guardado = True
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear el archivo")

    @Slot()
    def action_abrir(self):
        if self.abrir():
            QMessageBox.information(self, "Exito", "Se pudo abrir el archivo")
        else:
            QMessageBox.critical(self, "Error", "No se pudo abrir el archivo")