# ======================== window.py ========================

import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PIPES, MAX_PIPE_GAP, MIN_PIPE_GAP, bird_dict
from pipes import pipes_dict
from bird import bird_img

# Initialisation de la fenêtre
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Chargement des images
background_img = pygame.image.load("assets/background-day.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

floor_img = pygame.image.load("assets/base.png")
floor_img = pygame.transform.scale(floor_img, (SCREEN_WIDTH, 112))

floor_x = 0  # position horizontale du sol

# ======================== PARTIE 2.2 ========================
# TODO :
# Générer une paire de tuyaux avec :
# - position x juste après l’écran
# - un écart (gap) aléatoire entre MIN_PIPE_GAP et MAX_PIPE_GAP
# - une position verticale raisonnable pour le tuyau du bas
# - calculer la position du tuyau du haut à partir du tuyau du bas et du gap
# - si le tuyau du haut est trop haut (trop collé au haut de l’écran), le replacer correctement
# - recalculer le tuyau du bas si nécessaire pour conserver l’écart

def add_pipes():
    pass  # À compléter

# ======================== AFFICHAGE ========================

def draw_window():
    GAME_WINDOW.blit(background_img, (0, 0))

    for pipe in PIPES:
        GAME_WINDOW.blit(pipe["image"], (pipe["x"], pipe["y"]))

    GAME_WINDOW.blit(bird_img, (bird_dict["x"], bird_dict["y"]))

    font = pygame.font.SysFont(None, 48)
    lives_text = font.render(f"Vies : {bird_dict['lives']}", True, (255, 255, 255))
    score_text = font.render(f"Score : {int(bird_dict['score'])}", True, (255, 255, 255))
    GAME_WINDOW.blit(lives_text, (10, 10))
    GAME_WINDOW.blit(score_text, (10, 50))

    global floor_x
    floor_x -= 1
    if floor_x <= -SCREEN_WIDTH:
        floor_x = 0
    GAME_WINDOW.blit(floor_img, (floor_x, SCREEN_HEIGHT - 112))
    GAME_WINDOW.blit(floor_img, (floor_x + SCREEN_WIDTH, SCREEN_HEIGHT - 112))

def show_game_over_message():
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    GAME_WINDOW.blit(overlay, (0, 0))

    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over", True, (255, 0, 0))
    hint = pygame.font.SysFont(None, 36).render("Appuyer R pour recommencer", True, (255, 255, 255))

    GAME_WINDOW.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
    GAME_WINDOW.blit(hint, hint.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)))
    pygame.display.update()

