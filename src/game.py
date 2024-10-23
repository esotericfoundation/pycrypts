import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()

    distance_travelled = pygame.Vector2()

    if keys[pygame.K_w]:
        distance_travelled.y -= 300 * dt
    if keys[pygame.K_s]:
        distance_travelled.y += 300 * dt
    if keys[pygame.K_a]:
        distance_travelled.x -= 300 * dt
    if keys[pygame.K_d]:
        distance_travelled.x += 300 * dt

    if distance_travelled.magnitude_squared() != 0:
        distance_travelled = distance_travelled.normalize() * 5

        player_pos.x += distance_travelled.x
        player_pos.y += distance_travelled.y

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
