from PyQt5 import QtWidgets, QtCore
from sklearn.linear_model import BayesianRidge

from point_spectra_gui.ui.cv_BayesianRidge import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, BayesianRidge, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        self.numOfIterationsLineEdit.setText(str(self.n_iter))
        self.toleranceLineEdit.setText(str(self.tol))
        self.alpha1LineEdit.setText(str(self.alpha_1))
        self.alpha2LineEdit.setText(str(self.alpha_2))
        self.lambdaLineEdit.setText(str(self.lambda_1))
        self.lambda2LineEdit.setText(str(self.lambda_2))
        self.fitIntercept_List.setCurrentItem(self.fitIntercept_List.findItems(str(self.fit_intercept),QtCore.Qt.MatchExactly)[0])
        self.normalize_List.setCurrentItem(self.normalize_List.findItems(str(self.normalize),QtCore.Qt.MatchExactly)[0])

    def function(self):
        params = {'n_iter': self.numOfIterationsLineEdit.text().split(','),
                  'tol': self.toleranceLineEdit.text().split(','),
                  'alpha_1': self.alpha1LineEdit.text().split(','),
                  'alpha_2': self.alpha2LineEdit.text().split(','),
                  'lambda_1': self.lambdaLineEdit.text().split(','),
                  'lambda_2': self.lambda2LineEdit.text().split(','),
                  'compute_score': False,
                  'fit_intercept': self.fitIntercept_List.selectedItems(),
                  'normalize': self.normalize_List.selectedItems(),
                  'copy_X': True,
                  'verbose': True}
        modelkey = str(params)
        return params, modelkey


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
