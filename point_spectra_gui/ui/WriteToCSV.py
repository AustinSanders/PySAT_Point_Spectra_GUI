# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\WriteToCSV.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(294, 352)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chooseDataSetLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataSetLabel.setObjectName("chooseDataSetLabel")
        self.verticalLayout_2.addWidget(self.chooseDataSetLabel)
        self.chooseDataSetComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataSetComboBox.setObjectName("chooseDataSetComboBox")
        self.verticalLayout_2.addWidget(self.chooseDataSetComboBox)
        self.variablesToWriteLabel = QtWidgets.QLabel(self.groupBox)
        self.variablesToWriteLabel.setObjectName("variablesToWriteLabel")
        self.verticalLayout_2.addWidget(self.variablesToWriteLabel)
        self.variablesToWriteListWidget = QtWidgets.QListWidget(self.groupBox)
        self.variablesToWriteListWidget.setObjectName("variablesToWriteListWidget")
        item = QtWidgets.QListWidgetItem()
        self.variablesToWriteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variablesToWriteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.variablesToWriteListWidget.addItem(item)
        self.verticalLayout_2.addWidget(self.variablesToWriteListWidget)
        self.specifyAFilenameLabel = QtWidgets.QLabel(self.groupBox)
        self.specifyAFilenameLabel.setObjectName("specifyAFilenameLabel")
        self.verticalLayout_2.addWidget(self.specifyAFilenameLabel)
        self.specifyAFilenameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.specifyAFilenameLineEdit.setObjectName("specifyAFilenameLineEdit")
        self.verticalLayout_2.addWidget(self.specifyAFilenameLineEdit)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Write to CSV"))
        self.chooseDataSetLabel.setText(_translate("Form", "Choose data set to write to *.csv:"))
        self.variablesToWriteLabel.setText(_translate("Form", "Variables to write:"))
        __sortingEnabled = self.variablesToWriteListWidget.isSortingEnabled()
        self.variablesToWriteListWidget.setSortingEnabled(False)
        item = self.variablesToWriteListWidget.item(0)
        item.setText(_translate("Form", "comp"))
        item = self.variablesToWriteListWidget.item(1)
        item.setText(_translate("Form", "meta"))
        item = self.variablesToWriteListWidget.item(2)
        item.setText(_translate("Form", "wvl"))
        self.variablesToWriteListWidget.setSortingEnabled(__sortingEnabled)
        self.specifyAFilenameLabel.setText(_translate("Form", "Specify a filename:"))
        self.specifyAFilenameLineEdit.setText(_translate("Form", "output.csv"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

