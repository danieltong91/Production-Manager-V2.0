import sys
from PySide.QtGui import*
from PySide.QtCore import*

import informationDialog

class infoDialog(QDialog, informationDialog.Ui_infoDialog):
	def __init__ (self, parent = None):
		super(infoDialog, self).__init__(parent)
		self.setupUi(self)