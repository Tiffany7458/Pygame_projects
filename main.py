import pygame
import random
import time

WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 842
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

TITLE = "<WUKONG>"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/wukong.png")
        self.image = pygame.transform.scale(self.image, (160, 141))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.x_vel = 0
        self.y_vel = 0
        self.player_speed = 5

        self.score = 0

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def up(self):
        self.y_vel = -5

    def down(self):
        self.y_vel = 5

    def left(self):
        self.x_vel = -5

    def right(self):
        self.x_vel = 5

    def stop(self):
        self.x_vel = 0
        self.y_vel = 0


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/background.jpg")
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (0, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("./images/baigujing.png")
        self.image = pygame.transform.scale(self.image, (106, 147))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )
        self.x_vel = random.choice((-5, -3, 3, 5))
        self.y_vel = random.choice((-5, -3, 3, 5))

    def update(self) -> None:
        # Keep the enemy inside the screen
        self.rect.x += self.x_vel

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = -self.x_vel
        if self.rect.left <= 0:
            self.rect.left = 0
            self.x_vel = -self.x_vel

        self.rect.y += self.y_vel

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel
        if self.rect.top <= 0:
            self.rect.top = 0
            self.y_vel = -self.y_vel


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100
    nun_enemies = 10
    score = 0
    time_start = time.time()
    time_invincible = 5
    game_state = "running"
    endgame_cooldown = 5
    time_ended = 0.0

    font = pygame.font.SysFont("Arial", 25)
    pygame.mouse.set_visible(False)

    all_sprites = pygame.sprite.Group()
    background_sprite = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    background_sprite.add(Background())

    for i in range(nun_enemies):
        enemy = Enemy()
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)

    player = Player()
    all_sprites.add(player)
    pygame.mouse.set_visible(True)


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Player Movement
        if pygame.key.get_pressed()[pygame.K_UP]:
            player.up()
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            player.down()
        else:
            player.y_vel = 0
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            player.left()
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            player.right()
        else:
            player.x_vel = 0

        if player.score == nun_enemies:
            game_state = "won"
            if time_ended == 0:
                time_ended = time.time()
            if time.time() - time_ended >= endgame_cooldown:
                done = True

        # Update
        all_sprites.update()

        # Eat the enemies
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, True)
        for enemy in enemies_collided:
            player.score += 1


        # Draw
        background_sprite.draw(screen)
        all_sprites.draw(screen)

        pygame.display.flip()







if __name__ == "__main__":
    main()



