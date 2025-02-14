import pygame
import random
import numpy as np
from enum import Enum
from collections import namedtuple

# Initialize Pygame modules
pygame.init()

# Set up the font for displaying the score
font = pygame.font.Font('arial.ttf', 25)

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
SPEED = 100

# Main class for the Snake game
class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w  # Width of the game window
        self.h = h  # Height of the game window
        # Initialize the display window
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')  # Set the window title
        self.clock = pygame.time.Clock()  # Initialize the game clock
        self.reset()

    def reset(self):
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
        self.frame_iteration = 0

    def _place_food(self):
        # Randomly place the food on the screen within the grid
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        # Ensure the food is not placed on the snake's body
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        self.frame_iteration += 1
        # 1. Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 2. Move the snake
        self._move(action)  # Update the head position
        self.snake.insert(0, self.head)  # Add the new head to the snake

        # 3. Check if the game is over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        # 4. Check if the snake has eaten the food
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()  # Place new food on the screen
        else:
            self.snake.pop()  # Remove the last segment of the snake

        # 5. Update the game interface and control the game speed
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. Return the game over status and the current score
        return reward, game_over, self.score

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # Check if the snake has hit the boundaries
        if  pt.x >= self.w or pt.x < 0 or pt.y >= self.h or pt.y < 0:
            return True
        # Check if the snake has collided with itself
        if pt in self.snake[1:]:
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

    def _move(self, action):
        # [straigh, right, left]
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn r -> d -> l -> u
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn r -> u -> l -> d

        self.direction = new_dir

        # Calculate the new head position based on the current direction
        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

