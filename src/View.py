from PyQt6.QtWidgets import QWidget, QLabel, QTextEdit, QVBoxLayout, QGraphicsView, QGraphicsScene,\
                            QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsTextItem
from PyQt6.QtGui import QPixmap, QPen, QBrush, QColor, QMouseEvent
from PyQt6.QtCore import Qt

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

    # Button shapes
    buttons = {
        BUTTON_NAMES[0]: QGraphicsEllipseItem(659.5 - 41/2, 251 - 41/2, 41, 41),       # A
        BUTTON_NAMES[1]: QGraphicsEllipseItem(702 - 41/2, 208.5 - 41/2, 41, 41),       # B
        BUTTON_NAMES[2]: QGraphicsEllipseItem(617 - 41/2, 208.5 - 41/2, 41, 41),       # X
        BUTTON_NAMES[3]: QGraphicsEllipseItem(659.5 - 41/2, 166 - 41/2, 41, 41),       # Y
        BUTTON_NAMES[4]: QGraphicsRectItem(31, 55, 45, 40),                            # LB
        BUTTON_NAMES[5]: QGraphicsRectItem(918, 55, 45, 40),                           # RB
        BUTTON_NAMES[6]: QGraphicsEllipseItem(451 - 32/2, 208 - 32/2, 32, 32),         # Back
        BUTTON_NAMES[7]: QGraphicsEllipseItem(543 - 32/2, 208 - 32/2, 32, 32),         # Start
        BUTTON_NAMES[8]: QGraphicsEllipseItem(337 - 53/2, 208.5 - 53/2, 53, 53),       # LSB
        BUTTON_NAMES[9]: QGraphicsEllipseItem(582 - 53/2, 303 - 53/2, 53, 53),         # RSB
        BUTTON_NAMES[10]: QGraphicsEllipseItem(499 - 52/2, 145 - 52/2, 52, 52)         # Xbox
    }

    # Analog shapes
    axis = {
        AXIS_NAMES[0]: QGraphicsEllipseItem(337 - 84/2, 208.5 - 84/2, 84, 84),         # LS
        AXIS_NAMES[1]: QGraphicsEllipseItem(337 - 84/2, 208.5 - 84/2, 84, 84),         # LS
        AXIS_NAMES[2]: QGraphicsEllipseItem(582 - 84/2, 303 - 84/2, 84, 84),           # RS
        AXIS_NAMES[3]: QGraphicsEllipseItem(582 - 84/2, 303 - 84/2, 84, 84),           # RS
        AXIS_NAMES[4]: QGraphicsRectItem(31, -12, 45, 40),                             # LT
        AXIS_NAMES[5]: QGraphicsRectItem(918, -12, 45, 40),                            # RT
    }
    
    # DPAD shapes
    dpad = {
        DPAD[(0,1)]: QGraphicsRectItem(398, 261, 31, 34),                              # DPad_UP
        DPAD[(0,-1)]: QGraphicsRectItem(398, 325, 31, 34),                             # DPad_DOWN
        DPAD[(1,0)]: QGraphicsRectItem(364, 294, 34, 32),                              # DPad_LEFT
        DPAD[(-1,0)]: QGraphicsRectItem(429, 294, 34, 32),                             # DPad_RIGHT
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

        # Set stroke color
        pen = QPen(QColor(73,73,73,255))                # Grey

        # Set fill color
        self.Pressed = QBrush(QColor(73,73,73,100))     # Fill
        self.Unpressed = QBrush(QColor(30,30,30,0))     # Same as background
        
        for button in self.buttons.values():
            button.setPen(pen)
            scene.addItem(button)
        for a in self.axis.values():
            a.setPen(pen)
            scene.addItem(a)
        for pad in self.dpad.values():
            pad.setPen(pen)
            scene.addItem(pad)
        
        # Controller Name
        self.controllerName = QLabel("CONTROLLER NAME")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(graphicsView)
        layout.addWidget(self.controllerName)
        self.setLayout(layout)


    def draw(self):
        for controller in self.model.Controllers:
            controller_id = controller.get_id()
            controller_name = controller.get_name()
            self.controllerName.setText(controller_name)

        # Set color of buttons based on pressed status
        if ("xbox" in controller_name.lower()):
            number_of_buttons = 11
        else:
            number_of_buttons = controller.get_numbuttons()

        for button in range(number_of_buttons):
            button_name = self.BUTTON_NAMES.get(button, f"Unknown Button {button}")
            if self.model.Button_States[controller_id][button]:
                self.buttons[button_name].setBrush(self.Pressed)
            else:
                self.buttons[button_name].setBrush(self.Unpressed)


        # Set color of analogs based on pressed status
        for axis in range(controller.get_numaxes()):
            axis_name = self.AXIS_NAMES.get(axis, f"Unknown Axis {axis}")
            axis_value = round(self.model.Axis_States[controller_id][axis], 1)
            if axis_value:
                self.axis[axis_name].setBrush(self.Pressed)
            else:
                self.axis[axis_name].setBrush(self.Unpressed)


        # Set color of DPad directional buttons based on pressed status
        for hat in range(controller.get_numhats()):
            dpad_value = self.model.Hat_States[controller_id][hat]
    
            for direction, name in self.DPAD.items():
                if dpad_value == direction:
                    self.dpad[name].setBrush(self.Pressed)
                else:
                    self.dpad[name].setBrush(self.Unpressed)


    def setModel(self, model):
        self.model = model

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            print(f"Mouse pressed at position: {event.position().toPoint()}")

    def update(self):
        self.draw()