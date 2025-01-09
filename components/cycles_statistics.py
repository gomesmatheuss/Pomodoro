import flet as ft

class CyclesStatistics(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Container(height=15),
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
