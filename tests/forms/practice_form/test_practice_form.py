import allure

from helpers.application_manager.application_manager import demoqa


@allure.epic('Practice Form')
@allure.feature('Tests for registration on Practice Form page')
@allure.suite('Tests on Practice Form page')
class TestPracticeForm:

    @allure.title('Registration random user and submit form on Practice Form page')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.id('3')
    @allure.label('owner', 'Falin Pavel')
    @allure.tag('UI')
    @allure.link('https://demoqa.com/practice-form', name='Practice Form')
    @allure.description('Registration random user (Used Faker library) and submit form on Practice Form page')
    def test_success_submission_practice_form(self):
        demoqa.page_practice_form.open()
        demoqa.page_practice_form.registration_random_user_and_submit_form()

    @allure.title('Check that table is filled after registration random user and submit form on Practice Form page')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.id('4')
    @allure.label('owner', 'Falin Pavel')
    @allure.tag('UI')
    @allure.link('https://demoqa.com/practice-form', name='Practice Form')
    @allure.description('Registration random user (Used Faker library) and submit form on Practice Form page,'
                        ' finally check that table is currently filled')
    def test_successful_filling_table_practice_form(self):
        demoqa.page_practice_form.open()
        demoqa.page_practice_form.registration_random_user_and_submit_form()
        demoqa.page_practice_form.should_that_table_be_filled()

    @allure.title('Unsuccessful submission form on Practice Form page')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.id('5')
    @allure.label('owner', 'Falin Pavel')
    @allure.tag('UI')
    @allure.link('https://demoqa.com/practice-form', name='Practice Form')
    @allure.description('Check that form is not filled and not submitted on Practice Form page')
    def test_submission_form_with_empty_fields(self):
        demoqa.page_practice_form.open()
        demoqa.page_practice_form.form_not_filled_and_not_submitted()

    @allure.title('Check all texts into form on Practice Form page')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.id('6')
    @allure.label('owner', 'Falin Pavel')
    @allure.tag('UI')
    @allure.link('https://demoqa.com/practice-form', name='Practice Form')
    @allure.description('That test checks all texts into form on Practice Form page and that they are correct')
    def test_check_texts_on_form(self):
        demoqa.page_practice_form.open()
        demoqa.page_practice_form.should_all_texts_into_form()

    @allure.title('Registration random user and submit on Text Box page')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.id('7')
    @allure.label('owner', 'Falin Pavel')
    @allure.tag('UI')
    @allure.link('https://demoqa.com/practice-form', name='Practice Form')
    @allure.description('Registration random user and submit form on Practice Form page and go to Text Box page,'
                        ' registration random user and submit form on Text Box page')
    def test_registration_practice_form_and_go_to_registration_text_box_page(self):
        demoqa.page_practice_form.open()
        demoqa.page_practice_form.registration_random_user_and_submit_form()
        demoqa.page_practice_form.should_that_table_be_filled()
        demoqa.left_panel.click_to_forms()
        demoqa.left_panel.click_to_elements()
        demoqa.left_panel_elements.click_to_text_box()
        demoqa.page_text_box.registration_random_user_and_submit_form().should_all_values_after_submit()
