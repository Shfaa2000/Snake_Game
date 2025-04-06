from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = self.get_highscore()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    def get_highscore(self):
        with open("highscore.txt", "r") as file:
            return int(file.read())
    def save_highscore(self):
        with open("highscore.txt","w") as file:
            file.write(str(self.highscore))
    def update_scoreboard(self):
        self.write(f"Score: {self.score}    HighScore: {self.highscore}", align="center", font=("Arial",24,"normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.screen.bgcolor("darkRed")
        self.goto(0, 0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.write(f"-------Game Over-------- \n\n Final Score: {self.score} \n\n HighScore: {self.highscore}", align="center", font=("Arial",24,"normal"))