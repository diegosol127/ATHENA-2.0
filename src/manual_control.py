import RPi.GPIO
import time
import math
import pygame
import controls

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
athena_controls = controls.Controller()

try:
    pygame.init()
    dt = 0.01

    while True:
        for event in pygame.event.get():        
            x = round(100*joystick.get_axis(0),2)
            y = round(-100*joystick.get_axis(1),2)
            
            athena_controls.move_360(x,y,dt)

        time.sleep(dt)

except KeyboardInterrupt:
    print('\nProcess Manually Terminated')
    pygame.joystick.quit()
    pygame.quit()
    RPi.GPIO.cleanup()

except:
    print('\nProcess Interrupted')
    pygame.joystick.quit()
    pygame.quit()
    RPi.GPIO.cleanup()