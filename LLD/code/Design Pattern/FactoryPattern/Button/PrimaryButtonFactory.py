from PrimaryButton import PrimaryButton
from ButtonFactory import ButtonFactory
from button import Button
class PrimaryButtonFactory(ButtonFactory):

    def createButton(self) ->Button:
        a=PrimaryButton()
        return a
