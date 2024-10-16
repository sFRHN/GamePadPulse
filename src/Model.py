import pygame

class Model:

    Controllers = []
    Button_States = []
    Axis_States = []
    Hat_States = []
    Subscribers = []

    # Constructor
    def __init__(self):
        pass

    # Add a controller
    def addController(self, deviceIndex):
        joy = pygame.joystick.Joystick(deviceIndex)
        joy.init()
        self.Controllers.append(joy)

        self.Button_States.append([False] * joy.get_numbuttons())
        self.Axis_States.append([False] * joy.get_numaxes())
        self.Hat_States.append([False] * joy.get_numhats())

        self.notifySubscribers()

        print(f"{joy.get_name()} connected")


    # Remove a controller
    def removeController(self, deviceIndex):
        joy = self.Controllers[deviceIndex]
        joy.quit()
        self.Controllers.remove(joy)

        self.Button_States.pop(deviceIndex)
        self.Axis_States.pop(deviceIndex)
        self.Hat_States.pop(deviceIndex)

        self.notifySubscribers()

        print(f"{joy.get_name()} disconnected")


    # Add a subscriber
    def addSubscriber(self, subscriber):
        self.Subscribers.append(subscriber)


    # Notify subscribers
    def notifySubscribers(self):
        for subscriber in self.Subscribers:
            subscriber.update()


    # Setters
    def setButtonState(self, controllerID, buttonID, buttonState):
        self.Button_States[controllerID][buttonID] = buttonState
        self.notifySubscribers()

    def setAxisState(self, controllerID, axisID, axisState):
        self.Axis_States[controllerID][axisID] = axisState
        self.notifySubscribers()


    def setHatState(self, controllerID, hatID, hatState):
        self.Hat_States[controllerID][hatID] = hatState
        self.notifySubscribers()

    # Getters
    def getControllers(self):
        return self.Controllers

    def getButtonStates(self): 
        return self.ButtonStates

    def getAxisStates(self):
        return self.Axis_States
    
    def getHatStates(self):
        return self.Hat_States
    
