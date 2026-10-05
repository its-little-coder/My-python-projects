import pygame, random, math

class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        angle = math.atan2(dy, dx)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)

    def check_collision(self, t_x, t_y):
        dx = t_x - self.x
        dy = t_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance < 30

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
x, y = 300, 200
enemies = [Enemy(0, 0, 2), Enemy(600, 0, 2), Enemy(300, 400, 2)]
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 255), (x, y), 20)

    for e in enemies:
        e.move_towards(x, y)

        # Collision check MUST be inside the for loop
        if e.check_collision(x, y):
            print("Game Over!")
            seconds = (pygame.time.get_ticks() - start_time) / 1000
            with open("highscore.txt", "a") as file:
                file.write(str(seconds) + "\n")
            running = False

        pygame.draw.circle(screen, (255, 0, 0), (round(e.x), round(e.y)), 20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()