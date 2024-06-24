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

