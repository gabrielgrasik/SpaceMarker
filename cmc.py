# Gabriel Grasik da Rosa    RA: 1136052 
import pygame
import tkinter as tk
from tkinter import simpledialog
import json
import os

pygame.init

tela = pygame.display.set_mode(1000,563)

pygame.dysplay.set_caption("Space Marker")

icone = pygame.image.load('assets/space.png')
pygame.display. set_icon(icone)

fundo = pygame.image.load("assets/bg.jpg")

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
    for posicao, nome in marks.items():
        pygame.draw.circle(tela, (255, 0, 0), posicao, 5)
        font = pygame.font.Font(None, 24)
        text = font.render(nome, True (255, 255, 255))
        tela.blit(text, (posicao[0] + 10, posicao [1] - 10))

def get_star_name():
    root = tk.Tk()
    root.withdraw()
    star_name = simpledialog.askstring("input", "Qual o nome da Estrela?", parent=root)
    if star_name is None or star_name.strip() == "":
        star_name = "Desconhecido"
        root.destroy()
        return star_name
    
def draw_menu():
    font = pygame.font.Font(None, 36)
    save_text = font.render('F10: Salvar' True (255,255,255) )
    load_text = font.render('F11: Carregar' True (255,255,255) )
    clear_text = font.render('F12: Limpar' True (255,255,255) )
    tela.blit(save_text,(10,10))
    tela.blit(load_text,(10,50))
    tela.blit(clear_text,(10,90))

marks = load_marks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try:
                save_marks(marks)
            except Exception as e:
                print(f"Erro ao Salvar as marcações: {e}")
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            nome = get_star_name()
            marks[(x,y)] = nome
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                save_marks(marks)
            elif event.key == pygame.K_F11:
                marks = load_marks()
            elif event.key == pygame.K_F12:
                clear_marks()
                marks = ()
                