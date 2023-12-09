"""
Main page file
"""

import flet as ft
from config import VIEW_MODE


class MainPage:
    """
        Main piercier app class
    """

    def main_page(self, page: ft.Page):
        """
        Defines the type of main page
        """

        page.title = "Piercier CSP"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        txt_number = ft.TextField(
            value="0", text_align=ft.TextAlign.RIGHT, width=100)

        def minus_click(e):
            print(e)
            txt_number.value = str(int(txt_number.value) - 1)
            page.update()

        def plus_click(e):
            print(e)
            txt_number.value = str(int(txt_number.value) + 1)
            page.update()

        page.add(
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    def run(self, view_mode: str = "browser"):
        """
        The function of launching the application
        """
        ft.app(target=self.main_page, view=VIEW_MODE[view_mode])
