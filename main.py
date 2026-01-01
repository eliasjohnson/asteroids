import pygame as p
import constants as c
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {p.version.ver}!")
    print(f"Screen width: {c.SCREEN_WIDTH} \nScreen height: {c.SCREEN_HEIGHT}")
    
    #start game
    p.init()
    clock = p.time.Clock()
    dt = 0
    frame_rate = 60
    screen = p.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    
    #endless game loop, only exit on close window event (currently)
    while True:
        log_state()
        
        # will check for close window event, making the window close button work!
        for event in p.event.get():
            if event.type == p.QUIT:
                return
        screen.fill("black")
        p.display.flip()
        clock.tick(frame_rate)

        # delta time, delta being change in value. in gaming, delta time(dt) is
        # "time that has passed since the last frame was drawn".
        dt = clock.tick(frame_rate) / 1000
        

if __name__ == "__main__":
    main()
