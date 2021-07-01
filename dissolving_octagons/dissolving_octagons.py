import pygame

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
poly_count_x = 20
poly_count_y = 10

poly_size_y = int((screen_height // poly_count_y) * .75)
poly_size_x = poly_size_y

margin_x = (screen_width - (poly_size_x * poly_count_x)) // 2
margin_y = (screen_height - (poly_size_y * poly_count_y)) // 2
sp_x, sp_y = margin_x, margin_y

corner_to_center = ((poly_size_x ** 2 + poly_size_x ** 2) ** (1 / 2)) / 2
side_length = poly_size_x - ((poly_size_x - corner_to_center) * 2)
diag_dist = (side_length * 2 ** (1 / 2)) / 2

while True:

    screen.fill((0, 0, 0))
    clock.tick(fps)

    for event in pygame.event.get():  # able to quit by closing window
        if event.type == pygame.QUIT:
            quit()

    mx, my = pygame.mouse.get_pos()
    current_cell_x = f"x:{mx}"
    current_cell_y = f"y:{my}"

    font = pygame.font.Font("./dissolving_octagons/earthorbitertitle.ttf", 20)
    text_surface_x = font.render(str(current_cell_x), True, (200, 0, 0))
    text_surface_y = font.render(str(current_cell_y), True, (200, 0, 0))
    text_rect_x = text_surface_x.get_rect()
    text_rect_y = text_surface_y.get_rect()
    text_rect_x.centerx = screen_width // 2
    text_rect_y.centery = screen_height // 2
    text_rect_x.y = screen_height - (screen_height // 32) * 3
    text_rect_y.x = (screen_width // 128) * 3
    screen.blit(text_surface_x, text_rect_x)
    screen.blit(text_surface_y, text_rect_y)

    for r in range(0, poly_size_y * poly_count_y, poly_size_y):
        for c in range(0, poly_size_x * poly_count_x, poly_size_x):
            row = r + sp_y
            col = c + sp_x

            octagon = [(col + diag_dist, row), (col + diag_dist + side_length, row),
                       (col + (diag_dist * 2) + side_length, row + diag_dist),
                       (col + (diag_dist * 2) + side_length, row + diag_dist + side_length),
                       (col + diag_dist + side_length, row + (diag_dist * 2) + side_length),
                       (col + diag_dist, row + (diag_dist * 2) + side_length), (col, row + diag_dist + side_length),
                       (col, row + diag_dist)]



            pygame.draw.polygon(screen, (0, 0, 175),
                [(col, row),
                 (col + poly_size_x, row),
                 (col + poly_size_x, row + poly_size_y),
                 (col, row + poly_size_y)], 1)

            pygame.draw.polygon(screen, (255, 69, 0), octagon, 1)





    pygame.display.update()
