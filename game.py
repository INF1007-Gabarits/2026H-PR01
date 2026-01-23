# ======================== game.py ========================

from config import GRAVITY, JUMP_VELOCITY, PIPES, PIPE_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, bird_dict

# ======================== PARTIE 3.1 ========================
# TODO : Gérer la gravité
# - Ajouter GRAVITY à la vitesse verticale de l’oiseau (vel_y)
# - Mettre à jour la position verticale de l’oiseau avec vel_y
# - Cela simule la chute progressive de l’oiseau

def apply_gravity():
    pass  # À compléter


# ======================== PARTIE 3.2 ========================
# TODO : Sauter
# - Quand l’utilisateur appuie sur une touche, l’oiseau saute
# - Pour cela, on remet sa vitesse verticale à 0
# - Puis on applique JUMP_VELOCITY (valeur négative) pour le faire monter

def jump():
    pass  # À compléter


# ======================== PARTIE 3.3 ========================
# TODO : Déplacer les tuyaux
# - Pour créer l’illusion que l’oiseau avance, les tuyaux doivent défiler vers la gauche
# - Pour chaque tuyau, réduire sa position x de PIPE_SPEED

def move_pipes():
    pass  # À compléter


# ======================== PARTIE 3.4 ========================
# TODO : Supprimer les tuyaux hors écran
# - Quand un tuyau sort complètement de l’écran à gauche, on le retire de la liste PIPES
# - Cela permet d’optimiser les performances

def remove_offscreen_pipes():
    pass  # À compléter


# ======================== PARTIE 3.5 ========================
# TODO : Détection de collision
# - Créer un rectangle (x, y, largeur, hauteur) autour de l’oiseau
# - Pour chaque tuyau, créer aussi un rectangle
# - Si ces rectangles se chevauchent, il y a collision → retourner True
# - Si l’oiseau touche le sol ou sort de l’écran par le haut → retourner aussi True

def check_collision():
    pass  # À compléter


# Fonction utilitaire pour tester la collision entre deux rectangles
# (Ne pas modifier cette fonction)
def rects_collide(r1, r2):
    return not (r1[0] + r1[2] < r2[0] or r1[0] > r2[0] + r2[2] or
                r1[1] + r1[3] < r2[1] or r1[1] > r2[1] + r2[3])


# ======================== PARTIE 3.6 ========================
# TODO : Mise à jour du score
# - Pour chaque tuyau :
#     - Si l’oiseau a dépassé le tuyau (son x est à droite du tuyau)
#     - Et que le tuyau n’a pas encore été « compté » (passed == False)
#     - Alors marquer le tuyau comme passé, et ajouter 0.5 points au score
# - Chaque paire de tuyaux vaut 1 point (0.5 pour haut, 0.5 pour bas)

def update_score():
    pass  # À compléter
