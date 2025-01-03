import flet as ft
from components.navbar import Navbar
from components.counter import MainPage

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
    counter = MainPage()

    page.add(navbar, counter)

if __name__ == "__main__":
    ft.app(target=main)
 