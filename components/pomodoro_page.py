import flet as ft
import datetime
from time import sleep
from components.working_status import State
from components.buttons import CustomButton
from components.cycles_statistics import CyclesStatistics

class Pomodoro(ft.Column):
    def __init__(self):
        super().__init__()
        self.counter_ref = ft.Ref[ft.Text]()
        self.COUNTER = ft.Row(
            controls = [
                ft.Container(
                    alignment = ft.alignment.center,
                    expand = 1,
                    padding = ft.padding.only(top=-40),
                    content = ft.Text(
                        value = "25:00",
                        size = 205,
                        color = ft.Colors.PRIMARY,
                        font_family = "Rampart One",
                        ref = self.counter_ref
                    )
                )
            ]
        )
        self.BUTTONS = ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls = [
                CustomButton("Start", self.start_timer),
                ft.Container(width=100),
                CustomButton("Skip", None)
            ]
        )
        self.controls = [
            State(),
            self.COUNTER,
            self.BUTTONS,
            CyclesStatistics()
        ]

    def start_timer(self):
        def sec_to_min(seconds):
            return f"{int(seconds / 60):02d}:{seconds % 60:02d}"
        
        for i in range(1499, -1, -1):
            sleep(1)
            self.counter_ref.current.value = sec_to_min(i)
            self.counter_ref.current.update()
