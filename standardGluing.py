# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standardgluingdialogbox.ui'
#
# Created: Wed Jul 20 16:05:36 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_stdgluingDialog(object):
    def setupUi(self, stdgluingDialog):
        stdgluingDialog.setObjectName("stdgluingDialog")
        stdgluingDialog.resize(551, 171)
        font = QtGui.QFont()
        font.setPointSize(12)
        stdgluingDialog.setFont(font)
        self.gridLayout = QtGui.QGridLayout(stdgluingDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.stdgluing_SE_orderNo = QtGui.QLabel(stdgluingDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stdgluing_SE_orderNo.setFont(font)
        self.stdgluing_SE_orderNo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.stdgluing_SE_orderNo.setObjectName("stdgluing_SE_orderNo")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.stdgluing_SE_orderNo)
        self.stdgluing_SE_orderNo_le = QtGui.QLineEdit(stdgluingDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stdgluing_SE_orderNo_le.setFont(font)
        self.stdgluing_SE_orderNo_le.setObjectName("stdgluing_SE_orderNo_le")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.stdgluing_SE_orderNo_le)
        self.stdgluing_SE_batchNo = QtGui.QLabel(stdgluingDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stdgluing_SE_batchNo.setFont(font)
        self.stdgluing_SE_batchNo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.stdgluing_SE_batchNo.setObjectName("stdgluing_SE_batchNo")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.stdgluing_SE_batchNo)
        self.stdgluing_SE_batchNo_le = QtGui.QLineEdit(stdgluingDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stdgluing_SE_batchNo_le.setFont(font)
        self.stdgluing_SE_batchNo_le.setObjectName("stdgluing_SE_batchNo_le")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.stdgluing_SE_batchNo_le)
        self.stdgluing_SE_expiry = QtGui.QLabel(stdgluingDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stdgluing_SE_expiry.setFont(font)
        self.stdgluing_SE_expiry.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.stdgluing_SE_expiry.setObjectName("stdgluing_SE_expiry")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.stdgluing_SE_expiry)
        self.stdgluing_SE_expiry_date = QtGui.QDateEdit(stdgluingDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stdgluing_SE_expiry_date.setFont(font)
        self.stdgluing_SE_expiry_date.setObjectName("stdgluing_SE_expiry_date")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.stdgluing_SE_expiry_date)
        self.stdgluing_SE_tech = QtGui.QLabel(stdgluingDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stdgluing_SE_tech.setFont(font)
        self.stdgluing_SE_tech.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.stdgluing_SE_tech.setObjectName("stdgluing_SE_tech")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.stdgluing_SE_tech)
        self.stdgluing_SE_tech_cb = QtGui.QComboBox(stdgluingDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stdgluing_SE_tech_cb.setFont(font)
        self.stdgluing_SE_tech_cb.setObjectName("stdgluing_SE_tech_cb")
        self.stdgluing_SE_tech_cb.addItem("")
        self.stdgluing_SE_tech_cb.setItemText(0, "")
        self.stdgluing_SE_tech_cb.addItem("")
        self.stdgluing_SE_tech_cb.addItem("")
        self.stdgluing_SE_tech_cb.addItem("")
        self.stdgluing_SE_tech_cb.addItem("")
        self.stdgluing_SE_tech_cb.addItem("")
        self.stdgluing_SE_tech_cb.addItem("")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.stdgluing_SE_tech_cb)
        self.pushButton = QtGui.QPushButton(stdgluingDialog)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(stdgluingDialog)
        QtCore.QMetaObject.connectSlotsByName(stdgluingDialog)

    def retranslateUi(self, stdgluingDialog):
        stdgluingDialog.setWindowTitle(QtGui.QApplication.translate("stdgluingDialog", "Gluing for Standard Item", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_orderNo.setText(QtGui.QApplication.translate("stdgluingDialog", "Order No.", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_orderNo_le.setPlaceholderText(QtGui.QApplication.translate("stdgluingDialog", "Enter the Order No.", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_batchNo.setText(QtGui.QApplication.translate("stdgluingDialog", "Batch No.", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_batchNo_le.setPlaceholderText(QtGui.QApplication.translate("stdgluingDialog", "Enter the Batch No.", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_expiry.setText(QtGui.QApplication.translate("stdgluingDialog", "Expiry Date", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_expiry_date.setDisplayFormat(QtGui.QApplication.translate("stdgluingDialog", "dd/MMM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_tech.setText(QtGui.QApplication.translate("stdgluingDialog", "Technician Name", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_tech_cb.setItemText(1, QtGui.QApplication.translate("stdgluingDialog", "Technician A", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_tech_cb.setItemText(2, QtGui.QApplication.translate("stdgluingDialog", "Technician B", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_tech_cb.setItemText(3, QtGui.QApplication.translate("stdgluingDialog", "Technician C", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_tech_cb.setItemText(4, QtGui.QApplication.translate("stdgluingDialog", "Technician D", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_tech_cb.setItemText(5, QtGui.QApplication.translate("stdgluingDialog", "Technician E", None, QtGui.QApplication.UnicodeUTF8))
        self.stdgluing_SE_tech_cb.setItemText(6, QtGui.QApplication.translate("stdgluingDialog", "Technician F", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("stdgluingDialog", "Done", None, QtGui.QApplication.UnicodeUTF8))

