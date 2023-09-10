import pygame

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

try:
    pygame.init()
    while True:
        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     break
            # elif event.type == pygame.JOYBUTTONDOWN:
            #     print(event)
            # elif event.type == pygame.JOYAXISMOTION:
            #     print(event)
        
            x_speed = pygame.joystick.Joystick(0).get_axis(0)
            y_speed = -1*pygame.joystick.Joystick(0).get_axis(1)
            print('SPEED\n-----')
            print(f'X: {x_speed:0.4f}')
            print(f'y: {y_speed:0.4f}\n')

except KeyboardInterrupt:
    pygame.joystick.quit()
    pygame.quit()