from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtoncalculate.clicked.connect(self.on_calculate)

    def on_calculate(self):
        try:
            a = float(self.lineEditinputa.text())
            b = float(self.lineEditinputb.text())
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập số hợp lệ cho a và b.")
            return

        result = giai_phuong_trinh_bac_nhat(a, b)
        self.pushButtoncalculate.clicked.connect(self.on_calculate)
def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        x = -b / a
        return f"Phương trình có nghiệm x = {x:.2f}"
