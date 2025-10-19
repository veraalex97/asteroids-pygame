import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    running = True

    # Sprite Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Asteroid container
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Player
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        # player.update(dt)
        # player.draw(screen)
        updatable.update(dt)
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.kill()
                    shot.kill()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
