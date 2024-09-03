import pygame
import pygame.joystick

pygame.init()
pygame.joystick.init()

joysticks = []


while True:

    for event in pygame.event.get():

        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joy.init()
            print(f"{joy.get_name()} connected")
            joysticks.append(joy)

        if event.type == pygame.JOYBUTTONDOWN:
            print("Button pressed")

        if event.type == pygame.JOYBUTTONUP:
            print("Button released")