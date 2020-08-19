from pygame.locals import *
import pygame.freetype

import time

from turing_machine_func import generate_random_turing_machine
from turing_machine_configurations import create_machine_from_configuration, BACK_AND_FORTH, UNARY_ADDER

from draw_func import *

NUM_SYMBOLS = 10
NUM_STATES = 8
TAPE_LENGTH = 64

AUTO_MOVE_TIME = 0.2

pygame.init()

font = pygame.freetype.SysFont("Courier New", bold=True, size=14)

tm = create_machine_from_configuration(UNARY_ADDER)

screen_width, screen_height = screen_res = (1356, 480)
surface = pygame.display.set_mode(screen_res)
pygame.display.set_caption("Turing Machine")

# Where to draw turing machine
machine_draw_pos = ((screen_width // 2) - 640, 8,)

start_time = time.time()

do_loop = True
while do_loop:
    # Background
    surface.fill(BLACK)

    draw_turing_machine(surface, machine_draw_pos, font, tm)

    if pygame.key.get_pressed()[K_RETURN]:
        if time.time() - start_time > AUTO_MOVE_TIME:
            tm.step()
            start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # The user closed the window!
            do_loop = False  # Stop running
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                tm.step()
            if event.key == K_r:
                tm = generate_random_turing_machine(num_symbols=NUM_SYMBOLS, num_states=NUM_STATES,
                                                    tape_length=TAPE_LENGTH)

    pygame.display.update()

pygame.quit()