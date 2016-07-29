# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jobdialogbox.ui'
#
# Created: Fri Jul 22 14:36:35 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_jobDialog(object):
    def setupUi(self, jobDialog):
        jobDialog.setObjectName("jobDialog")
        jobDialog.resize(477, 264)
        font = QtGui.QFont()
        font.setPointSize(12)
        jobDialog.setFont(font)
        jobDialog.setAutoFillBackground(True)
        self.formLayout = QtGui.QFormLayout(jobDialog)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtGui.QPushButton(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 1, 1, 1)
        self.jobLabel_le = QtGui.QLineEdit(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jobLabel_le.setFont(font)
        self.jobLabel_le.setObjectName("jobLabel_le")
        self.gridLayout.addWidget(self.jobLabel_le, 0, 1, 1, 1)
        self.jobLabel = QtGui.QLabel(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jobLabel.setFont(font)
        self.jobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.jobLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.jobLabel.setObjectName("jobLabel")
        self.gridLayout.addWidget(self.jobLabel, 0, 0, 1, 1)
        self.quantityLabel = QtGui.QLabel(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quantityLabel.setFont(font)
        self.quantityLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.quantityLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.quantityLabel.setObjectName("quantityLabel")
        self.gridLayout.addWidget(self.quantityLabel, 4, 0, 1, 1)
        self.jobDate = QtGui.QLabel(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jobDate.setFont(font)
        self.jobDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.jobDate.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.jobDate.setObjectName("jobDate")
        self.gridLayout.addWidget(self.jobDate, 1, 0, 1, 1)
        self.jobDate_Date = QtGui.QDateEdit(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jobDate_Date.setFont(font)
        self.jobDate_Date.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.jobDate_Date.setObjectName("jobDate_Date")
        self.gridLayout.addWidget(self.jobDate_Date, 1, 1, 1, 1)
        self.jobType = QtGui.QLabel(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jobType.setFont(font)
        self.jobType.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.jobType.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.jobType.setObjectName("jobType")
        self.gridLayout.addWidget(self.jobType, 3, 0, 1, 1)
        self.partNo = QtGui.QLabel(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.partNo.setFont(font)
        self.partNo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.partNo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.partNo.setObjectName("partNo")
        self.gridLayout.addWidget(self.partNo, 2, 0, 1, 1)
        self.quantity_sb = QtGui.QSpinBox(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quantity_sb.setFont(font)
        self.quantity_sb.setMaximum(200)
        self.quantity_sb.setProperty("value", 0)
        self.quantity_sb.setObjectName("quantity_sb")
        self.gridLayout.addWidget(self.quantity_sb, 4, 1, 1, 1)
        self.jobType_cb = QtGui.QComboBox(jobDialog)
        self.jobType_cb.setObjectName("jobType_cb")
        self.jobType_cb.addItem("")
        self.jobType_cb.setItemText(0, "")
        self.jobType_cb.addItem("")
        self.jobType_cb.addItem("")
        self.jobType_cb.addItem("")
        self.jobType_cb.addItem("")
        self.jobType_cb.addItem("")
        self.jobType_cb.addItem("")
        self.jobType_cb.addItem("")
        self.jobType_cb.addItem("")
        self.jobType_cb.addItem("")
        self.gridLayout.addWidget(self.jobType_cb, 3, 1, 1, 1)
        self.urgentLabel = QtGui.QLabel(jobDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urgentLabel.setFont(font)
        self.urgentLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.urgentLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.urgentLabel.setObjectName("urgentLabel")
        self.gridLayout.addWidget(self.urgentLabel, 6, 0, 1, 1)
        self.partNo_cb = QtGui.QComboBox(jobDialog)
        self.partNo_cb.setObjectName("partNo_cb")
        self.partNo_cb.addItem("")
        self.partNo_cb.setItemText(0, "")
        self.partNo_cb.addItem("")
        self.partNo_cb.addItem("")
        self.partNo_cb.addItem("")
        self.partNo_cb.addItem("")
        self.partNo_cb.addItem("")
        self.partNo_cb.addItem("")
        self.partNo_cb.addItem("")
        self.partNo_cb.addItem("")
        self.partNo_cb.addItem("")
        self.gridLayout.addWidget(self.partNo_cb, 2, 1, 1, 1)
        self.urgent_cb = QtGui.QComboBox(jobDialog)
        self.urgent_cb.setObjectName("urgent_cb")
        self.urgent_cb.addItem("")
        self.urgent_cb.setItemText(0, "")
        self.urgent_cb.addItem("")
        self.urgent_cb.addItem("")
        self.gridLayout.addWidget(self.urgent_cb, 6, 1, 1, 1)
        self.serialNoLabel = QtGui.QLabel(jobDialog)
        self.serialNoLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.serialNoLabel.setObjectName("serialNoLabel")
        self.gridLayout.addWidget(self.serialNoLabel, 5, 0, 1, 1)
        self.serialNoLabel_le = QtGui.QLineEdit(jobDialog)
        self.serialNoLabel_le.setObjectName("serialNoLabel_le")
        self.gridLayout.addWidget(self.serialNoLabel_le, 5, 1, 1, 1)
        self.formLayout.setLayout(0, QtGui.QFormLayout.SpanningRole, self.gridLayout)

        self.retranslateUi(jobDialog)
        QtCore.QMetaObject.connectSlotsByName(jobDialog)
        jobDialog.setTabOrder(self.jobLabel_le, self.jobDate_Date)
        jobDialog.setTabOrder(self.jobDate_Date, self.partNo_cb)
        jobDialog.setTabOrder(self.partNo_cb, self.jobType_cb)
        jobDialog.setTabOrder(self.jobType_cb, self.quantity_sb)
        jobDialog.setTabOrder(self.quantity_sb, self.serialNoLabel_le)
        jobDialog.setTabOrder(self.serialNoLabel_le, self.urgent_cb)
        jobDialog.setTabOrder(self.urgent_cb, self.pushButton)

    def retranslateUi(self, jobDialog):
        jobDialog.setWindowTitle(QtGui.QApplication.translate("jobDialog", "New Job", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("jobDialog", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.jobLabel_le.setPlaceholderText(QtGui.QApplication.translate("jobDialog", "Enter The Job No.", None, QtGui.QApplication.UnicodeUTF8))
        self.jobLabel.setText(QtGui.QApplication.translate("jobDialog", "Job Number", None, QtGui.QApplication.UnicodeUTF8))
        self.quantityLabel.setText(QtGui.QApplication.translate("jobDialog", "Quantity", None, QtGui.QApplication.UnicodeUTF8))
        self.jobDate.setText(QtGui.QApplication.translate("jobDialog", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.jobDate_Date.setDisplayFormat(QtGui.QApplication.translate("jobDialog", "dd/MMM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType.setText(QtGui.QApplication.translate("jobDialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo.setText(QtGui.QApplication.translate("jobDialog", "Part Number", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType_cb.setItemText(1, QtGui.QApplication.translate("jobDialog", "Standard 1", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType_cb.setItemText(2, QtGui.QApplication.translate("jobDialog", "Standard 2", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType_cb.setItemText(3, QtGui.QApplication.translate("jobDialog", "Non-Conductive 1", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType_cb.setItemText(4, QtGui.QApplication.translate("jobDialog", "Non-Conductive 2", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType_cb.setItemText(5, QtGui.QApplication.translate("jobDialog", "Hybrid 1", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType_cb.setItemText(6, QtGui.QApplication.translate("jobDialog", "Hybrid 2", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType_cb.setItemText(7, QtGui.QApplication.translate("jobDialog", "Iconn Heavy 1", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType_cb.setItemText(8, QtGui.QApplication.translate("jobDialog", "Lower Heavy", None, QtGui.QApplication.UnicodeUTF8))
        self.jobType_cb.setItemText(9, QtGui.QApplication.translate("jobDialog", "Ultra", None, QtGui.QApplication.UnicodeUTF8))
        self.urgentLabel.setText(QtGui.QApplication.translate("jobDialog", "Urgency", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo_cb.setItemText(1, QtGui.QApplication.translate("jobDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo_cb.setItemText(2, QtGui.QApplication.translate("jobDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo_cb.setItemText(3, QtGui.QApplication.translate("jobDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo_cb.setItemText(4, QtGui.QApplication.translate("jobDialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo_cb.setItemText(5, QtGui.QApplication.translate("jobDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo_cb.setItemText(6, QtGui.QApplication.translate("jobDialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo_cb.setItemText(7, QtGui.QApplication.translate("jobDialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo_cb.setItemText(8, QtGui.QApplication.translate("jobDialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.partNo_cb.setItemText(9, QtGui.QApplication.translate("jobDialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.urgent_cb.setItemText(1, QtGui.QApplication.translate("jobDialog", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.urgent_cb.setItemText(2, QtGui.QApplication.translate("jobDialog", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.serialNoLabel.setText(QtGui.QApplication.translate("jobDialog", "Starting Serial Number", None, QtGui.QApplication.UnicodeUTF8))
        self.serialNoLabel_le.setPlaceholderText(QtGui.QApplication.translate("jobDialog", "Enter the first Serial No.", None, QtGui.QApplication.UnicodeUTF8))
