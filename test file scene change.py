##
# Scene Change demo - extends the Ball demo
# Here we use a variable to control which scene we are in.  
# Useful for instructions title and instruction screens or 
# even handling different levels.
#
# author: Mr. Reid
# course: ICS3UC
# Based on template from programarcadegames.com   

# Import a library of functions called 'pygame'
import pygame
import random

# Define Classes here
class Ball:
    # Attributes
    x = 0
    y = 0
    colour = (0, 0, 0)
    x_speed = 10
    y_speed = 10
    
    # Draw the ball
    def draw(self):    
        x = self.x
        y = self.y
        pygame.draw.ellipse(screen, self.colour, [x, y, 10, 10], 0)

    # Move the ball
    def move(self):
        self.x += self.x_speed
        self.y_speed += 2
        self.y += self.y_speed

        # Check the walls
        if (self.x >= screen.get_width()):
            self.x_speed = self.x_speed * -1
            self.x = screen.get_width()
        elif (self.x <= 0):
            self.x_speed = self.x_speed * -1
            self.x = 0
        if (self.y > screen.get_height()):
            self.y_speed = self.y_speed * -0.9
            self.y = screen.get_height()
        elif (self.y <= 0):
            self.y_speed = self.y_speed * -0.9
            self.y = 5
            

# Subprograms here
def drawScene0():
    # Intro
    font = pygame.font.SysFont("comicsansms", 50)
    startMsg = font.render("Click to Start", True, (0, 128, 0))
    pygame.draw.rect(screen, GREEN, [0,0,800,500], 0)
    screen.blit(startMsg,(100, 100))
    

def drawScene1():
    # Draw the model where it is
    for ball in ballList:
        ball.draw()

## MODEL 
# Define some colors
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
 
# Initialize pygame stuff
pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Scene Demo")
clock = pygame.time.Clock()

# Setup initial balls
ballList = []
for i in range(40):
    ball = Ball()
    ball.pos = [random.randint(50, 350), random.randrange(0, 300)]
    ball.speed = [random.randint(-10, 10), random.randrange(-10, 10)]
    ball.colour = [random.randint(0, 255), random.randrange(0, 255), random.randint(0,255)]
    ballList.append(ball)

# Variable to control which scene we are on
scene = 0


# Main Game Loop
done = False
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        # Time to quit
        if (event.type == pygame.QUIT): 
            done = True 
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            # Change the scene
            scene = scene + 1
            if (scene == 2):
                # Reset everything
                scene = 0
                for ball in ballList:
                    ball.pos = [random.randint(100, 700), 
                                random.randrange(0, 300)]
                    ball.speed = [random.randint(-10, 10),
                                random.randrange(-10, 10)]
                                    
    # Modify the MODEL depending on the scene
    if (scene == 1):
        for ball in ballList:
            ball.move();
    
    ## VIEW
    screen.fill(WHITE)

    # Which scene are we in
    if (scene == 0):
        drawScene0()
    elif (scene == 1):
        drawScene1()

    # Update the screen
    pygame.display.flip()
    clock.tick(40)
      
# Close the window and quit
pygame.quit()
