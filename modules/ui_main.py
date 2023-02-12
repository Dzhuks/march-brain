# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainGwPyFS.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 732)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.styleSheet)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.btn_about_cancer = QPushButton(self.topMenu)
        self.btn_about_cancer.setObjectName(u"btn_about_cancer")
        self.btn_about_cancer.setGeometry(QRect(0, 50, 60, 45))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_about_cancer.sizePolicy().hasHeightForWidth())
        self.btn_about_cancer.setSizePolicy(sizePolicy)
        self.btn_about_cancer.setMinimumSize(QSize(0, 45))
        self.btn_about_cancer.setFont(font)
        self.btn_about_cancer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_about_cancer.setLayoutDirection(Qt.LeftToRight)
        self.btn_about_cancer.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-pie.png);")
        self.btn_detection = QPushButton(self.topMenu)
        self.btn_detection.setObjectName(u"btn_detection")
        self.btn_detection.setGeometry(QRect(0, 0, 60, 45))
        sizePolicy.setHeightForWidth(self.btn_detection.sizePolicy().hasHeightForWidth())
        self.btn_detection.setSizePolicy(sizePolicy)
        self.btn_detection.setMinimumSize(QSize(0, 45))
        self.btn_detection.setFont(font)
        self.btn_detection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_detection.setLayoutDirection(Qt.LeftToRight)
        self.btn_detection.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);")
        self.btn_history = QPushButton(self.topMenu)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setGeometry(QRect(0, 100, 60, 45))
        sizePolicy.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy)
        self.btn_history.setMinimumSize(QSize(0, 45))
        self.btn_history.setFont(font)
        self.btn_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_history.setLayoutDirection(Qt.LeftToRight)
        self.btn_history.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-history.png);")

        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFont(font)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"")
        self.detection = QWidget()
        self.detection.setObjectName(u"detection")
        self.detection.setStyleSheet(u"")
        self.img_brain = QLabel(self.detection)
        self.img_brain.setObjectName(u"img_brain")
        self.img_brain.setGeometry(QRect(10, 10, 400, 400))
        self.btn_evaluate = QPushButton(self.detection)
        self.btn_evaluate.setObjectName(u"btn_evaluate")
        self.btn_evaluate.setGeometry(QRect(220, 480, 191, 121))
        font4 = QFont()
        font4.setBold(True)
        font4.setItalic(False)
        self.btn_evaluate.setFont(font4)
        self.btn_evaluate.setStyleSheet(u"border-radius: 25px; background-image: url(:/images/images/images/detect_btn.png); font-size: 19px; font-weight: bold; background-color: #DBA03A;")
        self.btn_load = QPushButton(self.detection)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(10, 480, 195, 121))
        self.btn_load.setStyleSheet(u"border-radius: 25px; background: url(:/images/images/images/load_btn.png);  font-size: 19px; font-weight: bold; background-color: #7dc68f;")
        self.label_diagnosis = QLabel(self.detection)
        self.label_diagnosis.setObjectName(u"label_diagnosis")
        self.label_diagnosis.setGeometry(QRect(470, -20, 641, 61))
        self.label_diagnosis.setFont(font4)
        self.label_diagnosis.setStyleSheet(u"font-weight: bold; font-size: 30px;")
        self.label_diagnosis.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.detection)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(460, 90, 661, 511))
        self.label_description.setStyleSheet(u"font-size: 17px;")
        self.label_description.setLineWidth(1)
        self.label_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_description.setWordWrap(True)
        self.label_description.setMargin(0)
        self.label_warning = QLabel(self.detection)
        self.label_warning.setObjectName(u"label_warning")
        self.label_warning.setGeometry(QRect(450, 40, 711, 31))
        self.label_warning.setStyleSheet(u"font-size: 26px; color: #FF0032; font-weight: bold")
        self.input_name = QLineEdit(self.detection)
        self.input_name.setObjectName(u"input_name")
        self.input_name.setGeometry(QRect(0, 431, 411, 31))
        self.input_name.setFont(font)
        self.stackedWidget.addWidget(self.detection)
        self.about_cancer = QWidget()
        self.about_cancer.setObjectName(u"about_cancer")
        self.about_cancer.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.label_2 = QLabel(self.about_cancer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 281, 51))
        self.label_2.setStyleSheet(u"font-size: 40px;\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.line = QFrame(self.about_cancer)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(220, 60, 3, 550))
        self.line.setStyleSheet(u"background-color: rgb(189, 147, 249)")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.btn_page1 = QPushButton(self.about_cancer)
        self.btn_page1.setObjectName(u"btn_page1")
        self.btn_page1.setGeometry(QRect(0, 110, 211, 51))
        self.btn_page1.setFont(font4)
        self.btn_page1.setStyleSheet(u"font-size: 16px;color: #EEEEEE; border-radius: 15px; font-weight: bold;")
        self.btn_page2 = QPushButton(self.about_cancer)
        self.btn_page2.setObjectName(u"btn_page2")
        self.btn_page2.setGeometry(QRect(0, 170, 211, 51))
        self.btn_page2.setFont(font4)
        self.btn_page2.setStyleSheet(u"font-size: 16px;color: #EEEEEE; border-radius: 15px; font-weight: bold;")
        self.btn_page3 = QPushButton(self.about_cancer)
        self.btn_page3.setObjectName(u"btn_page3")
        self.btn_page3.setGeometry(QRect(0, 230, 211, 51))
        self.btn_page3.setFont(font4)
        self.btn_page3.setStyleSheet(u"font-size: 16px;color: #EEEEEE; border-radius: 15px; font-weight: bold;")
        self.btn_page4 = QPushButton(self.about_cancer)
        self.btn_page4.setObjectName(u"btn_page4")
        self.btn_page4.setGeometry(QRect(0, 290, 211, 51))
        self.btn_page4.setFont(font4)
        self.btn_page4.setStyleSheet(u"font-size: 16px;color: #EEEEEE; border-radius: 15px; font-weight: bold;")
        self.stackedWidget_2 = QStackedWidget(self.about_cancer)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(230, 20, 941, 591))
        self.stackedWidget_2.setStyleSheet(u"background-color: transparent;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 0, 481, 41))
        self.label.setStyleSheet(u"font-size: 25px;")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 40, 941, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 939, 549))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 0, 481, 41))
        self.label_3.setStyleSheet(u"font-size: 25px;")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.scrollArea_2 = QScrollArea(self.page_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(10, 40, 931, 551))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 929, 549))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_9.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_9)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 0, 481, 41))
        self.label_4.setStyleSheet(u"font-size: 25px;")
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.scrollArea_3 = QScrollArea(self.page_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 40, 941, 551))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 931, 674))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"margin-bottom: 30px;")
        self.label_8.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_8)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"margin-bottom: 30px;")
        self.label_10.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_10)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_11)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 0, 481, 41))
        self.label_5.setStyleSheet(u"font-size: 25px;")
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.scrollArea_4 = QScrollArea(self.page_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(0, 40, 941, 551))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 939, 549))
        self.label_12 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 941, 501))
        self.label_12.setWordWrap(True)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.stackedWidget_2.addWidget(self.page_4)
        self.stackedWidget.addWidget(self.about_cancer)
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.title = QLabel(self.history)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, -10, 251, 41))
        self.title.setStyleSheet(u"font-size: 30px;\n"
"")
        self.title.setAlignment(Qt.AlignCenter)
        self.spinBox = QSpinBox(self.history)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(240, 70, 81, 41))
        self.spinBox.setStyleSheet(u"background-color: rgb(40, 44, 52); font-size: 16px;")
        self.spinBox.setMinimum(1)
        self.spinBox.setValue(15)
        self.label_column = QLabel(self.history)
        self.label_column.setObjectName(u"label_column")
        self.label_column.setGeometry(QRect(20, 70, 211, 51))
        self.label_column.setStyleSheet(u"font-size: 24px;")
        self.tableWidget = QTableWidget(self.history)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 130, 511, 481))
        self.tableWidget.setStyleSheet(u"font-size: 19px;\n"
"")
        self.label_stat = QLabel(self.history)
        self.label_stat.setObjectName(u"label_stat")
        self.label_stat.setGeometry(QRect(560, 0, 201, 51))
        self.label_stat.setStyleSheet(u"font-size: 24px;\n"
"color: rgb(0, 255, 127)")
        self.stat = QLabel(self.history)
        self.stat.setObjectName(u"stat")
        self.stat.setGeometry(QRect(560, 60, 581, 141))
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        self.stat.setFont(font5)
        self.stat.setStyleSheet(u"font-size: 16px;\n"
"")
        self.stat.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_diagram = QLabel(self.history)
        self.label_diagram.setObjectName(u"label_diagram")
        self.label_diagram.setGeometry(QRect(540, 220, 631, 391))
        self.label_diagram.setFont(font)
        self.line_2 = QFrame(self.history)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(530, -10, 3, 636))
        self.line_2.setStyleSheet(u"background-color: rgb(189, 147, 249)")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.history)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(533, 210, 655, 3))
        self.line_3.setStyleSheet(u"background-color: rgb(189, 147, 249)")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.history)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.gridLayout.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Nazvanie", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Brain Tumor detector", None))
        self.btn_about_cancer.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.btn_detection.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Tumbrainor - \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u0438\u044f \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u043c\u043e\u0437\u0433\u0430", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.img_brain.setText("")
        self.btn_evaluate.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u0430\u0440\u0443\u0436\u0438\u0442\u044c\n"
