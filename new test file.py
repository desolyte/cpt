import pygame
import sys
import random
import math

"""random.randrange(0, 2) USE THIS"""


class PuzzleBlock:
    def __init__(self, image, x, y, puzzle_x, puzzle_y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.puzzle_x = puzzle_x
        self.puzzle_y = puzzle_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Puzzle:
    def __init__(self, blocks, x, y):
        self.blocks = blocks
        self.x = x
        self.y = y
        self.puzzle_positions = []
        for j in range(3):
            row = []
            for i in range(3):
                position = (i * 100, j * 100)
                row.append(position)
            self.puzzle_positions.append(row)
        self.drag_block = None

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)
        for row in self.puzzle_positions:
            for position in row:
                pygame.draw.circle(screen, (255, 0, 0), position, 5)
        
    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for block in self.blocks:
                    if block.rect.collidepoint(event.pos):
                        self.drag_block = block
                        self.offset_x = event.pos[0] - block.rect.x
                        self.offset_y = event.pos[1] - block.rect.y
                        break
        elif event.type == pygame.MOUSEMOTION:
            if self.drag_block:
                self.drag_block.rect.x = event.pos[0] - self.offset_x
                self.drag_block.rect.y = event.pos[1] - self.offset_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for i in range(3):
                    for j in range(3):
                        if self.drag_block.rect.collidepoint(self.puzzle_positions[i][j]):
                            self.drag_block.puzzle_x = i
                            self.drag_block.puzzle_y = j
                self.drag_block = None

    def check_puzzle_solved(self):
        for block in self.blocks:
            distance = math.sqrt((block.rect.x - block.puzzle_x*100)**2 + (block.rect.y - block.puzzle_y*100)**2)
            if distance > 10:
                return False
        return True
        for block in self.blocks:
            block.rect.x = block.puzzle_x * 100
            block.rect.y = block.puzzle_y * 100
            block.draggable = False
        return True
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

size = (700, 700)
screen = pygame.display.set_mode(size)

# Define block images and load images for the blocks
block1 = pygame.image.load("1 sliding block.png")
block2 = pygame.image.load("2 sliding block.png")
block3 = pygame.image.load("3 sliding block.png")
block4 = pygame.image.load("4 sliding block.png")
block5 = pygame.image.load("5 sliding block.png")
block6 = pygame.image.load("6 sliding block.png")
block7 = pygame.image.load("7 sliding block.png")
block8 = pygame.image.load("8 sliding block.png")
block9 = pygame.image.load("9 sliding block.png")
block_images = [block1, block2, block3, block4, block5, block6, block7, block8, block9]

# Create the blocks and add them to a list
blocks = []
for i in range(9):
    block = PuzzleBlock(block_images[i], i * random.randrange(0, 70), i * random.randrange(0, 70), i, i)
    blocks.append(block)

# Create the puzzle
puzzle = Puzzle(blocks, 0, 0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        puzzle.handle_input(event)

        # Draw the puzzle
        screen.fill(BLUE)

        puzzle.draw(screen)

        if puzzle.check_puzzle_solved():
            print("Puzzle solved!")

        pygame.display.flip()

pygame.quit()
