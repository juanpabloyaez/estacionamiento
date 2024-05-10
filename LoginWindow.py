from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Login")
        self.resize(250,250)
        layout=QVBoxLayout()
        
        label_username=QLabel("Usuario: ")
        input_username=QLineEdit()
        label_password=QLabel("Contraseña: ")
        input_password=QLineEdit()
        
        btn_login=QPushButton()
        layout.addWidget(label_username)
        layout.addWidget(input_username)
        layout.addWidget(label_password)
        layout.addWidget(input_password)
        layout.addWidget(btn_login)
        layout.addWidget()