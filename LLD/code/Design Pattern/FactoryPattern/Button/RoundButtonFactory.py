
from ButtonFactory import ButtonFactory
from RoundButton import RoundButton
from button import Button
class RoundButtonFactory(ButtonFactory):

    def createButton(self)->Button:
        a=RoundButton()
        return a
