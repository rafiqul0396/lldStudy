
from models.Button import  Button

class LightButton(Button):

    def onClick(self):
        print("Light button")
    def render(self):
        print("render button")