"\u043e\u043f\u0443\u0445\u043e\u043b\u044c", None))
        self.btn_load.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c\n"
"\u0441\u043d\u0438\u043c\u043e\u043a \u041c\u0420\u0422", None))
        self.label_diagnosis.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043d\u0438\u043c\u043e\u043a \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443", None))
        self.label_description.setText("")
        self.label_warning.setText("")
        self.input_name.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0443\u0445\u043e\u043b\u044c \u043c\u043e\u0437\u0433\u0430", None))
        self.btn_page1.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.btn_page2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u043f\u0442\u043e\u043c\u044b", None))
        self.btn_page3.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0447\u0435\u043d\u0438\u0435 \u0438 \u043f\u0440\u043e\u0444\u0438\u043b\u0430\u043a\u0442\u0438\u043a\u0430", None))
        self.btn_page4.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b \u0440\u0438\u0441\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a name=\"docs-internal-guid-a91628e7-7fff-8216-f2aa-3f68672a8398\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">\u041e</span><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">\u043f\u0443\u0445\u043e\u043b\u044c \u043c\u043e\u0437\u0433\u0430</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> - \u044d\u0442\u043e \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0438\u043b\u0438 \u0440\u043e\u0441\u0442 \u0430\u043d\u043e\u043c\u0430\u043b\u044c\u043d\u044b\u0445 \u043a\u043b\u0435\u0442\u043e\u043a \u0432 \u0432\u0430\u0448\u0435\u043c \u043c\u043e\u0437\u0433\u0435.</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 \u043c\u043d\u043e\u0436\u0435\u0441\u0442"
                        "\u0432\u043e \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0442\u0438\u043f\u043e\u0432 \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u043c\u043e\u0437\u0433\u0430. \u041d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043e\u043f\u0443\u0445\u043e\u043b\u0438 \u043c\u043e\u0437\u0433\u0430 \u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u043d\u0435\u0440\u0430\u043a\u043e\u0432\u044b\u043c\u0438 (</span><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">\u0434\u043e\u0431\u0440\u043e\u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u043c\u0438</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">), \u0430 \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 -\u0440\u0430\u043a\u043e\u0432\u044b\u043c\u0438 (</span><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">\u0437\u043b\u043e\u043a\u0430"
                        "\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u043c\u0438</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">).</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u041e\u043f\u0443\u0445\u043e\u043b\u0438 \u043c\u043e\u0437\u0433\u0430 \u043c\u043e\u0433\u0443\u0442 \u0437\u0430\u0440\u043e\u0436\u0434\u0430\u0442\u044c\u0441\u044f \u0432 \u043c\u043e\u0437\u0433\u0435 (\u043f\u0435\u0440\u0432\u0438\u0447\u043d\u044b\u0435 \u043e\u043f\u0443\u0445\u043e\u043b\u0438 \u043c\u043e\u0437\u0433\u0430), \u0438\u043b\u0438 \u0440\u0430\u043a \u043c\u043e\u0436\u0435\u0442 \u0437\u0430\u0440\u043e\u0434\u0438\u0442\u044c\u0441\u044f \u0432 \u0434\u0440\u0443\u0433\u0438\u0445 \u0447\u0430\u0441\u0442\u044f\u0445 \u0442\u0435\u043b\u0430 \u0438 \u0440\u0430\u0441\u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0438\u0442\u044c\u0441\u044f \u043d\u0430 \u043c\u043e\u0437\u0433 \u0432 \u0432\u0438"
                        "\u0434\u0435 \u0432\u0442\u043e\u0440\u0438\u0447\u043d\u044b\u0445 (\u043c\u0435\u0442\u0430\u0441\u0442\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445) \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u043c\u043e\u0437\u0433\u0430.</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0440\u043e\u0441\u0442\u0430 \u043e\u043f\u0443\u0445\u043e\u043b\u0438 \u043c\u043e\u0437\u0433\u0430 \u043c\u043e\u0436\u0435\u0442 \u0441\u0438\u043b\u044c\u043d\u043e \u0432\u0430\u0440\u044c\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f. \u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0440\u043e\u0441\u0442\u0430, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043e\u043f\u0443\u0445\u043e\u043b\u0438 \u043c\u043e\u0437\u0433\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u044e\u0442, \u043a\u0430\u043a \u043e\u043d\u0430 \u043f"
                        "\u043e\u0432\u043b\u0438\u044f\u0435\u0442 \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443 \u0432\u0430\u0448\u0435\u0439 \u043d\u0435\u0440\u0432\u043d\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b.</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043b\u0435\u0447\u0435\u043d\u0438\u044f \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u043c\u043e\u0437\u0433\u0430 \u0437\u0430\u0432\u0438\u0441\u044f\u0442 \u043e\u0442 </span><span style=\" font-family:'Arial'; font-size:14pt; font-style:italic; color:#eeeeee; background-color:transparent;\">\u0442\u0438\u043f\u0430 \u043e\u043f\u0443\u0445\u043e\u043b\u0438 \u043c\u043e\u0437\u0433\u0430</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">, \u0430 \u0442\u0430\u043a\u0436\u0435 \u043e\u0442 \u0435\u0435 </span><span style=\" font-family:'Arial'; font-size:14pt; font-style:italic; color:#eeeeee; background-color:transparent;\">\u0440\u0430\u0437\u043c\u0435\u0440\u0430</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> \u0438 "
                        "</span><span style=\" font-family:'Arial'; font-size:14pt; font-style:italic; color:#eeeeee; background-color:transparent;\">\u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">.</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u041a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u043f\u043e \u0441\u0442\u0435\u043f\u0435\u043d\u0438 \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f \u0431\u043e\u043b\u0435\u0437\u043d\u0438:</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">- I \u0441\u0442\u0435\u043f\u0435\u043d\u044c \u2014 \u043d\u043e\u0432\u043e\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f, \u043d\u0435 \u0438\u043c\u0435\u044e\u0449\u0438\u0435 \u043f\u0440\u0438"
                        "\u0437\u043d\u0430\u043a\u043e\u0432 \u0437\u043b\u043e\u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0440\u0430\u0441\u0442\u0443\u0442 \u043c\u0435\u0434\u043b\u0435\u043d\u043d\u043e.</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">- II \u0441\u0442\u0435\u043f\u0435\u043d\u044c \u2014 \u043c\u0435\u0434\u043b\u0435\u043d\u043d\u044b\u0439 \u0440\u043e\u0441\u0442, \u043d\u043e \u043d\u043e\u0432\u043e\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0443\u0436\u0435 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442 \u043f\u0440\u0438\u043e\u0431\u0440\u0435\u0442\u0430\u0442\u044c \u0437\u043b\u043e\u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u044c, \u043a\u043b\u0435\u0442\u043a\u0438 \u0441\u0442\u0430\u043d\u043e\u0432\u044f\u0442\u0441\u044f \u0430\u0442\u0438\u043f\u0438\u0447\u043d\u044b\u043c\u0438.</sp"
                        "an></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">- III \u0441\u0442\u0435\u043f\u0435\u043d\u044c \u2014 \u0437\u043b\u043e\u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f, \u0431\u044b\u0441\u0442\u0440\u043e \u0440\u0430\u0441\u0442\u0443\u0442.</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">- IV \u0441\u0442\u0435\u043f\u0435\u043d\u044c \u2014 \u043e\u0447\u0435\u043d\u044c \u0431\u044b\u0441\u0442\u0440\u044b\u0439 \u0440\u043e\u0441\u0442 \u0438 \u0430\u0433\u0440\u0435\u0441\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u044c \u043d\u043e\u0432\u043e\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f, \u043f\u0440\u043e\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u0435 \u0432 \u0441\u043e\u0441\u0435\u0434\u043d\u0438\u0435 \u043e\u0442\u0434\u0435\u043b\u044b \u043c\u043e\u0437\u0433"
                        "\u0430, \u0441\u0436\u0430\u0442\u0438\u0435 \u0435\u0433\u043e \u0447\u0430\u0441\u0442\u0435\u0439.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u043f\u0442\u043e\u043c\u044b", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a name=\"docs-internal-guid-8bc89969-7fff-15b4-32ed-81a31a3dd331\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u041f\u0440\u0438\u0437\u043d\u0430\u043a\u0438 \u0438 \u0441\u0438\u043c\u043f\u0442\u043e\u043c\u044b \u043e\u043f\u0443\u0445\u043e\u043b\u0438 \u043c\u043e\u0437\u0433\u0430 \u0441\u0438\u043b\u044c\u043d\u043e \u0432\u0430\u0440\u044c\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u0438 \u0437\u0430\u0432\u0438\u0441\u044f\u0442 \u043e\u0442 \u0440\u0430\u0437\u043c\u0435\u0440\u0430, \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0438 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438 \u0440\u043e\u0441\u0442\u0430 \u043e\u043f\u0443\u0445\u043e\u043b\u0438 \u043c\u043e\u0437\u0433\u0430. </span><span style=\" font-family:'Arial'; font-size:14pt; font-weig"
                        "ht:700; color:#eeeeee; background-color:transparent;\">\u0417\u0430\u043f\u0438\u0448\u0438\u0442\u0435\u0441\u044c \u043d\u0430 \u043f\u0440\u0438\u0435\u043c \u043a \u0432\u0440\u0430\u0447\u0443</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">, \u0435\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u043f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u044b\u0435 \u043f\u0440\u0438\u0437\u043d\u0430\u043a\u0438 \u0438 \u0441\u0438\u043c\u043f\u0442\u043e\u043c\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0432\u0430\u0441 \u0431\u0435\u0441\u043f\u043e\u043a\u043e\u044f\u0442.</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u041e\u0431\u0449\u0438\u0435 \u043f\u0440\u0438\u0437\u043d\u0430\u043a\u0438 \u0438 \u0441\u0438\u043c\u043f\u0442\u043e\u043c\u044b, \u0432\u044b\u0437\u0432\u0430\u043d\u043d\u044b\u0435 \u043e\u043f"
                        "\u0443\u0445\u043e\u043b\u044f\u043c\u0438 \u0433\u043e\u043b\u043e\u0432\u043d\u043e\u0433\u043e \u043c\u043e\u0437\u0433\u0430, \u043c\u043e\u0433\u0443\u0442 \u0432\u043a\u043b\u044e\u0447\u0430\u0442\u044c:</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">-</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> \u0413\u043e\u043b\u043e\u0432\u043d\u044b\u0435 \u0431\u043e\u043b\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u043e\u0441\u0442\u0435\u043f\u0435\u043d\u043d\u043e \u0441\u0442\u0430\u043d\u043e\u0432\u044f\u0442\u0441\u044f \u0431\u043e\u043b\u0435\u0435 \u0447\u0430\u0441\u0442\u044b\u043c\u0438 \u0438 \u0431\u043e\u043b\u0435\u0435 \u0441\u0438\u043b\u044c\u043d\u044b\u043c\u0438</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeee"
                        "ee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">-</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> \u041d\u0435\u043e\u0431\u044a\u044f\u0441\u043d\u0438\u043c\u0430\u044f \u0442\u043e\u0448\u043d\u043e\u0442\u0430 \u0438\u043b\u0438 \u0440\u0432\u043e\u0442\u0430</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">-</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u044b \u0441\u043e \u0437\u0440\u0435\u043d\u0438\u0435\u043c, \u0442\u0430\u043a\u0438\u0435 \u043a\u0430\u043a \u043f\u043e\u043c\u0443\u0442\u043d\u0435\u043d\u0438\u0435 \u0437\u0440\u0435\u043d\u0438\u044f, \u0434"
                        "\u0432\u043e\u0435\u043d\u0438\u0435 \u0432 \u0433\u043b\u0430\u0437\u0430\u0445 \u0438\u043b\u0438 \u043f\u043e\u0442\u0435\u0440\u044f \u043f\u0435\u0440\u0438\u0444\u0435\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0437\u0440\u0435\u043d\u0438\u044f</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">- </span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u041f\u043e\u0441\u0442\u0435\u043f\u0435\u043d\u043d\u0430\u044f \u043f\u043e\u0442\u0435\u0440\u044f \u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0438\u043b\u0438 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u0432 \u0440\u0443\u043a\u0435 \u0438\u043b\u0438 \u043d\u043e\u0433\u0435</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee"
                        "; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">-</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> \u0422\u0440\u0443\u0434\u043d\u043e\u0441\u0442\u0438 \u0441 \u0440\u0430\u0432\u043d\u043e\u0432\u0435\u0441\u0438\u0435\u043c \u0438 \u0440\u0435\u0447\u044c\u044e</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">-</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> \u0427\u0443\u0432\u0441\u0442\u0432\u043e \u0441\u0438\u043b\u044c\u043d\u043e\u0439 \u0443\u0441\u0442\u0430\u043b\u043e\u0441\u0442\u0438</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span st"
                        "yle=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">-</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> \u041d\u0435\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u043f\u0440\u043e\u0441\u0442\u044b\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">-</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> \u0421\u0443\u0434\u043e\u0440\u043e\u0433\u0438, \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e \u0443 \u0442\u0435\u0445, \u043a\u0442\u043e \u043d\u0435 \u0441\u0442\u0440\u0430\u0434\u0430\u0435\u0442 \u0441\u0443\u0434\u043e\u0440\u043e\u0433\u0430"
                        "\u043c\u0438 \u0432 \u043f\u0440\u043e\u0448\u043b\u043e\u043c</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">-</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"> \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u044b \u0441\u043e \u0441\u043b\u0443\u0445\u043e\u043c</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0447\u0435\u043d\u0438\u0435 \u0438 \u043f\u0440\u043e\u0444\u0438\u043b\u0430\u043a\u0442\u0438\u043a\u0430", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a name=\"docs-internal-guid-58b891a1-7fff-3574-964c-449befa7400f\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u041b\u0435\u0447\u0435\u043d\u0438\u0435 \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u0433\u043e\u043b\u043e\u0432\u043d\u043e\u0433\u043e \u043c\u043e\u0437\u0433\u0430, \u043a\u0430\u043a \u0438 \u0432\u0441\u0435\u0445 \u043e\u043d\u043a\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u0439, \u2014 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441\u043d\u043e\u0435 \u0438 \u0434\u043e\u0432\u043e\u043b\u044c\u043d\u043e \u0434\u043e\u0440\u043e\u0433\u043e\u0441\u0442\u043e\u044f\u0449\u0435\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435. \u0412\u0441\u0435 \u043c\u0435\u0440"
                        "\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f, \u043f\u0440\u043e\u0432\u043e\u0434\u0438\u043c\u044b\u0435 \u0432 \u0445\u043e\u0434\u0435 \u043a\u0443\u0440\u0441\u0430 \u043b\u0435\u0447\u0435\u043d\u0438\u044f, \u043c\u043e\u0436\u043d\u043e \u0440\u0430\u0437\u0431\u0438\u0442\u044c \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 \u0433\u0440\u0443\u043f\u043f\u044b:</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u0421\u0438\u043c\u043f\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0442\u0435\u0440\u0430\u043f\u0438\u044f;</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u0425\u0438\u0440\u0443\u0440\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043b\u0435\u0447\u0435\u043d\u0438\u0435;</span></p><p><span style=\" font-family"
                        ":'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u041b\u0443\u0447\u0435\u0432\u0430\u044f \u0442\u0435\u0440\u0430\u043f\u0438\u044f;</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u0420\u0430\u0434\u0438\u043e\u0445\u0438\u0440\u0443\u0440\u0433\u0438\u044f;</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u0425\u0438\u043c\u0438\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u044f;</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u041a\u0440\u0438\u043e\u0445\u0438\u0440\u0443\u0440\u0433\u0438\u044f;</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:tran"
                        "sparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u041c\u0435\u0442\u043e\u0434\u044b \u043a\u043e\u043c\u0431\u0438\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e \u043b\u0435\u0447\u0435\u043d\u0438\u044f (\u043b\u0443\u0447\u0435\u0432\u0430\u044f \u0438 \u0445\u0438\u043c\u0438\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u044f);</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a name=\"docs-internal-guid-4bd46297-7fff-e927-960e-baf51b1845fe\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u0427\u0430\u0441\u0442\u043e \u0438\u043c\u0435\u043d\u043d\u043e \u043b\u0443\u0447\u0435\u0432\u0430\u044f \u0442\u0435\u0440\u0430\u043f\u0438\u044f \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u043c \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u043b\u0435\u0447\u0435\u043d\u0438\u044f \u0434\u043e \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u0438 \u043f\u043e\u0441\u043b\u0435 \u043d\u0435\u0435, \u0430 \u0438\u043d\u043e\u0433\u0434\u0430 \u043e\u043d\u0430 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0441\u0430\u043c\u043e\u0441\u0442\u043e\u044f\u0442\u0435\u043b\u044c\u043d\u044b\u043c \u0441"
                        "\u0440\u0435\u0434\u0441\u0442\u0432\u043e\u043c \u043b\u0435\u0447\u0435\u043d\u0438\u044f, \u043a\u043e\u0433\u0434\u0430 \u0438\u0441\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u043e\u043f\u0443\u0445\u043e\u043b\u0438 \u0433\u043e\u043b\u043e\u0432\u043d\u043e\u0433\u043e \u043c\u043e\u0437\u0433\u0430 \u043d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e. \u0412 \u044d\u0442\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435 \u0432\u0440\u0430\u0447\u0430\u043c \u0443\u0434\u0430\u0435\u0442\u0441\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0440\u043e\u0441\u0442 \u043d\u043e\u0432\u043e\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f.</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a name=\"docs-internal-guid-d4a20399-7fff-5c6b-5cae-77c342244ff8\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u0427\u0442\u043e\u0431\u044b \u043f\u0440\u0435\u0434\u043e\u0442\u0432\u0440\u0430\u0442\u0438\u0442\u044c \u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u0433\u043e\u043b\u043e\u0432\u043d\u043e\u0433\u043e \u043c\u043e\u0437\u0433\u0430, \u043d\u0430\u0434\u043e:</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0441\u043f\u0430\u0442\u044c \u0438 \u043e\u0442\u0434\u044b\u0445\u0430\u0442\u044c;</span></p><p><span style=\" font-family:'Arial'; font-s"
                        "ize:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u0438\u0437\u0431\u0435\u0433\u0430\u0442\u044c \u0447\u0440\u0435\u0437\u043c\u0435\u0440\u043d\u043e\u0433\u043e \u0443\u043f\u043e\u0442\u0440\u0435\u0431\u043b\u0435\u043d\u0438\u044f \u0430\u043b\u043a\u043e\u0433\u043e\u043b\u044f;</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0- \u043e\u0442\u0434\u0430\u0432\u0430\u0442\u044c \u043f\u0440\u0435\u0434\u043f\u043e\u0447\u0442\u0435\u043d\u0438\u0435 \u043d\u0430\u0442\u0443\u0440\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u0438\u0449\u0435 \u0438 \u043e\u0442\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u043e\u0442 \u043a\u043e\u043f\u0447\u0435\u043d\u043e\u0441\u0442\u0435\u0439;</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0"
                        "\u00a0\u00a0\u00a0- \u0441\u043e\u043a\u0440\u0430\u0442\u0438\u0442\u044c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430.</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u0417\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u0435 \u0447\u0430\u0449\u0435 \u0432\u0441\u0435\u0433\u043e \u043f\u0440\u043e\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0443 \u043b\u044e\u0434\u0435\u0439 50-60 \u043b\u0435\u0442, \u043f\u043e\u044d\u0442\u043e\u043c\u0443 \u0441\u043e\u0432\u0435\u0442\u0443\u0435\u043c \u0441\u043b\u0435\u0434\u0438\u0442\u044c \u0437\u0430 \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u0435\u043c \u0438 \u043d\u0435 \u043f\u0440\u043e\u0432\u043e\u0446\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0440\u0430\u043a \u0432 \u0441\u0438\u043b"
                        "\u0443 \u043d\u0435\u0437\u0434\u043e\u0440\u043e\u0432\u043e\u0433\u043e \u043e\u0431\u0440\u0430\u0437\u0430 \u0436\u0438\u0437\u043d\u0438.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b \u0440\u0438\u0441\u043a\u0430", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a name=\"docs-internal-guid-7c4aa128-7fff-939e-45c3-92de81bcf48f\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u041a \u0441\u043e\u0436\u0430\u043b\u0435\u043d\u0438\u044e, \u0434\u043e \u0441\u0438\u0445 \u043f\u043e\u0440 \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b \u043f\u0440\u0438\u0447\u0438\u043d\u044b \u0432\u043e\u0437\u043d\u0438\u043a\u043d\u043e\u0432\u0435\u043d\u0438\u044f \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u043c\u043e\u0437\u0433\u0430, \u043d\u043e \u0435\u0441\u0442\u044c \u0444\u0430\u043a\u0442\u043e\u0440\u044b \u0440\u0438\u0441\u043a\u0430, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043c\u043e\u0433\u0443\u0442 \u043f\u043e\u0432\u044b\u0441\u0438\u0442\u044c \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u043e"
                        "\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u043e\u0439 \u0431\u043e\u043b\u0435\u0437\u043d\u0438.</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u041a \u0444\u0430\u043a\u0442\u043e\u0440\u0430\u043c \u0440\u0438\u0441\u043a\u0430 \u043e\u0442\u043d\u043e\u0441\u044f\u0442\u0441\u044f:</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">- \u0412\u043e\u0437\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u0440\u0430\u0434\u0438\u0430\u0446\u0438\u0438</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">. \u041b\u044e\u0434\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u043e\u0434\u0432\u0435\u0440\u0433\u043b\u0438\u0441\u044c \u0432\u043e"
                        "\u0437\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044e \u0432\u0438\u0434\u0430 \u0438\u0437\u043b\u0443\u0447\u0435\u043d\u0438\u044f, \u0438\u043c\u0435\u044e\u0442 \u043f\u043e\u0432\u044b\u0448\u0435\u043d\u043d\u044b\u0439 \u0440\u0438\u0441\u043a \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f \u043e\u043f\u0443\u0445\u043e\u043b\u0438 \u043c\u043e\u0437\u0433\u0430. \u0412\u043e\u0437\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435\u043c \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043b\u0443\u0447\u0435\u0432\u0430\u044f \u0442\u0435\u0440\u0430\u043f\u0438\u044f, \u043f\u0440\u0438\u043c\u0435\u043d\u044f\u0435\u043c\u0430\u044f \u0434\u043b\u044f \u043b\u0435\u0447\u0435\u043d\u0438\u044f \u0440\u0430\u043a\u0430, \u0438 \u0440\u0430\u0434\u0438\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0435 \u043e\u0431\u043b\u0443\u0447\u0435\u043d\u0438\u0435.</span></p><p><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\"/><span style=\" font-family:'"
                        "Arial'; font-size:14pt; font-weight:700; color:#eeeeee; background-color:transparent;\">- \u0421\u0435\u043c\u0435\u0439\u043d\u0430\u044f \u0438\u0441\u0442\u043e\u0440\u0438\u044f \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u0439</span><span style=\" font-family:'Arial'; font-size:14pt; color:#eeeeee; background-color:transparent;\">. \u041d\u0435\u0431\u043e\u043b\u044c\u0448\u0430\u044f \u0447\u0430\u0441\u0442\u044c \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u043c\u043e\u0437\u0433\u0430 \u0432\u043e\u0437\u043d\u0438\u043a\u0430\u0435\u0442 \u0443 \u043b\u044e\u0434\u0435\u0439 \u0441 \u0441\u0435\u043c\u0435\u0439\u043d\u043e\u0439 \u0438\u0441\u0442\u043e\u0440\u0438\u0435\u0439 \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u043c\u043e\u0437\u0433\u0430 \u0438\u043b\u0438 \u0441\u0435\u043c\u0435\u0439\u043d\u043e\u0439 \u0438\u0441\u0442\u043e\u0440\u0438\u0435\u0439 \u0433\u0435\u043d\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0441\u0438\u043d\u0434\u0440\u043e"
                        "\u043c\u043e\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u043e\u0432\u044b\u0448\u0430\u044e\u0442 \u0440\u0438\u0441\u043a \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f \u043e\u043f\u0443\u0445\u043e\u043b\u0435\u0439 \u043c\u043e\u0437\u0433\u0430.</span></p></body></html>", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043e\u043a", None))
        self.spinBox.setSuffix("")
        self.label_column.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u043e\u043a", None))
        self.label_stat.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.stat.setText("")
        self.label_diagram.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"\u00a92023 NIS Autonomous Educational Organisation", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

