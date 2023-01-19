import pygame

# color dictionary
# colors = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}

goal_rects_1 = [
    pygame.Rect(195, 145, 60, 60),  # goal rect for sliding block 1
    pygame.Rect(245, 195, 60, 60),  # goal rect for sliding block 2
    pygame.Rect(295, 245, 60, 60),  # goal rect for sliding block 3
    # pygame.Rect()
]

class Barrier:
    def __init__(self, color, x, y, length, width):
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.rect = pygame.Rect(x, y, length, width)
            
    def collision(self, solid):
        if self.rect.colliderect(solid.rect):
            return True
        else:
            return False



class Draggable(Barrier):
    def __init__(self, color, x, y, length, width):
        super().__init__(color, x, y, length, width)
        self.drag_offset_x = 0
        self.drag_offset_y = 0

    def is_mouse_on(self, mouse_x, mouse_y):
        return self.rect.collidepoint(mouse_x, mouse_y)

    def start_drag(self, mouse_x, mouse_y):
        self.drag_offset_x = self.rect.x - mouse_x
        self.drag_offset_y = self.rect.y - mouse_y

    def continue_drag(self, mouse_x, mouse_y):
        self.rect.x = mouse_x + self.drag_offset_x
        self.rect.y = mouse_y + self.drag_offset_y

class draggableObjectRectangle(Draggable):
    def __init__(self, color, x, y, length, width):
        super().__init__(color, x, y, length, width)
        self.sliding_1 = pygame.image.load("1 sliding block.png").convert()
        self.sliding_2 = pygame.image.load("2 sliding block.png").convert()
        self.sliding_3 = pygame.image.load("3 sliding block.png").convert()
        self.sliding_4 = pygame.image.load("4 sliding block.png").convert()
        self.sliding_5 = pygame.image.load("5 sliding block.png").convert()
        self.sliding_6 = pygame.image.load("6 sliding block.png").convert()
        self.sliding_7 = pygame.image.load("7 sliding block.png").convert()
        self.sliding_8 = pygame.image.load("8 sliding block.png").convert()
        self.rect = pygame.Rect(x, y, length, width)
        self.goal_rect = pygame.Rect(x, y, length, width)

    def draw_sliding_1(self, screen):
        screen.blit(self.sliding_1, (self.rect.x, self.rect.y))
    def draw_sliding_2(self, screen):
        screen.blit(self.sliding_2, (self.rect.x, self.rect.y))
    def draw_sliding_3(self, screen):
        screen.blit(self.sliding_3, (self.rect.x, self.rect.y))
    def draw_sliding_4(self, screen):
        screen.blit(self.sliding_4, (self.rect.x, self.rect.y))
    def draw_sliding_5(self, screen):
        screen.blit(self.sliding_5, (self.rect.x, self.rect.y))
    def draw_sliding_6(self, screen):
        screen.blit(self.sliding_6, (self.rect.x, self.rect.y))
    def draw_sliding_7(self, screen):
        screen.blit(self.sliding_7, (self.rect.x, self.rect.y))
    def draw_sliding_8(self, screen):
        screen.blit(self.sliding_8, (self.rect.x, self.rect.y))
        

    def check_win(self):
        if self.rect.colliderect(self.goal_rect):
            return True
        else:
            return False

    def continue_drag(self, mouse_x, mouse_y):
        super().continue_drag(mouse_x, mouse_y)
        if self.check_win():
            print("Congratulations! You've won the level!")

class Character:
    def __init__(self, color, x, y, width, height, x_speed, y_speed):
        self.color = color
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.x_speed = x_speed        
        self.y_speed = y_speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, screen):
        self.rect.x += self.x_speed
        # self.y_speed += 0.3  # gravity
        self.rect.y += self.y_speed
        self.screen = screen
        
        if self.rect.x+self.rect.width > self.screen.get_width():
            self.x_speed = 0
            self.rect.x = self.screen.get_width() - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
            self.x_speed = 0
        if self.rect.y+self.rect.height > self.screen.get_height():
            self.y_speed = 0
            self.rect.y = self.screen.get_height() - self.rect.height
        if self.rect.y < 0:
            self.rect.y = 0
            self.y_speed = 0

        def char_collision(self, solid):
            if isinstance(solid, Barrier):
                if (self.x < solid.x + solid.width) and (self.x + self.width > solid.x) and (self.y < solid.y + solid.height) and (self.y + self.height > solid.y):
                    self.y_speed = 0
                    self.y = solid.y - self.height
            elif isinstance(solid, draggableObjectRectangle):
                if (self.x < solid.rect.x + solid.rect.width) and (self.x + self.width > solid.rect.x) and (self.y < solid.rect.y + solid.rect.height) and (self.y + self.height > solid.rect.y):
                    self.y_speed = 0
                    self.y = solid.rect.y - self.height

        
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
barrier_rect = pygame.Rect(0, 0, 500, 500)
pygame.display.set_caption("Santa Rush or something")


dragging = False
start_x, start_y = 0,0

# Starting position of the character
x_char_pos = 350
y_char_pos = 250

# Speed and direction of the character
x_char_speed = 0
y_char_speed = 0

# draw character
char = Character(RED, x_char_pos, y_char_pos, 50, 50, x_char_speed, y_char_speed)

