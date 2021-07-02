import pygame
from collections import deque

# WIP

pygame.init()
display_info_object = pygame.display.Info()
margin = 100
screen_width, screen_height = display_info_object.current_w - margin, display_info_object.current_h - (margin * 2)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("dissolving octagons")
clock = pygame.time.Clock()
fps = 60

# math
poly_count_x = 50
poly_count_y = 25

poly_size_y = int((screen_height // poly_count_y) * .75)
poly_size_x = poly_size_y

margin_x = (screen_width - (poly_size_x * poly_count_x)) // 2
margin_y = (screen_height - (poly_size_y * poly_count_y)) // 2

corner_to_center = ((poly_size_x ** 2 + poly_size_x ** 2) ** (1 / 2)) / 2
side_length = poly_size_x - ((poly_size_x - corner_to_center) * 2)
diag_dist = ((side_length * 2 ** (1 / 2)) / 2)

maxlength = 25
fader = deque([], maxlen=maxlength)

while True:

    screen.fill((190, 190, 190))
    clock.tick(fps)

    for event in pygame.event.get():  # able to quit by closing window
        if event.type == pygame.QUIT:
            quit()

    mx, my = pygame.mouse.get_pos()
    current_cell_x = f"x:{mx}"
    current_cell_y = f"y:{my}"

    font = pygame.font.Font("./dissolving_octagons/earthorbitertitle.ttf", 15)
    text_surface_x = font.render(str(current_cell_x), True, (50, 50, 50))
    text_surface_y = font.render(str(current_cell_y), True, (50, 50, 50))
    text_rect_x = text_surface_x.get_rect()
    text_rect_y = text_surface_y.get_rect()
    text_rect_x.x, text_rect_x.y = margin_x, screen_height - ((screen_height // 32) * 4)
    text_rect_y.x, text_rect_y.y = (margin_x * 1.5), screen_height - ((screen_height // 32) * 4)
    screen.blit(text_surface_x, text_rect_x)
    screen.blit(text_surface_y, text_rect_y)

    for r in range(0, poly_size_y * poly_count_y, poly_size_y):
        for c in range(0, poly_size_x * poly_count_x, poly_size_x):
            row = r + margin_y
            col = c + margin_x

            octagon = [(col + diag_dist, row),
                       (col + diag_dist + side_length, row),
                       (col + (diag_dist * 2) + side_length, row + diag_dist),
                       (col + (diag_dist * 2) + side_length, row + diag_dist + side_length),
                       (col + diag_dist + side_length, row + (diag_dist * 2) + side_length),
                       (col + diag_dist, row + (diag_dist * 2) + side_length),
                       (col, row + diag_dist + side_length),
                       (col, row + diag_dist)]

            square = [(col, row),
                      (col + poly_size_x, row),
                      (col + poly_size_x, row + poly_size_y),
                      (col, row + poly_size_y)]

            if col <= mx < (col + poly_size_x):
                if row <= my < (row + poly_size_y):
                    fader.appendleft((col, row))
                    pygame.draw.polygon(screen, (255, 0, 0), octagon)

            # pygame.draw.polygon(screen, (0, 0, 175), square, 1)
            # pygame.draw.polygon(screen, (255, 69, 0), octagon, 1)

    if len(set(fader)) > 1:
        for idx in range(len(fader)):
            col_p = fader[idx][0]
            row_p = fader[idx][-1]
            octagon_p = ((col_p + diag_dist, row_p),
                         (col_p + diag_dist + side_length, row_p),
                         (col_p + (diag_dist * 2) + side_length, row_p + diag_dist),
                         (col_p + (diag_dist * 2) + side_length, row_p + diag_dist + side_length),
                         (col_p + diag_dist + side_length, row_p + (diag_dist * 2) + side_length),
                         (col_p + diag_dist, row_p + (diag_dist * 2) + side_length),
                         (col_p, row_p + diag_dist + side_length),
                         (col_p, row_p + diag_dist))

            pygame.draw.polygon(
                    screen,
                    (idx * int(220 // maxlength), idx * int(220 // maxlength), idx * int(220 // maxlength)),
                    octagon_p)

            if idx == len(fader) - 1:
                pygame.draw.polygon(
                    screen,
                    (255, 69, 0),
                    octagon_p)

    pygame.display.update()
