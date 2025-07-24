import pygame
import sys

pygame.init()

oyna = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Salom Dunyo")

rang = (0, 0, 0)
x = 250
y = 200
tezlik = 20
sariq = (255, 230, 0)
    

while True:
    for n in pygame.event.get():
        if n.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if n.type == pygame.KEYDOWN:
            if n.key == pygame.K_RIGHT and x < 800-80:
                x += tezlik
            if n.key == pygame.K_LEFT and x > 0:
                x -= tezlik
            if n.key == pygame.K_DOWN and y < 600-80:
                y += tezlik
            if n.key == pygame.K_UP and y > 0:
                y -= tezlik
        if x <= 0 or x>= 800-80 or y <= 0 or y >= 600-80:
           sariq = (255, 0, 0)
        else:
            sariq = (255, 230, 0)   

    oyna.fill(rang)
    pygame.draw.rect(oyna, sariq, (x, y,  80, 80))
    pygame.display.update()