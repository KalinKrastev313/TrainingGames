import pygame
import os

width, height = 900, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("First game")

FPS = 60
spaceship_width = 55
spaceship_height = 44
yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 90)
red_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height))
red_spaceship = pygame.transform.rotate(red_spaceship, 270)


def draw_window(red, yellow):
    win.fill((255, 255, 255))
    win.blit(yellow_spaceship, (300, 100))
    win.blit(red_spaceship, (700, 100))
    pygame.display.update()


def main():
    red = pygame.Rect(100, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(700, 300, spaceship_width, spaceship_height)
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

mamamia