# -*- coding: utf-8 -*-

# Form implementation generated from reading util file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\util\MultiplyByVector.util'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 1)
        self.vectorFileLabel = QtWidgets.QLabel(self.groupBox)
        self.vectorFileLabel.setObjectName("vectorFileLabel")
        self.gridLayout.addWidget(self.vectorFileLabel, 1, 0, 1, 1)
        self.vectorFileLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.vectorFileLineEdit.setObjectName("vectorFileLineEdit")
        self.gridLayout.addWidget(self.vectorFileLineEdit, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Peak Areas"))
        self.chooseDataLabel.setText(_translate("Form", "Choose data"))
        self.vectorFileLabel.setText(_translate("Form", "Vector file"))
        self.vectorFileLineEdit.setText(_translate("Form", "*.csv"))
        self.pushButton.setText(_translate("Form", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

