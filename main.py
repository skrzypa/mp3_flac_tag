import windows

import sys

from PyQt6.QtWidgets import QApplication



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = windows.MainWindow()
    window.show()   # show program
    app.exec()