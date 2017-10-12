import kivy
kivy.require('1.10.0')
from kivy.app import App
# widget
from kivy.uix.widget import Widget
# properties
from kivy.properties import NumericProperty, ReferenceListProperty,ObjectProperty
# vector
from kivy.vector import Vector
# clock
from kivy.clock import Clock
# ranomizer

from random import randint


# pongpaddle
class PongPaddle(Widget):
	score = NumericProperty(0)

	def bounce_ball(self, ball):
		if self.collide_widget(ball):
			vx, vy = ball.velocity
			# unit to speed of ball on collide with puddle
			speedup = 1.1
			# position offset of ball(offset from original pos on x and y axis)
			offset = (ball.center_y - self.center_y)/ (self.height/2)
			bounced = Vector(-1*vx, vy)
			vel = bounced * 1.1
			ball.velocity = vel.x , vel.y + offset

#PongBall class
class PongBall(Widget):
	#ball's velocity on the x and y axis
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)

	#referencelist property so as to use ball.velocity as a shorthand, like :- pos for w.x and w.y
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	#`move` function to move ball one step.
	#function will be called at equal intevals to animate ball
	def move(self):
		self.pos =Vector(*self.velocity) + self.pos



class PongGame(Widget):
	#hooking PongBall child widget(in pong.kv file) to PongGame class.
	ball = ObjectProperty(None)
	player1 = ObjectProperty(None)
	player2 = ObjectProperty(None)

	def serve_ball(self, vel(4,0)):
		# ball position
		self.ball.center= self.center
		# ball velocity
		self.ball.velocity = vel


	def update(self, dt):
   		self.ball.move()

   		# bounce off paddle
   		self.player1.bounce_ball(self.ball)
   		self.player2.bounce_ball(self.ball)

   		#bounce off top and bottom side of 'wall'
   		if (self.ball.y < 0) or(self.ball.top > self.height):
   				self.ball.velocity_y *= -1

   		# bounce off left and righ side
   		if (self.ball.x < 0 )  or (self.ball.right > self.width):
   			self.ball.velocity_x *= -1 



class PongApp(App):
    def build(Self):
    	game =PongGame()
    	game.serve_ball()
    	Clock.schedule_interval(game.update, 1.0/60.0)
	return game

if __name__ == '__main__':
	PongApp().run()
