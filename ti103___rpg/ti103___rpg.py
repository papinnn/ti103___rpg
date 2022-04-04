"""
docstring = documentation
>>> factorielle(5)
120
"""

def factorielle(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

import pygame
HEIGHT = 16
WIDTH = 24
pygame.init()
window = pygame.display.set_mode((36 * WIDTH,36 * HEIGHT))
pygame.display.set_caption("Mon joli RPG")
run = True
import os
# creer un encodage poir representer vue de carte afficher
#Codec
# .= terrain libre
# # = mur
print(os.getcwd())
carte = """.....#..........
#.....##.....#..
#.....##.....#..
########.....#..
#......#.....#.#
#..##.....####.#
#..##........#.#
#..............#
################
"""

def charge_image():

    image = pygame.image.load("ressource/tuiles.png").convert()
    width, height = image.get_size()
    tuiles = []
    for x in range(width//WIDTH):
        ligne = []
        for y in range(height//HEIGHT):
            rect = (x *WIDTH, y * HEIGHT, WIDTH, HEIGHT)
            ligne.append(image.subsurface(rect))
        tuiles.append(ligne)
    return tuiles

lignes = carte.split("\n")

with open("ressource/tuiles.png","r") as f:
    print(":)")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    tuiles = charge_image()
    lignes = carte.split("\n")
    for i, ligne in enumerate(lignes):         # Ordonnees (lignes)
        for j, caractere in enumerate(ligne):  # Abscisses (colonnes)
            if caractere == '.':
                window.blit(tuiles[0][0], (WIDTH * j, HEIGHT * i))
            if caractere == '#':
                window.blit(tuiles[0][2], (WIDTH * j, HEIGHT * i))
    # for x, ligne in enumerate(charge_image()):
    #     for y, tuile in enumerate(ligne):
    #         tuile = pygame.transform.scale(tuile, (WIDTH * 8, HEIGHT * 8))
    #         window.blit(tuile, (x * (WIDTH * 9), y * (HEIGHT * 9)))
    pygame.display.flip()
pygame.quit()
