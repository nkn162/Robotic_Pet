import time
import pygame
from hw.servo_sim import SimServo
from core.behaviour import Behaviour
from sim.visualiser import Visualiser

clock = pygame.time.Clock()
servo = SimServo()
behaviour = Behaviour(servo)
viz = Visualiser(servo)

last_time = time.time()

running = True
while running:
    now = time.time()
    dt = now - last_time
    last_time = now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                behaviour.command("SIT")
            elif event.key == pygame.K_w:
                behaviour.command("WIGGLE")

    behaviour.update(dt)
    servo.update(dt)
    viz.draw()

    clock.tick(60)    # Limit to 60 FPS