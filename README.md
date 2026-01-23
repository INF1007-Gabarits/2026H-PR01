# Projet – Flappy Bird 🐦 (INF1007)

## Directives
:alarm_clock: **Date de remise** : 22 février 2026 à minuit 

:mailbox_with_mail: **Remise** : sur Moodle (voir directives en fin de document)

---

## Introduction

Dans ce projet, vous aurez comme tâche de compléter une version simplifiée du jeu **Flappy Bird** 🐦.

Flappy Bird est un jeu d’arcade dans lequel le joueur contrôle un oiseau qui avance automatiquement vers la droite. L’objectif est de **faire passer l’oiseau entre des paires de tuyaux** sans les toucher, tout en évitant de heurter le sol ou de sortir de l’écran par le haut.

Le joueur dispose de **3 vies**. Une vie est perdue lorsqu’une collision est détectée avec un tuyau ou lorsque l’oiseau touche le sol ou le haut de l’écran. La partie se termine lorsque toutes les vies sont perdues.

Afin de simplifier votre travail, **l’interface graphique et la structure générale du jeu sont déjà fournies**. Votre tâche consiste à implémenter la logique du jeu :
- le comportement de l’oiseau (gravité + saut),
- la génération et le déplacement des tuyaux,
- la détection des collisions,
- la gestion du score et des vies,
- le redémarrage de la partie.

> **Pour lancer le jeu, vous devez exécuter le fichier `main.py`.**

---

## Installations requises

Ce projet nécessite l’utilisation de la bibliothèque **pygame**, qui permet de créer des jeux 2D en Python.

Assurez-vous que votre environnement conda est activé (par exemple `INF1007`) :

```bash
conda activate INF1007
```

Installez ensuite pygame (version recommandée) :

```bash
pip install -U pygame
```

---

## Informations sur le projet

### Structure du projet

```plaintext
flappy_bird/
├── assets/
│   ├── background-day.png
│   ├── base.png
│   ├── pipe-green.png
│   └── bluebird-midflap.png
├── bird.py
├── pipes.py
├── config.py
├── window.py
├── game.py
└── main.py
```

### Description des fichiers

