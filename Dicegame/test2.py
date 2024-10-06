import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import random
import numpy as np
from kivy.uix.floatlayout import FloatLayout

cards = ['ace_spades', 'king_spades']
dict = {'ace_spades':'ace_of_spades.png', 'king_spades':'king_of_spades2.png'}

Builder.load_file("test2.kv")

class LoginScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class ScoreScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class RootLayout(FloatLayout):  # create a root layout
    pass

class ChaseTheAce(App):
    cardimagefile = StringProperty()
    def deal(self):
        mycard = random.choice(cards)
        cards.remove(mycard)
        self.cardimagefile = (dict[mycard])  # the cardimagefile is not local needs self.
    def build(self):
        return RootLayout()  # you must return the root layout here

if __name__ == "__main__":
    ChaseTheAce().run()