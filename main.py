from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=800)
    screen.bgcolor("black")
    screen.title("Snake 101")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.get_bigger()
            scoreboard.inc_score()

        #Collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            time.sleep(2)
            game_on = False

        #Collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()


if __name__ == '__main__':
    main()
