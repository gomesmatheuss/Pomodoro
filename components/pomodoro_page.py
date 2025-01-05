import flet as ft
from components.working_status import State
from components.counter import Counter
from components.buttons import Buttons
from components.cycles_statistics import CyclesStatistics

class Pomodoro(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            State(),
            Counter(),
            Buttons(),
            CyclesStatistics()
        ]
