import pygame
import pygame.joystick as joysticks

class Controller:

    model = None

    def __init__(self):
        self.model = None
        joysticks.init()

    def setModel(self, model):
        model = model

    # Listen for events
    def listenForEvents(self):

        for event in pygame.event.get():

            match event.type:
                case pygame.JOYDEVICEADDED:
                    self.model.addController(event.device_index)

                case pygame.JOYDEVICEREMOVED:
                    self.model.removeController(event.device_index)

                case pygame.JOYBUTTONDOWN:
                    self.model.setButtonState(event.joy, event.button, True)

                case pygame.JOYBUTTONUP:
                    self.model.setButtonState(event.joy, event.button, False)

                case pygame.JOYAXISMOTION:
                    self.model.setAxisState(event.joy, event.axis, event.value)

                case pygame.JOYHATMOTION:
                    self.model.setHatState(event.joy, event.hat, event.value)

                case pygame.QUIT:
                    pygame.quit()
                    exit()