"""
Main page file
"""

import flet as ft
from config import (
    VIEW_MODE,
    BACKGROUND_COLOR,
    APP_TITLE,
    APP_WIDTH,
    APP_HEIGHT,
)
from .elements import AppBody


class App:
    """
        Main piercier app class
    """

    def main_page(self, page: ft.Page):
        """
        Defines the type of main page
        """
        # ---App Settings---
        page.title = APP_TITLE
        page.window_width = APP_WIDTH
        page.window_height = APP_HEIGHT
        page.bgcolor = BACKGROUND_COLOR
        page.window_resizable = False
        page.update()

        # -----App body-----
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.update()

        body = AppBody()
        page.add(body)

    def run(self, view_mode: str = "browser"):
        """
        The function of launching the application
        """

        ft.app(
            target=self.main_page,
            view=VIEW_MODE[view_mode]
        )
