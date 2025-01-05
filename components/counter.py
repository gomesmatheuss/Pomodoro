import flet as ft

class Counter(ft.Row):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Container(
                alignment = ft.alignment.center,
                expand = 1,
                padding = ft.padding.only(top=-40),
                content = ft.Text(
                    value = "25:39",
                    size = 205,
                    color = ft.Colors.PRIMARY,
                    font_family = "Rampart One"
                )
            )
        ]
