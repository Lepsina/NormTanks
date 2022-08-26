import sys, pygame
def all_control(ship):
    """Считывание событий всей программы"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.mright = True
            elif event.key == pygame.K_a:
                ship.mleft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.mright = False
            elif event.key == pygame.K_a:
                ship.mleft = False
