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
from record import get_rows, FIELDNAMES, add_row
from matplotlib import pyplot as plt

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

DESCRIPTIONS_FILE = "descriptions.txt"

DIAGNOSIS = ['Не обнаружена', 'Менингиома', 'Глиома', 'Аденома гипофиза']
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

        # SPINBOX CHANGES
        widgets.spinBox.valueChanged.connect(self.show_table)

        # ABOUT CANCER BUTTONS
        widgets.btn_page1.clicked.connect(self.buttonClick)
        widgets.btn_page2.clicked.connect(self.buttonClick)
        widgets.btn_page3.clicked.connect(self.buttonClick)
        widgets.btn_page4.clicked.connect(self.buttonClick)
        self.pages = {"btn_page1": widgets.page,
                      "btn_page2": widgets.page_2,
                      "btn_page3": widgets.page_3,
                      "btn_page4": widgets.page_4}
        self.buttons = [widgets.btn_page1,
                        widgets.btn_page2,
                        widgets.btn_page3,
                        widgets.btn_page4]

        self.stages = []
        widgets.btn_page1.setStyleSheet("font-size: 16px;color: #EEEEEE; border-radius: 15px; font-weight: bold; background-color: rgb(189, 147, 249)")
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        self.show_stat()
        self.show_table()

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
        self.current_file = r"images\images\default.png"
        self.set_image(self.current_file)
        widgets.input_name.setText(self._get_filename())
        self.diagram_size = (521, 351)
        self.diagram_path = "images/images/diagram.png"

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

            self.show_stat()
            self.show_table()

        if btnName == "btn_load":
            self.open_image()
            widgets.label_diagnosis.clear()
            widgets.input_name.setText(self._get_filename())

        if btnName == "btn_evaluate":
            # определение, есть ли опухоль в мозге
            pred = detect(self.current_file)
            if pred:
                # если найдена опухоль, то нахождение ее вида
                diagnosis_num = classify(self.current_file)
                message = "Настоятельная просьба посетить врача-онколога!"
                color = "#FF0032"
            else:
                message = "Рекомендуем ежегодно проходить скрининг."
                color = "#51D581"
                diagnosis_num = 0

            diagnosis = DIAGNOSIS[diagnosis_num]
            label_diagnosis = LABELS[diagnosis_num]
            # добавление записи в базу данных
            add_row(widgets.input_name.text(), diagnosis)
            self.show_stat()
            self.show_table()

            # получение описания болезни из файла и корректное отображение символов перевода строки и табуляций
            description = get_descr_type(diagnosis_num).replace("\\n", "\n").replace("\\t", "\t")

            widgets.label_warning.setText(message)
            widgets.label_warning.setStyleSheet(f"font-size: 26px; color: {color}; font-weight: bold")

            widgets.label_diagnosis.setText(label_diagnosis)
            widgets.label_description.setText(QCoreApplication.translate("MainWindow", u"{}".format(description), None))

        if btnName == "btn_save":
            print("Save BTN clicked!")

        if btnName in self.pages.keys():
            print("true")
            for button in self.buttons:
                button.setStyleSheet("font-size: 16px;color: #EEEEEE; border-radius: 15px; font-weight: bold; background-color: rgb(40, 44, 52);")
            widgets.stackedWidget_2.setCurrentWidget(self.pages[btnName])
            btn.setStyleSheet("font-size: 16px;color: #EEEEEE; border-radius: 15px; font-weight: bold; background-color: rgb(189, 147, 249)")



        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def _get_filename(self):
        backslash = "\\"[0]
        return self.current_file.split(backslash)[-1]

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

    def show_table(self):
        num_rows, num_columns = widgets.spinBox.value(), len(FIELDNAMES)
        data = get_rows(num_rows)
        widgets.tableWidget.setRowCount(num_rows)
        widgets.tableWidget.setColumnCount(num_columns)
        widgets.tableWidget.setHorizontalHeaderLabels(FIELDNAMES)

        for i, row in enumerate(data):
            for j, elem in enumerate(row):
                widgets.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        widgets.tableWidget.resizeColumnsToContents()

    def show_stat(self):
        diagnoses = {diagnosis: 0 for diagnosis in DIAGNOSIS}
        for i in range(widgets.tableWidget.rowCount()):
            if not widgets.tableWidget.item(i, 2):
                break
            diagnoses[widgets.tableWidget.item(i, 2).text()] += 1
        stat = ""
        for key, value in diagnoses.items():
            stat += f"{key} - {value}\n"
        widgets.stat.setText(stat)
        widgets.stat.setStyleSheet(f"font-size: 26px; font-weight: bold")

        self.show_diagram(diagnoses)

    def show_diagram(self, diagnoses):
        if not any(diagnoses.values()):
            return
        labels = DIAGNOSIS
        colors = ["r", "y", "g", "b"]
        print(diagnoses)

        plt.pie(diagnoses.values(), labels=labels, colors=colors,
                startangle=90, shadow=False, explode=(0, 0, 0.1, 0),
                radius=1.2, autopct='%1.1f%%')
        plt.legend()
        plt.savefig(self.diagram_path)

        pixmap = QPixmap(self.diagram_path)
        # pixmap = pixmap.scaled(self.diagram_size[0], self.diagram_size[1])
        widgets.label_diagram.setPixmap(pixmap)
        plt.figure().clear()


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
