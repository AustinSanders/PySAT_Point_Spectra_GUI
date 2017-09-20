# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.gridLayout_2.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.figureNameLabel = QtWidgets.QLabel(self.groupBox)
        self.figureNameLabel.setObjectName("figureNameLabel")
        self.gridLayout_2.addWidget(self.figureNameLabel, 1, 0, 1, 1)
        self.plotTitleLabel = QtWidgets.QLabel(self.groupBox)
        self.plotTitleLabel.setObjectName("plotTitleLabel")
        self.gridLayout_2.addWidget(self.plotTitleLabel, 2, 0, 1, 1)
        self.xVariableLabel = QtWidgets.QLabel(self.groupBox)
        self.xVariableLabel.setObjectName("xVariableLabel")
        self.gridLayout_2.addWidget(self.xVariableLabel, 3, 0, 1, 1)
        self.xVariableListView = QtWidgets.QListView(self.groupBox)
        self.xVariableListView.setObjectName("xVariableListView")
        self.gridLayout_2.addWidget(self.xVariableListView, 3, 1, 1, 2)
        self.chooseColumnLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseColumnLabel.setObjectName("chooseColumnLabel")
        self.gridLayout_2.addWidget(self.chooseColumnLabel, 4, 0, 1, 1)
        self.chooseRowsLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseRowsLabel.setObjectName("chooseRowsLabel")
        self.gridLayout_2.addWidget(self.chooseRowsLabel, 5, 0, 1, 1)
        self.chooseRowsListView = QtWidgets.QListView(self.groupBox)
        self.chooseRowsListView.setObjectName("chooseRowsListView")
        self.gridLayout_2.addWidget(self.chooseRowsListView, 5, 1, 1, 2)
        self.colorLabel = QtWidgets.QLabel(self.groupBox)
        self.colorLabel.setObjectName("colorLabel")
        self.gridLayout_2.addWidget(self.colorLabel, 7, 0, 1, 1)
        self.lineLabel = QtWidgets.QLabel(self.groupBox)
        self.lineLabel.setObjectName("lineLabel")
        self.gridLayout_2.addWidget(self.lineLabel, 8, 0, 1, 1)
        self.alphaLabel = QtWidgets.QLabel(self.groupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.gridLayout_2.addWidget(self.alphaLabel, 9, 0, 1, 1)
        self.lineWidthLabel = QtWidgets.QLabel(self.groupBox)
        self.lineWidthLabel.setObjectName("lineWidthLabel")
        self.gridLayout_2.addWidget(self.lineWidthLabel, 10, 0, 1, 1)
        self.plotFilenameLabel = QtWidgets.QLabel(self.groupBox)
        self.plotFilenameLabel.setObjectName("plotFilenameLabel")
        self.gridLayout_2.addWidget(self.plotFilenameLabel, 11, 0, 1, 1)
        self.plotFilenameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.plotFilenameLineEdit.setObjectName("plotFilenameLineEdit")
        self.gridLayout_2.addWidget(self.plotFilenameLineEdit, 11, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 11, 2, 1, 1)
        self.figureNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.figureNameLineEdit.setObjectName("figureNameLineEdit")
        self.gridLayout_2.addWidget(self.figureNameLineEdit, 1, 1, 1, 2)
        self.plotTitleLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.plotTitleLineEdit.setObjectName("plotTitleLineEdit")
        self.gridLayout_2.addWidget(self.plotTitleLineEdit, 2, 1, 1, 2)
        self.chooseColumnComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseColumnComboBox.setObjectName("chooseColumnComboBox")
        self.gridLayout_2.addWidget(self.chooseColumnComboBox, 4, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minLabel = QtWidgets.QLabel(self.groupBox)
        self.minLabel.setObjectName("minLabel")
        self.horizontalLayout.addWidget(self.minLabel)
        self.minSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.minSpinBox.setObjectName("minSpinBox")
        self.horizontalLayout.addWidget(self.minSpinBox)
        self.maxLabel = QtWidgets.QLabel(self.groupBox)
        self.maxLabel.setObjectName("maxLabel")
        self.horizontalLayout.addWidget(self.maxLabel)
        self.maxSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.maxSpinBox.setObjectName("maxSpinBox")
        self.horizontalLayout.addWidget(self.maxSpinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 3)
        self.colorComboBox = QtWidgets.QComboBox(self.groupBox)
        self.colorComboBox.setObjectName("colorComboBox")
        self.gridLayout_2.addWidget(self.colorComboBox, 7, 1, 1, 2)
        self.lineComboBox = QtWidgets.QComboBox(self.groupBox)
        self.lineComboBox.setObjectName("lineComboBox")
        self.gridLayout_2.addWidget(self.lineComboBox, 8, 1, 1, 2)
        self.alphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.gridLayout_2.addWidget(self.alphaDoubleSpinBox, 9, 1, 1, 2)
        self.lineWidthDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.lineWidthDoubleSpinBox.setObjectName("lineWidthDoubleSpinBox")
        self.gridLayout_2.addWidget(self.lineWidthDoubleSpinBox, 10, 1, 1, 2)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.gridLayout_2.addWidget(self.chooseDataComboBox, 0, 1, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.chooseDataComboBox, self.figureNameLineEdit)
        Form.setTabOrder(self.figureNameLineEdit, self.plotTitleLineEdit)
        Form.setTabOrder(self.plotTitleLineEdit, self.xVariableListView)
        Form.setTabOrder(self.xVariableListView, self.chooseColumnComboBox)
        Form.setTabOrder(self.chooseColumnComboBox, self.chooseRowsListView)
        Form.setTabOrder(self.chooseRowsListView, self.minSpinBox)
        Form.setTabOrder(self.minSpinBox, self.maxSpinBox)
        Form.setTabOrder(self.maxSpinBox, self.colorComboBox)
        Form.setTabOrder(self.colorComboBox, self.lineComboBox)
        Form.setTabOrder(self.lineComboBox, self.alphaDoubleSpinBox)
        Form.setTabOrder(self.alphaDoubleSpinBox, self.lineWidthDoubleSpinBox)
        Form.setTabOrder(self.lineWidthDoubleSpinBox, self.plotFilenameLineEdit)
        Form.setTabOrder(self.plotFilenameLineEdit, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Plot Spectra"))
        self.chooseDataLabel.setText(("Choose Data"))
        self.figureNameLabel.setText(("Figure Name"))
        self.plotTitleLabel.setText(("Plot Title"))
        self.xVariableLabel.setText(("X Variable:"))
        self.chooseColumnLabel.setText(("Choose Column"))
        self.chooseRowsLabel.setText(("Choose Rows:"))
        self.colorLabel.setText(("Color"))
        self.lineLabel.setText(("Line"))
        self.alphaLabel.setText(("Alpha"))
        self.lineWidthLabel.setText(("Line width"))
        self.plotFilenameLabel.setText(("Plot Filename"))
        self.pushButton.setText(("..."))
        self.minLabel.setText(("Min"))
        self.maxLabel.setText(("Max"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

