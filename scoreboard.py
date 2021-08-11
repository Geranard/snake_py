from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Generate class untuk scoreboard"""
        super().__init__()
        self.score = 0
        self.temp = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 375)
        self.view()

    def view(self):
        """Untuk kasih tunjuk scoreboard"""
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        """Untuk refresh scoreboard kalo ularnya makan"""
        self.score += 1
        self.clear()
        self.view()

    def reset_score(self):
        self.clear()
        if self.score>self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.view()

    # def game_over(self):
    #     """Untuk display (GAME OVER) di screen"""
    #     self.goto(0, 0)
    #     self.write(arg="Bruh, gitgud", align=ALIGNMENT, font=("Courier", 30, "normal"))