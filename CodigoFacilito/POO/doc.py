class Page:
    def print_footer(self):
        print("Hola")

class LegalPage(Page):
    def print_footer(self):
        print("Mundo")
        super().print_footer()

# Creando una instancia de LegalPage y llamando al método print_footer
legal_page = LegalPage()
legal_page.print_footer()
