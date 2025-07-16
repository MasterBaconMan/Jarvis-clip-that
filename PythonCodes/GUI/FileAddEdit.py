import pygame

pygame.init() #initializes pygame
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("File Add/Edit") #GUI title

#colors
background_color = (128, 128, 128) #sets background to gray
text_color = (255, 255, 255) 
rect_color_active = (100, 100, 100) #color for text box when selected
rect_color_passive = (110, 110, 110) #default color for text box when not selected
#fonts
text_font = pygame.font.SysFont("Arial", 15)

class TextBox: #reuseable text box class
    def __init__(self, x, y, w, h, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_active = rect_color_active
        self.color_passive = rect_color_passive
        self.color = self.color_passive
        self.font = font
        self.inputtext = ""
        self.active = False

    def handle_event(self, event): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_passive

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE: #deletes text
                self.inputtext = self.inputtext[0:-1]
            else:
                self.inputtext += event.unicode #adds text to text input/box
    
    def draw_rect(self, surface): #draws shape for text box and aligns with text input
        pygame.draw.rect(surface, self.color, self.rect, 2)
        text_surface = self.font.render(self.inputtext, True, text_color)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        self.rect.w = max(100, text_surface.get_width() + 10)

textbox1 = TextBox(10, 35, 140, 32, text_font)
textbox2 = TextBox(10, 80, 140, 32, text_font)
textbox3 = TextBox(10, 125, 140, 32, text_font)

textboxes = [textbox1, textbox2, textbox3]

def draw_text(text, font, text_color, x, y): #function for text/label
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y)) #copies/draws string into image

#---------MAIN LOOP----------
running = True
while running:
    screen.fill(background_color)

    draw_text("Add or Edit:", text_font, (255, 255, 255), 10, 10)

    for box in textboxes:
        box.draw_rect(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exits the main loop
        
        for box in textboxes:
            box.handle_event(event)
            
    pygame.display.update()
