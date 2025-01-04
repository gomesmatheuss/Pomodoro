import flet as ft

class State(ft.Column):
    def __init__(self):
        super().__init__()
        self.spacing = 0
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Container(
                height = 23,
                content = ft.Text(
                    "Você está:",
                    size=20,
                    color=ft.Colors.PRIMARY,
                    font_family="Franklin Gothic"
                )
            ),
            ft.Text(
                "Trabalhando", 
                size=25, 
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.PRIMARY,
                font_family="Roboto"
            )
        ]


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


class PauseSkipButton(ft.Row):
    def __init__(self):
        super().__init__()
        self.expand = 1
        self.alignment = ft.MainAxisAlignment.SPACE_EVENLY
        self.controls = [
            ft.ElevatedButton("Parar", elevation=5),
            ft.ElevatedButton("Pular", elevation=5),
        ]


class CyclesStatistics(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Row(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    ft.Text(
                        "Ciclos completos:",
                        size=20,
                        weight=ft.FontWeight.W_100,
                        color=ft.Colors.PRIMARY,
                        font_family="Franklin Gothic"
                    ),
                    ft.Text(
                        "0", 
                        size=20, 
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PRIMARY,
                        font_family="Roboto"
                    )
                ]
            ),
            ft.Row(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    ft.Text(
                        "Horas trabalhadas:",
                        size=20,
                        color=ft.Colors.PRIMARY,
                        font_family="Franklin Gothic"
                    ),
                    ft.Text(
                        "00:00:00", 
                        size=20, 
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PRIMARY,
                        font_family="Roboto"
                    )
                ]
            ),
            ft.Row(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    ft.Text(
                        "Pomodoros completos:",
                        size=20,
                        color=ft.Colors.PRIMARY,
                        font_family="Franklin Gothic"
                    ),
                    ft.Text(
                        "0", 
                        size=20, 
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PRIMARY,
                        font_family="Roboto"
                    )
                ]
            )
        ]


class MainPage(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Row(
                expand = 1,
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    State()
                ]
            ),
            ft.Row(
                controls = [
                    Counter()
                ]
            ),
            PauseSkipButton(),
            CyclesStatistics()
        ]
