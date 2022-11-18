#
# Maze generator, recursive backtracker (https://en.wikipedia.org/wiki/Maze_generation_algorithm)
#
# --------------------------------------------------------------------------------
# Imports

import random
import os

from settings import *


# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

class Setup:
    
    def __init__(self):

        # Game window
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.grid = [[0] * SQX for _ in range(SQY)]
        self.stack = []
        self.maze = [[0] * (SQX*2 - 1) for _ in range(SQY*2 - 1)]

        for j in range(SQX):
            for i in range(SQY):
                self.grid[i][j] = Place(i, j)

        self.current = self.grid[0][0]
        self.current.visited = True

        self.calculating = True
        self.next = self.random_neighbor()

    def run(self):
        
        # Main loop
        while self.calculating:
            self.clock.tick(FPS/2)
            self.draw()
            pygame.display.flip()
            self.calculate()
            self.events()
            
        #pygame.quit()
    
    def events(self):
        for event in pygame.event.get():

            # Exit when pressing X
            if event.type == pygame.QUIT:
                if self.calculating:
                    self.calculating = False
                    pygame.quit()
                    # quit()

    def calculate(self):
        if self.next:
            self.next.visited = True
            self.remove_wall()

            self.stack.append(self.current)
            
            self.current = self.next
        elif len(self.stack) > 0:
            self.current = self.stack.pop()

    def random_neighbor(self):
        neighbors = []
        x = self.current.i
        y = self.current.j

        if y - 1 >= 0 and not self.grid[x][y-1].visited:
            neighbors.append(self.grid[x][y-1])
            
        if x + 1 <= SQY-1 and not self.grid[x+1][y].visited:
            neighbors.append(self.grid[x+1][y])
            
        if y + 1 <= SQY-1 and not self.grid[x][y+1].visited:
            neighbors.append(self.grid[x][y+1])
            
        if x - 1 >= 0 and not self.grid[x-1][y].visited:
            neighbors.append(self.grid[x-1][y])      

        if len(neighbors) > 0:
            return random.choice(neighbors)
        
        else:
            return False

    def remove_wall(self):
        x = self.current.i - self.next.i
        y = self.current.j - self.next.j
        
        if x < 0:
            self.current.wall[1] = False  # Right
            self.next.wall[3] = False
        elif x > 0:
            self.current.wall[3] = False  # Left
            self.next.wall[1] = False
        elif y > 0:
            self.current.wall[0] = False  # Top
            self.next.wall[2] = False
        elif y < 0:
            self.current.wall[2] = False  # Bottom
            self.next.wall[0] = False
        
    def draw(self):
        self.win.fill(BG)
        for j in range(SQX):
            for i in range(SQY):
                x, y = self.grid[i][j].i * SIZE, self.grid[i][j].j * SIZE
                if self.grid[i][j].wall[0]:
                    pygame.draw.line(self.win, WHITE, (x, y), (x+SIZE, y), 2) # Top
                if self.grid[i][j].wall[1]:
                    pygame.draw.line(self.win, WHITE, (x+SIZE, y), (x+SIZE, y+SIZE), 2) # Right
                if self.grid[i][j].wall[2]:
                    pygame.draw.line(self.win, WHITE, (x+SIZE, y+SIZE), (x, y+SIZE), 2) # Bottom
                if self.grid[i][j].wall[3]:
                    pygame.draw.line(self.win, WHITE, (x, y+SIZE), (x, y), 2) # Left

        # Visualize current cell
        if len(self.stack) > 0:
            x, y = self.current.i*SIZE, self.current.j*SIZE
            rect = (x + 1, y + 1, SIZE - 2, SIZE - 2)
            pygame.draw.rect(self.win, CURRENT_COLOR, rect)


# ---------------------------------------------------------------------------
# Object in the grid
# ---------------------------------------------------------------------------

class Place:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.wall = [True, True, True, True]
        self.visited = False


# ---------------------------------------------------------------------------
# Main program
# ---------------------------------------------------------------------------

def main():
    Setup().run()


# Initialize window and run main script
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.mixer.init()
main() 
