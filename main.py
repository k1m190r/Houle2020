from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty as NumP,
    ReferenceListProperty as RefP,
    ObjectProperty as ObjP,
)
from kivy.vector import Vector as Vec
from kivy.clock import Clock


class PongPaddle(Widget):
    score = NumP()

    def bounce_ball(self, ball):
        s = self
        if s.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - s.center_y) / (s.height / 2)
            bounced = Vec(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumP(0)
    velocity_y = NumP(0)
    velocity = RefP(velocity_x, velocity_y)

    def move(self):
        self.pos = Vec(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjP(None)
    player1 = ObjP(None)
    player2 = ObjP(None)

    def serve_ball(self, vel=(4, 0)):
        s = self
        s.ball.center = s.center
        s.ball.velocity = vel

    def update(self, dt):
        s = self
        s.ball.move()

        s.player1.bounce_ball(s.ball)
        s.player2.bounce_ball(s.ball)

        if (s.ball.y < s.y) or (s.ball.top > s.top):
            s.ball.velocity_y *= -1

        if s.ball.x < s.x:
            s.player2.score += 1
            s.serve_ball(vel=(4, 0))
        if s.ball.right > s.width:
            s.player1.score += 1
            s.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        s = self
        if touch.x < s.width / 3:
            s.player1.center_y = touch.y
        if touch.y > s.width - s.width / 3:
            s.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


PongApp().run()
