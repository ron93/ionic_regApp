import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
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
        return PongGame()

if __name__ == '__main__':
	PongApp().run()
