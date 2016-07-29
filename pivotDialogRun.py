from PySide.QtGui import*
from PySide.QtCore import*

import sys
import pivotDialog

class pivDialog(QDialog, pivotDialog.Ui_pivotDialog):
	def __init__ (self, parent = None):
		super(pivDialog, self).__init__(parent)
		self.setupUi(self)