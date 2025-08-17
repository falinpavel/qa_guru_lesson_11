import allure

from helpers.application_manager.application_manager import demoqa


@allure.epic('Left Panel')
@allure.feature('Navigate on Left Panel')
@allure.suite('Tests navigate on Left Panel')
class TestNavigateOnLeftPanel:

    @allure.title('Navigate to all sections')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.id('1')
    @allure.label('owner', 'Falin Pavel')
    @allure.tag('UI')
    @allure.link('https://demoqa.com/forms', name='Forms')
    @allure.description('Check that left panel is clickable, navigate to all sections')
    def test_left_panel_group_is_clickable(self):
        demoqa.page_practice_form.open_page()
        demoqa.left_panel.click_to_forms()
        demoqa.left_panel.click_to_elements()
        demoqa.left_panel.click_to_forms()
        demoqa.left_panel.click_to_alerts_frames_windows()
        demoqa.left_panel.click_to_widgets()
        demoqa.left_panel.click_to_interactions()
        demoqa.left_panel.click_to_book_store()

    @allure.title('Go to text box page from Practice Form page')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.id('2')
    @allure.label('owner', 'Falin Pavel')
    @allure.tag('UI')
    @allure.link('https://demoqa.com/text-box', name='Text Box')
    @allure.description('Navigate to Text Box page from Practice Form page and check that it is opened')
    def test_go_to_text_box_page(self):
        demoqa.page_practice_form.open_page()
        demoqa.left_panel.click_to_forms().click_to_elements()
        demoqa.left_panel_elements.click_to_text_box()
