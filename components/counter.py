import flet as ft
from threading import Timer

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


class StartButton(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.height = 50
        self.bgcolor = ft.Colors.PRIMARY_CONTAINER
        self.border = ft.border.all(2, ft.Colors.PRIMARY)
        self.border_radius = 5
        self.alignment = ft.alignment.center
        self.shadow = ft.BoxShadow(
            spread_radius = 0,
            blur_radius = 0,
            color = ft.Colors.with_opacity(0.55, ft.Colors.PRIMARY),
            offset = ft.Offset(4, 3)
        )
        self.content = ft.Text(
            "Iniciar",
            size = 18,
            weight = ft.FontWeight.BOLD,
            color = ft.Colors.PRIMARY
        )
        self.on_hover = self._on_hover
        self.on_click = self._on_click
        
    def _on_click(self, e):
        self.bgcolor = ft.Colors.ON_PRIMARY
        self.page.update()
        Timer(0.1, self.reset_color).start()

    def _on_hover(self, e):
        if e.data == "true":
            self.shadow = ft.BoxShadow(
                spread_radius = 0,
                blur_radius = 0,
                color = ft.Colors.with_opacity(0.35, ft.Colors.PRIMARY),
                offset = ft.Offset(2, 2),
            )
            self.bgcolor = ft.Colors.INVERSE_PRIMARY
        else:
            self.shadow = ft.BoxShadow(
                spread_radius = 0,
                blur_radius = 0,
                color = ft.Colors.with_opacity(0.55, ft.Colors.PRIMARY),
                offset = ft.Offset(4, 3),
            )
            self.bgcolor = ft.Colors.PRIMARY_CONTAINER
        self.page.update()

    def reset_color(self):
        self.bgcolor = ft.Colors.PRIMARY_CONTAINER
        self.page.update()


class SkipButton(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.height = 50
        self.bgcolor = ft.Colors.PRIMARY_CONTAINER
        self.border = ft.border.all(2, ft.Colors.PRIMARY)
        self.border_radius = 5
        self.alignment = ft.alignment.center
        self.shadow = ft.BoxShadow(
            spread_radius = 0,
            blur_radius = 0,
            color = ft.Colors.with_opacity(0.55, ft.Colors.PRIMARY),
            offset = ft.Offset(4, 3)
        )
        self.content = ft.Text(
            "Skip",
            size = 18,
            weight = ft.FontWeight.BOLD,
            color = ft.Colors.PRIMARY
        )
        self.on_hover = self._on_hover
        self.on_click = self._on_click
        
    def _on_click(self, e):
        self.bgcolor = ft.Colors.ON_PRIMARY
        self.page.update()
        Timer(0.1, self.reset_color).start()

    def _on_hover(self, e):
        if e.data == "true":
            self.shadow = ft.BoxShadow(
                spread_radius = 0,
                blur_radius = 0,
                color = ft.Colors.with_opacity(0.35, ft.Colors.PRIMARY),
                offset = ft.Offset(2, 2),
            )
            self.bgcolor = ft.Colors.INVERSE_PRIMARY
        else:
            self.shadow = ft.BoxShadow(
                spread_radius = 0,
                blur_radius = 0,
                color = ft.Colors.with_opacity(0.55, ft.Colors.PRIMARY),
                offset = ft.Offset(4, 3),
            )
            self.bgcolor = ft.Colors.PRIMARY_CONTAINER
        self.page.update()

    def reset_color(self):
        self.bgcolor = ft.Colors.PRIMARY_CONTAINER
        self.page.update()


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
            ft.Row(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    StartButton(),
                    ft.Container(width=100),
                    SkipButton()
                ]
            ),
            CyclesStatistics()
        ]
