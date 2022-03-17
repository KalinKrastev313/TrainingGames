import pygame
import os

width, height = 900, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("First game")

FPS = 60

yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.scale(yellow_spaceship_image, (55, 44))
red_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.scale(red_spaceship_image, (55, 44))


def draw_window():
    win.fill((255, 255, 255))
    win.blit(yellow_spaceship_image, (300, 100))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    pygame.quit()



if __name__ == "__main__":
    main()