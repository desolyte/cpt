import pygame
import random

#initialize pygame 
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Puzzle Game")

#load puzzle pieces / create list to store positions
pieces = []
for i in range(1, 17):
    pieces.append(pygame.image.load(f"{i} sliding block.png"))
positions = [[0, 0], [100, 0], [200, 0], [300, 0],
             [0, 100], [100, 100], [200, 100], [300, 100],
             [0, 200], [100, 200], [200, 200], [300, 200],
             [0, 300], [100, 300], [200, 300], [300, 300]]
random.shuffle(positions)

#keep track of selected piece / original position
selected_piece = None
original_position = None

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #check if piece clicked
            for i in range(16):
                if pieces[i].get_rect(topleft=positions[i]).collidepoint(event.pos):
                    selected_piece = i
                    original_position = positions[i]
        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if a piece was dropped
            if selected_piece is not None:
                for i in range(16):
                    if pieces[i].get_rect(topleft=positions[i]).collidepoint(event.pos):
                        print(positions[i])
                        print(positions[selected_piece])
                        temp_pos = positions[i]
                        positions[i] = positions[selected_piece]
                        positions[selected_piece] = temp_pos
                        selected_piece = None
            

    # Draw puzzle pieces on screen
    for i in range(16):
        screen.blit(pieces[i], positions[i])

    # Draw selected piece on top of other pieces
    if selected_piece is not None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(pieces[selected_piece], (mouse_x-50, mouse_y-50))

    pygame.display.update()

pygame.quit()
