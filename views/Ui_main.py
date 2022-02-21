# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(569, 562)
        MainWindow.setMinimumSize(QSize(569, 562))
        MainWindow.setMaximumSize(QSize(569, 562))
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionCargar = QAction(MainWindow)
        self.actionCargar.setObjectName(u"actionCargar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(11, 11, 546, 130))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.nombre_lineEdit = QLineEdit(self.groupBox)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")

        self.gridLayout.addWidget(self.nombre_lineEdit, 0, 1, 1, 2)

        self.marca_lineEdit = QLineEdit(self.groupBox)
        self.marca_lineEdit.setObjectName(u"marca_lineEdit")

        self.gridLayout.addWidget(self.marca_lineEdit, 0, 4, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.precio_doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.precio_doubleSpinBox.setObjectName(u"precio_doubleSpinBox")
        self.precio_doubleSpinBox.setMaximum(100000.000000000000000)

        self.gridLayout.addWidget(self.precio_doubleSpinBox, 0, 6, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 4, 1, 1)

        self.cantidad_spinBox = QSpinBox(self.groupBox)
        self.cantidad_spinBox.setObjectName(u"cantidad_spinBox")
        self.cantidad_spinBox.setMaximum(100000)

        self.gridLayout.addWidget(self.cantidad_spinBox, 2, 5, 1, 2)

        self.categoria_lineEdit = QLineEdit(self.groupBox)
        self.categoria_lineEdit.setObjectName(u"categoria_lineEdit")

        self.gridLayout.addWidget(self.categoria_lineEdit, 2, 2, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.registrar_pushButton = QPushButton(self.groupBox)
        self.registrar_pushButton.setObjectName(u"registrar_pushButton")

        self.gridLayout.addWidget(self.registrar_pushButton, 3, 0, 1, 7)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 140, 551, 367))
        self.registros_tableWidget = QTableWidget(self.groupBox_2)
        if (self.registros_tableWidget.columnCount() < 6):
            self.registros_tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.registros_tableWidget.setObjectName(u"registros_tableWidget")
        self.registros_tableWidget.setGeometry(QRect(10, 20, 531, 291))
        self.registros_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.limpiar_pushButton = QPushButton(self.groupBox_2)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")
        self.limpiar_pushButton.setGeometry(QRect(22, 320, 511, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 569, 26))
        self.menuGuardar = QMenu(self.menubar)
        self.menuGuardar.setObjectName(u"menuGuardar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGuardar.menuAction())
        self.menuGuardar.addAction(self.actionGuardar)
        self.menuGuardar.addAction(self.actionCargar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionCargar.setText(QCoreApplication.translate("MainWindow", u"Cargar", None))
#if QT_CONFIG(shortcut)
        self.actionCargar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Categoria:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Marca:", None))
        self.registrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Tabla", None))
        ___qtablewidgetitem = self.registros_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem1 = self.registros_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.registros_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Marca", None));
        ___qtablewidgetitem3 = self.registros_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem4 = self.registros_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem5 = self.registros_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.menuGuardar.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

