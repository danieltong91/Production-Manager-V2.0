import sys
from PySide.QtCore import*
from PySide.QtGui import*
import jobDialog

class jbDialog(QWidget, jobDialog.Ui_jobDialog):
	def __init__(self, parent = None):
		super(jbDialog, self).__init__(parent)
		self.setupUi(self)
# app = QApplication(sys.argv)
# program = jbDialog()
# program.show()
# sys.exit(app.exec_())
