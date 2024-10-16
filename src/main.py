import sys
from PyQt6.QtWidgets import QApplication
import Model, View, Controller
import pygame


class Main:
    def __init__(self):
        # Initialize QApplication first
        self.app = QApplication(sys.argv)
        
        # Initialize Pygame
        pygame.init()

        # Create the Model
        self.model = Model.Model()

        # Create the View
        self.view = View.View()
        self.view.setModel(self.model)
        self.model.addSubscriber(self.view)

        # Create the Controller
        self.controller = Controller.Controller()
        self.controller.setModel(self.model)

    def run(self):

        self.view.show()

        # Run the event loop
        while self.view.isVisible():
            self.controller.listenForEvents()
            self.app.processEvents()

        pygame.quit()
        self.app.quit()


# Entry point of the application
if __name__ == "__main__":
    main = Main()
    main.run()