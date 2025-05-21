from pygame import *

# Initialize Pygame and constants
init()
win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong with Scoring")
back_color = (200, 255, 255)
FPS = 60
clock = time.Clock()

# Scoring variables
score1 = 0
score2 = 0
game_over = False

# Font setup
font.init()
score_font = font.Font(None, 50)
win_font = font.Font(None, 80)

# Sprite classes
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x, y))
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

# Create paddles and ball
paddle1 = Player('racket.png', 30, 200, 30, 150, 4)  # Left paddle
paddle2 = Player('racket.png', win_width - 60, 200, 30, 150, 4)  # Right paddle
ball = GameSprite('ball.png', win_width // 2 - 25, win_height // 2 - 25, 50, 50, 4)

# Ball movement direction
dx = ball.speed
dy = ball.speed

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    if not game_over:

        # Move sprites
        paddle1.update_left()
        paddle2.update_right()
        ball.rect.x += dx
        ball.rect.y += dy

        # Collision with top/bottom
        if ball.rect.y <= 0 or ball.rect.y >= win_height - ball.rect.height:
            dy *= -1

        # Collision with paddles
        if sprite.collide_rect(ball, paddle1) or sprite.collide_rect(ball, paddle2):
            dx *= -1
            # Increase speed slightly on each paddle hit
            dx *= 1.05
            dy *= 1.05

        # Check for scoring
        if ball.rect.x < 0:
            score2 += 1
            # Reset ball
            ball.rect.center = (win_width // 2, win_height // 2)
            dx = ball.speed
            dy = ball.speed
        if ball.rect.x > win_width:
            score1 += 1
            ball.rect.center = (win_width // 2, win_height // 2)
            dx = -ball.speed
            dy = ball.speed

        if score1 >= 5:
            win_text = win_font.render("Player 1 Wins!", True, (255, 0, 0))
            game_over = True
        elif score2 >= 5:
            win_text = win_font.render("Player 2 Wins!", True, (255, 0, 0))
            game_over = True

        # Drawing
        window.fill(back_color)
        paddle1.draw()
        paddle2.draw()
        ball.draw()

        # Render scores
        score_text = score_font.render(f"{score1} : {score2}", True, (0, 0, 0))
        text_rect = score_text.get_rect(center=(win_width // 2, 50))
        window.blit(score_text, text_rect)

    if game_over == True:
        win_rect = win_text.get_rect(center=(win_width // 2, win_height // 2))
        window.blit(win_text, win_rect)

    display.update()
    clock.tick(FPS)
