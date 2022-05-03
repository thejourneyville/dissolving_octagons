import pygame


# text rendered using blit
def render_text(screen, current_cell_x, current_cell_y, margin_x, screen_height):

    font = pygame.font.Font("./earthorbitertitle.ttf", 15)

    text_surface_x = font.render(str(current_cell_x), True, (50, 50, 50))
    text_rect_x = text_surface_x.get_rect()
    text_rect_x.x, text_rect_x.y = margin_x, screen_height - ((screen_height // 32) * 4)

    text_surface_y = font.render(str(current_cell_y), True, (50, 50, 50))
    text_rect_y = text_surface_y.get_rect()
    text_rect_y.x, text_rect_y.y = (margin_x * 1.5), screen_height - ((screen_height // 32) * 4)

    screen.blit(text_surface_x, text_rect_x)
    screen.blit(text_surface_y, text_rect_y)


# octagons have 8 points naturally :)
def octagon(col, diag_dist, row, side_length):

    return [(col + diag_dist, row),
            (col + diag_dist + side_length, row),
            (col + (diag_dist * 2) + side_length, row + diag_dist),
            (col + (diag_dist * 2) + side_length, row + diag_dist + side_length),
            (col + diag_dist + side_length, row + (diag_dist * 2) + side_length),
            (col + diag_dist, row + (diag_dist * 2) + side_length),
            (col, row + diag_dist + side_length),
            (col, row + diag_dist)]


def square(col, row, poly_size_x, poly_size_y):

    return [(col, row),
            (col + poly_size_x, row),
            (col + poly_size_x, row + poly_size_y),
            (col, row + poly_size_y)]
