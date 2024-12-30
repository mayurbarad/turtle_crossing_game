from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVING_UP = False


class Player(Turtle,):
    def __init__(self,screen):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.screen = screen

    def move_up(self):
        if MOVING_UP:
            self.forward(MOVE_DISTANCE)
            self.screen.ontimer(self.move_up, 1000)

    def start_moving(self):
        global MOVING_UP
        MOVING_UP = True
        self.move_up()

    def stop_moving(self):
        global MOVING_UP
        MOVING_UP = False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False





