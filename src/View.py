from PyQt6.QtWidgets import QWidget, QLabel, QTextEdit, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class View(QWidget):
    
    def __init__(self):
        super().__init__()
        self.InitializeUI()


    def InitializeUI(self):
        # Set fixed window size
        # self.setFixedSize(800, 800)
        self.setWindowTitle("GamePad Pulse")

        # Controller image area
        self.controllerImage = QLabel(self)
        # self.controllerImage.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("assets/xbox-layout.png")
        self.controllerImage.setPixmap(pixmap.scaled(700, 371))
        
        # Log area
        self.log = QTextEdit(self)
        self.log.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.controllerImage)
        layout.addWidget(self.log)

        self.setLayout(layout)


    def draw(self):
        self.log.clear()
        for controller in self.model.Controllers:
            for button in range(0, controller.get_numbuttons()):
                if self.model.Button_States[controller.get_id()][button]:
                    self.log.append(f"Button {button} pressed on {controller.get_name()}")
                else:
                    self.log.append(f"Button {button} released on {controller.get_name()}")

            for axis in range(0, controller.get_numaxes()):
                self.log.append(f"Axis {axis} value: {controller.get_axis(axis)} on {controller.get_name()}")

            for hat in range(0, controller.get_numhats()):
                self.log.append(f"Hat {hat} value: {controller.get_hat(hat)} on {controller.get_name()}")


    def setModel(self, model):
        self.model = model


    def update(self):
        self.draw()