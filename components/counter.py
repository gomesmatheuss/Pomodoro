import flet as ft

class Counter(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.center
        self.expand = 1
        # self.padding = ft.padding.only(bottom=200)
        self.content=ft.Text(
            value="25:39",
            size=205,
            color=ft.Colors.PRIMARY,
            font_family="Rampart One"
        )

class MainPage(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Row(
                controls = [
                    Counter()
                ]
            )
        ]