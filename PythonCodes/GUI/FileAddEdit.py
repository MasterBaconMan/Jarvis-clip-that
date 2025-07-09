import pygame

pygame.init() #initializes pygame
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("File Add/Edit")

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #set running to False to exit the main loop

