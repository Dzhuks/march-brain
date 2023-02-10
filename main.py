# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import os
import sys

import pyqtgraph as pg

from evaluate import classify
from detect import detect
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from PyQt6.QtCore import QCoreApplication

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

DESCRIPTIONS_FILE = "descriptions.txt"

LABELS = ['Опухоль не обнаружена.', 'Обнаружена менингиома!', 'Обнаружена глиома!', 'Обнаружена аденома гипофиза!']


def get_descr_type(diagnosis_num):
    with open(DESCRIPTIONS_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[diagnosis_num]


# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "MBrain"
        description = "Kakoi to text"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU (DELETED)
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, False))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        # LEFT MENUS
        widgets.btn_detection.clicked.connect(self.buttonClick)
        widgets.btn_about_cancer.clicked.connect(self.buttonClick)
        widgets.btn_history.clicked.connect(self.buttonClick)

        # MAIN PAGE BUTTONS
        widgets.btn_load.clicked.connect(self.buttonClick)
        widgets.btn_evaluate.clicked.connect(self.buttonClick)

        self.stages = []
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = r"themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET detection PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.detection)
        widgets.btn_detection.setStyleSheet(UIFunctions.selectMenu(widgets.btn_detection.styleSheet()))

        self.img_width = self.img_height = 400
        self.set_image(r"images\images\default.png")

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW detection PAGE
        if btnName == "btn_detection":
            widgets.stackedWidget.setCurrentWidget(widgets.detection)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_about_cancer":
            widgets.stackedWidget.setCurrentWidget(widgets.about_cancer)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW history PAGE
        if btnName == "btn_history":
            widgets.stackedWidget.setCurrentWidget(widgets.history)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_load":
            self.open_image()
            widgets.label_diagnosis.clear()

        if btnName == "btn_evaluate":
            # определение, есть ли опухоль в мозге
            pred = detect(self.current_file)
            if pred:
                # если найдена опухоль, то нахождение ее вида
                diagnosis_num = classify(self.current_file)
                message = "Настоятельная просьба посетить врача-онколога!"
                color = "#FF0032"
            else:
                message = "Рекомендуем удостовериться в этом у врача-онколога."
                color = "#51D581"
                diagnosis_num = 0

            diagnosis = LABELS[diagnosis_num]
            # получение описания болезни из файла и корректное отображение символов перевода строки и табуляций
            description = get_descr_type(diagnosis_num).replace("\\n", "\n").replace("\\t", "\t")

            widgets.label_warning.setText(message)
            widgets.label_warning.setStyleSheet(f"font-size: 26px; color: {color}; font-weight: bold")

            widgets.label_diagnosis.setText(diagnosis)
            widgets.label_description.setText(QCoreApplication.translate("MainWindow", u"{}".format(description), None))

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def set_image(self, filename):
        self.current_file = filename
        pixmap = QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.img_width, self.img_height)
        widgets.img_brain.setPixmap(pixmap)

    def open_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Виды изображение (*.png, *.jpg)",
                                                  options=options)
        if filename != "":
            self.set_image(filename)
            widgets.label_description.clear()
            widgets.label_warning.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
