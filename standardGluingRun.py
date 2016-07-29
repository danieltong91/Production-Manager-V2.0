from PySide.QtGui import*
from PySide.QtCore import*

import sys
import standardGluing

class stdgluingDialog(QDialog, standardGluing.Ui_stdgluingDialog):
	def __init__ (self, parent = None):
		super(stdgluingDialog, self).__init__(parent)
		self.setupUi(self)