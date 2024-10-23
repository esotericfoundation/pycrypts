import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

imp = pygame.image.load("./assets/characters/pro.png").convert()

imp = pygame.transform.scale(imp, (64, 64))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))

    distance_travelled = pygame.Vector2()

    if keys[pygame.K_w]:
        distance_travelled.y -= 1
    if keys[pygame.K_s]:
        distance_travelled.y += 1
    if keys[pygame.K_a]:
        distance_travelled.x -= 1
    if keys[pygame.K_d]:
        distance_travelled.x += 1

    if distance_travelled.magnitude_squared() != 0:
        distance_travelled = distance_travelled.normalize() * 225 * dt

        player_pos.x += distance_travelled.x
        player_pos.y += distance_travelled.y

    screen.blit(imp, (player_pos.x, player_pos.y))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
