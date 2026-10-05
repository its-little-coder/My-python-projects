import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

x, y = 300, 200

def spawn_enemy():
    side = random.choice(["top", "bottom", "left", "right"])
    if side == "top":
        return {"x": random.randint(0,600), "y": 0, "speed": 2}
    elif side == "bottom":
        return {"x": random.randint(0,300*2), "y": 400, "speed": 2}
    elif side == "left":
        return {"x": 0, "y": random.randint(0,400), "speed": 2}
    else:
        return {"x": 600, "y": random.randint(0,400), "speed": 2}

enemies = [spawn_enemy(), spawn_enemy(), spawn_enemy()]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()

    for enemy in enemies:
        dx = x - enemy["x"]
        dy = y - enemy["y"]
        angle = math.atan2(dy, dx)
        enemy["x"] += enemy["speed"] * math.cos(angle)
        enemy["y"] += enemy["speed"] * math.sin(angle)

        distance = math.sqrt((x-enemy["x"])**2 + (y-enemy["y"])**2)
        if distance < 40:
            print("Game Over!")
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 20)
    for enemy in enemies:
        pygame.draw.circle(screen, (255, 0, 0), (int(enemy["x"]), int(enemy["y"])), 20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()