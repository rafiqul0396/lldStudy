from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        ...

    @abstractmethod
    def turn_off(self) -> None:
        ...


class LightBulb(Switchable):
    def turn_on(self) -> None:
        print("LightBulb: turned on...")

    def turn_off(self) -> None:
        print("LightBulb: turned off...")


class Fun(Switchable):
    def turn_on(self) -> None:
        print("Fun: turn on...")

    def turn_off(self) -> None:
        print("Fun: turn off...")


class ElectricPowerSwitch:

    def __init__(self, l: Switchable):
        self.switch = l
        self.on = False

    def press(self):
        if self.on:
            self.switch.turn_off()
            self.on = False
        else:
            self.switch.turn_on()
            self.on = True


f = Fun()
l = LightBulb()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
