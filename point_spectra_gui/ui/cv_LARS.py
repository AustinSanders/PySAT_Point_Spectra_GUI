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
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.fit_interceptLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fit_interceptLabel.setObjectName("fit_interceptLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fit_interceptLabel)
        self.fit_interceptCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fit_interceptCheckBox.setObjectName("fit_interceptCheckBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fit_interceptCheckBox)
        self.verboseLabel = QtWidgets.QLabel(self.formGroupBox)
        self.verboseLabel.setObjectName("verboseLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.verboseLabel)
        self.verboseCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.verboseCheckBox)
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.precomputeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.precomputeLabel.setObjectName("precomputeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.precomputeLabel)
        self.precomputeComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.precomputeComboBox.setObjectName("precomputeComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.precomputeComboBox)
        self.n_nonzero_coefsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.n_nonzero_coefsLabel.setObjectName("n_nonzero_coefsLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.n_nonzero_coefsLabel)
        self.n_nonzero_coefsLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.n_nonzero_coefsLineEdit.setObjectName("n_nonzero_coefsLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.n_nonzero_coefsLineEdit)
        self.copy_XLabel = QtWidgets.QLabel(self.formGroupBox)
        self.copy_XLabel.setObjectName("copy_XLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.copy_XLabel)
        self.copy_XCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.copy_XCheckBox.setObjectName("copy_XCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.copy_XCheckBox)
        self.fit_pathLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fit_pathLabel.setObjectName("fit_pathLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.fit_pathLabel)
        self.fit_pathCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fit_pathCheckBox.setObjectName("fit_pathCheckBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.fit_pathCheckBox)
        self.positiveLabel = QtWidgets.QLabel(self.formGroupBox)
        self.positiveLabel.setObjectName("positiveLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.positiveLabel)
        self.positiveCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.positiveCheckBox.setObjectName("positiveCheckBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.positiveCheckBox)
        self.max_iterLabel = QtWidgets.QLabel(self.formGroupBox)
        self.max_iterLabel.setObjectName("max_iterLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.max_iterLabel)
        self.max_iterLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.max_iterLineEdit.setEnabled(False)
        self.max_iterLineEdit.setObjectName("max_iterLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.max_iterLineEdit)
        self.cvLabel = QtWidgets.QLabel(self.formGroupBox)
        self.cvLabel.setObjectName("cvLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.cvLabel)
        self.cvLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.cvLineEdit.setEnabled(False)
        self.cvLineEdit.setProperty("value", 3)
        self.cvLineEdit.setObjectName("cvLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.cvLineEdit)
        self.max_n_alphasLabel = QtWidgets.QLabel(self.formGroupBox)
        self.max_n_alphasLabel.setObjectName("max_n_alphasLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.max_n_alphasLabel)
        self.max_n_alphasLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.max_n_alphasLineEdit.setEnabled(False)
        self.max_n_alphasLineEdit.setObjectName("max_n_alphasLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.max_n_alphasLineEdit)
        self.n_jobsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.n_jobsLabel.setObjectName("n_jobsLabel")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.n_jobsLabel)
        self.n_jobsLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.n_jobsLineEdit.setEnabled(False)
        self.n_jobsLineEdit.setObjectName("n_jobsLineEdit")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.n_jobsLineEdit)
        self.cVLabel = QtWidgets.QLabel(self.formGroupBox)
        self.cVLabel.setObjectName("cVLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.cVLabel)
        self.cVCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.cVCheckBox.setObjectName("cVCheckBox")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.cVCheckBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        self.cVCheckBox.toggled['bool'].connect(self.max_iterLineEdit.setEnabled)
        self.cVCheckBox.toggled['bool'].connect(self.cvLineEdit.setEnabled)
        self.cVCheckBox.toggled['bool'].connect(self.max_n_alphasLineEdit.setEnabled)
        self.cVCheckBox.toggled['bool'].connect(self.n_jobsLineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setToolTip(("<html><head/><body><p>Least-angle regression (LARS) is a regression algorithm for high-dimensional data, developed by Bradley Efron, Trevor Hastie, Iain Johnstone and Robert Tibshirani. LARS is similar to forward stepwise regression. At each step, it finds the predictor most correlated with the response. When there are multiple predictors having equal correlation, instead of continuing along the same predictor, it proceeds in a direction equiangular between the predictors.</p><p><span style=\" font-weight:600;\">The advantages of LARS are:</span></p><p>It is numerically efficient in contexts where p &gt;&gt; n (i.e., when the number of dimensions is significantly greater than the number of points)</p><p>It is computationally just as fast as forward selection and has the same order of complexity as an ordinary least squares.</p><p>It produces a full piecewise linear solution path, which is useful in cross-validation or similar attempts to tune the model.</p><p>If two variables are almost equally correlated with the response, then their coefficients should increase at approximately the same rate. The algorithm thus behaves as intuition would expect, and also is more stable.</p><p>It is easily modified to produce solutions for other estimators, like the Lasso.</p><p><span style=\" font-weight:600;\">The disadvantages of the LARS method include:</span></p><p>Because LARS is based upon an iterative refitting of the residuals, it would appear to be especially sensitive to the effects of noise. This problem is discussed in detail by Weisberg in the discussion section of the Efron et al. (2004) Annals of Statistics article.</p></body></html>"))
        self.fit_interceptLabel.setText(("fit_intercept"))
        self.verboseLabel.setText(("verbose"))
        self.normalizeLabel.setText(("normalize"))
        self.precomputeLabel.setText(("precompute"))
        self.n_nonzero_coefsLabel.setText(("n_nonzero_coefs"))
        self.copy_XLabel.setText(("copy_X"))
        self.fit_pathLabel.setText(("fit_path"))
        self.positiveLabel.setText(("positive"))
        self.max_iterLabel.setText(("max_iter"))
        self.cvLabel.setText(("cv"))
        self.max_n_alphasLabel.setText(("max_n_alphas"))
        self.n_jobsLabel.setText(("n_jobs"))
        self.cVLabel.setText(("Cross Validate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

