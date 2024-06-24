import pygame                           #Gabriel Grasik da Rosa RA: 1136052
import tkinter as tk
from tkinter import simpledialog
import json
import os

pygame.init()

tela = pygame.display.set_mode((1000, 563))

pygame.display.set_caption("SPACE MARKER")

icone = pygame.image.load('assets/space.png')
pygame.display.set_icon(icone)

fundo = pygame.image.load('assets/bg.jpg')

def save_marks(marks):
    with open('marks.json', 'w') as file:
        json.dump(list(marks.items()), file)

def load_marks():
    if os.path.exists('marks.json'):
        with open('marks.json', 'r') as file:
            return dict(json.load(file))
    return {}

def clear_marks():
    if os.path.exists('marks.json'):
        os.remove('marks.json')

def draw_marks(marks):
    for position, name in marks.items():
        pygame.draw.circle(tela, (255, 0, 0), position, 5)
        font = pygame.font.Font(None, 24)
        text = font.render(name, True, (255, 255, 255))
        tela.blit(text, (position[0] + 10, position[1] - 10))

def get_star_name():
    root = tk.Tk()
    root.withdraw()  
    star_name = simpledialog.askstring("Input", "Qual o nome da estrela?", parent=root)
    if star_name is None or star_name.strip() == "":
        star_name = "Desconhecido"
    root.destroy()
    return star_name

def draw_menu():
    font = pygame.font.Font(None, 36)
    save_text = font.render('F10: Salvar', True, (255, 255, 255))
    load_text = font.render('F11: Carregar', True, (255, 255, 255))
    clear_text = font.render('F12: Limpar', True, (255, 255, 255))
    tela.blit(save_text, (10, 10))
    tela.blit(load_text, (10, 50))
    tela.blit(clear_text, (10, 90))

marks = load_marks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try:
                save_marks(marks)
            except Exception as e:
                print(f"Erro ao salvar as marcações: {e}")
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            name = get_star_name()
            marks[(x, y)] = name
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                save_marks(marks)
            elif event.key == pygame.K_F11:
                marks = load_marks()
            elif event.key == pygame.K_F12:
                clear_marks()
                marks = {}

    tela.blit(fundo, (0, 0))
    draw_marks(marks)
    draw_menu()
    pygame.display.flip()

pygame.quit()