from PyQt5.QtWidgets import QMessageBox

class Ui_Qmessagebox():
    """
    Class
    """
    def __init__(self):
        pass

    def qmessagebox(self, title, text):
        """
        Show pop up
        """
        msg = QMessageBox()
        if title in ["Password", "OTP Not Verified","Network"]:
            msg.setIcon(QMessageBox.Critical)
        elif title in ["Email","Name","Date Of Birth","Image"]:
            msg.setIcon(QMessageBox.Warning)
        else:
            msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec_()