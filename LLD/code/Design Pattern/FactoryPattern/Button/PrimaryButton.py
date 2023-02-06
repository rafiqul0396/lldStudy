from tkinter import Button


class PrimaryButton(Button):

    def render(self):
        print("Primary")
    def onClick(self):
        print("onClick")
        