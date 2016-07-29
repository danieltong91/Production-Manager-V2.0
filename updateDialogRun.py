from PySide.QtCore import*
from PySide.QtGui import*

import sys
import updateBox

class upDialog(QDialog, updateBox.Ui_Dialog):
	def __init__ (self, parent = None):
		super(upDialog, self).__init__(parent)
		self.setupUi(self)
