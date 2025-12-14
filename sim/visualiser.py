import pygame

class Visualiser:
    def __init__(self, servo):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.servo = servo

    def draw(self):
        self.screen.fill((30, 30, 30))

        # body
        pygame.draw.rect(self.screen, (200,200,200), (150,120,100,50))

        # legs (very simplified)
        for name, angle in self.servo.angles.items():
            x = 170 if "L" in name else 230
            y = 170 if "F" in name else 190
            pygame.draw.line(self.screen, (255,255,255),
                             (x, y),
                             (x + 20, y + (angle-90)/2), 4)

        pygame.display.flip()