import pygame
import random
from enum import Enum
from collections import namedtuple

# Initialize Pygame modules
pygame.init()

# Set up the font for displaying the score
font = pygame.font.Font('arial.ttf', 25)
# Alternatively, you can use a system font:
# font = pygame.font.SysFont('arial', 25)

# Define possible directions for the snake using an enumeration
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# Define a point on the screen with x and y coordinates
Point = namedtuple('Point', 'x, y')

# Define RGB color values
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

# Set the size of each block and the game speed
BLOCK_SIZE = 20
SPEED = 20

# Main class for the Snake game
class SnakeGame:
    def __init__(self, w=640, h=480):
        self.w = w  # Width of the game window
        self.h = h  # Height of the game window
        # Initialize the display window
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')  # Set the window title
        self.clock = pygame.time.Clock()  # Initialize the game clock

        # Initialize the starting direction of the snake
        self.direction = Direction.RIGHT

        # Initialize the starting position of the snake's head
        self.head = Point(self.w / 2, self.h / 2)
        # Create the initial snake body with three segments
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)
        ]

        self.score = 0  # Initialize the score
        self.food = None  # Initialize the food position
        self._place_food()  # Place the first food item on the screen

    def _place_food(self):
        # Randomly place the food on the screen within the grid
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        # Ensure the food is not placed on the snake's body
        if self.food in self.snake:
            self._place_food()

    def play_step(self):
        # 1. Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # Change the direction based on the key pressed
                if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN

        # 2. Move the snake
        self._move(self.direction)  # Update the head position
        self.snake.insert(0, self.head)  # Add the new head to the snake

        # 3. Check if the game is over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        # 4. Check if the snake has eaten the food
        if self.head == self.food:
            self.score += 1
            self._place_food()  # Place new food on the screen
        else:
            self.snake.pop()  # Remove the last segment of the snake

        # 5. Update the game interface and control the game speed
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. Return the game over status and the current score
        return game_over, self.score

    def _is_collision(self):
        # Check if the snake has hit the boundaries
        if (self.head.x >= self.w or self.head.x < 0 or
                self.head.y >= self.h or self.head.y < 0):
            return True
        # Check if the snake has collided with itself
        if self.head in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        self.display.fill(BLACK)  # Fill the background with black

        # Draw the snake
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        # Draw the food
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        # Display the current score
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()  # Update the full display

    def _move(self, direction):
        # Calculate the new head position based on the current direction
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

# Main section to run the game
if __name__ == '__main__':
    game = SnakeGame()  # Create a new game instance

    # Game loop
    while True:
        game_over, score = game.play_step()

        if game_over:
            break

    print('Final Score', score)

    pygame.quit()  # Quit the game
