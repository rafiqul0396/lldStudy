from msilib.schema import CheckBox

from  models.Button import Button
from formFactory import FormFactory
from lightbutton import LightButton
from lightCheckBox import LightCheckBox

class LightFormFactory(FormFactory):

    def createButton(self) ->Button:
        a=LightButton()
        return a
    def createCheckBox(self)->CheckBox:
        b=LightCheckBox()
        return b
