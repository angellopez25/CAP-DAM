# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\create_product.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 276)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 40, 304, 190))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.imput_codigo = QtWidgets.QLineEdit(self.widget)
        self.imput_codigo.setObjectName("imput_codigo")
        self.gridLayout.addWidget(self.imput_codigo, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.imput_name = QtWidgets.QLineEdit(self.widget)
        self.imput_name.setObjectName("imput_name")
        self.gridLayout.addWidget(self.imput_name, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.imput_precio = QtWidgets.QLineEdit(self.widget)
        self.imput_precio.setObjectName("imput_precio")
        self.gridLayout.addWidget(self.imput_precio, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.imput_categoria = QtWidgets.QLineEdit(self.widget)
        self.imput_categoria.setObjectName("imput_categoria")
        self.gridLayout.addWidget(self.imput_categoria, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.btn_create = QtWidgets.QPushButton(self.widget)
        self.btn_create.setObjectName("btn_create")
        self.gridLayout_2.addWidget(self.btn_create, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Crear Nuevo Producto"))
        self.label_2.setText(_translate("Form", "Codigo"))
        self.imput_codigo.setPlaceholderText(_translate("Form", "Codigo"))
        self.label_3.setText(_translate("Form", "Nombre"))
        self.imput_name.setPlaceholderText(_translate("Form", "Nombre"))
        self.label_4.setText(_translate("Form", "Precio"))
        self.imput_precio.setPlaceholderText(_translate("Form", "Precio"))
        self.label_5.setText(_translate("Form", "Categoria"))
        self.imput_categoria.setPlaceholderText(_translate("Form", "Categoria"))
        self.btn_create.setText(_translate("Form", "Crear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
