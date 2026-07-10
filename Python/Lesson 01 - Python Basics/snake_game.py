import random
import tkinter as tk


class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.resizable(False, False)

        self.cell_size = 20
        self.width = 400
        self.height = 400
        self.board_width = self.width // self.cell_size
        self.board_height = self.height // self.cell_size

        self.canvas = tk.Canvas(
            self.window,
            width=self.width,
            height=self.height,
            bg="black",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.window.bind("<KeyPress>", self.on_key_press)
        self.window.focus_set()
        self.reset_game()
        self.window.mainloop()

    def reset_game(self):
        self.direction = "Right"
        self.next_direction = "Right"
        self.snake = [(self.board_width // 2, self.board_height // 2)]
        self.score = 0
        self.food = self.spawn_food()
        self.running = True
        self.draw()
        self.window.after(120, self.game_loop)

    def spawn_food(self):
        while True:
            position = (
                random.randint(0, self.board_width - 1),
                random.randint(0, self.board_height - 1),
            )
            if position not in self.snake:
                return position

    def on_key_press(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.next_direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.next_direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.next_direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.next_direction = "Right"
        elif key.lower() == "r":
            self.reset_game()

    def game_loop(self):
        if not self.running:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= 1
        elif self.direction == "Down":
            head_y += 1
        elif self.direction == "Left":
            head_x -= 1
        elif self.direction == "Right":
            head_x += 1

        new_head = (head_x, head_y)

        if self.is_collision(new_head):
            self.running = False
            self.draw_game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

        self.draw()
        self.window.after(120, self.game_loop)

    def is_collision(self, position):
        x, y = position
        if x < 0 or y < 0 or x >= self.board_width or y >= self.board_height:
            return True
        if position in self.snake[1:]:
            return True
        return False

    def draw(self):
        self.canvas.delete("all")

        for x, y in self.snake:
            self.canvas.create_rectangle(
                x * self.cell_size,
                y * self.cell_size,
                x * self.cell_size + self.cell_size,
                y * self.cell_size + self.cell_size,
                fill="lime",
                outline="green",
            )

        food_x, food_y = self.food
        self.canvas.create_rectangle(
            food_x * self.cell_size,
            food_y * self.cell_size,
            food_x * self.cell_size + self.cell_size,
            food_y * self.cell_size + self.cell_size,
            fill="red",
            outline="darkred",
        )

        self.canvas.create_text(
            10,
            10,
            anchor=tk.NW,
            fill="white",
            text=f"Score: {self.score}",
        )

    def draw_game_over(self):
        self.canvas.create_text(
            self.width // 2,
            self.height // 2,
            text="Game Over! Press R to restart",
            fill="white",
            font=("Arial", 16, "bold"),
        )


if __name__ == "__main__":
    SnakeGame()
