# ======================== main.py ========================

import pygame
import sys
from config import FPS, bird_dict, PIPES, SCREEN_WIDTH
from window import draw_window, show_game_over_message, add_pipes
from game import apply_gravity, move_pipes, remove_offscreen_pipes, check_collision, update_score, jump

pygame.init()
clock = pygame.time.Clock()
running = True

# ======================== PARTIE 4.1 ========================
# TODO : Générer une première paire de tuyaux au début du jeu
add_pipes()


# ======================== PARTIE 4.2 ========================
# TODO : Fonction pour recommencer une partie
# - Remettre l’oiseau au centre
# - Réinitialiser vitesse, vies, score
# - Supprimer les anciens tuyaux
# - Ajouter une nouvelle paire

def restart_game():
    pass  # À compléter


# ======================== PARTIE 4.3 ========================
# TODO : Boucle principale du jeu
# - Appliquer la gravité
# - Gérer les événements clavier :
#     - Espace pour sauter
#     - R pour recommencer quand perdu
# - Vérifier les collisions
# - Générer une nouvelle paire de tuyaux régulièrement
# - Mettre à jour le score
# - Afficher le jeu (appel à draw_window)

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if bird_dict["lives"] <= 0 and event.key in [pygame.K_SPACE, pygame.K_r]:
                restart_game()
            elif event.key == pygame.K_SPACE and bird_dict["lives"] > 0:
                jump()

    if bird_dict["lives"] <= 0:
        show_game_over_message()
        continue

    apply_gravity()
    move_pipes()
    remove_offscreen_pipes()
    update_score()

    # TODO : Générer une nouvelle paire si le dernier tuyau est suffisamment avancé
    pass  # À compléter

    if check_collision():
        bird_dict["lives"] -= 1
        bird_dict["x"] = 100
        bird_dict["y"] = 512
        bird_dict["vel_y"] = 0
        PIPES.clear()
        add_pipes()

    draw_window()

pygame.quit()
sys.exit()

