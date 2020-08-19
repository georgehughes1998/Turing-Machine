import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(100, 100, 145)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(64, 128, 255)
YELLOW = pygame.Color(255, 255, 0)


def draw_text(surface, text, font, pos, color):
    text_surface, text_rect = font.render(text, fgcolor=color)
    text_rect.topleft = pos
    surface.blit(text_surface, text_rect)


def draw_turing_machine(surface, pos, font, turing_machine):
    x, y = pos
    width, height = 1300, 72

    draw_color = WHITE
    tape_text_color = GREEN
    if turing_machine.is_halted():
        draw_color = RED
        tape_text_color = WHITE

    pygame.draw.rect(surface, WHITE, (x, y, width, height), 2)

    tape = turing_machine.get_tape()
    head_pos = turing_machine.get_head_pos()
    for pos in tape:
        if pos > head_pos - 19 and pos < head_pos + 19:
            draw_pos = (( (pos - head_pos) * 32) + (width // 2), y + height // 2, 30, 30)
            pygame.draw.rect(surface, draw_color, draw_pos, 0)
            pygame.draw.rect(surface, GREY, draw_pos, 2)
            draw_text(surface, tape[pos], font, (draw_pos[0] + 4, draw_pos[1] + 8), tape_text_color)

    head = 0
    polypos = ((head * 32 + (width // 2), y - 16 + height // 2),
               (head * 32 + (width // 2) + 32, y - 16 + height // 2),
               (head * 32 + (width // 2) + 16, y + height // 2))
    draw_pos = ((head * 32) + (width // 2), y - 38 + height // 2, 32, 32)
    pygame.draw.polygon(surface, draw_color, polypos, 0)
    pygame.draw.polygon(surface, WHITE, polypos, 2)
    draw_text(surface, f"{turing_machine.get_state()} ({head_pos})", font, (draw_pos[0] + 4, draw_pos[1] + 8), BLUE)

    rules = turing_machine.get_rules()
    last_move = turing_machine.get_last_move()
    next_move = turing_machine.get_next_move()

    if last_move:
        last_move = last_move[0]
    if next_move:
        next_move = next_move[0]
    yoff = 0
    for r in rules:
        text = f"{r}->{rules[r]}"
        move_colour = draw_color

        if last_move == r:
            text = "[L]" + text
            move_colour = GREEN
        if next_move == r:
            text = "[N]" + text
            move_colour = YELLOW

        rules_draw_by_rows = False
        if rules_draw_by_rows:
            # Draw rules by rows
            num_rule_rows = 4
            rule_text_x = x + (yoff%num_rule_rows)*340
            rule_text_y = y + 90 + (yoff - yoff%num_rule_rows)*4
        else:
            # Draw rules by columns
            num_rule_col = 22
            rule_text_y = y + 90 + (yoff%num_rule_col)*16
            rule_text_x = x + (yoff - yoff % num_rule_col) * 15
        rule_text_pos = (rule_text_x, rule_text_y)

        draw_text(surface, text, font, rule_text_pos, move_colour)
        yoff += 1
