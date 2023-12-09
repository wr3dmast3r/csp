import flet as ft


class AppBody(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.new_csp = None
        self.csp_view = None
        self.csp_result = None

    def build(self):
        self.new_csp = ft.TextField(
            label="CSP option",
            hint_text="An other CSP option?",
            expand=True
        )
        self.csp_view = ft.Column()

        return ft.Column(
            width=1220,
            controls=[
                ft.Row(
                    controls=[
                        self.new_csp,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.csp_view,
            ],
        )

    def add_clicked(self, e):
        self.csp_view.controls.append(
            CSPOption(self.new_csp.value, self.csp_delete))
        self.new_csp.value = ""
        self.update()

    def csp_delete(self, csp):
        self.csp_view.controls.remove(csp)
        self.update()


class CSPOption(ft.UserControl):
    def __init__(self, csp, csp_delete):
        super().__init__()
        self.csp = csp
        self.csp_delete = csp_delete
        self.display_csp = None
        self.edit_csp = None
        self.display_view = None
        self.edit_view = None

    def build(self):
        self.display_csp = ft.Text(value=self.csp)
        self.edit_csp = ft.TextField(expand=True)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_csp,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE,
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            on_click=self.delete_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.PLAY_ARROW,
                            on_click=self.execute_clicked,
                        )
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_csp,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    on_click=self.save_clicked,
                ),
            ],
        )

        return ft.Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_csp.value = self.display_csp.value
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_csp.value = self.edit_csp.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.csp_delete(self)

    def execute_clicked(self, e):
        csp = self.display_csp.value
        print(csp)
