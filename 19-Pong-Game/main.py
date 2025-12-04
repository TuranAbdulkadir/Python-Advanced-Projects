import pygame
pygame.init()

win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Pong Game")

white = (255, 255, 255)
black = (0, 0, 0)

class Paddle(pygame.Rect):
    def __init__(self, x, y, w, h, speed):
        super().__init__(x, y, w, h)
        self.speed = speed
    def move(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up] and self.y > 0: self.y -= self.speed
        if keys[down] and self.y < 400: self.y += self.speed

p1 = Paddle(10, 200, 10, 100, 5)
p2 = Paddle(730, 200, 10, 100, 5)
ball = pygame.Rect(375, 250, 10, 10)
ball_speed = [4, 4]

run = True
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    p1.move(pygame.K_w, pygame.K_s)
    p2.move(pygame.K_UP, pygame.K_DOWN)

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.y <= 0 or ball.y >= 490: ball_speed[1] *= -1
    if ball.colliderect(p1) or ball.colliderect(p2): ball_speed[0] *= -1
    if ball.x <= 0 or ball.x >= 750: ball.x, ball.y = 375, 250

    win.fill(black)
    pygame.draw.rect(win, white, p1)
    pygame.draw.rect(win, white, p2)
    pygame.draw.ellipse(win, white, ball)
    pygame.display.update()

pygame.quit()