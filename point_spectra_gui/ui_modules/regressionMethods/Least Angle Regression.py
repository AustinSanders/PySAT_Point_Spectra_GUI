from PyQt5 import QtWidgets


class LeastAngleRegression:
    def LAR(self):
        self.line = QtWidgets.QFrame(self.regression)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.min_max_layout.addWidget(self.line)
        self.groupbox = QtWidgets.QGroupBox(self.regression)
        self.groupbox.setObjectName("groupbox")
        self.Least_Angle_Regression_form = QtWidgets.QFormLayout(self.groupbox)
        self.Least_Angle_Regression_form.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.Least_Angle_Regression_form.setContentsMargins(11, 11, 11, 11)
        self.Least_Angle_Regression_form.setSpacing(6)
        self.Least_Angle_Regression_form.setObjectName("Least_Angle_Regression_form")
        self.n_nonzero_coefs_label = QtWidgets.QLabel(self.groupbox)
        self.n_nonzero_coefs_label.setObjectName("n_nonzero_coefs_label")
        self.Least_Angle_Regression_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.n_nonzero_coefs_label)
        self.n_nonzero_coefs_spinBox = QtWidgets.QSpinBox(self.groupbox)
        self.n_nonzero_coefs_spinBox.setMaximum(999999999)
        self.n_nonzero_coefs_spinBox.setProperty("value", 500)
        self.n_nonzero_coefs_spinBox.setObjectName("n_nonzero_coefs_spinBox")
        self.Least_Angle_Regression_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.n_nonzero_coefs_spinBox)
        self.fit_intercept_label = QtWidgets.QLabel(self.groupbox)
        self.fit_intercept_label.setObjectName("fit_intercept_label")
        self.Least_Angle_Regression_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fit_intercept_label)
        self.fit_intercept_checkBox = QtWidgets.QCheckBox(self.groupbox)
        self.fit_intercept_checkBox.setCheckable(True)
        self.fit_intercept_checkBox.setChecked(True)
        self.fit_intercept_checkBox.setObjectName("fit_intercept_checkBox")
        self.Least_Angle_Regression_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fit_intercept_checkBox)
        self.positive_label = QtWidgets.QLabel(self.groupbox)
        self.positive_label.setObjectName("positive_label")
        self.Least_Angle_Regression_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.positive_label)
        self.positive_checkBox = QtWidgets.QCheckBox(self.groupbox)
        self.positive_checkBox.setCheckable(True)
        self.positive_checkBox.setChecked(False)
        self.positive_checkBox.setObjectName("positive_checkBox")
        self.Least_Angle_Regression_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.positive_checkBox)
        self.verbose_label = QtWidgets.QLabel(self.groupbox)
        self.verbose_label.setObjectName("verbose_label")
        self.Least_Angle_Regression_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.verbose_label)
        self.verbose_checkBox = QtWidgets.QCheckBox(self.groupbox)
        self.verbose_checkBox.setCheckable(True)
        self.verbose_checkBox.setChecked(False)
        self.verbose_checkBox.setObjectName("verbose_checkBox")
        self.Least_Angle_Regression_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.verbose_checkBox)
        self.copy_X_label = QtWidgets.QLabel(self.groupbox)
        self.copy_X_label.setObjectName("copy_X_label")
        self.Least_Angle_Regression_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.copy_X_label)
        self.precompute_checkBox = QtWidgets.QCheckBox(self.groupbox)
        self.precompute_checkBox.setCheckable(True)
        self.precompute_checkBox.setChecked(True)
        self.precompute_checkBox.setTristate(True)
        self.precompute_checkBox.setObjectName("precompute_checkBox")
        self.Least_Angle_Regression_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.precompute_checkBox)
        self.compute_score_label = QtWidgets.QLabel(self.groupbox)
        self.compute_score_label.setObjectName("compute_score_label")
        self.Least_Angle_Regression_form.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.compute_score_label)
        self.copy_X_checkBox = QtWidgets.QCheckBox(self.groupbox)
        self.copy_X_checkBox.setCheckable(True)
        self.copy_X_checkBox.setChecked(False)
        self.copy_X_checkBox.setObjectName("copy_X_checkBox")
        self.Least_Angle_Regression_form.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.copy_X_checkBox)
        self.eps_label = QtWidgets.QLabel(self.groupbox)
        self.eps_label.setObjectName("eps_label")
        self.Least_Angle_Regression_form.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.eps_label)
        self.eps_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupbox)
        self.eps_doubleSpinBox.setDecimals(16)
        self.eps_doubleSpinBox.setMinimum(-999999999.0)
        self.eps_doubleSpinBox.setMaximum(999999999.0)
        self.eps_doubleSpinBox.setSingleStep(0.0)
        self.eps_doubleSpinBox.setProperty("value", 2.220446)
        self.eps_doubleSpinBox.setObjectName("eps_doubleSpinBox")
        self.Least_Angle_Regression_form.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.eps_doubleSpinBox)
        self.fit_path_label = QtWidgets.QLabel(self.groupbox)
        self.fit_path_label.setObjectName("fit_path_label")
        self.Least_Angle_Regression_form.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.fit_path_label)
        self.fit_path_checkBox = QtWidgets.QCheckBox(self.groupbox)
        self.fit_path_checkBox.setCheckable(True)
        self.fit_path_checkBox.setChecked(True)
        self.fit_path_checkBox.setObjectName("fit_path_checkBox")
        self.Least_Angle_Regression_form.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.fit_path_checkBox)
        self.verticalLayout_2.addWidget(self.groupbox)

        self.n_nonzero_coefs_label.setText("n_nonzero_coefs")
        self.fit_intercept_label.setText("fit_intercept")
        self.fit_intercept_checkBox.setText("calculate the intercept for this model")
        self.positive_label.setText("positive")
        self.positive_checkBox.setText("Restrict coefficients to be >= 0")
        self.verbose_label.setText("verbose")
        self.verbose_checkBox.setText("Verbose mode when fitting the model")
        self.copy_X_label.setText("precompute")
        self.precompute_checkBox.setText("True | False | ‘auto’")
        self.compute_score_label.setText("copy_X")
        self.copy_X_checkBox.setText("compute the objective function at each step of the model")
        self.eps_label.setText("eps")
        self.fit_path_label.setText("fit_path")
        self.fit_path_checkBox.setText("store full path in the coef_path_ attribute")
