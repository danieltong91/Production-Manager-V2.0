from PySide.QtGui import*
from PySide.QtCore import*

import groupBox
import informationDialogRun
import standardGluingRun
import pivotDialogRun
import finalDialogRun
import updateDialogRun

class form(QWidget, groupBox.Ui_Form):
	def __init__(self, parent = None):
		super(form, self).__init__(parent)
		self.setupUi(self)

		self.cb_gluing.clicked.connect(self.checkstate)
		self.cb_pivot.clicked.connect(self.checkstate)
		self.cb_final.clicked.connect(self.checkstate)

		self.hit = 0

		self.stdgluingdialog = standardGluingRun.stdgluingDialog(self)
		self.stdgluingdialog_start = False
		self.stdgluingdialog_checked = False
		self.stdgluingdialog_start_datetime = QDateTime()
		self.completedgluingDateTime = QDateTime()

		self.pivdialog = pivotDialogRun.pivDialog(self)
		self.pivdialog_start = False
		self.pivdialog_checked = False
		self.pivdialog_start_datetime = QDateTime()
		self.completedpivotDateTime = QDateTime()

		self.findialog = finalDialogRun.finDialog(self)
		self.findialog_start = False
		self.findialog_checked = False
		self.findialog_start_datetime = QDateTime()
		self.completedfinalDateTime = QDateTime()

		self.infoform = informationDialogRun.infoDialog(self)

		self.updatebox = updateDialogRun.upDialog(self)

		# self.updatebox.update_pb_gluing.clicked.connect(self.completedgluing)
		self.updatebox.connect(self.updatebox.update_pb_gluing, SIGNAL('clicked()'), self.completedgluing)

		# self.updatebox.update_pb_pivot.clicked.connect(self.completedpivot)
		self.updatebox.connect(self.updatebox.update_pb_pivot, SIGNAL('clicked()'), self.completedpivot)

		# self.updatebox.update_pb_final.clicked.connect(self.completedfinal)
		self.updatebox.connect(self.updatebox.update_pb_final,SIGNAL('clicked()'), self.completedfinal)
		# self.updatebox.update_tray_pb.clicked.connect(self.completedtray)
		self.updatebox.connect(self.updatebox.update_tray_pb, SIGNAL('clicked()'), self.completedtray)

		# self.updatebox.update_pb_declare_rework.clicked.connect(self.declareRework)
		self.updatebox.connect(self.updatebox.update_pb_declare_rework, SIGNAL('clicked()'), self.declareRework)

		# self.updatebox.update_pb_attempt_rework.clicked.connect(self.attemptRework)
		self.updatebox.connect(self.updatebox.update_pb_attempt_rework, SIGNAL('clicked()'), self.attemptRework)

		self.completedGLUING = False
		self.completedPIVOT = False
		self.completedFINAL = False
		self.trayoutput = []
		self.trayoutputWCAssembly = []
		self.trayoutputWCAssemblyDetailed=[]
	

	def newjobupdate(self, i, jobinformation, partinformation, quantityinformation,dateinformation, typeinformation, urgentinformation, trayquantity):
		
		self.infoform.setWindowTitle("Tray " + str(i+1)+ " Information")
		self.infoform.info_jobNo_le.setText(jobinformation)
		self.infoform.info_partNo_le.setText(partinformation)
		self.infoform.info_quantity_le.setText(quantityinformation)
		self.infoform.info_jobDate_date.setDate(dateinformation)
		self.infoform.info_type_le.setText(typeinformation)
		self.infoform.info_urgent_le.setText(urgentinformation)
		self.lcd.display(trayquantity)
		self.label_job.setText(unicode("Job Number: ") + jobinformation)

	def info(self):
		self.updateinfocaller()
		self.infoform.show()

	def updateinfocaller(self):
		self.infoform.info_serialNo.clearContents()
		self.updateinfotop()
		self.updateinfobottom()

	def updateinfotop(self):
		self.infoform.info_SE_orderNo_le.setText(self.stdgluingdialog.stdgluing_SE_orderNo_le.text())
		self.infoform.info_SE_batchNo_le.setText(self.stdgluingdialog.stdgluing_SE_batchNo_le.text())
		self.infoform.info_SE_expiry_date.setDate(self.stdgluingdialog.stdgluing_SE_expiry_date.date())
		self.infoform.info_gluing_le.setText(self.stdgluingdialog.stdgluing_SE_tech_cb.currentText())
		self.infoform.info_gluingDatetime_start_datetime.setDateTime(self.stdgluingdialog_start_datetime)
		self.infoform.info_gluingDatetime_end_datetime.setDateTime(self.completedgluingDateTime)

		self.infoform.info_hysol_batchNo_le.setText(self.pivdialog.pivot_hysol_batchNo_le.text())
		self.infoform.info_hysol_mfg_expiry_date.setDate(self.pivdialog.pivot_hysol_mfgexpiry_date.date())
		self.infoform.info_hysol_prod_expiry_date.setDate(self.pivdialog.pivot_hysol_prodexpiry_date.date())
		self.infoform.info_7471_batchNo_le.setText(self.pivdialog.pivot_7471_batchNo_le.text())
		self.infoform.info_7471_expiry_date.setDate(self.pivdialog.pivot_7471_expiry_date.date())
		self.infoform.info_pivot_le.setText(self.pivdialog.pivot_tech_cb.currentText())
		self.infoform.info_pivotDatetime_start_datetime.setDateTime(self.pivdialog_start_datetime)
		self.infoform.info_pivotDatetime_end_datetime.setDateTime(self.completedpivotDateTime)

		self.infoform.info_222_batchNo_le.setText(self.findialog.final_222_batchNo_le.text())
		self.infoform.info_222_expiry_date.setDate(self.findialog.final_222_expiry_date.date())
		self.infoform.info_varnish_batchNo_le.setText(self.findialog.final_varnish_batchNo_le.text())
		self.infoform.info_varnish_expiry_date.setDate(self.findialog.final_varnish_expiry_date.date())
		self.infoform.info_final_le.setText(self.findialog.final_tech_cb.currentText())
		self.infoform.info_finalDatetime_start_datetime.setDateTime(self.findialog_start_datetime)
		self.infoform.info_finalDatetime_end_datetime.setDateTime(self.completedfinalDateTime)

	def updateinfobottom(self):
		for i in range(self.updatebox.update_tray_tw.rowCount()):
			if self.infoform.info_serialNo.rowCount()<self.updatebox.update_tray_tw.rowCount():
				self.infoform.info_serialNo.insertRow(i)
				# print i
			else:
				pass
			for j in range(self.updatebox.update_tray_tw.columnCount()):
				if self.updatebox.update_tray_tw.item(i,j) is None:
					pass
				else:
					self.infoform.info_serialNo.setItem(i,j, self.updatebox.update_tray_tw.item(i,j).clone())

			strikeoutinfo = self.infoform.info_serialNo.item(i,0).font()
			if self.infoform.info_serialNo.item(i,5) is not None:
				if self.infoform.info_serialNo.item(i,5).text() == unicode("Scrap"):
					strikeoutinfo.setStrikeOut(True)
				else:
					strikeoutinfo.setStrikeOut(False)
			else:
				strikeoutinfo.setStrikeOut(False)
			self.infoform.info_serialNo.item(i,0).setFont(strikeoutinfo)

	def checkstate(self):
		if self.cb_gluing.isChecked():
			if self.stdgluingdialog_checked == False:
				self.stdgluingdialog.show()
				self.stdgluingdialog.pushButton.clicked.connect(self.stdgluingClicked)
				# self.stdglugingdialog.connect(self.stdgluingdialog.pushButton, SIGNAL('clicked()'), self.stdgluingClicked)
				self.label.setText(unicode("Gluing in Progress"))
		elif self.cb_pivot.isChecked():
			if self.pivdialog_checked == False:
				self.pivdialog.show()
				self.pivdialog.pushButton.clicked.connect(self.pivClicked)
				# self.pivdialog.connect(self.pivdialog.pushButton, SIGNAL('clicked()'), self.pivClicked)
				self.label.setText(unicode("Pivot in Progress"))
		elif self.cb_final.isChecked():
			if self.findialog_checked == False:
				self.findialog.show()
				self.findialog.pushButton.clicked.connect(self.finClicked)
				# self.findialog.connect(self.findialog.pushButton, SIGNAL('clicked()'), self.finClicked)
				self.label.setText(unicode("Final in Progress"))

	def updatedialogbox(self):
		#do a save here? separate save?
		self.updatebox.show()

	def updateboxtablefromorders(self, i, trayinfo):
		self.updatebox.setWindowTitle("Tray " + str(i+1) + " Update")
		self.updatebox.update_serialno_declare_cb.addItem(unicode(""))
		self.updatebox.update_serialno_attempt_cb.addItem(unicode(""))
		for i in trayinfo:
			self.updatebox.update_tray_tw.insertRow(trayinfo.index(i))
			self.updatebox.update_tray_tw.setItem(trayinfo.index(i),0,QTableWidgetItem(unicode(trayinfo[trayinfo.index(i)]['serialno'])))
			self.updatebox.update_serialno_declare_cb.addItem(unicode(trayinfo[trayinfo.index(i)]['serialno']))

	def declareRework(self):
		msgBox = QMessageBox()
		msgBox.setWindowTitle(unicode("Warning!"))
		msgBox.setText("Remember to complete the rework process before saving the rework data to the database by clicking the button above!")
		msgBox.exec_()
		self.updatebox.update_serialno_attempt_cb.addItem(self.updatebox.update_serialno_declare_cb.currentText())

		for i in range(self.updatebox.update_tray_tw.rowCount()):
			if self.updatebox.update_tray_tw.item(i,0).text() == self.updatebox.update_serialno_declare_cb.currentText():
				datetime = QDateTime()
				currentdatetime = datetime.currentDateTime().toString("hh:mm:ssap dd MMM yyyy")
				if self.updatebox.update_tray_tw.item(i,4) is not None:
					a = int(self.updatebox.update_tray_tw.takeItem(i,4).text()) +1
				else:
					a = 1
				self.updatebox.update_tray_tw.setItem(i,4,QTableWidgetItem(unicode(a)))
				# self.updatebox.update_tray_tw.setItem(i,4, QTableWidgetItem(unicode("True")))
				self.updatebox.update_tray_tw.setItem(i,5, QTableWidgetItem(self.updatebox.update_type_cb.currentText()))

				strikeouttext = self.updatebox.update_tray_tw.item(i,0).font()
				if self.updatebox.update_type_cb.currentText() == unicode("Scrap"):
					strikeouttext.setStrikeOut(True)
				else:
					strikeouttext.setStrikeOut(False)
				self.updatebox.update_tray_tw.item(i,0).setFont(strikeouttext)
				self.updatebox.update_tray_tw.setItem(i,6, QTableWidgetItem(self.updatebox.update_doneby_declare_cb.currentText()))
				self.updatebox.update_tray_tw.setItem(i,7,QTableWidgetItem(currentdatetime))
				break

	def attemptRework(self):
		msgBox = QMessageBox()
		msgBox.setWindowTitle(unicode("Warning!"))
		msgBox.setText("Remember to save the rework data to the database by clicking the button above!")
		msgBox.exec_()
		for i in range(self.updatebox.update_tray_tw.rowCount()):
			if self.updatebox.update_tray_tw.item(i,0).text() == self.updatebox.update_serialno_attempt_cb.currentText():
				datetime = QDateTime()
				currentdatetime = datetime.currentDateTime().toString("hh:mm:ssap dd MMM yyyy")
				self.updatebox.update_tray_tw.setItem(i,8, QTableWidgetItem(self.updatebox.update_doneby_attempt_cb.currentText()))
				self.updatebox.update_tray_tw.setItem(i,9, QTableWidgetItem(currentdatetime))
				removal = self.updatebox.update_serialno_attempt_cb.currentIndex()
				self.updatebox.update_serialno_attempt_cb.removeItem(removal)

				strikeoutcheck = self.updatebox.update_tray_tw.item(i,0).font()
				if strikeoutcheck.strikeOut() is True:
					strikeoutcheck.setStrikeOut(False)
				self.updatebox.update_tray_tw.item(i,0).setFont(strikeoutcheck)

				break

	def stdgluingClicked(self):
		if self.stdgluingdialog_start == False:
			self.stdgluingdialog_start_datetime = QDateTime.currentDateTime()
			self.stdgluingdialog_start = True
			self.stdgluingdialog_checked = True
			self.cb_pivot.setCheckable(False)
			self.cb_final.setCheckable(False)
		self.stdgluingdialog.close()
	def pivClicked(self):
		if self.pivdialog_start == False:
			self.pivdialog_start_datetime = QDateTime.currentDateTime()
			self.pivdialog_start = True
			self.pivdialog_checked = True
			self.cb_gluing.setCheckable(False)
			self.cb_final.setCheckable(False)
		self.pivdialog.close()
	def finClicked(self):
		if self.findialog_start == False:
			self.findialog_start_datetime = QDateTime.currentDateTime()
			self.findialog_start = True
			self.findialog_checked = True
			self.cb_pivot.setCheckable(False)
			self.cb_gluing.setCheckable(False)
		self.findialog.close()

	def completedgluing(self):
		if self.completedGLUING is False:
			if self.cb_gluing.isChecked():
				self.completedgluingDateTime = QDateTime.currentDateTime()
				self.updatebox.close()
				self.trialmili = 100     #10 = 1 second
				self.completedGLUING = True
				self.label.setText(unicode("Curing in Progress"))
				self.runtimer()
			else:
				msgBox = QMessageBox()
				msgBox.setWindowTitle(unicode("Warning!"))
				msgBox.setText("Please start the Gluing process first.")
				msgBox.exec_()
		else:
			self.updatebox.close()

	def completedpivot(self):
		if self.completedPIVOT is False:
			if self.cb_pivot.isChecked():
				# print "completed pivot"
				self.completedpivotDateTime = QDateTime.currentDateTime()
				self.updatebox.close()
				self.trialmili = 400
				self.completedPIVOT = True
				self.label.setText(unicode("Curing in Progress"))
				self.runtimer()
			else:
				msgBox = QMessageBox()
				msgBox.setWindowTitle(unicode("Warning!"))
				msgBox.setText("Please complete the Gluing process first.")
				msgBox.exec_()
		else:
			self.updatebox.close()

	def completedfinal(self):
		if self.completedFINAL is False:
			if self.cb_final.isChecked():
				self.completedfinalDateTime = QDateTime.currentDateTime()
				self.updatebox.close()
				self.trialmili = 1
				# self.completedFINAL = True
				self.label.setText(unicode("Saving in Progress"))
				self.runtimer()
				# self.datacollection()
			else:
				msgBox = QMessageBox()
				msgBox.setWindowTitle(unicode("Warning!"))
				msgBox.setText("Please start the Pivot process first.")
				msgBox.exec_()
		else:
			self.updatebox.close()

	def runtimer(self):
		# print "running"
		if self.hit ==0:
			self.value = 0
			self.timer = QTimer(self)
			self.timer.setSingleShot(False)
			self.timer.timeout.connect(self.increaseValue)
			self.timer.connect(self.timer, SIGNAL('timeout()'), self.increaseValue)
			self.timer.start(self.trialmili)
			self.hit = 1
		else:
			self.timer.stop()
			self.tray.pb.setValue(0)
			self.hit=0		
	def increaseValue(self):
		self.pb.setValue(self.value)
		self.value = self.value+1
		if self.value == 101:
			self.timer.stop()
			self.hit = 0
			self.label.setText(unicode("COMPLETED!"))
			self.cb_gluing.setCheckable(True)
			self.cb_pivot.setCheckable(True)
			self.cb_final.setCheckable(True)

	def completedtray(self):
		self.toggle = False
		self.datacollection()
		self.toggle = True
		if self.toggle == True:
		# self.over1000()
			msgBox = QMessageBox()
			msgBox.setWindowTitle(unicode("Success!"))
			msgBox.setText("Update Succeeded and is now reflected in the Info Dialog. Data has been Saved!")
			msgBox.exec_()
			self.updatebox.close()

	def datacollection(self):
		# self.updateinfocaller()
		self.updateinfotop()
		# self.updateinfobottom()
		
		self.dictkeys = ['SerialNo', 'TorqueValue','ClampForce','Remarks','Rework','ReworkType','ReworkSubmit','ReworkSubmitDateTime','ReworkAttempt','ReworkAttempDateTime']
		for i in range(self.updatebox.update_tray_tw.rowCount()):				#changed to updatebox instead of infoform because of bug?
			self.singleWireClamp = {}
			self.WireClampBasic={}
			self.WireClampDetailed={}
			for j in range(self.updatebox.update_tray_tw.columnCount()):
				if self.updatebox.update_tray_tw.item(i,j) is not None:
					self.singleWireClamp[self.dictkeys[j]] = str(self.updatebox.update_tray_tw.item(i,j).text())
				else:
					self.singleWireClamp[self.dictkeys[j]] = "None"
			self.singleWireClamp['JobNo'] = str(self.infoform.info_jobNo_le.text())
			self.singleWireClamp['PartNo'] = str(self.infoform.info_partNo_le.text())
			self.singleWireClamp['JobDate'] = str(self.infoform.info_jobDate_date.date().toString("dd MMM yyyy"))
			self.singleWireClamp['Type'] = str(self.infoform.info_type_le.text())
			self.singleWireClamp['Urgent'] = str(self.infoform.info_urgent_le.text())
			self.singleWireClamp['SEBatchNo'] = str(self.infoform.info_SE_batchNo_le.text())
			self.singleWireClamp['SEOrderNo'] = str(self.infoform.info_SE_orderNo_le.text())
			self.singleWireClamp['SEDate'] = str(self.infoform.info_SE_expiry_date.date().toString("dd MMM yyyy"))
			self.singleWireClamp['HysolBatchNo'] = str(self.infoform.info_hysol_batchNo_le.text())
			self.singleWireClamp['HysolMFGDate'] = str(self.infoform.info_hysol_mfg_expiry_date.date().toString("dd MMM yyyy"))
			self.singleWireClamp['HysolPRODDate'] = str(self.infoform.info_hysol_prod_expiry_date.date().toString("dd MMM yyyy"))
			self.singleWireClamp['7471BatchNo'] = str(self.infoform.info_7471_batchNo_le.text())
			self.singleWireClamp['7471Date'] = str(self.infoform.info_7471_expiry_date.date().toString("dd MMM yyyy"))
			self.singleWireClamp['222BatchNo'] = str(self.infoform.info_222_batchNo_le.text())
			self.singleWireClamp['222Date'] = str(self.infoform.info_222_expiry_date.date().toString("dd MMM yyyy"))
			self.singleWireClamp['VarnishNo'] = str(self.infoform.info_varnish_batchNo_le.text())
			self.singleWireClamp['VarnishDate'] = str(self.infoform.info_varnish_expiry_date.date().toString("dd MMM yyyy"))
			self.singleWireClamp['GluingDoneby'] = str(self.infoform.info_gluing_le.text())
			self.singleWireClamp['GluingStart'] = str(self.infoform.info_gluingDatetime_start_datetime.dateTime().toString("hh:mm:ssap dd MMM yyyy"))
			self.singleWireClamp['GluingEnd'] = str(self.infoform.info_gluingDatetime_end_datetime.dateTime().toString("hh:mm:ssap dd MMM yyyy"))
			self.singleWireClamp['PivotDoneby'] = str(self.infoform.info_pivot_le.text())
			self.singleWireClamp['PivotStart'] = str(self.infoform.info_pivotDatetime_start_datetime.dateTime().toString("hh:mm:ssap dd MMM yyyy"))
			self.singleWireClamp['PivotEnd'] = str(self.infoform.info_pivotDatetime_end_datetime.dateTime().toString("hh:mm:ssap dd MMM yyyy"))
			self.singleWireClamp['FinalDoneby'] = str(self.infoform.info_final_le.text())
			self.singleWireClamp['FinalStart'] = str(self.infoform.info_finalDatetime_start_datetime.dateTime().toString("hh:mm:ssap dd MMM yyyy"))
			self.singleWireClamp['FinalEnd'] = str(self.infoform.info_finalDatetime_end_datetime.dateTime().toString("hh:mm:ssap dd MMM yyyy"))
			self.trayoutput.append(self.singleWireClamp)

			self.WireClampBasic['Job'] = str(self.infoform.info_jobNo_le.text())
			self.WireClampBasic['Quantity'] = str(self.infoform.info_quantity_le.text())
			self.WireClampBasic['RecDate'] = str(self.infoform.info_jobDate_date.date().toString("dd MMM yyyy"))
			self.WireClampBasic['EpoxyLotA'] = str(self.infoform.info_SE_orderNo_le.text())
			self.WireClampBasic['EpoxyLotB'] = str(self.infoform.info_SE_batchNo_le.text())
			self.trayoutputWCAssembly.append(self.WireClampBasic)
			# print self.trayoutputWCAssembly

			self.WireClampDetailed['Job'] = str(self.infoform.info_jobNo_le.text())
			self.WireClampDetailed['EpoxyLotA'] = str(self.infoform.info_SE_orderNo_le.text())
			self.WireClampDetailed['EpoxyLotB'] = str(self.infoform.info_SE_batchNo_le.text())
			self.WireClampDetailed['GluingEmp#'] = str(self.infoform.info_gluing_le.text())
			self.WireClampDetailed['GluingDateTime'] = str(self.infoform.info_gluingDatetime_start_datetime.dateTime().toString("dd MMM yyyy hh:mm:ssap"))
			self.WireClampDetailed['PivotEmp#'] = str(self.infoform.info_pivot_le.text())
			self.WireClampDetailed['PivotDateTime'] = str(self.infoform.info_pivotDatetime_start_datetime.dateTime().toString("dd MMM yyyy hh:mm:ssap"))
			self.WireClampDetailed['FinalEmp#'] = str(self.infoform.info_final_le.text())
			self.WireClampDetailed['FinalDateTime'] = str(self.infoform.info_finalDatetime_start_datetime.dateTime().toString("dd MMM yyyy hh:mm:ssap"))
			self.WireClampDetailed['BimorphEmp#'] = str(self.infoform.info_final_le.text())

			self.dictkeysDetailed = ['wc S/N', 'TorqueValue','','T1 Comment']
			for sub_j in range(3):
				if self.updatebox.update_tray_tw.item(i,sub_j) is not None:
					self.WireClampDetailed[self.dictkeysDetailed[sub_j]] = str(self.updatebox.update_tray_tw.item(i,sub_j).text())
					# print self.updatebox.update_tray_tw.item(i,sub_j).text()
				else:
					self.WireClampDetailed[self.dictkeysDetailed[sub_j]] = "None"
			self.trayoutputWCAssemblyDetailed.append(self.WireClampDetailed)
			# print self.trayoutput
			# print self.trayoutputWCAssembly
			# print self.trayoutputWCAssemblyDetailed
	# def over1000(self):
	# 	i = 0
	# 	while i <1001:
	# 		self.datacollection()
	# 		# print i
	# 		i +=1
# app = QApplication(sys.argv)
# program = form()
# program.show()
# sys.exit(app.exec_())
