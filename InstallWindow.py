from PyQt5.QtWidgets import QWdidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class InstallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instalacion")
        self.resize(300,200)
        
        layout=QVBoxLayout()
        
        label_db_name=QLabel("Nombre de la BD: ")
        label_db_username=QLabel("Usuario BD: ")
        label_db_password=QLabel("Contraseña: ")
        label_admin_username=QLabel("Usuario : ")
        label_admin_password=QLabel("Contraseña : ")
        label_espacios=QLabel("Espacios disponibles: ") #reemplaza a las líneas 16 y 17 del video 16.2
        
        input_db_name=QLineEdit()
        input_db_username=QLineEdit()
        input_db_password=QLineEdit()
        input_admin_username=QLineEdit()
        input_admin_password=QLineEdit()
        input_espacios=QLineEdit()
        
        buttonsave=QPushButton("save config")
        
        layout.addWidget(label_db_name)
        layout.addWidget(input_db_name)
        layout.addWidget(label_db_username)
        layout.addWidget(input_db_username)
        layout.addWidget(label_db_password)
        layout.addWidget(input_db_password)
        layout.addWidget(label_admin_username)
        layout.addWidget(input_admin_username)
        layout.addWidget(label_admin_password)
        layout.addWidget(input_admin_password)
        layout.addWidget(label_espacios)
        layout.addWidget(input_espacios)
        layout.addWidget(buttonsave)
        
        buttonsave.clicked.connect(self.showStepInfo)
        
        self.setLayout(layout)
        
    def showStepInfo(self):
        
        
        
        
        

