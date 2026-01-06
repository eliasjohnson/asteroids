import pygame as p
from pygame.display import update
import constants as c
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
import sys



def main():
    # groups
    asteroids = p.sprite.Group()
    updatable = p.sprite.Group()
    drawable = p.sprite.Group()
    shots = p.sprite.Group()
    

    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = updatable, drawable, shots
    
    print(f"Starting Asteroids with pygame version: {p.version.ver}!")
    print(f"Screen width: {c.SCREEN_WIDTH} \nScreen height: {c.SCREEN_HEIGHT}")

    # start game
    p.init()
    clock = p.time.Clock()
    dt = 0
    frame_rate = 60
    screen = p.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    
    # actual player
    player_ship = Player(
        x=c.SCREEN_WIDTH / 2, y=c.SCREEN_HEIGHT / 2, radius=c.PLAYER_RADIUS
    )
    
    asteroid_f = AsteroidField()

    # endless game loop, only exit on close window event (currently)
    while True:
        log_state()

        # will check for close window event, making the window close button work!
        for event in p.event.get():
            if event.type == p.QUIT:
                return
        screen.fill("black")
        clock.tick(frame_rate)

        # delta time, delta being change in value. in gaming, delta time(dt) is
        # "time that has passed since the last frame was drawn".
        dt = clock.tick(frame_rate) / 1000

        # rotate ship
        # updates the group "updatable" of all updatable objects
        updatable.update(dt)
        
        # iterate through all asteroids in asteroid group, and use collide with method to check if you got hit.
        for asteroid in asteroids:
            if asteroid.collides_with(player_ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        # render
        for item in drawable:
            item.draw(screen)
            
        p.display.flip()

        # update() moves the objects in your data, Changes the game state: positions, velocities, health, timers, etc.
        # draw() paints that data to the off-screen buffer by reading the state (like player.position) and draws sprites at those coordinates onto the screen surface.
        # and flip() shows that buffer. Makes whatever draw() rendered actually appear on the monitor.

if __name__ == "__main__":
    main()
