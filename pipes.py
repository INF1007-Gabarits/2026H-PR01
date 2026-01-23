# ======================== pipes.py ========================

import pygame
from config import PIPE_SIZE

# ======================== PARTIE 2.1 ========================
# TODO :
# 1. Charger l’image du tuyau depuis le dossier assets : "assets/pipe-green.png"
# 2. Redimensionner cette image avec PIPE_SIZE
# 3. Créer un dictionnaire "pipes_dict" contenant :
#    - "bottom" : l’image normale (tuyau orienté vers le bas)
#    - "top" : l’image retournée verticalement (tuyau orienté vers le haut)

# Rappel : pour retourner une image verticalement, utiliser pygame.transform.flip(image, False, True)

# Exemple attendu (à compléter vous-même) :
# pipe_img = ...
# pipe_img = pygame.transform.scale(..., PIPE_SIZE)
# pipes_dict = {
#     "bottom": pipe_img,
#     "top": pygame.transform.flip(pipe_img, False, True)
# }

# Ce dictionnaire sera ensuite utilisé dans window.py pour dessiner les tuyaux correctement positionnés

# ===========================================================

