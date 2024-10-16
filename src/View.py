from PyQt6.QtWidgets import QWidget, QLabel, QTextEdit, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class View(QWidget):

    
    BUTTON_NAMES = {
        0: "A",
        1: "B",
        2: "X",
        3: "Y",
        4: "Left Bumper",
        5: "Right Bumper",
        6: "Back",
        7: "Start",
        8: "Left Stick",
        9: "Right Stick",
        10: "Xbox",
        11: "SHARE",
    }

    AXIS_NAMES = {
        0: "Left Stick X",
        1: "Left Stick Y",
        2: "Right Stick X",
        3: "Right Stick Y",
        4: "LT",
        5: "RT"
    }

    DPAD = {
        (0, 1): "D-Pad UP",
        (0, -1): "D-Pad DOWN",
        (1, 0): "D-Pad RIGHT",
        (-1, 0): "D-Pad LEFT",
    }

    
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
        self.controllerImage.setPixmap(pixmap.scaled(1000, 530))
        
        # Log area
        self.log = QTextEdit(self)
        self.log.setFixedSize(320, 530)
        self.log.setReadOnly(True)

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(self.controllerImage)
        layout.addWidget(self.log)

        self.setLayout(layout)


    def draw(self):
        self.log.clear()
        for controller in self.model.Controllers:
            controller_id = controller.get_id()
            controller_name = controller.get_name()
            self.log.append(f"Controller {controller_id}: {controller_name}\n")

        # Log button states with names
        if ("xbox" in controller_name.lower()):
            number_of_buttons = 11
        else:
            number_of_buttons = controller.get_numbuttons()

        for button in range(number_of_buttons):
            button_name = self.BUTTON_NAMES.get(button, f"Unknown Button {button}")
            if self.model.Button_States[controller_id][button]:
                self.log.append(f"{button_name}: PRESSED")
            else:
                self.log.append(f"{button_name}: -")


        self.log.append("")


        # Log axis states with names
        for axis in range(controller.get_numaxes()):
            axis_name = self.AXIS_NAMES.get(axis, f"Unknown Axis {axis}")
            axis_value = self.model.Axis_States[controller_id][axis]
            self.log.append(f"{axis_name} value: {axis_value:.2f}")


        self.log.append("")


        # Log D-pad states with names
        for hat in range(controller.get_numhats()):
            dpad_value = self.model.Hat_States[controller_id][hat]
    
            for direction, name in self.DPAD.items():
                if dpad_value == direction:
                    self.log.append(f"{name}: PRESSED")
                else:
                    self.log.append(f"{name}: -")


    def setModel(self, model):
        self.model = model


    def update(self):
        self.draw()