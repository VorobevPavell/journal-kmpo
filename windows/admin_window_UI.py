# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(475, 308)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(54, 56, 54);\n"
"color: rgb(184, 199, 216);\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 231, 131))
        font = QFont()
        font.setFamilies([u"Party LET"])
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u"../static/\u043b\u043e\u0433\u043e.png"))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(210, 130, 239, 146))
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.get_data_button = QPushButton(self.verticalLayoutWidget)
        self.get_data_button.setObjectName(u"get_data_button")
        self.get_data_button.setFont(font)
        self.get_data_button.setStyleSheet(u"background-color:rgb(75, 80, 89);")

        self.verticalLayout.addWidget(self.get_data_button)

        self.teacher_button = QPushButton(self.verticalLayoutWidget)
        self.teacher_button.setObjectName(u"teacher_button")
        self.teacher_button.setFont(font)
        self.teacher_button.setStyleSheet(u"background-color:rgb(75, 80, 89);")

        self.verticalLayout.addWidget(self.teacher_button)

        self.signUpButton = QPushButton(self.verticalLayoutWidget)
        self.signUpButton.setObjectName(u"signUpButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.signUpButton.sizePolicy().hasHeightForWidth())
        self.signUpButton.setSizePolicy(sizePolicy1)
        self.signUpButton.setFont(font)
        self.signUpButton.setLayoutDirection(Qt.LeftToRight)
        self.signUpButton.setStyleSheet(u"background-color:rgb(75, 80, 89);")

        self.verticalLayout.addWidget(self.signUpButton)

        self.update_database_button = QPushButton(self.verticalLayoutWidget)
        self.update_database_button.setObjectName(u"update_database_button")
        self.update_database_button.setFont(font)
        self.update_database_button.setStyleSheet(u"background-color:rgb(75, 80, 89);")

        self.verticalLayout.addWidget(self.update_database_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u041c\u041f\u041e \u0416\u0443\u0440\u043d\u0430\u043b[\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440]", None))
        self.label.setText("")
        self.get_data_button.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0437\u0430\u043d\u044f\u0442\u0438\u044f\u0445", None))
        self.teacher_button.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044f\u0445", None))
        self.signUpButton.setText(QCoreApplication.translate("Form", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.update_database_button.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0431\u0430\u0437\u0443 \u0434\u0430\u043d\u043d\u044b\u0445", None))
    # retranslateUi

