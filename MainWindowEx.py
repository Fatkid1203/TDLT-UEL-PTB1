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
        # Kết nối nút bấm với hàm xử lý
        self.pushButtoncalculate.clicked.connect(self.on_calculate)

    def on_calculate(self):
        try:
            # Lấy giá trị a và b từ ô nhập
            a = float(self.lineEditinputa.text())
            b = float(self.lineEditinputb.text())
        except ValueError:
            # Hiển thị thông báo lỗi nếu giá trị không hợp lệ
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập số hợp lệ cho a và b.")
            return

        # Gọi hàm giải phương trình
        result = giai_phuong_trinh_bac_nhat(a, b)

        # Hiển thị kết quả lên ô lineEditinputc
        self.lineEditinputc.setText(result)


def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        x = -b / a
        return f"Phương trình có nghiệm x = {x:.2f}"
