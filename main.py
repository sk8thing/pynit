import sys
from PySide6.QtWidgets import QApplication
from GUI import main_window, load_theme
from HardwareMonitor import Monitor

def main():
    try:
        app = QApplication(sys.argv)
        Monitor()
        window = main_window()
        load_theme(app)
        window.show()
        app.exec()
    except Exception as e:
        sys.exit(e)

if __name__ == '__main__':
    main()
