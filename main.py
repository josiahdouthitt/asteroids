# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

import sys

from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        
        for thing in asteroids:
            if thing.is_collide(p):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if shot.is_collide(thing):
                    thing.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()