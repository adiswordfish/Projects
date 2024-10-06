import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle



class Roller(Widget):
    def __init__(self):
        super(Roller, self).__init__()
    def rollit(self):
        r = random.randint(1,6)
        # self.img = Image('dice-clipart-dice-faces-2.png')
        # if self.r == 1:
        #     self.magei = Image(source="images.png")
        #     print(self.r)
        # if self.r == 2:
        #     self.magei = Image(source="unnamed.png")
        #     print(self.r)
        # if self.r == 3:
        #     self.magei = Image(source="images (1).png")
        #     print(self.r)
        # if self.r == 4:
        #     self.magei = Image(source="images (2).png")
        #     print(self.r)
        # if self.r == 5:
        #     self.magei = Image(source="download.png")
        #     print(self.r)
        # if self.r == 6:
        #     self.magei = Image(source="dice-clipart-dice-faces-2.png")
        #     print(self.r)



class DiceApp(App):

    def build(self):
        return Roller()


if __name__ == '__main__':
    DiceApp().run()

# print(self.r)

