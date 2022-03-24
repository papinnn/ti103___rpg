import pygame


pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pavgame")  # le nom du jeu

run = True
shift = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shift -= 10
                shift %= 100

    window.fill((100, 255, 255))
    pygame.draw.circle(window,(255,0,0),(shift,shift),100)

    pygame.display.flip()#jamais oublier pour faire des fenetre en couleur et le remplis de cet couleur
pygame.quit()
