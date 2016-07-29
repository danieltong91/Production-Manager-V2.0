from PySide.QtGui import*
from PySide.QtCore import*

import sys
import finalDialog

class finDialog(QDialog, finalDialog.Ui_finalDialog):
	def __init__ (self, parent = None):
		super(finDialog, self).__init__(parent)
		self.setupUi(self)