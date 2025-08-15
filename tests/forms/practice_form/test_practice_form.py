from helpers.application_manager.application_manager import demoqa


class TestPracticeForm:
    def test_success_submission_practice_form(self):
        demoqa.page_practice_form.open_page()
        demoqa.page_practice_form.registration_random_user_and_submit_form()

    def test_successful_filling_table_practice_form(self):
        demoqa.page_practice_form.open_page()
        demoqa.page_practice_form.registration_random_user_and_submit_form()
        demoqa.page_practice_form.should_that_table_be_filled()

    def test_submission_form_with_empty_fields(self):
        demoqa.page_practice_form.open_page()
        demoqa.page_practice_form.form_not_filled_and_not_submitted()

    def test_check_texts_on_form(self):
        demoqa.page_practice_form.open_page()
        demoqa.page_practice_form.should_all_texts_into_form()

    def test_registration_practice_form_and_go_to_registration_text_box_page(self):
        demoqa.page_practice_form.open_page()
        demoqa.page_practice_form.registration_random_user_and_submit_form()
        demoqa.page_practice_form.should_that_table_be_filled()
        demoqa.left_panel.click_to_forms()
        demoqa.left_panel.click_to_elements()
        demoqa.left_panel_elements.click_to_text_box()
        demoqa.page_text_box.registration_random_user_and_submit_form().should_all_values_after_submit()