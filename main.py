import sys
import os

from qt_core import *

from gui.windows.main_window.ui_main_window import UI_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Curso de Python e Pyside6')

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button
        self.ui.toggle_button.clicked.connect(self.toggle_button) #Esse parâmetro "self.toggle_button" é a função logo a baixo e não o botão

        self.show()

    def toggle_button(self):
        # Get menu width
        menu_width = self.ui.left_menu.width()

        # Check with
        width = 50
        if menu_width == 50:
            width = 240

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
