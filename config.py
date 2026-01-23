# ======================== config.py ========================

# Dimensions de la fenêtre
SCREEN_WIDTH = 576
SCREEN_HEIGHT = 1024

# Dimensions de l’oiseau
BIRD_SIZE = (68, 48)
BIRD_X = 100

# Dimensions des tuyaux
PIPE_WIDTH = 104
PIPE_HEIGHT = 640
PIPE_SIZE = (PIPE_WIDTH, PIPE_HEIGHT)
MIN_PIPE_GAP = 190
MAX_PIPE_GAP = 360

# Vitesse de défilement
PIPE_SPEED = 5

# Gravité réaliste adaptée au jeu
GRAVITY = 0.98
JUMP_VELOCITY = -15

# Vies du joueur
LIVES = 3

# Images par seconde
FPS = 60

# Liste globale des tuyaux
PIPES = []

# Dictionnaire global de l’oiseau
bird_dict = {}  # sera rempli dans bird.py

