# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QGridLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(981, 397)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(54, 56, 54);\n"
"color: rgb(184, 199, 216);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 231, 131))
        self.label.setPixmap(QPixmap(u"../static/\u043b\u043e\u0433\u043e.png"))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(275, 20, 691, 361))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(15)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(5)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 160, 186, 201))
        font1 = QFont()
        font1.setFamilies([u"Party LET"])
        font1.setPointSize(15)
        self.layoutWidget.setFont(font1)
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_2.setWordWrap(False)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.date_from = QDateEdit(self.layoutWidget)
        self.date_from.setObjectName(u"date_from")
        self.date_from.setFont(font)
        self.date_from.setDateTime(QDateTime(QDate(2024, 1, 12), QTime(0, 0, 0)))
        self.date_from.setCalendarPopup(True)
        self.date_from.setDate(QDate(2024, 1, 12))

        self.gridLayout.addWidget(self.date_from, 1, 2, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.date_to = QDateEdit(self.layoutWidget)
        self.date_to.setObjectName(u"date_to")
        self.date_to.setFont(font)
        self.date_to.setDateTime(QDateTime(QDate(2024, 1, 15), QTime(0, 0, 0)))
        self.date_to.setCurrentSection(QDateTimeEdit.DaySection)
        self.date_to.setCalendarPopup(True)
        self.date_to.setDate(QDate(2024, 1, 15))

        self.gridLayout.addWidget(self.date_to, 2, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)

        self.gridLayout.addWidget(self.comboBox, 3, 2, 1, 1)

        self.res_button = QPushButton(self.layoutWidget)
        self.res_button.setObjectName(u"res_button")
        self.res_button.setFont(font1)
        self.res_button.setStyleSheet(u"background-color: rgb(75, 80, 89);")

        self.gridLayout.addWidget(self.res_button, 4, 1, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u041c\u041f\u041e \u0416\u0443\u0440\u043d\u0430\u043b[\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440]", None))
        self.label.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0440\u044b", None));
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u0437\u0430\u043d\u044f\u0442\u0438\u044f\u0445", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041e\u0442", None))
        self.date_from.setDisplayFormat(QCoreApplication.translate("Form", u"d.M.yyyy", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041f\u043e", None))
        self.date_to.setDisplayFormat(QCoreApplication.translate("Form", u"d.M.yyyy", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.res_button.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
    # retranslateUi

