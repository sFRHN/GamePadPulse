import pygame

class Model:

    # Constructor
    def __init__(self):
        self.Controllers = []
        self.Button_States = []
        self.Axis_States = []
        self.Hat_States = []

    # Add a controller
    def addController(self, deviceIndex):
        joy = pygame.joystick.Joystick(deviceIndex)
        joy.init()
        self.Controllers.append(joy)

        self.Button_States.append([False] * joy.get_numbuttons)
        self.Axis_States.append([False] * joy.get_numaxes)
        self.Hat_States.append([False] * joy.get_numhats)

        print(f"{joy.get_name()} connected")

    # Remove a controller
    def removeController(self, deviceIndex):
        joy = self.Controllers[deviceIndex]
        joy.quit()
        self.Controllers.remove(joy)

        self.Button_States.pop(deviceIndex)
        self.Axis_States.pop(deviceIndex)
        self.Hat_States.pop(deviceIndex)

        print(f"{joy.get_name()} disconnected")


    # Setters
    def setButtonState(self, controllerID, buttonID, buttonState):
        self.ButtonStates[controllerID][buttonID] = buttonState

    def setAxisState(self, controllerID, axisID, axisState):
        self.Axis_States[controllerID][axisID] = axisState

    def setHatState(self, controllerID, hatID, hatState):
        self.Hat_States[controllerID][hatID] = hatState

    # Getters
    def getControllers(self):
        return self.Controllers

    def getButtonStates(self): 
        return self.ButtonStates

    def getAxisStates(self):
        return self.Axis_States
    
    def getHatStates(self):
        return self.Hat_States
    
