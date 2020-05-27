
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from frame.promWindow import ProMWidget




def main():
    
    app = QApplication(sys.argv)

    ui = ProMWidget()
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
