# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_teacherData_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(998, 398)
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
        self.label.setPixmap(QPixmap(u"../static/\u043b\u043e\u0433\u043e.png"))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(370, 20, 591, 341))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(4)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 199, 331, 171))
        font1 = QFont()
        font1.setFamilies([u"Party LET"])
        font1.setPointSize(15)
        self.widget.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.teacher_comboBox = QComboBox(self.widget)
        self.teacher_comboBox.setObjectName(u"teacher_comboBox")
        self.teacher_comboBox.setFont(font)

        self.gridLayout.addWidget(self.teacher_comboBox, 1, 1, 1, 1)

        self.select_teacher_pushButton = QPushButton(self.widget)
        self.select_teacher_pushButton.setObjectName(u"select_teacher_pushButton")
        self.select_teacher_pushButton.setFont(font1)
        self.select_teacher_pushButton.setStyleSheet(u"background-color:rgb(75, 80, 89);")

        self.gridLayout.addWidget(self.select_teacher_pushButton, 1, 2, 1, 2)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.subject_comboBox = QComboBox(self.widget)
        self.subject_comboBox.setObjectName(u"subject_comboBox")
        self.subject_comboBox.setFont(font)

        self.gridLayout.addWidget(self.subject_comboBox, 2, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.group_comboBox = QComboBox(self.widget)
        self.group_comboBox.setObjectName(u"group_comboBox")
        self.group_comboBox.setFont(font)

        self.gridLayout.addWidget(self.group_comboBox, 3, 1, 1, 3)

        self.select_subject_pushButton = QPushButton(self.widget)
        self.select_subject_pushButton.setObjectName(u"select_subject_pushButton")
        self.select_subject_pushButton.setFont(font1)
        self.select_subject_pushButton.setStyleSheet(u"background-color:rgb(75, 80, 89);")

        self.gridLayout.addWidget(self.select_subject_pushButton, 2, 2, 1, 2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 4)


        self.verticalLayout.addLayout(self.gridLayout)

        self.res_button = QPushButton(self.widget)
        self.res_button.setObjectName(u"res_button")
        self.res_button.setFont(font1)
        self.res_button.setStyleSheet(u"background-color:rgb(75, 80, 89);")

        self.verticalLayout.addWidget(self.res_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u041c\u041f\u041e \u0416\u0443\u0440\u043d\u0430\u043b[\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440]", None))
        self.label.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0427\u0430\u0441\u043e\u0432", None));
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.select_teacher_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.select_subject_pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044f\u0445", None))
        self.res_button.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
    # retranslateUi

