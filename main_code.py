from pygame import *

window = display.set_mode((700, 500))
window.fill((50, 240, 240))

font.init()
font = font.Font(None, 35)
lose1 = font.render("Player 2 wins, player 1 loses", True, (0, 0, 255))
lose2 = font.render("Player 1 wins, player 2 loses", True, (0, 0, 255))

game = True
finish = False
FPS = 60
clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 410:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 410:
            self.rect.y += self.speed
        
player1 = Player("SpritePing-Pong/racket.png", 10, 20, 20, 80, 7)
player2 = Player("SpritePing-Pong/racket.png", 670, 20, 20, 80, 7)

ball = GameSprite("SpritePing-Pong/tenis_ball.png", 327, 247, 40, 40, 2)
speed_x = 2
speed_y = 2


while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((50, 240, 240))
        player1.reset()
        player2.reset()
        ball.reset()
        player1.update1()
        player2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <= 10 or ball.rect.y >= 450:
            speed_y *= -1
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            speed_x *= -1
        if ball.rect.x >= 660:
            window.blit(lose2, (180, 220))
            finish = True
        if ball.rect.x <= 0:
            window.blit(lose1, (180, 220))
            finish = True

    display.update()
    clock.tick(FPS)


