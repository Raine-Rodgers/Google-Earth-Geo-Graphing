# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingnxZcz.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
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
                MainWindow.resize(1280, 720)
                MainWindow.setMinimumSize(QSize(940, 560))
                self.styleSheet = QWidget(MainWindow)
                self.styleSheet.setObjectName(u"styleSheet")
                font = QFont()
                font.setFamily(u"Segoe UI")
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
                self.appMargins = QVBoxLayout(self.styleSheet)
                self.appMargins.setSpacing(0)
                self.appMargins.setObjectName(u"appMargins")
                self.appMargins.setContentsMargins(10, 10, 10, 10)
                self.bgApp = QFrame(self.styleSheet)
                self.bgApp.setObjectName(u"bgApp")
                self.bgApp.setStyleSheet(u"")
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

                self.verticalLayout_3.addWidget(self.topLogoInfo)

                self.leftMenuFrame = QFrame(self.leftMenuBg)
                self.leftMenuFrame.setObjectName(u"leftMenuFrame")
                self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
                self.leftMenuFrame.setFrameShadow(QFrame.Raised)
                self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
                self.verticalMenuLayout.setSpacing(0)
                self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
                self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
                self.toggleBox = QFrame(self.leftMenuFrame)
                self.toggleBox.setObjectName(u"toggleBox")
                self.toggleBox.setMaximumSize(QSize(16777215, 45))
                self.toggleBox.setFrameShape(QFrame.NoFrame)
                self.toggleBox.setFrameShadow(QFrame.Raised)
                self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
                self.verticalLayout_4.setSpacing(0)
                self.verticalLayout_4.setObjectName(u"verticalLayout_4")
                self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.toggleButton = QPushButton(self.toggleBox)
                self.toggleButton.setObjectName(u"toggleButton")
                sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
                self.toggleButton.setSizePolicy(sizePolicy)
                self.toggleButton.setMinimumSize(QSize(0, 45))
                self.toggleButton.setFont(font)
                self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
                self.toggleButton.setLayoutDirection(Qt.LeftToRight)
                self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

                self.verticalLayout_4.addWidget(self.toggleButton)


                self.verticalMenuLayout.addWidget(self.toggleBox)

                self.topMenu = QFrame(self.leftMenuFrame)
                self.topMenu.setObjectName(u"topMenu")
                self.topMenu.setFrameShape(QFrame.NoFrame)
                self.topMenu.setFrameShadow(QFrame.Raised)
                self.verticalLayout_8 = QVBoxLayout(self.topMenu)
                self.verticalLayout_8.setSpacing(0)
                self.verticalLayout_8.setObjectName(u"verticalLayout_8")
                self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
                self.btn_home = QPushButton(self.topMenu)
                self.btn_home.setObjectName(u"btn_home")
                sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
                self.btn_home.setSizePolicy(sizePolicy)
                self.btn_home.setMinimumSize(QSize(0, 45))
                self.btn_home.setFont(font)
                self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
                self.btn_home.setLayoutDirection(Qt.LeftToRight)
                self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

                self.verticalLayout_8.addWidget(self.btn_home)

                self.btn_new = QPushButton(self.topMenu)
                self.btn_new.setObjectName(u"btn_new")
                sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
                self.btn_new.setSizePolicy(sizePolicy)
                self.btn_new.setMinimumSize(QSize(0, 45))
                self.btn_new.setFont(font)
                self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
                self.btn_new.setLayoutDirection(Qt.LeftToRight)
                self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-pencil.png);")

                self.verticalLayout_8.addWidget(self.btn_new)


                self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

                self.bottomMenu = QFrame(self.leftMenuFrame)
                self.bottomMenu.setObjectName(u"bottomMenu")
                self.bottomMenu.setFrameShape(QFrame.NoFrame)
                self.bottomMenu.setFrameShadow(QFrame.Raised)
                self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
                self.verticalLayout_9.setSpacing(0)
                self.verticalLayout_9.setObjectName(u"verticalLayout_9")
                self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
                self.toggleLeftBox = QPushButton(self.bottomMenu)
                self.toggleLeftBox.setObjectName(u"toggleLeftBox")
                sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
                self.toggleLeftBox.setSizePolicy(sizePolicy)
                self.toggleLeftBox.setMinimumSize(QSize(0, 45))
                self.toggleLeftBox.setFont(font)
                self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
                self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
                self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

                self.verticalLayout_9.addWidget(self.toggleLeftBox)


                self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


                self.verticalLayout_3.addWidget(self.leftMenuFrame)


                self.appLayout.addWidget(self.leftMenuBg)

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
                self.settingsTopBtn = QPushButton(self.rightButtons)
                self.settingsTopBtn.setObjectName(u"settingsTopBtn")
                self.settingsTopBtn.setMinimumSize(QSize(28, 28))
                self.settingsTopBtn.setMaximumSize(QSize(28, 28))
                self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
                icon = QIcon()
                icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
                self.settingsTopBtn.setIcon(icon)
                self.settingsTopBtn.setIconSize(QSize(20, 20))

                self.horizontalLayout_2.addWidget(self.settingsTopBtn)

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
                font1 = QFont()
                font1.setFamilies([u"Segoe UI"])
                font1.setPointSize(10)
                font1.setBold(False)
                font1.setItalic(False)
                font1.setStyleStrategy(QFont.PreferDefault)
                self.maximizeRestoreAppBtn.setFont(font1)
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
                icon3 = QIcon()
                icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
                self.closeAppBtn.setIcon(icon3)
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
                self.stackedWidget.setStyleSheet(u"background: transparent;")
                self.home = QWidget()
                self.home.setObjectName(u"home")
                self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
        "background-position: center;\n"
        "background-repeat: no-repeat;")
                self.stackedWidget.addWidget(self.home)
                self.widgets = QWidget()
                self.widgets.setObjectName(u"widgets")
                self.widgets.setStyleSheet(u"b")
                self.verticalLayout = QVBoxLayout(self.widgets)
                self.verticalLayout.setSpacing(10)
                self.verticalLayout.setObjectName(u"verticalLayout")
                self.verticalLayout.setContentsMargins(10, 10, 10, 10)
                self.row_1 = QFrame(self.widgets)
                self.row_1.setObjectName(u"row_1")
                self.row_1.setFrameShape(QFrame.StyledPanel)
                self.row_1.setFrameShadow(QFrame.Raised)
                self.verticalLayout_16 = QVBoxLayout(self.row_1)
                self.verticalLayout_16.setSpacing(0)
                self.verticalLayout_16.setObjectName(u"verticalLayout_16")
                self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
                self.frame_div_content_1 = QFrame(self.row_1)
                self.frame_div_content_1.setObjectName(u"frame_div_content_1")
                self.frame_div_content_1.setMinimumSize(QSize(0, 110))
                self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
                self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
                self.frame_div_content_1.setFrameShadow(QFrame.Raised)
                self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
                self.verticalLayout_17.setSpacing(0)
                self.verticalLayout_17.setObjectName(u"verticalLayout_17")
                self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
                self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
                self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
                self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
                self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
                self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
                self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
                self.verticalLayout_18.setObjectName(u"verticalLayout_18")
                self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
                self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
                self.labelBoxBlenderInstalation.setFont(font)
                self.labelBoxBlenderInstalation.setStyleSheet(u"")

                self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


                self.verticalLayout_17.addWidget(self.frame_title_wid_1)

                self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
                self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
                self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
                self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
                self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
                self.gridLayout = QGridLayout()
                self.gridLayout.setObjectName(u"gridLayout")
                self.gridLayout.setContentsMargins(-1, -1, -1, 0)
                self.lineEdit = QLineEdit(self.frame_content_wid_1)
                self.lineEdit.setObjectName(u"lineEdit")
                self.lineEdit.setMinimumSize(QSize(0, 30))
                self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

                self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

                self.pushButton = QPushButton(self.frame_content_wid_1)
                self.pushButton.setObjectName(u"pushButton")
                self.pushButton.setMinimumSize(QSize(150, 30))
                self.pushButton.setFont(font)
                self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
                self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
                icon4 = QIcon()
                icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
                self.pushButton.setIcon(icon4)

                self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)


                self.horizontalLayout_9.addLayout(self.gridLayout)


                self.verticalLayout_17.addWidget(self.frame_content_wid_1)


                self.verticalLayout_16.addWidget(self.frame_div_content_1)


                self.verticalLayout.addWidget(self.row_1)

                self.row_3 = QFrame(self.widgets)
                self.row_3.setObjectName(u"row_3")
                self.row_3.setMinimumSize(QSize(0, 150))
                self.row_3.setFrameShape(QFrame.StyledPanel)
                self.row_3.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_12 = QHBoxLayout(self.row_3)
                self.horizontalLayout_12.setSpacing(0)
                self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
                self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
                self.tableWidget = QTableWidget(self.row_3)
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
                if (self.tableWidget.rowCount() < 16):
                        self.tableWidget.setRowCount(16)
                font2 = QFont()
                font2.setFamilies([u"Segoe UI"])
                __qtablewidgetitem4 = QTableWidgetItem()
                __qtablewidgetitem4.setFont(font2);
                self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
                __qtablewidgetitem5 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
                __qtablewidgetitem6 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
                __qtablewidgetitem7 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
                __qtablewidgetitem8 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
                __qtablewidgetitem9 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
                __qtablewidgetitem10 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
                __qtablewidgetitem11 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
                __qtablewidgetitem12 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
                __qtablewidgetitem13 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
                __qtablewidgetitem14 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
                __qtablewidgetitem15 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
                __qtablewidgetitem16 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
                __qtablewidgetitem17 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
                __qtablewidgetitem18 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
                __qtablewidgetitem19 = QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
                __qtablewidgetitem20 = QTableWidgetItem()
                self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
                __qtablewidgetitem21 = QTableWidgetItem()
                self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
                __qtablewidgetitem22 = QTableWidgetItem()
                self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
                __qtablewidgetitem23 = QTableWidgetItem()
                self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
                self.tableWidget.setObjectName(u"tableWidget")
                self.tableWidget.setEnabled(True)
                sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                sizePolicy3.setHorizontalStretch(0)
                sizePolicy3.setVerticalStretch(0)
                sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
                self.tableWidget.setSizePolicy(sizePolicy3)
                palette = QPalette()
                brush = QBrush(QColor(221, 221, 221, 255))
                brush.setStyle(Qt.SolidPattern)
                palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
                brush1 = QBrush(QColor(0, 0, 0, 0))
                brush1.setStyle(Qt.SolidPattern)
                palette.setBrush(QPalette.Active, QPalette.Button, brush1)
                palette.setBrush(QPalette.Active, QPalette.Text, brush)
                palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
                brush2 = QBrush(QColor(0, 0, 0, 255))
                brush2.setStyle(Qt.NoBrush)
                palette.setBrush(QPalette.Active, QPalette.Base, brush2)
                palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
                palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        #endif
                palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
                palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
                palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
                palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
                brush3 = QBrush(QColor(0, 0, 0, 255))
                brush3.setStyle(Qt.NoBrush)
                palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
                palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
                palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        #endif
                palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
                palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
                palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
                palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
                brush4 = QBrush(QColor(0, 0, 0, 255))
                brush4.setStyle(Qt.NoBrush)
                palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
                palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
                palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        #endif
                self.tableWidget.setPalette(palette)
                self.tableWidget.setMouseTracking(True)
                self.tableWidget.setTabletTracking(True)
                self.tableWidget.setAcceptDrops(True)
                self.tableWidget.setFrameShape(QFrame.NoFrame)
                self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
                self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
                self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
                self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
                self.tableWidget.setShowGrid(True)
                self.tableWidget.setGridStyle(Qt.SolidLine)
                self.tableWidget.setSortingEnabled(False)
                self.tableWidget.horizontalHeader().setVisible(False)
                self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
                self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
                self.tableWidget.horizontalHeader().setStretchLastSection(True)
                self.tableWidget.verticalHeader().setVisible(False)
                self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
                self.tableWidget.verticalHeader().setHighlightSections(False)
                self.tableWidget.verticalHeader().setStretchLastSection(True)

                self.horizontalLayout_12.addWidget(self.tableWidget)


                self.verticalLayout.addWidget(self.row_3)

                self.AddRowButton = QPushButton(self.widgets)
                self.AddRowButton.setObjectName(u"AddRowButton")

                self.verticalLayout.addWidget(self.AddRowButton)

                self.DeleteRowButton = QPushButton(self.widgets)
                self.DeleteRowButton.setObjectName(u"DeleteRowButton")

                self.verticalLayout.addWidget(self.DeleteRowButton)

                self.stackedWidget.addWidget(self.widgets)
                self.new_page = QWidget()
                self.new_page.setObjectName(u"new_page")
                self.verticalLayout_20 = QVBoxLayout(self.new_page)
                self.verticalLayout_20.setObjectName(u"verticalLayout_20")
                self.verticalLayout_5 = QVBoxLayout()
                self.verticalLayout_5.setSpacing(0)
                self.verticalLayout_5.setObjectName(u"verticalLayout_5")
                self.horizontalLayout_6 = QHBoxLayout()
                self.horizontalLayout_6.setSpacing(0)
                self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
                self.horizontalLayout_6.setContentsMargins(-1, -1, 300, -1)
                self.radioButton = QRadioButton(self.new_page)
                self.radioButton.setObjectName(u"radioButton")
                self.radioButton.setIconSize(QSize(16, 20))

                self.horizontalLayout_6.addWidget(self.radioButton)

                self.radioButton_2 = QRadioButton(self.new_page)
                self.radioButton_2.setObjectName(u"radioButton_2")

                self.horizontalLayout_6.addWidget(self.radioButton_2)

                self.label = QLabel(self.new_page)
                self.label.setObjectName(u"label")

                self.horizontalLayout_6.addWidget(self.label)

                self.lineEdit_2 = QLineEdit(self.new_page)
                self.lineEdit_2.setObjectName(u"lineEdit_2")

                self.horizontalLayout_6.addWidget(self.lineEdit_2)

                self.formLayout = QFormLayout()
                self.formLayout.setObjectName(u"formLayout")
                self.formLayout.setContentsMargins(-1, -1, 0, -1)

                self.horizontalLayout_6.addLayout(self.formLayout)


                self.verticalLayout_5.addLayout(self.horizontalLayout_6)

                self.gridLayout_2 = QGridLayout()
                self.gridLayout_2.setObjectName(u"gridLayout_2")
                self.groupBox_2 = QGroupBox(self.new_page)
                self.groupBox_2.setObjectName(u"groupBox_2")
                self.horizontalLayout_11 = QHBoxLayout(self.groupBox_2)
                self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
                self.label_2 = QLabel(self.groupBox_2)
                self.label_2.setObjectName(u"label_2")

                self.horizontalLayout_11.addWidget(self.label_2)

                self.lineEdit_3 = QLineEdit(self.groupBox_2)
                self.lineEdit_3.setObjectName(u"lineEdit_3")
                self.lineEdit_3.setMinimumSize(QSize(761, 23))
                self.lineEdit_3.setMaximumSize(QSize(761, 16777215))

                self.horizontalLayout_11.addWidget(self.lineEdit_3)

                self.label_3 = QLabel(self.groupBox_2)
                self.label_3.setObjectName(u"label_3")

                self.horizontalLayout_11.addWidget(self.label_3)

                self.spinBox = QSpinBox(self.groupBox_2)
                self.spinBox.setObjectName(u"spinBox")

                self.horizontalLayout_11.addWidget(self.spinBox)


                self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)

                self.groupBox_4 = QGroupBox(self.new_page)
                self.groupBox_4.setObjectName(u"groupBox_4")
                self.horizontalLayout_13 = QHBoxLayout(self.groupBox_4)
                self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
                self.label_4 = QLabel(self.groupBox_4)
                self.label_4.setObjectName(u"label_4")

                self.horizontalLayout_13.addWidget(self.label_4)

                self.lineEdit_4 = QLineEdit(self.groupBox_4)
                self.lineEdit_4.setObjectName(u"lineEdit_4")

                self.horizontalLayout_13.addWidget(self.lineEdit_4)

                self.label_5 = QLabel(self.groupBox_4)
                self.label_5.setObjectName(u"label_5")

                self.horizontalLayout_13.addWidget(self.label_5)

                self.lineEdit_5 = QLineEdit(self.groupBox_4)
                self.lineEdit_5.setObjectName(u"lineEdit_5")

                self.horizontalLayout_13.addWidget(self.lineEdit_5)


                self.gridLayout_2.addWidget(self.groupBox_4, 1, 1, 1, 1)

                self.groupBox_3 = QGroupBox(self.new_page)
                self.groupBox_3.setObjectName(u"groupBox_3")
                self.horizontalLayout_8 = QHBoxLayout(self.groupBox_3)
                self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
                self.radioButton_5 = QRadioButton(self.groupBox_3)
                self.radioButton_5.setObjectName(u"radioButton_5")

                self.horizontalLayout_8.addWidget(self.radioButton_5)

                self.radioButton_6 = QRadioButton(self.groupBox_3)
                self.radioButton_6.setObjectName(u"radioButton_6")

                self.horizontalLayout_8.addWidget(self.radioButton_6)


                self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)

                self.groupBox = QGroupBox(self.new_page)
                self.groupBox.setObjectName(u"groupBox")
                self.horizontalLayout_7 = QHBoxLayout(self.groupBox)
                self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
                self.radioButton_3 = QRadioButton(self.groupBox)
                self.radioButton_3.setObjectName(u"radioButton_3")

                self.horizontalLayout_7.addWidget(self.radioButton_3)

                self.radioButton_4 = QRadioButton(self.groupBox)
                self.radioButton_4.setObjectName(u"radioButton_4")

                self.horizontalLayout_7.addWidget(self.radioButton_4)


                self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

                self.groupBox_5 = QGroupBox(self.new_page)
                self.groupBox_5.setObjectName(u"groupBox_5")
                self.horizontalLayout_10 = QHBoxLayout(self.groupBox_5)
                self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
                self.radioButton_7 = QRadioButton(self.groupBox_5)
                self.radioButton_7.setObjectName(u"radioButton_7")

                self.horizontalLayout_10.addWidget(self.radioButton_7)

                self.radioButton_8 = QRadioButton(self.groupBox_5)
                self.radioButton_8.setObjectName(u"radioButton_8")

                self.horizontalLayout_10.addWidget(self.radioButton_8)


                self.gridLayout_2.addWidget(self.groupBox_5, 2, 0, 1, 1)

                self.groupBox_6 = QGroupBox(self.new_page)
                self.groupBox_6.setObjectName(u"groupBox_6")
                self.horizontalLayout_14 = QHBoxLayout(self.groupBox_6)
                self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
                self.checkBox = QCheckBox(self.groupBox_6)
                self.checkBox.setObjectName(u"checkBox")

                self.horizontalLayout_14.addWidget(self.checkBox)

                self.label_6 = QLabel(self.groupBox_6)
                self.label_6.setObjectName(u"label_6")

                self.horizontalLayout_14.addWidget(self.label_6)


                self.gridLayout_2.addWidget(self.groupBox_6, 2, 1, 1, 1)


                self.verticalLayout_5.addLayout(self.gridLayout_2)


                self.verticalLayout_20.addLayout(self.verticalLayout_5)

                self.stackedWidget.addWidget(self.new_page)

                self.verticalLayout_15.addWidget(self.stackedWidget)


                self.horizontalLayout_4.addWidget(self.pagesContainer)


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
                font3 = QFont()
                font3.setFamilies([u"Segoe UI"])
                font3.setBold(False)
                font3.setItalic(False)
                self.creditsLabel.setFont(font3)
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


                self.appMargins.addWidget(self.bgApp)

                MainWindow.setCentralWidget(self.styleSheet)

                self.retranslateUi(MainWindow)

                self.stackedWidget.setCurrentIndex(2)


                QMetaObject.connectSlotsByName(MainWindow)
                # setupUi

        def retranslateUi(self, MainWindow):
                MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
                self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
                self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
                self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
                self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
                self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Google Earth Graph Creator", None))
        #if QT_CONFIG(tooltip)
                self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
        #endif // QT_CONFIG(tooltip)
                self.settingsTopBtn.setText("")
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
                self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"File Name", None))
                self.lineEdit.setText("")
                self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
                self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
                ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
                ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
                ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
                ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
                ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
                ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
                ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
                ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
                ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
                ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
                ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
                ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
                ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
                ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
                ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
                ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
                ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
                ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
                ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
                ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
                ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
                ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

                __sortingEnabled = self.tableWidget.isSortingEnabled()
                self.tableWidget.setSortingEnabled(False)
                ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
                ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
                ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
                ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
                ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
                ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
                ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
                ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
                self.tableWidget.setSortingEnabled(__sortingEnabled)

                self.AddRowButton.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
                self.DeleteRowButton.setText(QCoreApplication.translate("MainWindow", u"Delete Row", None))
                self.radioButton.setText(QCoreApplication.translate("MainWindow", u"2D          ", None))
                self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"3D          ", None))
                self.label.setText(QCoreApplication.translate("MainWindow", u"Polygon Count  ", None))
                self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Size", None))
                self.label_2.setText(QCoreApplication.translate("MainWindow", u"Size", None))
                self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
                self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Height", None))
                self.label_4.setText(QCoreApplication.translate("MainWindow", u"Factor", None))
                self.label_5.setText(QCoreApplication.translate("MainWindow", u"          Add Altitude", None))
                self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Height", None))
                self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
                self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
                self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Size", None))
                self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
                self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
                self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
                self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
                self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
                self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
                self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Outline", None))
                self.label_6.setText(QCoreApplication.translate("MainWindow", u"Work in Progress Function", None))
                self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Raine M. Rodgers", None))
                self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
                # retranslateUi

