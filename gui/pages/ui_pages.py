# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesEPqoIq.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(924, 541)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_Principal = QFrame(self.page_1)
        self.frame_Principal.setObjectName(u"frame_Principal")
        self.frame_Principal.setMinimumSize(QSize(500, 100))
        self.frame_Principal.setMaximumSize(QSize(500, 100))
        self.frame_Principal.setFrameShape(QFrame.StyledPanel)
        self.frame_Principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_Principal)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_ola = QLabel(self.frame_Principal)
        self.label_ola.setObjectName(u"label_ola")
        self.label_ola.setMinimumSize(QSize(0, 50))
        self.label_ola.setMaximumSize(QSize(16777215, 50))
        self.label_ola.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_ola)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.frame_Principal)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.psb_AlterarNome = QPushButton(self.frame_Principal)
        self.psb_AlterarNome.setObjectName(u"psb_AlterarNome")
        self.psb_AlterarNome.setMinimumSize(QSize(120, 36))
        self.psb_AlterarNome.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setBold(True)
        self.psb_AlterarNome.setFont(font1)
        self.psb_AlterarNome.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 133, 200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 0, 127)	\n"
"}")

        self.gridLayout.addWidget(self.psb_AlterarNome, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame_Principal, 0, Qt.AlignHCenter)

        application_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        application_pages.addWidget(self.page_3)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_ola.setText(QCoreApplication.translate("application_pages", u"Ol\u00e1", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"Escreva o seu nome", None))
        self.psb_AlterarNome.setText(QCoreApplication.translate("application_pages", u"Alterar Texto", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Pagina 2", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Pagina 3", None))
    # retranslateUi

