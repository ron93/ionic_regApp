import kivy
kivy.require('1.10.0')
from kivy.app import App
# widget
from kivy.uix.widget import Widget
# properties
from kivy.properties import NumericProperty, ReferenceListProperty
# vector
from kivy.vector import Vector

class PongGame(Widget):
	#hooking PongBall child widget(in pong.kv file) to PongGame class.
	ball = ObjectProperty(None)
   
	def update(self, dt):
   		#call ball.move and any other method
   		pass

#Ball
class PongBall(Widget):
	#ball's velocity on the x and y axis
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)

	#referencelist property so as to use ball.velocity as a shorthand, like :- pos for w.x and w.y
	velocity = ReferenceListProperty(velocity_x, velocity_y)
	#`move` function to move ball one step.
	#function will be called at equal intevals to animate ball
	def move(self):
		self.pos =vector(*Self.velocity) + self.pos



class PongApp(App):
    def build(Self):
    	game =PongGame()
    	clock.schedule_interval(game.update, 1.0/60.0)
		return game

if __name__ == '__main__':
	PongApp().run()
