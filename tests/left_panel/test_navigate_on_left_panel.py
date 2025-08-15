from helpers.application_manager.application_manager import demoqa


class TestNavigateOnLeftPanel:

    def test_left_panel_group_is_clickable(self):
        demoqa.page_practice_form.open_page()
        demoqa.left_panel.click_to_forms()
        demoqa.left_panel.click_to_elements()
        demoqa.left_panel.click_to_forms()
        demoqa.left_panel.click_to_alerts_frames_windows()
        demoqa.left_panel.click_to_widgets()
        demoqa.left_panel.click_to_interactions()
        demoqa.left_panel.click_to_book_store()

    def test_go_to_text_box_page(self):
        demoqa.page_practice_form.open_page()
        demoqa.left_panel.click_to_forms().click_to_elements()
        demoqa.left_panel_elements.click_to_text_box()