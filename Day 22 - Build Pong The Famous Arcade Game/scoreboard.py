from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 35, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"{self.score_1} - {self.score_2}", align=ALIGNMENT, font=FONT)

    def update_score_1(self):
        self.score_1 += 1
        self.clear()
        self.update_scoreboard()

    def update_score_2(self):
        self.score_2 += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        if self.score_1 > self.score_2:
            winner = "Right"
            winner_score = self.score_1
        else:
            winner = "Left"
            winner_score = self.score_2
        self.goto(0, 0)
        self.write(arg=f"GAME OVER! {winner} player win with {winner_score} point.", align="center", font=("Courier", 20, "normal"))

