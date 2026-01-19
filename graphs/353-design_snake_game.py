#353. Design Snake Game
#Medium
#
#Design a Snake game that is played on a device with screen size height x
#width. The snake is initially positioned at the top left corner (0, 0) with a
#length of 1 unit.
#
#You are given an array food where food[i] = (ri, ci) is the row and column
#position of a piece of food that the snake can eat. When a snake eats a piece
#of food, its length and the game's score both increase by 1.
#
#Each piece of food appears one by one on the screen, meaning the second piece
#of food will not appear until the snake eats the first piece of food.
#
#When a piece of food appears on the screen, it is guaranteed that it will not
#appear on a block occupied by the snake.
#
#The snake can move in four directions (up, down, left, right). If the snake
#goes out of bounds or bites itself, the game is over.
#
#Implement the SnakeGame class:
#- SnakeGame(int width, int height, int[][] food) Initializes the object with a
#  screen of size height x width and the positions of the food.
#- int move(String direction) Returns the score of the game after applying one
#  direction move by the snake. If the game is over, return -1.
#
#Example:
#Input: ["SnakeGame", "move", "move", "move", "move", "move", "move"]
#       [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
#Output: [null, 0, 0, 1, 1, 2, -1]
#
#Constraints:
#    1 <= width, height <= 10^4
#    1 <= food.length <= 50
#    food[i].length == 2
#    0 <= ri < height
#    0 <= ci < width
#    direction.length == 1
#    direction is 'U', 'D', 'L', or 'R'.
#    At most 10^4 calls will be made to move.

from typing import List
from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0

        # Snake body as deque: front is head, back is tail
        self.snake = deque([(0, 0)])
        self.snake_set = {(0, 0)}  # For O(1) collision check
        self.score = 0

    def move(self, direction: str) -> int:
        # Direction mapping
        directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

        # Calculate new head position
        head_row, head_col = self.snake[0]
        dr, dc = directions[direction]
        new_row, new_col = head_row + dr, head_col + dc

        # Check wall collision
        if not (0 <= new_row < self.height and 0 <= new_col < self.width):
            return -1

        # Check if eating food
        eating = (self.food_index < len(self.food) and
                  self.food[self.food_index] == [new_row, new_col])

        if not eating:
            # Remove tail
            tail = self.snake.pop()
            self.snake_set.remove(tail)

        # Check self collision (after potentially removing tail)
        if (new_row, new_col) in self.snake_set:
            return -1

        # Move snake
        self.snake.appendleft((new_row, new_col))
        self.snake_set.add((new_row, new_col))

        if eating:
            self.score += 1
            self.food_index += 1

        return self.score


class SnakeGameSimple:
    """Simpler implementation using list"""

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = deque(food)
        self.snake = deque([(0, 0)])
        self.occupied = {(0, 0)}

    def move(self, direction: str) -> int:
        dir_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        dr, dc = dir_map[direction]

        head_r, head_c = self.snake[0]
        new_head = (head_r + dr, head_c + dc)

        # Check bounds
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1

        # Check food
        if self.food and [new_head[0], new_head[1]] == self.food[0]:
            self.food.popleft()
        else:
            # Remove tail
            tail = self.snake.pop()
            self.occupied.remove(tail)

        # Check self collision
        if new_head in self.occupied:
            return -1

        # Add new head
        self.snake.appendleft(new_head)
        self.occupied.add(new_head)

        return len(self.snake) - 1
