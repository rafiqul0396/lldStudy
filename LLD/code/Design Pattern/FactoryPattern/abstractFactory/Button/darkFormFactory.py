from formFactory import FormFactory
from darkbutton import DarkButton
from DarkCheckbox import DarkCheckBox
from models.Button import Button
from models.checkBox import CheckBox
class DarkFormFactory(FormFactory):

    def createButton(self) ->Button:
        a=DarkButton()
        return a
    def createCheckBox(self)->CheckBox:
        b=DarkCheckBox()
        return b
    