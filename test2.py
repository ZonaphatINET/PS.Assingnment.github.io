import pygame

# initialize Pygame
pygame.init()

# create a window
screen = pygame.display.set_mode((800, 600))

# create nodes
node_1 = pygame.draw.circle(screen, (255, 255, 255), (100, 100), 20)
node_2 = pygame.draw.circle(screen, (255, 255, 255), (200, 200), 20)

# create edges
pygame.draw.line(screen, (255, 255, 255), node_1.center, node_2.center)

# update display
pygame.display.update()

# wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()