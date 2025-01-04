import flet as ft

class State(ft.Row):
    def __init__(self):
        super().__init__()
        self.expand = 1
        self.alignment = ft.MainAxisAlignment.CENTER
        self.controls = [
            ft.Column(
                spacing = 0,
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                height = 100,
                controls = [
                    ft.Container(
                        height = 23,
                        content = ft.Text(
                            "Você está:",
                            size = 20,
                            color = ft.Colors.PRIMARY,
                            font_family = "Franklin Gothic"
                        )
                    ),
                    ft.Text(
                        "Trabalhando", 
                        size = 25, 
                        weight = ft.FontWeight.BOLD,
                        color = ft.Colors.PRIMARY,
                        font_family = "Roboto"
                    )
                ]
            )
        ]


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


class PauseSkipButton(ft.Row):
    def __init__(self):
        super().__init__()
        self.expand = 1
        self.alignment = ft.MainAxisAlignment.SPACE_EVENLY
        self.height = 80
        self.controls = [
            ft.ElevatedButton("Parar", elevation=5),
            ft.ElevatedButton("Pular", elevation=5),
        ]


class CyclesStatistics(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            self.CustomRow("Ciclos completos:", "0"),
            self.CustomRow("Horas trabalhadas:", "00:00:00"),
            self.CustomRow("Pomodoros completos:", "0")
        ]

    def CustomRow(self, title, value):
        return ft.Row(
            alignment = ft.MainAxisAlignment.CENTER,
            controls = [
                ft.Text(
                    title,
                    size = 20,
                    color = ft.Colors.PRIMARY,
                    font_family = "Franklin Gothic"
                ),
                ft.Text(
                    value, 
                    size = 20, 
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.PRIMARY,
                    font_family = "Roboto"
                )
            ]
        )


class MainPage(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            State(),
            Counter(),
            PauseSkipButton(),
            CyclesStatistics()
        ]
