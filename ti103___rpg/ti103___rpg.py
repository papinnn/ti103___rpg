import pygame


pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pavgame")  # le nom du jeu

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
