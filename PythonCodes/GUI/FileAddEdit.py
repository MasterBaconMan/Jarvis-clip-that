import pygame
import tkinter as tk
from tkinter import scrolledtext
import pyautogui
import time
import json

def readStatus():
    with open("PythonCodes\\Jarvis\\Status.txt", "rt") as f:
        f.readline()
        line = f.readline()
        f.close()
        return line

def run_typing_record(typing_record):
    for key, delay in typing_record:
        time.sleep(delay)
        if key == '\n':
            pyautogui.press('enter')
        elif key == '\b':
            pyautogui.press('backspace')
        else:
            pyautogui.write(key)

pygame.init() #initializes pygame
pygame.key.set_repeat(300, 50) #for repeating characters when key is held down
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
macros = {}
def open_text_editor(initial_text, initial_record):
    edited_text = initial_text
    typing_record = initial_record[:]  # copy so we don't overwrite original until saved
    last_time = time.time()

    def save_and_close():
        nonlocal edited_text
        edited_text = text_area.get("1.0", tk.END).strip()
        root.destroy()

    def run_macro():
        root.destroy()
        time.sleep(2)
        for key, delay in typing_record:
            time.sleep(delay)
            if key == '\n':
                pyautogui.press('enter')
            elif key == '\b':
                pyautogui.press('backspace')
            else:
                pyautogui.write(key)
    
    def on_key(event):
        nonlocal last_time
        now = time.time()
        delay = now - last_time
        last_time = now

        if event.keysym == "backspace":
            typing_record.append(('\b', delay))
        elif event.keysym == "return":
            typing_record.append(('\n', delay))
        elif event.char:
            typing_record.append((event.char, delay))

    root = tk.Tk()
    root.title("Text Editor")
    root.geometry("700x500")

    toolbar = tk.Frame(root, bg="#e0e0e0", pady=5, padx=8)
    toolbar.pack(side="top", fill="x")

    save_button = tk.Button(toolbar, text="Save", command=save_and_close)
    save_button.pack(side="left", padx=5)

    macro_button = tk.Button(toolbar, text="Run Macro", command=run_macro)
    macro_button.pack(side="left", padx=5)

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
    text_area.pack(expand=True, fill='both', padx=10, pady=10)
    text_area.insert(tk.END, initial_text)

    text_area.bind("<Key>", on_key)

    root.mainloop()
    return edited_text, typing_record

#---------pygame text box---------------
class TextBox: #text box class
    def __init__(self, x, y, w, h, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.edit_button = pygame.Rect(x + w + 5, y, 30, h) #edit button
        self.delete_button = pygame.Rect(x + w + 40, y, 30, h)  #delete "X" button

        self.color_active = rect_color_active
        self.color_passive = rect_color_passive
        self.color = self.color_passive
        self.font = font
        self.inputtext = ""
        self.macro_text = ""
        self.active = False

        self.typing_record = []

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

        #DELETE BUTTON
        pygame.draw.rect(surface, (110, 110, 110), self.delete_button, border_radius=5)
        x_font = pygame.font.SysFont("Arial", 20)
        x_text = x_font.render("X", True, (255, 255, 255))
        x_rect = x_text.get_rect(center=self.delete_button.center)
        surface.blit(x_text, x_rect)

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
last_macro = None
while running:
    current_macro = readStatus().strip()
    if current_macro != last_macro:
        for box in textboxes:
            if box.inputtext.strip().lower() == current_macro.lower():
                run_typing_record(box.typing_record)
                last_macro = readStatus()
                last_macro = None
                break

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

        labels = [box.inputtext for box in textboxes]
        with open("PythonCodes\\GUI\\macro.txt", "wt") as f:
                f.write(str(labels))
        # print(labels)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                start_y = 40
                if textboxes:
                    last_y = textboxes[-1].rect.bottom + 10
                else:
                    last_y = start_y

                if last_y + 32 < screen.get_height() - 10:
                    new_box = TextBox(10, last_y, 200, 32, text_font)
                    textboxes.append(new_box)
                    button_rect.y = new_box.rect.bottom + 10
        
            for i, box in enumerate(textboxes):
                if box.edit_button.collidepoint(event.pos):
                    updated_macro, updated_record = open_text_editor(box.macro_text, box.typing_record)
                    box.macro_text = updated_macro
                    box.typing_record = updated_record

                if box.delete_button.collidepoint(event.pos):
                    del textboxes[i]
                    #re-layout remaining textboxes
                    y = 40
                    for tb in textboxes:
                        tb.rect.y = y
                        tb.edit_button.y = y
                        tb.delete_button.y = y
                        y += 40  # spacing
            #update add button position
            button_rect.y = textboxes[-1].rect.bottom + 10 if textboxes else 40
            break  # exit loop early since list changed

    # quit function
    file = open("PythonCodes\\Jarvis\\Status.txt", "rt")
    quit = file.readlines()
    if "quit" in quit:
        break
            
    pygame.display.update()
