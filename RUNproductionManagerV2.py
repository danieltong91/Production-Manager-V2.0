import time
import sys
from PySide.QtCore import*
from PySide.QtGui import*
import copy
import csv
import random
import PySide
print PySide.__version__

import productionManagerV2
import groupBoxRun
import jobDialogRun



class mainWindow(QMainWindow, productionManagerV2.Ui_MainWindow):
	def __init__(self, parent = None, arg = None):
		super(mainWindow, self).__init__(parent)

		self.setupUi(self)
		self.totaloutput =[]

		self.actionAdd.triggered.connect(self.newJob)
		self.actionCSV.triggered.connect(self.exportCSV)
		self.actionDetailed.triggered.connect(self.exportDetailed)
		self.actionBasic.triggered.connect(self.exportBasic)
		self.colourful = QPalette()
		
	def newJob(self):
		self.newjob = jobDialogRun.jbDialog(self)
		self.newjob.show()
		self.newjob.pushButton.clicked.connect(self.LayoutManager)
		self.newjob.partNo_cb.activated.connect(self.setType)
		self.newjob.jobType_cb.activated.connect(self.setPart)
		self.has_run = False
		self.tray=[]
		self.trays = 0
	def setType(self):
		self.newjob.jobType_cb.setCurrentIndex(self.newjob.partNo_cb.currentIndex())
	def setPart(self):
		self.newjob.partNo_cb.setCurrentIndex(self.newjob.jobType_cb.currentIndex())
	
	def LayoutManager(self):
		SerialCodeFront = ""
		SerialCodeBack = ""
		if str(self.newjob.serialNoLabel_le.text()) is "":
			msgBox = QMessageBox()
			msgBox.setWindowTitle(unicode("Warning!"))
			msgBox.setText("Please key in the Starting Serial Number")
			msgBox.exec_()
		if self.newjob.quantity_sb.value() == 0:
			msgBox = QMessageBox()
			msgBox.setWindowTitle(unicode("Warning!"))
			msgBox.setText("Please key in the Quantity")
			msgBox.exec_()
		else:
			self.newjob.close()
			
			batch = self.newjob.quantity_sb.value() - (self.newjob.quantity_sb.value() % 10)
			numTrays = batch/10
			if self.newjob.quantity_sb.value() == 0:
				numTrays = 0
			elif numTrays == 0 and self.newjob.quantity_sb.value() % 10 <=9:
				numTrays = 1
			elif numTrays != 0 and self.newjob.quantity_sb.value() %10 <=4:
				numTrays = numTrays
			elif numTrays != 0 and self.newjob.quantity_sb.value() %10 >= 5 and self.newjob.quantity_sb.value() %10 <=9:
				numTrays = numTrays+1

			# if str(self.newjob.serialNoLabel_le.text())[0].isdigit() is False:
			# 	a = int(str(self.newjob.serialNoLabel_le.text())[1:])
			# else:
			# 	a = int(str(self.newjob.serialNoLabel_le.text()))
			a=""
			numbers = []
			for i in str(self.newjob.serialNoLabel_le.text()):
				if i.isdigit() is True:
					numbers.append(i)
			for numb in numbers:
				a = a+ numb
			a = int(a)

			if str(self.newjob.jobType_cb.currentText()) == "Lower Heavy" :
				SerialCodeFront = ""
				SerialCodeBack = ""
			elif str(self.newjob.jobType_cb.currentText()) == "Ultra":
				SerialCodeFront = ""
				SerialCodeBack = "L"
			elif str(self.newjob.jobType_cb.currentText()) == "Iconn Heavy (175-180 gram force)":
				SerialCodeFront = "H"
				SerialCodeBack = ""
			else:
				SerialCodeFront = "K"
				SerialCodeBack = ""
			serialcounter = a

			quantity = self.newjob.quantity_sb.value()
			while self.trays != numTrays:
				self.trayinfo = []
				count = 0
				oneshot_switch = False
				oneshot_switch2 = False
				while self.has_run == False:
					if quantity >=20:
						quantity = quantity -10
						calculate = True
					if quantity <20 and quantity >10:
						quantity = quantity -10
						calculate = True
					else:
						calculate =True
					if calculate == True:
						# print quantity
						if quantity <5:
							if quantity == 4:
								oneshot = quantity
								oneshot_switch = True
								oneshot_switch2 = True
								self.has_run = True
								quantity =quantity -2
								break
							elif quantity == 3:
								oneshot = quantity
								oneshot_switch = True
								oneshot_switch2 = True
								self.has_run = True
								quantity = quantity-2
								# print quantity
								break
							elif quantity == 2:
								oneshot = quantity
								oneshot_switch = True
								self.has_run = True
								break
							elif quantity == 1:
								oneshot = quantity
								oneshot_switch = True
								self.has_run = True
								break
							else:
								oneshot_switch = False
								self.has_run = True
								break
						elif quantity <=10 and quantity>=5:
							break
				if oneshot_switch == True:
					if oneshot_switch2 == True:
						x = 10+ 2
						if quantity == 2:
							self.has_run = False
						if quantity == 1:
							self.has_run = False
					else:
						x = 10+ oneshot
				else:
					x = 10
				while count != x:
					WCdata  = {}
					if serialcounter + count == (a+self.newjob.quantity_sb.value()):
						break
					WCdata['serialno'] = SerialCodeFront + str(serialcounter + count) + SerialCodeBack
					WCdata['jobno'] = self.newjob.jobLabel_le.text()
					WCdata['jobdate'] = self.newjob.jobDate_Date.date()
					WCdata['partno'] = self.newjob.partNo_cb.currentText()
					WCdata['type'] = self.newjob.jobType_cb.currentText()
					self.trayinfo.append(WCdata)
					count +=1
					oneshot_switch = False
				serialcounter = serialcounter + count

				self.creation = groupBoxRun.form(self)

				self.creation.updateboxtablefromorders(self.trays,self.trayinfo)

				self.creation.pb_info.clicked.connect(self.creation.info)
				self.creation.pb_update.clicked.connect(self.creation.updatedialogbox)

				

				self.creation.newjobupdate(self.trays,self.newjob.jobLabel_le.text(),self.newjob.partNo_cb.currentText(), 
					unicode(self.newjob.quantity_sb.value()), self.newjob.jobDate_Date.date(), self.newjob.jobType_cb.currentText(), 
					self.newjob.urgent_cb.currentText(), len(self.trayinfo)) 
				self.creation.groupBox.setTitle(unicode("Tray " + str(self.trays +1) + " - SR:" 
					+ str(self.creation.updatebox.update_tray_tw.item(0,0).text())))

				for i in range(6):
					for j in range(6):
						if self.GL_orders.itemAtPosition(i,j) is None:
							self.GL_orders.addWidget(self.creation, i, j)
					
				self.tray.append(self.creation)
				self.trays +=1

				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)
				self.colourful.setColor(self.colourful.Window, QColor(r,g,b))
			for i in range(len(self.tray)):
				self.tray[i].cb_gluing.clicked.connect(self.checkstate)
				self.tray[i].cb_pivot.clicked.connect(self.checkstate)
				self.tray[i].cb_final.clicked.connect(self.checkstate)
				self.tray[i].updatebox.update_pb_final.clicked.connect(self.completedtrayshift)
				self.tray[i].setPalette(self.colourful)

			self.totaloutput.append(self.tray)
			
			

	def checkstate(self):
		for x in self.totaloutput:
			for a in range(len(x)):
				if x[a].cb_gluing.isChecked():
					if x[a].stdgluingdialog_checked == False:
						for i in range(6):
							for j in range(6):
								if self.GL_gluing.itemAtPosition(i,j) is None:
									self.GL_gluing.addWidget(x[a],i,j)
									x[a].pb.setValue(0)
				elif x[a].cb_pivot.isChecked():
					if x[a].pivdialog_checked == False:
						for i in range(6):
							for j in range(6):
								if self.GL_pivot.itemAtPosition(i,j) is None:
									self.GL_pivot.addWidget(x[a],i,j)
									x[a].pb.setValue(0)
				elif x[a].cb_final.isChecked():
					if x[a].findialog_checked == False:
						for i in range(6):
							for j in range(6):
								if self.GL_final.itemAtPosition(i,j) is None:
									self.GL_final.addWidget(x[a],i,j)
									x[a].pb.setValue(0)
	def completedtrayshift(self):
		for x in self.totaloutput:
			for a in range(len(x)):
				if x[a].cb_final.isChecked():
					if x[a].findialog_checked == True:
						if str(x[a].label.text()) != "Final in Progress":
							for i in range(6):
								for j in range(10):
									if self.GL_completed.itemAtPosition(i,j) is None:
										self.GL_completed.addWidget(x[a],i,j)
										x[a].pb.setValue(100)
		
	def exportCSV(self):
		name = QFileDialog.getSaveFileName(self, 'Save File')
		grandmasterlist = []
		for x in self.totaloutput:
			for a in range(len(x)):
				for i in x[a].trayoutput:
					grandmasterlist.append(i)
		with open(name[0] + '.csv', 'wb') as output_file:
			fieldnames = ['JobNo','PartNo', 'JobDate', 'Type','Urgent','SEBatchNo','SEOrderNo','SEDate','HysolBatchNo','HysolMFGDate',
			'HysolPRODDate','7471BatchNo','7471Date','222BatchNo','222Date','VarnishNo','VarnishDate','GluingDoneby','GluingStart',
			'GluingEnd','PivotDoneby','PivotStart','PivotEnd','FinalDoneby','FinalStart','FinalEnd', 'Rework', 'ReworkType','ReworkSubmit', 'ReworkSubmitDateTime', 
			'ReworkAttempt', 'ReworkAttempDateTime',  'Remarks', 'SerialNo', 'ClampForce','TorqueValue']
			dict_writer = csv.DictWriter(output_file,fieldnames, extrasaction = 'ignore')
			dict_writer.writeheader()
			dict_writer.writerows(grandmasterlist)
	def exportDetailed(self):
		name = QFileDialog.getSaveFileName(self, 'Save File')
		grandmasterlist = []
		for x in self.totaloutput:
			for a in range(len(x)):
				for i in x[a].trayoutputWCAssemblyDetailed:
					grandmasterlist.append(i)
		# print grandmasterlist
		with open(name[0]+'oracleDetailed.csv', 'wb') as output_file:
			fieldnames = ['Job','EpoxyLotA','EpoxyLotB', 'wc S/N', 'GluingEmp#','GluingDateTime','PivotEmp#','PivotDateTime','FinalEmp#','FinalDateTime', 'BimorphEmp#', 'TorqueValue','T1 comment']
			dict_writer = csv.DictWriter(output_file,fieldnames, extrasaction = 'ignore')
			dict_writer.writeheader()
			dict_writer.writerows(grandmasterlist)
	def exportBasic(self):
		name = QFileDialog.getSaveFileName(self, 'Save File')
		grandmasterlist = []
		for x in self.totaloutput:
			for a in range(len(x)):
				for i in x[a].trayoutputWCAssembly:
					grandmasterlist.append(i)
		with open(name[0]+'oracleBasic.csv', 'wb') as output_file:
			fieldnames = ['Job','Quantity','RecDate','EpoxyLotA','EpoxyLotB']
			dict_writer = csv.DictWriter(output_file,fieldnames, extrasaction = 'ignore')
			dict_writer.writeheader()
			dict_writer.writerows(grandmasterlist)

app = QApplication(sys.argv)
program = mainWindow()
program.show()
sys.exit(app.exec_())
