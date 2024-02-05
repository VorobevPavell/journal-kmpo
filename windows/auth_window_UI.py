# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(483, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"American Typewriter"])
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(54, 56, 54);\n"
"color: rgb(184, 199, 216);\n"
"role_comboBox::drop-down { border: 0px; }\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 231, 131))
        font1 = QFont()
        font1.setFamilies([u"Party LET"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.label_4.setFont(font1)
        self.label_4.setPixmap(QPixmap(u"../static/\u043b\u043e\u0433\u043e.png"))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 170, 361, 111))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.password_lineEdit = QLineEdit(self.layoutWidget)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.password_lineEdit.sizePolicy().hasHeightForWidth())
        self.password_lineEdit.setSizePolicy(sizePolicy1)
        self.password_lineEdit.setFont(font1)
        self.password_lineEdit.setStyleSheet(u"border: 1px solid rgb(35, 35, 35);;")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password_lineEdit, 1, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.role_comboBox = QComboBox(self.layoutWidget)
        self.role_comboBox.addItem("")
        self.role_comboBox.addItem("")
        self.role_comboBox.addItem("")
        self.role_comboBox.setObjectName(u"role_comboBox")
        sizePolicy.setHeightForWidth(self.role_comboBox.sizePolicy().hasHeightForWidth())
        self.role_comboBox.setSizePolicy(sizePolicy)
        self.role_comboBox.setFont(font1)
        self.role_comboBox.setToolTipDuration(-1)
        self.role_comboBox.setStyleSheet(u"border: 1px solid rgb(35, 35, 35);\n"
"drop-down { border: 0px; }\n"
"")
        self.role_comboBox.setInputMethodHints(Qt.ImhUppercaseOnly)
        self.role_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.role_comboBox.setFrame(False)

        self.gridLayout.addWidget(self.role_comboBox, 2, 0, 1, 3)

        self.login_lineEdit = QLineEdit(self.layoutWidget)
        self.login_lineEdit.setObjectName(u"login_lineEdit")
        sizePolicy1.setHeightForWidth(self.login_lineEdit.sizePolicy().hasHeightForWidth())
        self.login_lineEdit.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(15)
        font2.setBold(False)
        self.login_lineEdit.setFont(font2)
        self.login_lineEdit.setStyleSheet(u"\n"
"    border: 1px solid rgb(35, 35, 35);")
        self.login_lineEdit.setFrame(True)

        self.gridLayout.addWidget(self.login_lineEdit, 0, 2, 1, 1)

        self.sign_in_button = QPushButton(self.centralwidget)
        self.sign_in_button.setObjectName(u"sign_in_button")
        self.sign_in_button.setGeometry(QRect(100, 290, 359, 31))
        sizePolicy.setHeightForWidth(self.sign_in_button.sizePolicy().hasHeightForWidth())
        self.sign_in_button.setSizePolicy(sizePolicy)
        self.sign_in_button.setFont(font1)
        self.sign_in_button.setStyleSheet(u"background-color: rgb(75, 80, 89);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.role_comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u041a\u041c\u041f\u041e ", None))
        self.label_4.setText("")
        self.password_lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.role_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.role_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.role_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442", None))

        self.login_lineEdit.setInputMask("")
        self.login_lineEdit.setText("")
        self.sign_in_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

