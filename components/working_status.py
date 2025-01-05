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
