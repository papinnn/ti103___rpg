import pygame
"""

>>> len(charge_image())
12
"""




HEIGHT = 16
WIDTH = 24


pygame.init()
window = pygame.display.set_mode((36 * WIDTH, 36 * HEIGHT))
window.fill((255, 255, 255))
run = True


import os           # Module os de python - Qui permet a Python de communiquer avec Windows
                    # Systeme de fichier de Windows est accessible a travers le module 'os'
print(os.getcwd())  # getcwd = get current working directory, autrement dit, la ou s'execute votre programme



def charge_image():#decoupe l image en 16 rectangle
    image = pygame.image.load("ressources/tuiles.png").convert()
    width, height = image.get_size()
    tuiles = []
    for x in range(width//WIDTH):
      ligne = []
      for y in range(height//HEIGHT):
        rect = (x * WIDTH, y * HEIGHT, WIDTH, HEIGHT)
        ligne.append(image.subsurface(rect))
      tuiles.append(ligne)
    return tuiles

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for x, ligne in enumerate(charge_image()):
        for y, tuile in enumerate(ligne):
            tuile = pygame.transform.scale(tuile, (WIDTH * 8, HEIGHT * 8))
            window.blit(tuile, (x * (WIDTH * 9), y * (HEIGHT * 9)))

    pygame.display.flip()

pygame.quit()

