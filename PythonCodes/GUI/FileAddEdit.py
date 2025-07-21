import pygame
import tkinter as tk
from tkinter import scrolledtext

pygame.init() #initializes pygame
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("File Add/Edit") #GUI title

#colors
background_color = (150, 150, 150) #sets background to gray
text_color = (255, 255, 255) 
rect_color_active = (80, 80, 80) #color for text box when selected
rect_color_passive = (110, 110, 110) #default color for text box when not selected
#fonts
text_font = pygame.font.SysFont("Arial", 20)
#--------tkinter text editor-----------
def open_text_editor():
    root = tk.Tk()
    root.title("Text Editor")
    root.geometry("400x300")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
    text_area.pack(expand=True, fill='both')

    root.mainloop()

#---------pygame text box---------------
class TextBox: #text box class
    def __init__(self, x, y, w, h, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.edit_button = pygame.Rect(x + w + 5, y, 30, h) #edit button
        self.color_active = rect_color_active
        self.color_passive = rect_color_passive
        self.color = self.color_passive
        self.font = font
        self.inputtext = ""
        self.active = False

    def handle_event(self, event): 
        if event.type == pygame.MOUSEBUTTONDOWN: #changes color of text box outline, indicating if it selecting or not
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_passive
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE: #deletes text
                self.inputtext = self.inputtext[0:-1]
            else:
                self.inputtext += event.unicode #append characters to text input/box
    
    def draw_rect(self, surface): #draws shape for text box and aligns with text input
        pygame.draw.rect(surface, (160, 160, 160), self.rect, 0, border_radius=5) #bg fill
        pygame.draw.rect(surface, self.color, self.rect, 1, border_radius=5) #border
        #clips the text area
        clip_rect = self.rect.inflate(-10, -10)
        previous_clip = surface.get_clip()
        surface.set_clip(clip_rect)
        #renders text
        text_surface = self.font.render(self.inputtext, True, text_color)
        #centers text
        text_rect = text_surface.get_rect()
        text_rect.y = self.rect.y + (self.rect.height - text_rect.height) // 2
        max_width = self.rect.width - 10
        #stops horizontal overflow outside the text area
        text_width = text_surface.get_width()
        if text_width > max_width:
            offset = text_width - max_width
            text_rect.x = self.rect.x + 5 - offset
        else:
            text_rect.x = self.rect.x + 5

        surface.blit(text_surface, text_rect.topleft)

        surface.set_clip(previous_clip)

        #EDIT BUTTON
        pygame.draw.rect(surface, (110, 110, 110), self.edit_button, border_radius=5)
        font = pygame.font.SysFont("Arial", 20)
        dots = font.render("...", True, (0, 0, 0))
        dots_rect = dots.get_rect(center=self.edit_button.center)
        surface.blit(dots, dots_rect)

textbox1 = TextBox(10, 40, 200, 32, text_font)
textbox2 = TextBox(10, 80, 200, 32, text_font)
textbox3 = TextBox(10, 120, 200, 32, text_font)

textboxes = [textbox1, textbox2, textbox3]

#add text box button
button_size = 30
button_x = 10
button_y = textbox3.rect.bottom + 10
button_rect = pygame.Rect(button_x, button_y, button_size, button_size)
button_color = (110, 110, 110)

def draw_button(surface, rect, color, symbol="+"): #draw button function
    pygame.draw.rect(surface, color, rect, border_radius=5)
    font = pygame.font.SysFont("Arial", 20)
    text_surf = font.render(symbol, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)
    #manually centers the symbol
    #...

#draw text
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

    draw_button(screen, button_rect, button_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exits the main loop
        
        for box in textboxes:
            box.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                last_y = textboxes[-1].rect.bottom + 10
                if last_y + 32 < screen.get_height() - 10:
                    new_box = TextBox(10, last_y, 200, 32, text_font)
                    textboxes.append(new_box)
                    button_rect.y = new_box.rect.bottom + 10

            for i, box in enumerate(textboxes):
                if box.edit_button.collidepoint(event.pos):
                    open_text_editor()

    # quit function
    file = open("PythonCodes\\Jarvis\\Status.txt", "rt")
    quit = file.readlines()
    if "quit" in quit:
        break

            
    pygame.display.update()
