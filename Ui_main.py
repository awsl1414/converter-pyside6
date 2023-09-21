# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(398, 278)
        font = QFont()
        font.setPointSize(16)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.originDataLable = QLabel(Form)
        self.originDataLable.setObjectName(u"originDataLable")
        self.originDataLable.setMinimumSize(QSize(100, 30))
        self.originDataLable.setFont(font)
        self.originDataLable.setStyleSheet(u"color:rgb(139, 139, 139)")

        self.gridLayout.addWidget(self.originDataLable, 0, 0, 1, 1)

        self.twoInputLineEdit = QLineEdit(Form)
        self.twoInputLineEdit.setObjectName(u"twoInputLineEdit")
        self.twoInputLineEdit.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.twoInputLineEdit, 4, 0, 1, 1)

        self.dataTypeComboBox = QComboBox(Form)
        self.dataTypeComboBox.setObjectName(u"dataTypeComboBox")

        self.gridLayout.addWidget(self.dataTypeComboBox, 2, 0, 1, 2)

        self.oneComboBox = QComboBox(Form)
        self.oneComboBox.setObjectName(u"oneComboBox")
        self.oneComboBox.setMinimumSize(QSize(180, 40))

        self.gridLayout.addWidget(self.oneComboBox, 3, 1, 1, 1)

        self.transDataLable = QLabel(Form)
        self.transDataLable.setObjectName(u"transDataLable")
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.transDataLable.setFont(font1)

        self.gridLayout.addWidget(self.transDataLable, 1, 0, 1, 2)

        self.twoComboBox = QComboBox(Form)
        self.twoComboBox.setObjectName(u"twoComboBox")
        self.twoComboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.twoComboBox, 4, 1, 1, 1)

        self.oneInputLineEdit = QLineEdit(Form)
        self.oneInputLineEdit.setObjectName(u"oneInputLineEdit")
        self.oneInputLineEdit.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.oneInputLineEdit, 3, 0, 1, 1)

        self.calcBtn = QPushButton(Form)
        self.calcBtn.setObjectName(u"calcBtn")

        self.gridLayout.addWidget(self.calcBtn, 5, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8fdb\u5236\u8f6c\u6362\u5668", None))
        self.originDataLable.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.transDataLable.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.calcBtn.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
    # retranslateUi

