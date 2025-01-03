from PyQt6.QtWidgets import QWidget, QLabel, QTextEdit, QVBoxLayout, QGraphicsView, QGraphicsScene,\
                            QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsTextItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QBrush, QColor, QMouseEvent

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
        self.setWindowTitle("GamePad Pulse")

        # Creating a graphics view
        graphicsView = QGraphicsView(self)
        graphicsView.setFixedSize(1100, 600)

        # Creating a graphics scene
        scene = QGraphicsScene(self)
        graphicsView.setScene(scene)

        # Adding the controller image to the scene
        controllerImage = QPixmap("assets/xbox-layout.png")
        imageItem = QGraphicsPixmapItem(controllerImage)
        
        scene.addItem(imageItem)

        # Button rectangles
        buttons = [
            QGraphicsRectItem(31, -12, 45, 40),                             # LT
            QGraphicsRectItem(31, 55, 45, 40),                              # LB
            QGraphicsRectItem(918, -12, 45, 40),                            # RT
            QGraphicsRectItem(918, 55, 45, 40),                             # RB
            QGraphicsEllipseItem(582 - 84/2, 303 - 84/2, 84, 84),           # RS
            QGraphicsEllipseItem(582 - 53/2, 303 - 53/2, 53, 53),           # RSB
            QGraphicsEllipseItem(337 - 84/2, 208.5 - 84/2, 84, 84),         # LS
            QGraphicsEllipseItem(337 - 53/2, 208.5 - 53/2, 53, 53),         # LSB
            QGraphicsRectItem(398, 261, 31, 34),                            # DPad_UP
            QGraphicsRectItem(398, 325, 31, 34),                            # DPad_DOWN
            QGraphicsRectItem(364, 294, 34, 32),                            # DPad_LEFT
            QGraphicsRectItem(429, 294, 34, 32),                            # DPad_RIGHT
            QGraphicsEllipseItem(451 - 32/2, 208 - 32/2, 32, 32),           # Select
            QGraphicsEllipseItem(499 - 52/2, 145 - 52/2, 52, 52),           # Xbox
            QGraphicsEllipseItem(543 - 32/2, 208 - 32/2, 32, 32),           # Start
            QGraphicsEllipseItem(659.5 - 41/2, 251 - 41/2, 41, 41),         # A
            QGraphicsEllipseItem(702 - 41/2, 208.5 - 41/2, 41, 41),         # B
            QGraphicsEllipseItem(617 - 41/2, 208.5 - 41/2, 41, 41),         # X
            QGraphicsEllipseItem(659.5 - 41/2, 166 - 41/2, 41, 41),         # Y
        ]
        for button in buttons:
            scene.addItem(button)
        
        # Controller Name
        controllerName = QLabel()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(graphicsView)
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

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            print(f"Mouse pressed at position: {event.position().toPoint()}")

    def update(self):
        self.draw()