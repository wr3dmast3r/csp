"""
Main page file
"""

import flet as ft
from config import (
    VIEW_MODE,
    APP_TITLE,
    APP_PORT
)


class MainPage:
    """
        Main piercier app class
    """

    def main_page(self, page: ft.Page):
        """
        Defines the type of main page
        """
        
        #---App Settings---
        page.title = APP_TITLE
        
        #-----App body-----

    def run(self, view_mode: str = "browser"):
        """
        The function of launching the application
        """
        if view_mode == "browser":
            ft.app(target=self.main_page,
                   view=VIEW_MODE[view_mode], port=APP_PORT)
        else:
            ft.app(target=self.main_page, view=VIEW_MODE[view_mode])
