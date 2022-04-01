import pygame

"""

>>> len(charge_image())
12
"""




HEIGHT = 16
WIDTH = 24


pygame.init()
window = pygame.display.set_mode((40 * WIDTH, 40 * HEIGHT))
window.fill((0, 0, 0))
run = True


import os           # Module os de python - Qui permet a Python de communiquer avec Windows
                    # Systeme de fichier de Windows est accessible a travers le module 'os'
print(os.getcwd())  # getcwd = get current working directory, autrement dit, la ou s'execute votre programme

#on creer un encodage pour representer une vue de la carte
#codec
# .=trrain libre
# #=mur
# carte de taille 16 x 16 chaque case fait 24 par 16
#16 x 24 par 16 x 16
carte = """.....................................###
.........####...####.................###
####.....###.....###....................
####.....##.......##....................
####.....###########....................
#............###.......##..##.##........
#............###.......##..##.##........
######..#############............###....
#######..###########............#####...
########..#########............#######..
#########..#######............#########.
##########..#####............###########
....#######..###............############
....########..#............#############
"""


def charge_image():#decoupe l image en 16 rectangle
    image = pygame.image.load("ressources/th.png").convert()
    width, height = image.get_size()
    th = []
    for x in range(width//WIDTH):
      ligne = []
      for y in range(height//HEIGHT):
        rect = (x * WIDTH, y * HEIGHT, WIDTH, HEIGHT)
        ligne.append(image.subsurface(rect))
        th.append(ligne)
    return th

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    th = charge_image()

    lignes = carte.split("\n")
    for i, ligne in enumerate(lignes):  # Ordonnees (lignes)
        for j, caractere in enumerate(ligne):  # Abscisses (colonnes)
            if caractere == '.':
                window.blit(th[0][4], (WIDTH * j, HEIGHT * i))
            if caractere == '#':
                window.blit(th[0][8], (WIDTH * j, HEIGHT * i))


            """
                24    48  72
              +---+---+---+---+----------------+----+> x
            16|0,0|0,1|0,2|0,3|   ...          |0,15|
              +---+---+---+---+                +----+
              |1,0|
              +---+   +---+
              |2,0|   |2,2|
              +---+   +---+
              |
              |
              |
              V
              y
            """

    #for x, ligne in enumerate(charge_image()):
        #for y, tuile in enumerate(ligne):
        #    tuile = pygame.transform.scale(tuile, (WIDTH * 8, HEIGHT * 8))
        #    window.blit(tuile, (x * (WIDTH * 9), y * (HEIGHT * 9)))

    pygame.display.flip()

pygame.quit()

