import pygame
import os

width, height = 900, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("First game")

FPS = 60
vel = 5
bullet_vel = 7
border = pygame.Rect(width/2 - 5, 0, 10, height)
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
    pygame.draw.rect(win, (0, 0, 0), pygame.Rect(width/2 - 5, 0, 10, height))
    win.blit(yellow_spaceship, (yellow.x, yellow.y))
    win.blit(red_spaceship, (red.x, red.y))
    pygame.display.update()


def yellow_rectangle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - vel > border.x:
        yellow.x -= vel
    elif keys_pressed[pygame.K_RIGHT] and yellow.x + vel + yellow.width < width:
        yellow.x += vel
    elif keys_pressed[pygame.K_UP] and yellow.y - vel > 0:
        yellow.y -= vel
    elif keys_pressed[pygame.K_DOWN] and yellow.y + vel + yellow.height < height:
        yellow.y += vel


def red_rectangle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - vel > 0:
        red.x -= vel
    elif keys_pressed[pygame.K_d] and red.x + vel + red.width < border.x:
        red.x += vel
    elif keys_pressed[pygame.K_w] and red.y - vel > 0:
        red.y -= vel
    elif keys_pressed[pygame.K_s] and red.y + vel + red.height < height:
        red.y += vel


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if bullet.colliderect():


def main():
    red = pygame.Rect(100, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(700, 300, spaceship_width, spaceship_height)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height / 2, 10, 5)
                    red_bullets.append(bullet)
                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2, 10, 5)
                    yellow_bullets.append(bullet)

        print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_rectangle_movement(keys_pressed, yellow)
        red_rectangle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
