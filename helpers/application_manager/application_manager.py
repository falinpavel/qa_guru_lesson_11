from helpers.pages.elements.text_box.page_text_box import TextBoxPage
from helpers.pages.forms.practice_form.page_practice_form import PracticeFormPage
from helpers.pages.left_panel.left_panel import LeftPanel, LeftPanelElements, LeftPanelForms


class ApplicationManager:

    def __init__(self):

        self.page_practice_form = PracticeFormPage()
        self.page_text_box = TextBoxPage()

        self.left_panel = LeftPanel()
        self.left_panel_elements = LeftPanelElements()
        self.left_panel_forms = LeftPanelForms()


demoqa = ApplicationManager()