import time
import pybullet as p
#import pygame
from hw.servo_pybullet import PyBulletServo
from core.behaviour import Behaviour
#from sim.visualiser import Visualiser

#clock = pygame.time.Clock()
servo = PyBulletServo()
behaviour = Behaviour(servo)
#viz = Visualiser(servo)

last_time = time.time()

print("PyBullet controls:")
print("  S = Sit")
print("  W = Wiggle")
print("  Q = Quit")

running = True
while running:
    now = time.time()
    dt = now - last_time
    last_time = now

#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_s:
#                behaviour.command("SIT")
#            elif event.key == pygame.K_w:
#                behaviour.command("WIGGLE")
# --- PyBullet keyboard input (NON-BLOCKING) ---
    keys = p.getKeyboardEvents()
    KEY_TRIGGERED = 1

    if keys.get(ord('s'), 0) & KEY_TRIGGERED:
        behaviour.command("SIT")

    if keys.get(ord('w'), 0) & KEY_TRIGGERED:
        behaviour.command("WIGGLE")

    if keys.get(ord('q'), 0) & KEY_TRIGGERED:
        running = False
    # --- Update robot ---
    behaviour.update(dt)
    servo.update(dt)
    #viz.draw()
    time.sleep(1/240)  # small sleep is OK
    #clock.tick(60)    # Limit to 60 FPS