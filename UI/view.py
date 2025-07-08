import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Simulazione esame"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddLocalization = None
        self._btn_grafo = None
        self._btn_statistiche = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Simulazione esame", color="blue", size=24)
        self._page.controls.append(self._title)

        self._ddLocalization = ft.Dropdown(label="Localization")
        self._controller.fillDDLoc()
        self._btn_grafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handle_creaGrafo)
        self._btn_statistiche = ft.ElevatedButton(text="Statistiche", on_click=self._controller.handle_statistiche)
        row1 = ft.Row([ self._btn_grafo, self._ddLocalization, self._btn_statistiche],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._btn_ricorsione = ft.ElevatedButton(text="Ricorsione", on_click=self._controller.handle_ricorsione)
        row2 = ft.Row([ self._btn_ricorsione],
                     alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
