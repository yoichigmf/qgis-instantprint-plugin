# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printdialog.ui'
#
# Created: Sat Jun 24 14:57:10 2017
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_InstantPrintDialog(object):
    def setupUi(self, InstantPrintDialog):
        InstantPrintDialog.setObjectName(_fromUtf8("InstantPrintDialog"))
        InstantPrintDialog.resize(987, 524)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("printer"))
        InstantPrintDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(InstantPrintDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox_composers = QtGui.QComboBox(InstantPrintDialog)
        self.comboBox_composers.setObjectName(_fromUtf8("comboBox_composers"))
        self.gridLayout.addWidget(self.comboBox_composers, 0, 1, 1, 1)
        self.label_fileformat = QtGui.QLabel(InstantPrintDialog)
        self.label_fileformat.setObjectName(_fromUtf8("label_fileformat"))
        self.gridLayout.addWidget(self.label_fileformat, 3, 0, 1, 1)
        self.label_composers = QtGui.QLabel(InstantPrintDialog)
        self.label_composers.setObjectName(_fromUtf8("label_composers"))
        self.gridLayout.addWidget(self.label_composers, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(InstantPrintDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)
        self.spinBoxScale = QtGui.QSpinBox(InstantPrintDialog)
        self.spinBoxScale.setPrefix(_fromUtf8("1:"))
        self.spinBoxScale.setMinimum(1)
        self.spinBoxScale.setMaximum(1000000000)
        self.spinBoxScale.setObjectName(_fromUtf8("spinBoxScale"))
        self.gridLayout.addWidget(self.spinBoxScale, 2, 1, 1, 1)
        self.comboBox_fileformat = QtGui.QComboBox(InstantPrintDialog)
        self.comboBox_fileformat.setObjectName(_fromUtf8("comboBox_fileformat"))
        self.gridLayout.addWidget(self.comboBox_fileformat, 3, 1, 1, 1)
        self.label = QtGui.QLabel(InstantPrintDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 200, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(InstantPrintDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 885, 381))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 5, 1, 1, 1)

        self.retranslateUi(InstantPrintDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), InstantPrintDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), InstantPrintDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InstantPrintDialog)

    def retranslateUi(self, InstantPrintDialog):
        InstantPrintDialog.setWindowTitle(_translate("InstantPrintDialog", "Instant Print", None))
        self.label_fileformat.setText(_translate("InstantPrintDialog", "File format:", None))
        self.label_composers.setText(_translate("InstantPrintDialog", "Composer:", None))
        self.label.setText(_translate("InstantPrintDialog", "Scale:", None))

