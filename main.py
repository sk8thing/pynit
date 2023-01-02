import sys
from PySide6.QtWidgets import QApplication
from GUI import main_window, load_theme
from HardwareMonitor import Monitor

def main():
    app = QApplication(sys.argv)
    monitor = Monitor()
    window = main_window()
    load_theme(app)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
