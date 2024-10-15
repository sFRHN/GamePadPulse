import pygame
import pygame.joystick

pygame.init()
pygame.joystick.init()

joysticks = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Detect joystick connection
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joy.init()
            print(f"{joy.get_name()} connected")
            joysticks.append(joy)

        # Detect button presses
        if event.type == pygame.JOYBUTTONDOWN:
            for joy in joysticks:
                for button in range(joy.get_numbuttons()):
                    if joy.get_button(button):
                        print(f"Button {button} pressed")

        if event.type == pygame.JOYBUTTONUP:
            for joy in joysticks:
                for button in range(joy.get_numbuttons()):
                    if joy.get_button(button):
                        print(f"Button {button} released")

        # Detect axis motion (e.g., triggers)
        if event.type == pygame.JOYAXISMOTION:
            for joy in joysticks:
                for axis in range(joy.get_numaxes()):
                    value = joy.get_axis(axis)
                    print(f"Axis {axis} moved to {value:.2f}")

        # Detect hat motion (e.g., D-pad)
        if event.type == pygame.JOYHATMOTION:
            for joy in joysticks:
                for hat in range(joy.get_numhats()):
                    value = joy.get_hat(hat)
                    print(f"Hat {hat} moved to {value}")
