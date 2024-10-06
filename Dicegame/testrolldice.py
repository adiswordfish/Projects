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
        if r == 1:
            # img = Image(source="images.png"
            self.img.source = "images.png"
            print(r)
        if r == 2:
            self.img.source="unnamed.png"
            print(r)
        if r == 3:
            self.img.source="images (1).png"
            print(r)
        if r == 4:
            self.img.source="images (2).png"
            print(r)
        if r == 5:
            self.img.source="download.png"
            print(r)
        if r == 6:
            self.img.source="dice-clipart-dice-faces-2.png"
            print(r)



class DicetestApp(App):

    def build(self):
        return Roller()


if __name__ == '__main__':
    DicetestApp().run()