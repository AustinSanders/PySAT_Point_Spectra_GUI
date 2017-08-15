# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 856)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 678, 764))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setObjectName("widgetLayout")
        self.verticalLayout_3.addLayout(self.widgetLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.progress_OK = QtWidgets.QHBoxLayout()
        self.progress_OK.setObjectName("progress_OK")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progress_OK.addWidget(self.progressBar)
        self.deleteModulePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteModulePushButton.setObjectName("deleteModulePushButton")
        self.progress_OK.addWidget(self.deleteModulePushButton)
        self.okPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.okPushButton.setObjectName("okPushButton")
        self.progress_OK.addWidget(self.okPushButton)
        self.verticalLayout.addLayout(self.progress_OK)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPreprocessing = QtWidgets.QMenu(self.menubar)
        self.menuPreprocessing.setObjectName("menuPreprocessing")
        self.menuRegression = QtWidgets.QMenu(self.menubar)
        self.menuRegression.setObjectName("menuRegression")
        self.menuVisualization = QtWidgets.QMenu(self.menubar)
        self.menuVisualization.setObjectName("menuVisualization")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRead_ChemCam_Data = QtWidgets.QAction(MainWindow)
        self.actionRead_ChemCam_Data.setObjectName("actionRead_ChemCam_Data")
        self.actionLoad_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Data.setObjectName("actionLoad_Data")
        self.actionSet_Output_Path = QtWidgets.QAction(MainWindow)
        self.actionSet_Output_Path.setObjectName("actionSet_Output_Path")
        self.actionSave_Current_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Data.setObjectName("actionSave_Current_Data")
        self.actionCreate_New_Workflow = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Workflow.setObjectName("actionCreate_New_Workflow")
        self.actionRestore_Workflow = QtWidgets.QAction(MainWindow)
        self.actionRestore_Workflow.setObjectName("actionRestore_Workflow")
        self.actionSave_Current_Workflow = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Workflow.setObjectName("actionSave_Current_Workflow")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRemove_Rows = QtWidgets.QAction(MainWindow)
        self.actionRemove_Rows.setObjectName("actionRemove_Rows")
        self.actionSplit_Data = QtWidgets.QAction(MainWindow)
        self.actionSplit_Data.setObjectName("actionSplit_Data")
        self.actionInterpolate = QtWidgets.QAction(MainWindow)
        self.actionInterpolate.setObjectName("actionInterpolate")
        self.actionRemove_Baseline = QtWidgets.QAction(MainWindow)
        self.actionRemove_Baseline.setObjectName("actionRemove_Baseline")
        self.actionApply_Mask = QtWidgets.QAction(MainWindow)
        self.actionApply_Mask.setObjectName("actionApply_Mask")
        self.actionPeak_Areas = QtWidgets.QAction(MainWindow)
        self.actionPeak_Areas.setObjectName("actionPeak_Areas")
        self.actionMultiply_by_Vector = QtWidgets.QAction(MainWindow)
        self.actionMultiply_by_Vector.setObjectName("actionMultiply_by_Vector")
        self.actionNormalization = QtWidgets.QAction(MainWindow)
        self.actionNormalization.setObjectName("actionNormalization")
        self.actionDimensionality_Reduction = QtWidgets.QAction(MainWindow)
        self.actionDimensionality_Reduction.setObjectName("actionDimensionality_Reduction")
        self.actionStratified_Folds = QtWidgets.QAction(MainWindow)
        self.actionStratified_Folds.setObjectName("actionStratified_Folds")
        self.actionCross_Validation = QtWidgets.QAction(MainWindow)
        self.actionCross_Validation.setObjectName("actionCross_Validation")
        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.actionSubmodel_Predict = QtWidgets.QAction(MainWindow)
        self.actionSubmodel_Predict.setObjectName("actionSubmodel_Predict")
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")
        self.actionPlot = QtWidgets.QAction(MainWindow)
        self.actionPlot.setObjectName("actionPlot")
        self.actionPlot_Spectra = QtWidgets.QAction(MainWindow)
        self.actionPlot_Spectra.setObjectName("actionPlot_Spectra")
        self.actionPlot_ICA_PCA = QtWidgets.QAction(MainWindow)
        self.actionPlot_ICA_PCA.setObjectName("actionPlot_ICA_PCA")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionOpen_Workflow = QtWidgets.QAction(MainWindow)
        self.actionOpen_Workflow.setObjectName("actionOpen_Workflow")
        self.menuFile.addAction(self.actionRead_ChemCam_Data)
        self.menuFile.addAction(self.actionLoad_Data)
        self.menuFile.addAction(self.actionSet_Output_Path)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Current_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_New_Workflow)
        self.menuFile.addAction(self.actionOpen_Workflow)
        self.menuFile.addAction(self.actionRestore_Workflow)
        self.menuFile.addAction(self.actionSave_Current_Workflow)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuPreprocessing.addAction(self.actionRemove_Rows)
        self.menuPreprocessing.addAction(self.actionSplit_Data)
        self.menuPreprocessing.addAction(self.actionInterpolate)
        self.menuPreprocessing.addAction(self.actionRemove_Baseline)
        self.menuPreprocessing.addAction(self.actionApply_Mask)
        self.menuPreprocessing.addAction(self.actionPeak_Areas)
        self.menuPreprocessing.addAction(self.actionMultiply_by_Vector)
        self.menuPreprocessing.addAction(self.actionNormalization)
        self.menuPreprocessing.addAction(self.actionDimensionality_Reduction)
        self.menuPreprocessing.addAction(self.actionStratified_Folds)
        self.menuRegression.addAction(self.actionCross_Validation)
        self.menuRegression.addAction(self.actionTrain)
        self.menuRegression.addAction(self.actionSubmodel_Predict)
        self.menuRegression.addAction(self.actionPredict)
        self.menuVisualization.addAction(self.actionPlot)
        self.menuVisualization.addAction(self.actionPlot_Spectra)
        self.menuVisualization.addAction(self.actionPlot_ICA_PCA)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreprocessing.menuAction())
        self.menubar.addAction(self.menuRegression.menuAction())
        self.menubar.addAction(self.menuVisualization.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.deleteModulePushButton.setText(_translate("MainWindow", "Delete Module"))
        self.okPushButton.setText(_translate("MainWindow", "OK"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPreprocessing.setTitle(_translate("MainWindow", "Preprocessing"))
        self.menuRegression.setTitle(_translate("MainWindow", "Regression"))
        self.menuVisualization.setTitle(_translate("MainWindow", "Visualization"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionRead_ChemCam_Data.setText(_translate("MainWindow", "Read ChemCam Data"))
        self.actionLoad_Data.setText(_translate("MainWindow", "Load Data"))
        self.actionSet_Output_Path.setText(_translate("MainWindow", "Set Output Path"))
        self.actionSave_Current_Data.setText(_translate("MainWindow", "Save Current Data"))
        self.actionCreate_New_Workflow.setText(_translate("MainWindow", "Create New Workflow"))
        self.actionRestore_Workflow.setText(_translate("MainWindow", "Restore Workflow"))
        self.actionSave_Current_Workflow.setText(_translate("MainWindow", "Save Current Workflow"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRemove_Rows.setText(_translate("MainWindow", "Remove Rows"))
        self.actionSplit_Data.setText(_translate("MainWindow", "Split Data"))
        self.actionInterpolate.setText(_translate("MainWindow", "Interpolate"))
        self.actionRemove_Baseline.setText(_translate("MainWindow", "Remove Baseline"))
        self.actionApply_Mask.setText(_translate("MainWindow", "Apply Mask"))
        self.actionPeak_Areas.setText(_translate("MainWindow", "Peak Areas"))
        self.actionMultiply_by_Vector.setText(_translate("MainWindow", "Multiply by Vector"))
        self.actionNormalization.setText(_translate("MainWindow", "Normalization"))
        self.actionDimensionality_Reduction.setText(_translate("MainWindow", "Dimensionality Reduction"))
        self.actionStratified_Folds.setText(_translate("MainWindow", "Stratified Folds"))
        self.actionCross_Validation.setText(_translate("MainWindow", "Cross Validation"))
        self.actionTrain.setText(_translate("MainWindow", "Train"))
        self.actionSubmodel_Predict.setText(_translate("MainWindow", "Submodel Predict"))
        self.actionPredict.setText(_translate("MainWindow", "Predict"))
        self.actionPlot.setText(_translate("MainWindow", "Plot"))
        self.actionPlot_Spectra.setText(_translate("MainWindow", "Plot Spectra"))
        self.actionPlot_ICA_PCA.setText(_translate("MainWindow", "Plot ICA/PCA"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt..."))
        self.actionOpen_Workflow.setText(_translate("MainWindow", "Open Workflow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

