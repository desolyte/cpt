import pygame
import random

class PuzzlePiece:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

class PuzzleGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Puzzle Game")
        self.clock = pygame.time.Clock()

        self.pieces = []
        for i in range(1, 17):
            image = pygame.image.load(f"{i} sliding block.png")
            self.pieces.append(PuzzlePiece(image, [0,0]))
        self.positions = [[0, 0], [100, 0], [200, 0], [300, 0],
                          [0, 100], [100, 100], [200, 100], [300, 100],
                          [0, 200], [100, 200], [200, 200], [300, 200],
                          [0, 300], [100, 300], [200, 300], [300, 300]]
        random.shuffle(self.positions)
        for i in range(16):
            self.pieces[i].position = self.positions[i]
            self.pieces[i].rect = self.pieces[i].image.get_rect(topleft=self.pieces[i].position)
        
        self.selected_piece = None
        self.original_position = None
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a piece was clicked
                    for piece in self.pieces:
                        if piece.rect.collidepoint(event.pos):
                            self.selected_piece = piece
                            self.original_position = piece.position
                elif event.type == pygame.MOUSEBUTTONUP:
                    # Check if a piece was dropped
                    if self.selected_piece:
                        for piece in self.pieces:
                            if piece.rect.collidepoint(event.pos):
                                self.selected_piece.position, piece.position = piece.position, self.selected_piece.position
                                self.selected_piece.rect.topleft = self.selected_piece.position
                                piece.rect.topleft = piece.position
                                self.selected_piece = None
                                self.original_position = None

            # Draw puzzle pieces on screen
            for piece in self.pieces:
                self.screen.blit(piece.image, piece.position)

            # Draw selected piece on top of other pieces
            if self.selected_piece:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.screen.blit(self.selected_piece.image, (mouse_x-50, mouse_y-50))

        pygame.display.update()
        self.clock.tick(60)

    pygame.quit()
