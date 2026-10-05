import pygame
import math
import datetime

def hand_tip(cx, cy, length, angle):
    x = cx + length * math.sin(math.radians(angle))
    y = cy - length * math.cos(math.radians(angle))
    return round(x), round(y)

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
cx, cy = 200, 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    h, m, s = now.hour % 12, now.minute, now.second

    s_ang = s * 6
    m_ang = m * 6 + s * 0.1
    h_ang = h * 30 + m * 0.5

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (cx, cy), 150, 3)
    pygame.draw.line(screen, (255, 255, 255), (cx, cy), hand_tip(cx, cy, 80, h_ang), 6)
    pygame.draw.line(screen, (0, 150, 255), (cx, cy), hand_tip(cx, cy, 110, m_ang), 4)
    pygame.draw.line(screen, (254, 0, 0), (cx, cy), hand_tip(cx, cy, 130, s_ang), 2)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()