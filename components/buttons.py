import flet as ft
from threading import Timer

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

class Buttons(ft.Row):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.CENTER
        self.controls = [
            StartButton(),
            ft.Container(width=100),
            SkipButton()
        ]
