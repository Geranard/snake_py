from turtle import Turtle
from os import system

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        """Generate class untuk ular"""
        self.segment = []
        for index in range(3):
            self.add_segment(POSITION[index])
    
    def extend(self):
        """Untuk tambahin panjang kalo dapet makanan"""
        self.add_segment(self.segment[-1].position())

    def add_segment(self, position):
        """Untuk tambahin atau ngebuat ularnya"""
        temp = Turtle("square")
        temp.color("red")
        temp.penup()
        temp.goto(position)
        self.segment.append(temp)

    def reset_snake(self):
        """Untuk clear seluruh snakenya"""
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        for index in range(3):
            self.add_segment(POSITION[index])

    def move(self):
        """Untuk kepala ularnya jalan, belakangnya tinggal ikutin"""
        length = len(self.segment)-1

        for index in range(length, 0, -1):
            x = int(self.segment[index-1].xcor())
            y = int(self.segment[index-1].ycor())
            self.segment[index].goto(x, y)
        self.segment[0].forward(20)

    def up(self):
        """Untuk naik ke atas pake arrow atas"""
        if self.segment[0].heading() != DOWN:
            self.move()
            self.segment[0].setheading(90)

    def left(self):
        """Untuk belok ke kiri pake arrow kiri"""
        if self.segment[0].heading() != RIGHT:
            self.move()
            self.segment[0].setheading(180)

    def down(self):
        """Untuk turun ke bawah pake arrow bawah"""
        if self.segment[0].heading() != UP:
            self.move()
            self.segment[0].setheading(270)

    def right(self):
        """Untuk belok ke kanan pake arrow kanan"""
        if self.segment[0].heading() != LEFT:
            self.move()
            self.segment[0].setheading(0)
    
    def info(self):
        """Untuk print di command bagian bagian ularnya dimana aja"""
        system("cls")
        index = 0
        for segment in self.segment:
            x = int(segment.xcor())
            y = int(segment.ycor())
            facing = int(segment.heading())
            print(f"index: {index}, coor: ({x}, {y}), facing: {facing}")
            index += 1
        print("")
