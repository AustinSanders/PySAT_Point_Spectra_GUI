from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import sys
from pysat_function import pysat_func
from functools import partial
from PyQt4.QtGui import QMessageBox


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class pysat_ui(object):
    def __init__(self):
        self.pysat_fun = pysat_func()
        self.addFunc = []
        self.addPara = []

    def mainframe(self, MainWindow):
            MainWindow.setObjectName(_fromUtf8("MainWindow"))
            MainWindow.resize(581, 843)
            self.centralWidget = QtGui.QWidget(MainWindow)
            self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
            self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralWidget)
            self.verticalLayout_9.setMargin(11)
            self.verticalLayout_9.setSpacing(6)
            self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
            self.scrollArea = QtGui.QScrollArea(self.centralWidget)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
            self.scrollAreaWidgetContents_2 = QtGui.QWidget()
            self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 561, 742))
            font = QtGui.QFont()
            font.setPointSize(8)
            self.scrollAreaWidgetContents_2.setFont(font)
            self.scrollAreaWidgetContents_2.setStyleSheet(_fromUtf8("QGroupBox {\n"
                                                                    "  border: 2px solid gray;\n"
                                                                    "  border-radius: 6px;\n"
                                                                    "  margin-top: 0.5em;\n"
                                                                    "}\n"
                                                                    "\n"
                                                                    "QGroupBox::title {\n"
                                                                    "\n"
                                                                    "  padding-top: -14px;\n"
                                                                    "  padding-left: 8px;\n"
                                                                    "}\n"
                                                                    ""))
            self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
            self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
            self.verticalLayout_8.setMargin(11)
            self.verticalLayout_8.setSpacing(6)
            self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
            self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
            self.verticalLayout_9.addWidget(self.scrollArea)
            self.OK = QtGui.QGroupBox(self.centralWidget)
            self.OK.setObjectName(_fromUtf8("OK"))
            self.ok = QtGui.QHBoxLayout(self.OK)
            self.ok.setMargin(11)
            self.ok.setSpacing(6)
            self.ok.setObjectName(_fromUtf8("ok"))
            spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.ok.addItem(spacerItem)
            self.okButton = QtGui.QPushButton(self.OK)
            font = QtGui.QFont()
            font.setPointSize(8)
            self.okButton.setFont(font)
            self.okButton.setMouseTracking(False)
            self.okButton.setObjectName(_fromUtf8("okButton"))
            self.ok.addWidget(self.okButton)
            self.verticalLayout_9.addWidget(self.OK)
            MainWindow.setCentralWidget(self.centralWidget)
            self.mainToolBar = QtGui.QToolBar(MainWindow)
            self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
            MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
            self.statusBar = QtGui.QStatusBar(MainWindow)
            self.statusBar.setObjectName(_fromUtf8("statusBar"))
            MainWindow.setStatusBar(self.statusBar)
            self.actionLoad_Refence_Data = QtGui.QAction(MainWindow)
            self.actionLoad_Refence_Data.setObjectName(_fromUtf8("actionLoad_Refence_Data"))
            self.actionLoad_Unknown_Data = QtGui.QAction(MainWindow)
            self.actionLoad_Unknown_Data.setObjectName(_fromUtf8("actionLoad_Unknown_Data"))
            self.actionSave_Current_Workflow = QtGui.QAction(MainWindow)
            self.actionSave_Current_Workflow.setObjectName(_fromUtf8("actionSave_Current_Workflow"))
            self.actionSave_Current_Plots = QtGui.QAction(MainWindow)
            self.actionSave_Current_Plots.setObjectName(_fromUtf8("actionSave_Current_Plots"))
            self.actionSave_Current_Data = QtGui.QAction(MainWindow)
            self.actionSave_Current_Data.setObjectName(_fromUtf8("actionSave_Current_Data"))
            self.actionCreate_New_Workflow = QtGui.QAction(MainWindow)
            self.actionCreate_New_Workflow.setObjectName(_fromUtf8("actionCreate_New_Workflow"))
            self.actionNoise_Reduction = QtGui.QAction(MainWindow)
            self.actionNoise_Reduction.setObjectName(_fromUtf8("actionNoise_Reduction"))
            self.actionApply_Mask = QtGui.QAction(MainWindow)
            self.actionApply_Mask.setObjectName(_fromUtf8("actionApply_Mask"))
            self.actionInterpolate = QtGui.QAction(MainWindow)
            self.actionInterpolate.setObjectName(_fromUtf8("actionInterpolate"))
            self.actionInstrument_Response = QtGui.QAction(MainWindow)
            self.actionInstrument_Response.setObjectName(_fromUtf8("actionInstrument_Response"))
            self.actionALS = QtGui.QAction(MainWindow)
            self.actionALS.setObjectName(_fromUtf8("actionALS"))
            self.actionDietrich = QtGui.QAction(MainWindow)
            self.actionDietrich.setObjectName(_fromUtf8("actionDietrich"))
            self.actionPolyFit = QtGui.QAction(MainWindow)
            self.actionPolyFit.setObjectName(_fromUtf8("actionPolyFit"))
            self.actionAirPLS = QtGui.QAction(MainWindow)
            self.actionAirPLS.setObjectName(_fromUtf8("actionAirPLS"))
            self.actionFABC = QtGui.QAction(MainWindow)
            self.actionFABC.setObjectName(_fromUtf8("actionFABC"))
            self.actionKK = QtGui.QAction(MainWindow)
            self.actionKK.setObjectName(_fromUtf8("actionKK"))
            self.actionMario = QtGui.QAction(MainWindow)
            self.actionMario.setObjectName(_fromUtf8("actionMario"))
            self.actionMedian = QtGui.QAction(MainWindow)
            self.actionMedian.setObjectName(_fromUtf8("actionMedian"))
            self.actionRubberband = QtGui.QAction(MainWindow)
            self.actionRubberband.setObjectName(_fromUtf8("actionRubberband"))
            self.actionUndecimated_Wavelet = QtGui.QAction(MainWindow)
            self.actionUndecimated_Wavelet.setObjectName(_fromUtf8("actionUndecimated_Wavelet"))
            self.actionRatio = QtGui.QAction(MainWindow)
            self.actionRatio.setObjectName(_fromUtf8("actionRatio"))
            self.actionTommy_s_Methgod = QtGui.QAction(MainWindow)
            self.actionTommy_s_Methgod.setObjectName(_fromUtf8("actionTommy_s_Methgod"))
            self.actionPiecewise_Direct_Standardization = QtGui.QAction(MainWindow)
            self.actionPiecewise_Direct_Standardization.setObjectName(
                _fromUtf8("actionPiecewise_Direct_Standardization"))
            self.actionPCA = QtGui.QAction(MainWindow)
            self.actionPCA.setObjectName(_fromUtf8("actionPCA"))
            self.actionICA = QtGui.QAction(MainWindow)
            self.actionICA.setObjectName(_fromUtf8("actionICA"))
            self.actionK_Means = QtGui.QAction(MainWindow)
            self.actionK_Means.setObjectName(_fromUtf8("actionK_Means"))
            self.actionHierarchical = QtGui.QAction(MainWindow)
            self.actionHierarchical.setObjectName(_fromUtf8("actionHierarchical"))
            self.actionOthers = QtGui.QAction(MainWindow)
            self.actionOthers.setObjectName(_fromUtf8("actionOthers"))
            self.actionOthers_2 = QtGui.QAction(MainWindow)
            self.actionOthers_2.setObjectName(_fromUtf8("actionOthers_2"))
            self.actionOthers_3 = QtGui.QAction(MainWindow)
            self.actionOthers_3.setObjectName(_fromUtf8("actionOthers_3"))
            self.actionPLS = QtGui.QAction(MainWindow)
            self.actionPLS.setObjectName(_fromUtf8("actionPLS"))
            self.actionSM_PLS = QtGui.QAction(MainWindow)
            self.actionSM_PLS.setObjectName(_fromUtf8("actionSM_PLS"))
            self.actionICA_Regression = QtGui.QAction(MainWindow)
            self.actionICA_Regression.setObjectName(_fromUtf8("actionICA_Regression"))
            self.actionGaussian_Process = QtGui.QAction(MainWindow)
            self.actionGaussian_Process.setObjectName(_fromUtf8("actionGaussian_Process"))
            self.actionMLP = QtGui.QAction(MainWindow)
            self.actionMLP.setObjectName(_fromUtf8("actionMLP"))
            self.actionSVM = QtGui.QAction(MainWindow)
            self.actionSVM.setObjectName(_fromUtf8("actionSVM"))
            self.actionOthers_4 = QtGui.QAction(MainWindow)
            self.actionOthers_4.setObjectName(_fromUtf8("actionOthers_4"))
            self.actionOthers_5 = QtGui.QAction(MainWindow)
            self.actionOthers_5.setObjectName(_fromUtf8("actionOthers_5"))
            self.actionIndex = QtGui.QAction(MainWindow)
            self.actionIndex.setObjectName(_fromUtf8("actionIndex"))
            self.actionContent_2 = QtGui.QAction(MainWindow)
            self.actionContent_2.setObjectName(_fromUtf8("actionContent_2"))
            self.actionAbout = QtGui.QAction(MainWindow)
            self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
            self.actionAbout_QtCreator = QtGui.QAction(MainWindow)
            self.actionAbout_QtCreator.setObjectName(_fromUtf8("actionAbout_QtCreator"))
            self.actionExit = QtGui.QAction(MainWindow)
            self.actionExit.setObjectName(_fromUtf8("actionExit"))
            self.actionNormalization = QtGui.QAction(MainWindow)
            self.actionNormalization.setObjectName(_fromUtf8("actionNormalization"))
            self.actionICA_2 = QtGui.QAction(MainWindow)
            self.actionICA_2.setObjectName(_fromUtf8("actionICA_2"))
            self.actionPCA_2 = QtGui.QAction(MainWindow)
            self.actionPCA_2.setObjectName(_fromUtf8("actionPCA_2"))
            self.actionPLS_DA = QtGui.QAction(MainWindow)
            self.actionPLS_DA.setObjectName(_fromUtf8("actionPLS_DA"))
            self.actionSIMCA = QtGui.QAction(MainWindow)
            self.actionSIMCA.setObjectName(_fromUtf8("actionSIMCA"))
            self.actionK_means = QtGui.QAction(MainWindow)
            self.actionK_means.setObjectName(_fromUtf8("actionK_means"))
            self.actionHierarchical_2 = QtGui.QAction(MainWindow)
            self.actionHierarchical_2.setObjectName(_fromUtf8("actionHierarchical_2"))
            self.actionCross_Validation = QtGui.QAction(MainWindow)
            self.actionCross_Validation.setObjectName(_fromUtf8("actionCross_Validation"))
            self.actionTrain = QtGui.QAction(MainWindow)
            self.actionTrain.setObjectName(_fromUtf8("actionTrain"))
            self.actionPredict = QtGui.QAction(MainWindow)
            self.actionPredict.setObjectName(_fromUtf8("actionPredict"))
            self.actionLine_Plot = QtGui.QAction(MainWindow)
            self.actionLine_Plot.setObjectName(_fromUtf8("actionLine_Plot"))
            self.action1_to_1_Plot = QtGui.QAction(MainWindow)
            self.action1_to_1_Plot.setObjectName(_fromUtf8("action1_to_1_Plot"))
            self.actionScatter_Plot = QtGui.QAction(MainWindow)
            self.actionScatter_Plot.setObjectName(_fromUtf8("actionScatter_Plot"))
            self.actionSet_output_location = QtGui.QAction(MainWindow)
            self.actionSet_output_location.setObjectName(_fromUtf8("actionSet_output_location"))
            self.actionCreate_N_Folds = QtGui.QAction(MainWindow)
            self.actionCreate_N_Folds.setObjectName(_fromUtf8("actionCreate_N_Folds"))
            self.actionCreate_Test_Folds = QtGui.QAction(MainWindow)
            self.actionCreate_Test_Folds.setObjectName(_fromUtf8("actionCreate_Test_Folds"))
            self.actionStratified_Folds = QtGui.QAction(MainWindow)
            self.actionStratified_Folds.setObjectName(_fromUtf8("actionStratified_Folds"))
            self.actionTrain_Submodels = QtGui.QAction(MainWindow)
            self.actionTrain_Submodels.setObjectName(_fromUtf8("actionTrain_Submodels"))

            QtCore.QMetaObject.connectSlotsByName(MainWindow)

            MainWindow.setWindowTitle(_translate("MainWindow", "PYSAT", None))
            self.okButton.setText(_translate("MainWindow", "OK", None))
            self.actionLoad_Refence_Data.setText(_translate("MainWindow", "Load Refence Data", None))
            self.actionLoad_Unknown_Data.setText(_translate("MainWindow", "Load Unknown Data", None))
            self.actionSave_Current_Workflow.setText(_translate("MainWindow", "Save Current Workflow", None))
            self.actionSave_Current_Plots.setText(_translate("MainWindow", "Save Current Plots", None))
            self.actionSave_Current_Data.setText(_translate("MainWindow", "Save Current Data", None))
            self.actionCreate_New_Workflow.setText(_translate("MainWindow", "Create New Workflow", None))
            self.actionNoise_Reduction.setText(_translate("MainWindow", "Noise Reduction", None))
            self.actionApply_Mask.setText(_translate("MainWindow", "Apply Mask", None))
            self.actionInterpolate.setText(_translate("MainWindow", "Interpolate (unknown to known)", None))
            self.actionInstrument_Response.setText(_translate("MainWindow", "Instrument Response", None))
            self.actionALS.setText(_translate("MainWindow", "ALS", None))
            self.actionDietrich.setText(_translate("MainWindow", "Dietrich", None))
            self.actionPolyFit.setText(_translate("MainWindow", "PolyFit", None))
            self.actionAirPLS.setText(_translate("MainWindow", "AirPLS", None))
            self.actionFABC.setText(_translate("MainWindow", "FABC", None))
            self.actionKK.setText(_translate("MainWindow", "KK", None))
            self.actionMario.setText(_translate("MainWindow", "Mario", None))
            self.actionMedian.setText(_translate("MainWindow", "Median", None))
            self.actionRubberband.setText(_translate("MainWindow", "Rubberband", None))
            self.actionUndecimated_Wavelet.setText(_translate("MainWindow", "Undecimated Wavelet", None))
            self.actionRatio.setText(_translate("MainWindow", "Ratio", None))
            self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))
            self.actionPiecewise_Direct_Standardization.setText(
                _translate("MainWindow", "Piecewise Direct Standardization", None))
            self.actionPCA.setText(_translate("MainWindow", "PCA", None))
            self.actionICA.setText(_translate("MainWindow", "ICA", None))
            self.actionK_Means.setText(_translate("MainWindow", "K-Means", None))
            self.actionHierarchical.setText(_translate("MainWindow", "Hierarchical", None))
            self.actionOthers.setText(_translate("MainWindow", "Others...", None))
            self.actionOthers_2.setText(_translate("MainWindow", "Others...", None))
            self.actionOthers_3.setText(_translate("MainWindow", "Others...", None))
            self.actionPLS.setText(_translate("MainWindow", "PLS", None))
            self.actionSM_PLS.setText(_translate("MainWindow", "SM-PLS", None))
            self.actionICA_Regression.setText(_translate("MainWindow", "ICA Regression", None))
            self.actionGaussian_Process.setText(_translate("MainWindow", "Gaussian Process", None))
            self.actionMLP.setText(_translate("MainWindow", "MLP", None))
            self.actionSVM.setText(_translate("MainWindow", "SVM", None))
            self.actionOthers_4.setText(_translate("MainWindow", "Others...", None))
            self.actionOthers_5.setText(_translate("MainWindow", "Others...", None))
            self.actionIndex.setText(_translate("MainWindow", "Index", None))
            self.actionContent_2.setText(_translate("MainWindow", "Content", None))
            self.actionAbout.setText(_translate("MainWindow", "About...", None))
            self.actionAbout_QtCreator.setText(_translate("MainWindow", "About Qt...", None))
            self.actionExit.setText(_translate("MainWindow", "Exit", None))
            self.actionNormalization.setText(_translate("MainWindow", "Normalization", None))
            self.actionICA_2.setText(_translate("MainWindow", "ICA", None))
            self.actionPCA_2.setText(_translate("MainWindow", "PCA", None))
            self.actionPLS_DA.setText(_translate("MainWindow", "PLS-DA", None))
            self.actionSIMCA.setText(_translate("MainWindow", "SIMCA", None))
            self.actionK_means.setText(_translate("MainWindow", "K-means", None))
            self.actionHierarchical_2.setText(_translate("MainWindow", "Hierarchical", None))
            self.actionCross_Validation.setText(_translate("MainWindow", "Cross Validation", None))
            self.actionTrain.setText(_translate("MainWindow", "Train", None))
            self.actionPredict.setText(_translate("MainWindow", "Predict", None))
            self.actionLine_Plot.setText(_translate("MainWindow", "Line Plot", None))
            self.action1_to_1_Plot.setText(_translate("MainWindow", "1 to 1 Plot", None))
            self.actionScatter_Plot.setText(_translate("MainWindow", "Scatter Plot", None))
            self.actionSet_output_location.setText(_translate("MainWindow", "Output Location", None))
            self.actionCreate_N_Folds.setText(_translate("MainWindow", "Create N Folds", None))
            self.actionCreate_Test_Folds.setText(_translate("MainWindow", "Create Test Folds", None))
            self.actionStratified_Folds.setText(_translate("MainWindow", "Stratified Folds", None))
            self.actionTrain_Submodels.setText(_translate("MainWindow", "Train Submodels", None))

    def unknown_data(self, MainWindow):
        self.unknownData = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unknownData.setFont(font)
        self.unknownData.setObjectName(_fromUtf8("unknownData"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.unknownData)
        self.verticalLayout_6.setMargin(11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.unknownData)
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.unknownData)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setMargin(11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.unknownDataButton = QtGui.QToolButton(self.unknownData)
        self.unknownDataButton.setObjectName(_fromUtf8("unknownDataButton"))
        self.verticalLayout_5.addWidget(self.unknownDataButton)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_8.addWidget(self.unknownData)
        self.unknownData.raise_()
        self.unknownData.setTitle(_translate("MainWindow", "File", None))
        self.label.setText(_translate("MainWindow", "Unknown Data", None))
        self.lineEdit_2.setText(_translate("MainWindow", "*.csv", None))
        self.unknownDataButton.setText(_translate("MainWindow", "...", None))
        try:
            self.unknownDataButton.clicked.connect(
                lambda: pysat_ui.on_getDataButton_clicked(self, self.lineEdit_2, 'Unknown Data'))
        except:
            pass

    def known_data(self, MainWindow):
        self.referenceData = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.referenceData.setFont(font)
        self.referenceData.setObjectName(_fromUtf8("referenceData"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.referenceData)
        self.verticalLayout_15.setMargin(11)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setMargin(11)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setMargin(11)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.label_8 = QtGui.QLabel(self.referenceData)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_16.addWidget(self.label_8)
        self.horizontalLayout_11.addLayout(self.verticalLayout_16)
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setMargin(11)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.lineEdit_9 = QtGui.QLineEdit(self.referenceData)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.verticalLayout_20.addWidget(self.lineEdit_9)
        self.horizontalLayout_11.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtGui.QVBoxLayout()
        self.verticalLayout_21.setMargin(11)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.fullDataBaseButton_3 = QtGui.QToolButton(self.referenceData)
        self.fullDataBaseButton_3.setObjectName(_fromUtf8("fullDataBaseButton_3"))
        self.verticalLayout_21.addWidget(self.fullDataBaseButton_3)
        self.horizontalLayout_11.addLayout(self.verticalLayout_21)
        self.verticalLayout_15.addLayout(self.horizontalLayout_11)
        self.verticalLayout_8.addWidget(self.referenceData)
        self.referenceData.raise_()
        self.referenceData.setTitle(_translate("MainWindow", "File", None))
        self.label_8.setText(_translate("MainWindow", "Full Database", None))
        self.lineEdit_9.setText(_translate("MainWindow", "*.csv", None))
        self.fullDataBaseButton_3.setText(_translate("MainWindow", "...", None))
        try:
            self.fullDataBaseButton_3.clicked.connect(
                lambda: pysat_ui.on_getDataButton_clicked(self, self.lineEdit_9, 'Known Data'))
        except:
            pass

    def output_folder(self, MainWindow):
        self.outputFolder = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outputFolder.setFont(font)
        self.outputFolder.setObjectName(_fromUtf8("outputFolder"))
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.outputFolder)
        self.verticalLayout_22.setMargin(11)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setMargin(11)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_25 = QtGui.QVBoxLayout()
        self.verticalLayout_25.setMargin(11)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.label_9 = QtGui.QLabel(self.outputFolder)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_25.addWidget(self.label_9)
        self.horizontalLayout_13.addLayout(self.verticalLayout_25)
        self.verticalLayout_28 = QtGui.QVBoxLayout()
        self.verticalLayout_28.setMargin(11)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(_fromUtf8("verticalLayout_28"))
        self.lineEdit_10 = QtGui.QLineEdit(self.outputFolder)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.verticalLayout_28.addWidget(self.lineEdit_10)
        self.horizontalLayout_13.addLayout(self.verticalLayout_28)
        self.verticalLayout_29 = QtGui.QVBoxLayout()
        self.verticalLayout_29.setMargin(11)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(_fromUtf8("verticalLayout_29"))
        self.fullDataBaseButton_4 = QtGui.QToolButton(self.outputFolder)
        self.fullDataBaseButton_4.setObjectName(_fromUtf8("fullDataBaseButton_4"))
        self.verticalLayout_29.addWidget(self.fullDataBaseButton_4)
        self.horizontalLayout_13.addLayout(self.verticalLayout_29)
        self.verticalLayout_22.addLayout(self.horizontalLayout_13)
        self.verticalLayout_8.addWidget(self.outputFolder)
        self.outputFolder.raise_()
        self.outputFolder.setTitle(_translate("MainWindow", "Output", None))
        self.label_9.setText(_translate("MainWindow", "Output Folder", None))
        self.lineEdit_10.setText(_translate("MainWindow", "*.*", None))
        self.fullDataBaseButton_4.setText(_translate("MainWindow", "...", None))
        try:
            self.fullDataBaseButton_4.clicked.connect(
                lambda: pysat_ui.on_outPutLocationButton_clicked(self, self.lineEdit_10))
        except:
            pass

    """ =============================================
    Please do not delete the files below this line!
    These files are the working files that allow the UI
    to operate and do things!
    ============================================== """
    #### Opening Files
    def on_maskFile_clicked(self, lineEdit):
        filename = QFileDialog.getOpenFileName(None, "Open Mask File", '.', "(*.csv)")
        lineEdit.setText(filename)
        self.pysat_fun.set_file_maskfile(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.pysat_fun.set_mask()

    def on_getDataButton_clicked(self, lineEdit, key):
        filename = QFileDialog.getOpenFileName(None, "Open Uknown Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.pysat_fun.get_data(filename, key)

    def on_outPutLocationButton_clicked(self, lineEdit):
        filename = QFileDialog.getExistingDirectory(None, "Select Output Directory", '.')
        lineEdit.setText(filename)
        self.pysat_fun.set_file_outpath(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*/*")

    #### Shortcuts
    def menu_item_shortcuts(self):
        self.actionExit.setShortcut("ctrl+Q")

    def menu_item_functions(self, MainWindow):
        self.actionSet_output_location.triggered.connect(lambda: pysat_ui.output_folder(self, MainWindow))
        self.actionLoad_Unknown_Data.triggered.connect(lambda: pysat_ui.unknown_data(self, MainWindow))
        self.actionLoad_reference_Data.triggered.connect(lambda: pysat_ui.reference_data(self, MainWindow))
        self.actionNormalization.triggered.connect(lambda: pysat_ui.normalization(self, MainWindow))
        self.actionInterpolate.triggered.connect(lambda: pysat_ui.interpolated(self, MainWindow))
        self.actionApply_Mask.triggered.connect(lambda: pysat_ui.masked(self, MainWindow))
        self.actionStratified_Folds.triggered.connect(lambda: pysat_ui.stratified_folds(self, MainWindow))
        self.actionTrain.triggered.connect(lambda: pysat_ui.regression_train(self, MainWindow))

    #### Ok Button Clicked
    def on_okButton_clicked(self):
        self.pysat_fun.set_sm()
        self.pysat_fun.get_sm_fit()
        self.pysat_fun.get_plots()

    def strat_fold_change_vars(self):
        self.strat_folds_choose_var.clear()
        choices = self.pysat_fun.data[self.strat_folds_choose_data.currentText()].df['meta'].columns.values
        print(choices)
        self.strat_folds_choose_var.addItems(choices)

    def strat_fold_change_testfolds(self):
        self.choose_test_fold.clear()
        choices = list(map(str, list(range(1, self.nfolds_spin.value() + 1))))
        print(choices)
        self.choose_test_fold.addItems(choices)
        
    def make_ransac_widget(self):
        try:
            self.ransac_widget.deleteLater()
        except:
            pass
        self.ransac_widget=QtGui.QWidget()
        if self.regression_ransac_checkbox.isChecked():

            ransac_widget_hlayout = QtGui.QHBoxLayout(self.ransac_widget)
            ransac_lossfunc_hlayout = QtGui.QHBoxLayout()
            ransac_lossfunc_label = QtGui.QLabel(self.ransac_widget)
            ransac_lossfunc_label.setText('Loss function:')
            ransac_lossfunc_hlayout.addWidget(ransac_lossfunc_label)
            ransac_lossfunc_combobox = QtGui.QComboBox(self.ransac_widget)
            ransac_lossfunc_combobox.addItem(_fromUtf8("Squared Error"))
            ransac_lossfunc_combobox.addItem(_fromUtf8("Absolute Error"))
            ransac_lossfunc_hlayout.addWidget(ransac_lossfunc_combobox)
            ransac_lossfunc_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            ransac_lossfunc_hlayout.addItem(ransac_lossfunc_spacer)
            ransac_widget_hlayout.addLayout(ransac_lossfunc_hlayout)
            ransac_thresh_hlayout = QtGui.QHBoxLayout()
            ransac_thresh_label = QtGui.QLabel(self.ransac_widget)
            ransac_thresh_label.setText('Threshold:')
            ransac_thresh_hlayout.addWidget(ransac_thresh_label)
            ransac_thresh_spin = QtGui.QDoubleSpinBox(self.ransac_widget)
            ransac_thresh_hlayout.addWidget(ransac_thresh_spin)
            ransac_thresh_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            ransac_thresh_hlayout.addItem(ransac_thresh_spacer)
            ransac_widget_hlayout.addLayout(ransac_thresh_hlayout)
            self.ransac_hlayout.addWidget(self.ransac_widget)

        
        
            
            
    def make_regression_widget(self):
        alg=self.regression_choosealg.currentText()
        print(alg)
        try:
            self.reg_widget.deleteLater()
        except:
            pass
        self.reg_widget=QtGui.QWidget()
        if alg=='Choose an algorithm':
            pass
        if alg=='PLS':
            pls_hlayout = QtGui.QHBoxLayout(self.reg_widget)
            pls_nc_label = QtGui.QLabel(self.reg_widget)
            pls_nc_label.setText('# of components:')
            pls_hlayout.addWidget(pls_nc_label)
            pls_nc_spinbox = QtGui.QSpinBox(self.reg_widget)
            pls_hlayout.addWidget(pls_nc_spinbox)
            pls_spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            pls_hlayout.addItem(pls_spacer)
            
        if alg=='GP':
            gp_vlayout = QtGui.QVBoxLayout(self.reg_widget)
            gp_dim_red_hlayout = QtGui.QHBoxLayout()
            gp_dim_red_label = QtGui.QLabel(self.reg_widget)
            gp_dim_red_label.setText('Choose dimensionality reduction method:')
            gp_dim_red_hlayout.addWidget(gp_dim_red_label)
            gp_dim_red_combobox = QtGui.QComboBox(self.reg_widget)
            gp_dim_red_combobox.addItem(_fromUtf8("PCA"))
            gp_dim_red_combobox.addItem(_fromUtf8("ICA"))
            gp_dim_red_hlayout.addWidget(gp_dim_red_combobox)
            gp_vlayout.addLayout(gp_dim_red_hlayout)
            gp_rand_starts_hlayout = QtGui.QHBoxLayout()
            gp_rand_starts_label = QtGui.QLabel(self.reg_widget)
            gp_rand_starts_label.setText('# of random starts:')
            gp_rand_starts_hlayout.addWidget(gp_rand_starts_label)
            gp_rand_starts_spin = QtGui.QSpinBox(self.reg_widget)
            gp_rand_starts_spin.setValue(1)
            gp_rand_starts_hlayout.addWidget(gp_rand_starts_spin)
            spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            gp_rand_starts_hlayout.addItem(spacerItem4)
            gp_vlayout.addLayout(gp_rand_starts_hlayout)
            gp_theta_vlayout = QtGui.QVBoxLayout()
            gp_theta0_label = QtGui.QLabel(self.reg_widget)
            gp_theta0_label.setText('Starting Theta:')
            gp_theta_vlayout.addWidget(gp_theta0_label)
            gp_theta0_spin = QtGui.QDoubleSpinBox(self.reg_widget)
            gp_theta0_spin.setValue(1.0)
            gp_theta_vlayout.addWidget(gp_theta0_spin)
            gp_thetaL_label = QtGui.QLabel(self.reg_widget)
            gp_thetaL_label.setText('Lower bound on Theta:')
            gp_theta_vlayout.addWidget(gp_thetaL_label)
            gp_thetaL_spin = QtGui.QDoubleSpinBox(self.reg_widget)
            gp_thetaL_spin.setValue(0.1)            
            gp_theta_vlayout.addWidget(gp_thetaL_spin)
            gp_thetaU_label = QtGui.QLabel(self.reg_widget)
            gp_thetaU_label.setText('Upper bound on Theta:')
            gp_theta_vlayout.addWidget(gp_thetaU_label)
            gp_thetaU_spin = QtGui.QDoubleSpinBox(self.reg_widget)
            gp_thetaU_spin.setMaximum(10000)
            gp_thetaU_spin.setValue(100.0)
            
            gp_theta_vlayout.addWidget(gp_thetaU_spin)
            spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            gp_theta_vlayout.addItem(spacerItem5)
            gp_vlayout.addLayout(gp_theta_vlayout)
            
        self.regression_vlayout.addWidget(self.reg_widget)
        

def make_combobox(choices):
    combo=QtGui.QComboBox()
   
    for i,choice in enumerate(choices):
        combo.addItem(_fromUtf8(""))
        combo.setItemText(i,_translate('',choice,None))
        
    return combo

    
def make_listwidget(choices):
    listwidget = QtGui.QListWidget()
    listwidget.setItemDelegate
    for item in choices:
        item = QtGui.QListWidgetItem(item)
        listwidget.addItem(item)
    return listwidget