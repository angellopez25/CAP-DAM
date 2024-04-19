# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 20, 544, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ventana_principal = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ventana_principal.setFont(font)
        self.ventana_principal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ventana_principal.setAlignment(QtCore.Qt.AlignCenter)
        self.ventana_principal.setObjectName("ventana_principal")
        self.gridLayout_2.addWidget(self.ventana_principal, 0, 0, 1, 1)
        self.table_products = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_products.setRowCount(10)
        self.table_products.setObjectName("table_products")
        self.table_products.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.table_products, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_list = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_list.setFont(font)
        self.btn_list.setObjectName("btn_list")
        self.gridLayout.addWidget(self.btn_list, 0, 0, 1, 1)
        self.btn_update = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setObjectName("btn_update")
        self.gridLayout.addWidget(self.btn_update, 0, 1, 1, 1)
        self.btn_create = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setObjectName("btn_create")
        self.gridLayout.addWidget(self.btn_create, 0, 2, 1, 1)
        self.btn_select = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_select.setFont(font)
        self.btn_select.setObjectName("btn_select")
        self.gridLayout.addWidget(self.btn_select, 0, 3, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 0, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ventana_principal.setText(_translate("MainWindow", "Ventana Principal"))
        item = self.table_products.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CODIGO"))
        item = self.table_products.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE"))
        item = self.table_products.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PRECIO"))
        item = self.table_products.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CATEGORIA"))
        self.btn_list.setText(_translate("MainWindow", "Listar"))
        self.btn_update.setText(_translate("MainWindow", "Actualizar"))
        self.btn_create.setText(_translate("MainWindow", "Crear"))
        self.btn_select.setText(_translate("MainWindow", "Seleccionar"))
        self.btn_delete.setText(_translate("MainWindow", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
