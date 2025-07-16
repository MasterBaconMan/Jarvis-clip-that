import pygame

pygame.init() #initializes pygame
screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("File Add/Edit") #GUI title

#colors
background_color = (128, 128, 128) #sets background to gray
#fonts
text_font = pygame.font.SysFont("Arial", 15)
#user text input
user_text = ""

input_rect = pygame.Rect(10, 35, 140, 32) #creates rectangle and coordinates
rect_color_active = (100, 100, 100)
rect_color_passive = (110, 110, 110)
rect_color = rect_color_passive

active = False

def draw_text(text, font, text_color, x, y): #function for text
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y)) #copies/draws string into image

#main loop
running = True
while running:
    screen.fill(background_color)

    draw_text("Add or Edit:", text_font, (255, 255, 255), 10, 10)

    pygame.draw.rect(screen, rect_color, input_rect, 2)
    text_surface = text_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(100, text_surface.get_width() + 10)

    if active:
        rect_color = rect_color_active
    else:
        rect_color = rect_color_passive

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exits the main loop
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN: #checks if any button is pressed
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode 
            
    pygame.display.update()
