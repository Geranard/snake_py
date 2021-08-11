from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """Generate class untuk makanan"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        """Untuk generate makanan baru lagi"""
        rand_x = random.randint(-480, 480)
        rand_y = random.randint(-380, 380)
        self.goto(rand_x, rand_y)

