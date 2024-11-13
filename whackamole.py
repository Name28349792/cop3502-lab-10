# whack-a-mole game
import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_location = (0, 0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    print(pos)
                    if pos[0] in range(mole_location[0], mole_location[0] + 32) and pos[1] in range(mole_location[1], mole_location[1] + 32):
                        mole_location = (random.randrange(0, 21) * 32, random.randrange(0, 17) * 32)
            screen.fill("light green")
            for i in range(0, 640, 32):
                pygame.draw.line(screen, "black", (i, 0), (i, 512))
            for i in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, i), (640, i))
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_location))
            mouse = pygame.MOUSEBUTTONDOWN
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
