import pygame
import os

pygame.init()

clock = pygame.Clock()

screen = pygame.display.set_mode((500, 500))
screen_rect = screen.get_rect()

comicsans = pygame.Font("assets/COMIC.TTF")
lose_text = comicsans.render(
    "HAHAHAHA YOU LOSE MUAHAHAHHAHAHAHAHAHAHA (R to restart btw)",
    True,
    "White",
    wraplength=500,
)

game_screen = pygame.image.load("assets/nahidwin.png")
game_screen = pygame.transform.grayscale(game_screen)

lost_screen = pygame.image.load("assets/megamind.png")
dino_standing = pygame.image.load("assets/standingdino.png")
dino_jumping = pygame.image.load("assets/standingdino.png")
cheese = pygame.image.load("assets/cheese.png")
bg = game_screen

game_over = False

jump_counter = 0


dino = dino_standing
dino_rect = dino.get_frect(bottomleft=(120, 500))
cheese_counter = 0

xpos_dino, ypos_dino = 120, 500
ygravity = 1
jumpvelocity = 16
moved = 0
yvelocity_dino = 0
jump = False

cheese_rect = cheese.get_frect(bottomleft=(500, 500))

xpos_cheese, ypos_cheese = (500, 500)
xvelocity_cheese = 1

while True:
    clock.tick(60)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            os.system("cls")
            raise (SystemExit)

    keys = pygame.key.get_just_pressed()

    yvelocity_dino -= ygravity
    ypos_dino -= yvelocity_dino

    xpos_cheese -= xvelocity_cheese

    if jump_counter % 10 == 0:
        xvelocity_cheese += 0.1

    if ypos_dino > 500:
        ypos_dino = 500

    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and ypos_dino == screen_rect.height:
        yvelocity_dino = jumpvelocity
        dino = dino_standing
        jump_counter += 1
    else:
        dino = dino_standing

    if xpos_cheese < -59:
        xpos_cheese = 500
        if not game_over:
            cheese_counter += 1

    dino_rect = dino.get_frect(bottomleft=(xpos_dino, ypos_dino))
    cheese_rect = cheese.get_frect(bottomleft=(xpos_cheese, ypos_cheese))

    if dino_rect.colliderect(cheese_rect):
        game_over = True
    if game_over:
        bg = lost_screen

    screen.fill("black")
    screen.blit(bg, (0, 0))

    score_text = comicsans.render(f"Score: {cheese_counter}", True, "yellow", "black")
    screen.blit(score_text, (0, 0))

    if not game_over:
        screen.blit(dino, dino_rect)
        screen.blit(cheese, cheese_rect)
    else:
        screen.blit(lose_text, lose_text.get_rect(bottomleft=screen_rect.bottomleft))
        if keys[pygame.K_r]:
            game_over = False
            jump_counter = 0
            bg = game_screen

            xpos_dino, ypos_dino = 120, 500
            ygravity = 1
            jumpvelocity = 16
            moved = 0
            yvelocity_dino = 0
            jump = False

            cheese_rect = cheese.get_frect(bottomleft=(500, 500))

            xpos_cheese, ypos_cheese = (500, 500)
            xvelocity_cheese = 1

    pygame.display.update()
