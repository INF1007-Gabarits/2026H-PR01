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

    # ======================== PARTIE 5.4 ========================
    # TODO : Boucle d'événements (clavier + fermeture fenêtre)
    # - Parcourir les événements Pygame avec pygame.event.get()
    # - Si l'utilisateur ferme la fenêtre (pygame.QUIT), mettre running = False
    # - Si une touche est pressée (pygame.KEYDOWN) :
    #     - Si la partie est terminée (bird_dict["lives"] <= 0) et que la touche est R (pygame.K_r) :
    #           appeler restart_game()
    #     - Sinon, si la touche est ESPACE (pygame.K_SPACE) et que l'oiseau a encore des vies :
    #           appeler jump()
    #
    # TODO : Gestion de l'état "Game Over"
    # - Si bird_dict["lives"] <= 0 :
    #     - afficher le message show_game_over_message()
    #     - ignorer le reste de la boucle (utiliser continue)

    pass  # À compléter (gestion des événements)


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