# how fast screen updates
clock = pygame.time.Clock()

    

all_slidable_objects = [draggableObjectRectangle(GREEN, 100, 50, 100, 100), draggableObjectRectangle(WHITE, 200, 50, 100, 100)]
char = Character(RED, x_char_pos, y_char_pos, 50, 50, x_char_speed, y_char_speed)

def scene2():
    all_slidable_objects = [draggableObjectRectangle(BLUE, 200, 50, 100, 100), draggableObjectRectangle(BLUE, 300, 300, 50, 100)]
    char = Character(RED, x_char_pos, y_char_pos, 50, 50, x_char_speed, y_char_speed)

def gameover():
    all_slidable_objects = [draggableObjectRectangle(BLUE, 200, 50, 100, 100), draggableObjectRectangle(BLUE, 300, 300, 50, 100)]


current_stage = 0

# bool for closing project
done = False

# -------- main Program Loop -----------
while not done:
    # --- main event loop
    for event in pygame.event.get():
        if current_stage == 0:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_stage = 1
            font = pygame.font.SysFont(None, 24)
            img = font.render('Click Anywhere to Start', True, BLUE)
            screen.blit(img, (20, 20))
            
        if current_stage == 1:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    char.x_speed = -5
                elif event.key == pygame.K_UP:
                    char.y_speed = -5
                elif event.key == pygame.K_RIGHT:
                    char.x_speed = 5
                elif event.key == pygame.K_DOWN:
                    char.y_speed = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    char.x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    char.y_speed = 0
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_x, start_y = event.pos
                for obj in all_slidable_objects:
                    if obj.is_mouse_on(start_x, start_y):
                        obj.start_drag(start_x, start_y)
                        dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    for obj in all_slidable_objects:
                        if obj.is_mouse_on(start_x, start_y):
                            obj.continue_drag(event.pos[0], event.pos[1])
            char.move(screen)
    
        
        for rect1 in all_slidable_objects:
            for rect2 in all_slidable_objects:
                if rect1 != rect2:
                    if rect1.collision(rect2):
                        print(f"rect 1 x {rect1.rect.x}")
                        print(f"rect 2 x {rect2.rect.x}")
                        if rect1.rect.x+rect1.rect.width > rect2.rect.x:# collision moving right
                            rect1.rect.x -= 10
                        if rect1.rect.x < rect2.rect.x+rect2.rect.width:# collision moving left
                            rect1.rect.x += 10
                        if rect1.rect.y < rect2.rect.y+rect2.rect.height:# collision moving up
                            rect1.rect.y += 10
                        if rect1.rect.y+rect1.rect.height > rect2.rect.y:# collision moving down
                            rect1.rect.y -= 10
                        
            # if obj.rect.colliderect(obj_2.rect):
            #     if obj.rect.x+obj.rect.length >= obj_2.rect.x:# checking if on top
            #         dragging = False
            #         obj.rect.x -= 5
            #     if 
    
        # pygame.time.wait(1000)
            
        # --- drawing code 
        # clear the screen to white
        screen.fill(BLUE)
    
        pygame.draw.line(screen, BLACK, (50, 0), (50, 500))
        pygame.draw.line(screen, BLACK, (100, 0), (100, 500))
        pygame.draw.line(screen, BLACK, (150, 0), (150, 500))
        pygame.draw.line(screen, BLACK, (200, 0), (200, 500))
        pygame.draw.line(screen, BLACK, (250, 0), (250, 500))
        pygame.draw.line(screen, BLACK, (300, 0), (300, 500))
        pygame.draw.line(screen, BLACK, (350, 0), (350, 500))
        pygame.draw.line(screen, BLACK, (400, 0), (400, 500))
        pygame.draw.line(screen, BLACK, (450, 0), (450, 500))
        pygame.draw.line(screen, BLACK, (0, 50), (500, 50))
        pygame.draw.line(screen, BLACK, (0, 100), (500, 100))
        pygame.draw.line(screen, BLACK, (0, 150), (500, 150))
        pygame.draw.line(screen, BLACK, (0, 200), (500, 200))
        pygame.draw.line(screen, BLACK, (0, 250), (500, 250))
        pygame.draw.line(screen, BLACK, (0, 300), (500, 300))
        pygame.draw.line(screen, BLACK, (0, 350), (500, 350))
        pygame.draw.line(screen, BLACK, (0, 400), (500, 400))
        pygame.draw.line(screen, BLACK, (0, 450), (500, 450))
    
        # draw everything on the screen
        slidable_1 = all_slidable_objects[0]
        slidable_2 = all_slidable_objects[1]

        slidable_1.draw_sliding_1(screen)
        slidable_2.draw_sliding_2(screen)
        
        for obj in all_slidable_objects:
            if obj.collision(char):
                y_char_speed = -10
        char.draw(screen)
        char.move(screen)
        pygame.draw.rect(screen, BLACK, pygame.Rect(195, 145, 60, 60))
        pygame.draw.rect(screen, BLACK, pygame.Rect(245, 195, 60, 60))
        pygame.draw.rect(screen, BLACK, pygame.Rect(295, 245, 60, 60))
    
        # --- update the screen.
        pygame.display.flip()
    
        # --- 120 frames per second
        clock.tick(120)

# close the window 
pygame.quit()
