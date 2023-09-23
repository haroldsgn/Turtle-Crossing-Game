from turtle import Turtle, Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.y_positions = list(range(-245, 245))
        self.x_positions = 310
        self.move_increment = 5

    def generate_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(self.x_positions, random.choice(self.y_positions))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.goto(car.xcor() - self.move_increment, car.ycor())

            if car.xcor() < -400:
                car.hideturtle()

    def next_level(self):
        self.move_increment += 5