- **assets/** : contient toutes les images utilisées par le jeu (oiseau, tuyaux, fond, sol).

- **config.py** : constantes globales du jeu :
  - dimensions de la fenêtre (`SCREEN_WIDTH`, `SCREEN_HEIGHT`),
  - dimensions de l’oiseau (`BIRD_SIZE`, `BIRD_X`),
  - dimensions des tuyaux (`PIPE_SIZE`, `MIN_PIPE_GAP`, `MAX_PIPE_GAP`),
  - paramètres physiques (`GRAVITY`, `JUMP_VELOCITY`),
  - vitesse de défilement (`PIPE_SPEED`),
  - nombre de vies (`LIVES`),
  - liste globale des tuyaux (`PIPES`),
  - dictionnaire global de l’oiseau (`bird_dict`).

- **bird.py** :
  - charge et redimensionne l’image de l’oiseau,
  - initialise le dictionnaire `bird_dict` (position, vitesse verticale, vies, score).

- **pipes.py** :
  - charge l’image du tuyau,
  - crée un dictionnaire `pipes_dict` contenant les versions **haut** et **bas** des tuyaux.

- **window.py** :
  - initialise la fenêtre pygame,
  - affiche le fond, le sol, l’oiseau et les tuyaux,
  - génère les paires de tuyaux (`add_pipes`),
  - affiche le score, les vies et le message de fin de partie.

- **game.py** :
  - contient la logique du jeu : gravité, saut, déplacement/suppression des tuyaux,
  - détection des collisions,
  - mise à jour du score.

- **main.py** :
  - point d’entrée du programme,
  - contient la boucle principale du jeu,
  - gère les événements clavier,
  - gère le redémarrage de la partie.
 
Le schéma suivant illustre les variables `SCREEN_WIDTH`, `SCREEN_HEIGHT` et `LANE_HEIGHT`. À noter que la coordonnée `(0,0)` se retrouve en haut à gauche de l'écran du jeu.

<img width="3389" height="4679" alt="Coordonnees_Flappy_Bird" src="https://github.com/user-attachments/assets/97101aa0-cc33-472f-add2-647cd9171d97" />

---

# Travail à réaliser

Vous devez compléter les parties indiquées par `TODO` dans les fichiers **bird.py**, **pipes.py**, **window.py**, **game.py** et **main.py**.

> [!IMPORTANT]
> Plusieurs éléments (affichage, structure générale, boucle d’événements) sont déjà fournis.  
> Prenez le temps de lire et comprendre le code existant avant d’ajouter vos modifications.

---

## PARTIE 1 : L’oiseau 

### 1.1 : Chargement de l’image et redimensionnement

Dans le fichier `bird.py`, vous devez charger l’image représentant l’oiseau à l’aide de la fonction `pygame.image.load()`.

**Indications :**
- L’image de l’oiseau se trouve dans le dossier `assets/`.
- Une fois chargée, l’image doit être redimensionnée à l’aide de `pygame.transform.scale()`.
- Les dimensions finales doivent correspondre exactement à la variable `BIRD_SIZE` définie dans `config.py`.
- L’image redimensionnée doit être stockée dans la variable `bird_img`, qui sera utilisée pour l’affichage dans la fenêtre de jeu.

---

### 1.2 : Initialisation du dictionnaire `bird_dict`

Toujours dans `bird.py`, vous devez initialiser le dictionnaire global `bird_dict`, qui contient l’état courant de l’oiseau.

**Clés à initialiser :**
- `x` : position horizontale initiale de l’oiseau. Vous devez utiliser la constante `BIRD_X`.
- `y` : position verticale initiale. L’oiseau doit être centré verticalement dans la fenêtre. Pour cela, utilisez la variable `SCREEN_HEIGHT`.
- `vel_y` : vitesse verticale initiale, qui doit commencer à `0`.
- `lives` : nombre de vies initiales, défini par la constante `LIVES`.
- `score` : score initial, qui doit commencer à `0`.

À la fin de cette étape, l’oiseau doit apparaître immobile, centré verticalement, lorsqu’on exécute `main.py`.

---

## PARTIE 2 : Les tuyaux 

### 2.1 : Chargement et orientation des images des tuyaux

Dans le fichier `pipes.py`, vous devez préparer les images des tuyaux qui serviront d’obstacles dans le jeu.

⚠️ **Cette étape est obligatoire avant toute génération de tuyaux.**


1. Chargez l’image du tuyau.
2. Redimensionnez immédiatement cette image pour qu'elle soit à la taille de `PIPE_SIZE`.
3. Créez un dictionnaire nommé `pipes_dict` contenant exactement deux clés :
   - `"bottom"` : image du tuyau orientée vers le bas (image normale)
   - `"top"` : image retournée verticalement à l’aide de :
     ```python
     pygame.transform.flip(image, False, True)
     ```

💡 **Rappel** : la fonction `flip` retourne l’image selon l’axe vertical lorsque le deuxième argument vaut `True`.

---

### 2.2 : Génération d’une paire de tuyaux (fonction `add_pipes`)

Cette étape est l’une des plus importantes du projet. Vous devez générer **deux tuyaux liés entre eux** : un en haut et un en bas.

Dans le fichier `window.py`, complétez la fonction `add_pipes()`.

---

#### Étape 1 : Position horizontale

- Les tuyaux doivent apparaître **à droite de l’écran**.
- Calculez la position `x` de départ comme suit :
  ```python
  x = SCREEN_WIDTH + 50
  ```

---

#### Étape 2 : Calcul du gap vertical

- Générez un nombre aléatoire représentant l’espace libre entre les deux tuyaux. Ce nombre doit être compris entre la valeur minimale et la valeur maximale définies pour le "gap" dans le fichier config.py.
- Pour cela, utiliser la fonction random.randint().

---

#### Étape 3 : Position du tuyau du bas

- Choisissez d’abord la position verticale du **tuyau du bas**.
- Cette position doit respecter deux contraintes :
  - ne pas être trop près du bas de l’écran (sinon l’oiseau n’a aucune chance de passer),
  - laisser assez de place pour le tuyau du haut.

💡 **Indication concrète** (vous pouvez reprendre cette logique telle quelle) :
```python
min_bottom_y = ...
max_bottom_y = SCREEN_HEIGHT - ...
bottom_y = random.randint(min_bottom_y, max_bottom_y)
```

---

#### Étape 4 : Calcul du tuyau du haut

- La position `y` du tuyau du haut **ne doit pas être choisie au hasard**.
- Elle doit être calculée à partir du tuyau du bas. Ainsi, calculez `top_y` qui correspond à la position `y` du tuyau du haut.

---

#### Étape 5 : Correction si le tuyau du haut sort de l’écran

- Si le tuyau du haut est trop proche du haut de l’écran, vous devez **corriger les positions**.

💡 Exemple de test :
```python
if top_y + PIPE_SIZE[1] < 100:
    top_y = 100 - PIPE_SIZE[1]
    bottom_y = top_y + PIPE_SIZE[1] + gap
```

⚠️ Le `gap` doit **rester identique** après correction.

---

#### Étape 6 : Création des dictionnaires de tuyaux

Chaque tuyau doit être représenté par un dictionnaire contenant **exactement** les clés suivantes :

```python
{
  "x": ...,
  "y": ...,
  "width": ..., 
  "height": ...,
  "image": ...,
  "passed": False
}
```

- Le tuyau du bas utilise `pipes_dict["bottom"]`
- Le tuyau du haut utilise `pipes_dict["top"]`

---

#### Étape 7 : Ajout à la liste globale

- Ajoutez **les deux dictionnaires** à la liste globale `PIPES`.
- L’ordre n’a pas d’importance, mais les deux doivent être ajoutés.

---

## PARTIE 3 : Physique et déplacements 

### 3.1 : Application de la gravité

Dans le fichier `game.py`, complétez la fonction `apply_gravity()`.

**Principe :** la gravité accélère progressivement l’oiseau vers le bas.

**Étapes à suivre :**
1. Ajouter la valeur `GRAVITY` à la vitesse verticale `vel_y` de l’oiseau.
2. Mettre ensuite à jour la position verticale `y` de l’oiseau en ajoutant `vel_y`.

✅ Cette fonction doit être appelée à chaque itération de la boucle principale afin de simuler une chute continue.

---

### 3.2 : Gestion du saut

Complétez la fonction `jump()` dans `game.py`.

Lorsqu’un saut est déclenché :
1. Réinitialisez d’abord la vitesse verticale `vel_y` à `0`.
2. Appliquez ensuite une impulsion verticale négative à l’aide de la constante `JUMP_VELOCITY`.

✅ Cela permet d’obtenir un saut net et contrôlé, indépendant de la vitesse de chute actuelle.

---

### 3.3 : Déplacement et suppression des tuyaux

Toujours dans `game.py` :

**Déplacement (`move_pipes`)**
- Parcourez la liste `PIPES`
- Pour chaque tuyau, faites :
  - `pipe["x"] -= PIPE_SPEED`

**Suppression (`remove_offscreen_pipes`)**
- Supprimez les tuyaux qui sont entièrement sortis de l’écran par la gauche.
- Condition typique :
  - un tuyau est hors écran si `pipe["x"] + pipe["width"] < 0`

✅ Ces deux fonctions permettent de maintenir un nombre raisonnable de tuyaux et d’assurer un défilement fluide.

---

## PARTIE 4 : Collisions et score 

### 4.1 : Détection des collisions

Dans la fonction `check_collision()` du fichier `game.py`, vous devez vérifier si l’oiseau entre en collision avec un obstacle ou sort de la zone de jeu.

**Indications :**
1. Créez un rectangle représentant l’oiseau à partir de sa position (`x`, `y`) et de ses dimensions (`BIRD_SIZE`).
2. Pour chaque tuyau dans la liste `PIPES`, créez un rectangle similaire à partir de ses propriétés.
3. Vérifiez si les rectangles se chevauchent (collision).
4. Vérifiez également si l’oiseau :
   - touche le sol,
   - dépasse le haut de l’écran.

✅ La fonction doit retourner `True` si une collision est détectée, sinon `False`.

---

### 4.2 : Mise à jour du score

Complétez la fonction `update_score()`.

**Principe :** le score augmente lorsque l’oiseau dépasse un tuyau.

**Étapes à suivre :**
1. Pour chaque tuyau, vérifiez si le tuyau est entièrement derrière l’oiseau.
   - Exemple de condition : `pipe["x"] + pipe["width"] < bird_dict["x"]`
2. Assurez-vous que le tuyau n’a pas déjà été comptabilisé (`passed == False`).
3. Marquez le tuyau comme passé : `pipe["passed"] = True`
4. Ajoutez `0.5` au score.

✅ Chaque paire de tuyaux (haut + bas) rapporte ainsi **1 point** au total.

---

## PARTIE 5 : Boucle principale & redémarrage 

### 5.1 : Générer une première paire de tuyaux

Dans `main.py`, vous devez générer une première paire de tuyaux **avant** que la boucle principale démarre.

- Appelez la fonction `add_pipes()` une première fois au lancement du jeu.

---

### 5.2 : Fonction `restart_game()`

Dans `main.py`, complétez la fonction `restart_game()` pour recommencer une partie.

**Elle doit :**
1. Remettre l’oiseau en position de départ :
   - `x = 100` (ou `BIRD_X`)
   - `y = 512` (ou `SCREEN_HEIGHT // 2`)
2. Remettre la vitesse verticale à `0`
3. Réinitialiser :
   - `lives = 3` (ou `LIVES`)
   - `score = 0`
4. Vider la liste `PIPES` (`PIPES.clear()`)
5. Ajouter une nouvelle paire de tuyaux (`add_pipes()`)

---

### 5.3 : Génération continue des tuyaux

Dans la boucle principale de `main.py`, vous devez générer de nouvelles paires de tuyaux au fur et à mesure.

**Principe :**
- On ajoute une nouvelle paire lorsque la dernière paire est suffisamment avancée vers la gauche.

💡 Indice typique :
- si le dernier tuyau de la liste est rendu à une certaine distance, on ajoute une nouvelle paire.

---

# Directives pour la remise 

Pour remettre votre travail, vous devez créez un fichier zip nommé XXXXX_YYYYY-PR01.zip, où XXXXX est votre nom de famille et YYYYY, votre prénom. Ce fichier zip devra contenir le dossier `2026H-PR01` avec l'ensemble des fichiers du projet.

Votre fichier zip est à remettre dans la boîte de remise sur Moodle prévue à cet effet, le 22 février avant minuit. 

---

# Barème de correction

Le projet est noté sur **20 points**. Le barème détaillé est le suivant :

| **Partie** | **Tâche** | **Points** |
|-----------|----------|------------|
| **PARTIE 1 : L’oiseau 🐦** | | **/4** |
| 1.1 : Chargement de l’image de l’oiseau | | |
| | Image chargée depuis le dossier `assets` | 0.5 |
| | Image redimensionnée avec `BIRD_SIZE` | 0.5 |
| 1.2 : Initialisation du dictionnaire `bird_dict` | | |
| | Position horizontale correcte (`BIRD_X`) | 0.5 |
| | Position verticale centrée dans l’écran | 0.5 |
| | Initialisation correcte de `vel_y`, `lives`, `score` | 1 |
| **PARTIE 2 : Les tuyaux 🟩** | | **/6** |
| 2.1 : Chargement des images des tuyaux | | |
| | Image du tuyau chargée correctement | 0.5 |
| | Redimensionnement avec `PIPE_SIZE` | 0.5 |
| | Création du dictionnaire `pipes_dict` avec tuyau haut et bas | 1 |
| 2.2 : Génération des paires de tuyaux | | |
| | Génération d’un gap aléatoire entre `MIN_PIPE_GAP` et `MAX_PIPE_GAP` | 1 |
| | Positionnement cohérent du tuyau du bas | 1 |
| | Calcul correct de la position du tuyau du haut | 1 |
| **PARTIE 3 : Physique et déplacements 🎮** | | **/5** |
| 3.1 : Gravité | | |
| | Ajout de la gravité à la vitesse verticale | 1 |
| | Mise à jour correcte de la position verticale | 1 |
| 3.2 : Saut | | |
| | Réinitialisation de la vitesse verticale | 0.5 |
| | Application correcte de `JUMP_VELOCITY` | 0.5 |
| 3.3 : Déplacement et suppression des tuyaux | | |
| | Déplacement des tuyaux vers la gauche avec `PIPE_SPEED` | 1 |
| | Suppression des tuyaux hors écran | 1 |
| **PARTIE 4 : Collisions et score 💥** | | **/5** |
| 4.1 : Détection de collision | | |
| | Création correcte des rectangles de collision | 1 |
| | Détection des collisions oiseau / tuyaux | 1 |
| | Détection des collisions avec le sol ou le haut de l’écran | 1 |
| 4.2 : Score | | |
| | Détection du passage de l’oiseau devant un tuyau | 1 |
| | Incrémentation correcte du score (0.5 par tuyau) | 1 |
| **Total** | | **/20** |

---

