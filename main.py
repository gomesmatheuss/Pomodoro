import flet as ft
from components.navbar import Navbar

def main(page: ft.Page):
    page.title = "Pomodoro"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.INVERSE_PRIMARY

    page.window.width = 1080
    page.window.height = 720
    page.window.min_width = 480

    page.fonts = {
        "Rampart One": "RampartOne-Regular.ttf",
    }

    navbar = Navbar()

    contador = ft.Container(
        alignment=ft.alignment.center,
        expand=1,
        padding=ft.padding.only(bottom=200),
        content=ft.Text(
            value="25:39",
            size=205,
            color=ft.Colors.PRIMARY,
            font_family="Rampart One"
        )
    )

    page.add(navbar, contador)

if __name__ == "__main__":
    ft.app(target=main)
