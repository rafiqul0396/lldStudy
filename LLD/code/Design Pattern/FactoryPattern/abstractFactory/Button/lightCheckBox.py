
from models.checkBox import  CheckBox

class LightCheckBox(CheckBox):

    def onSelect(self):
        print("Select this light checkbox")
    def render(self):
        print("Render light checkbox")

