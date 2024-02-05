# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_up_window.ui'
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
        MainWindow.resize(475, 308)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Optima"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(54, 56, 54);\n"
"color: rgb(184, 199, 216);\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 231, 131))
        self.label_4.setPixmap(QPixmap(u"../static/\u043b\u043e\u0433\u043e.png"))
        self.sign_up_button = QPushButton(self.centralwidget)
        self.sign_up_button.setObjectName(u"sign_up_button")
        self.sign_up_button.setGeometry(QRect(200, 250, 121, 27))
        font1 = QFont()
        font1.setFamilies([u"Party LET"])
        font1.setPointSize(15)
        self.sign_up_button.setFont(font1)
        self.sign_up_button.setStyleSheet(u"background-color: rgb(75, 80, 89);")
        self.delete_user_button = QPushButton(self.centralwidget)
        self.delete_user_button.setObjectName(u"delete_user_button")
        self.delete_user_button.setGeometry(QRect(330, 250, 121, 27))
        self.delete_user_button.setFont(font1)
        self.delete_user_button.setStyleSheet(u"background-color: rgb(75, 80, 89);")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(200, 150, 251, 54))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.password_lineEdit = QLineEdit(self.widget)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setStyleSheet(u"    border: 1px solid rgb(35, 35, 35);")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password_lineEdit, 1, 2, 1, 1)

        self.login_lineEdit = QLineEdit(self.widget)
        self.login_lineEdit.setObjectName(u"login_lineEdit")
        self.login_lineEdit.setStyleSheet(u"    border: 1px solid rgb(35, 35, 35);")

        self.gridLayout.addWidget(self.login_lineEdit, 0, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.role_comboBox = QComboBox(self.centralwidget)
        self.role_comboBox.addItem("")
        self.role_comboBox.addItem("")
        self.role_comboBox.addItem("")
        self.role_comboBox.setObjectName(u"role_comboBox")
        self.role_comboBox.setGeometry(QRect(200, 210, 251, 31))
        self.role_comboBox.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u041c\u041f\u041e \u0416\u0443\u0440\u043d\u0430\u043b[\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440]", None))
        self.label_4.setText("")
        self.sign_up_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.delete_user_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.role_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.role_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.role_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442", None))

    # retranslateUi

