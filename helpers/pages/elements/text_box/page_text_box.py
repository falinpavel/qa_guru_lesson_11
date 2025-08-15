import allure

from selene import browser, be, have, command
from selene.core.condition import Condition

from helpers.config.links import Links
from helpers.data.user_info import TextBoxUserGenerator


class TextBoxPage:
    URL = Links.TEXT_BOX

    user = TextBoxUserGenerator().get_random_user()

    @allure.step("Open Text Box page")
    def open_page(self):
        with allure.step(f"Open {self.URL}"):
            browser.open(self.URL)
        return self

    @allure.step("Filling form on Text Box page and submit it")
    def registration_random_user_and_submit_form(self) -> 'TextBoxPage':
        with allure.step("Filling #userName field"):
            browser.element('#userName').should(be.blank).type(f'{self.user.first_name} {self.user.last_name}').should(
                be.not_.blank).should(have.attribute("value").value(f'{self.user.first_name} {self.user.last_name}'))
        with allure.step("Filling #userEmail field"):
            browser.element('#userEmail').should(be.blank).type(self.user.user_email).should(be.not_.blank).should(
                have.attribute("value").value(self.user.user_email))
        with allure.step("Filling #currentAddress field"):
            browser.element('#currentAddress').should(be.blank).type(self.user.current_address).should(
                be.not_.blank).should(
                have.attribute("value").value(self.user.current_address))
        with allure.step("Filling #permanentAddress field"):
            browser.element('#permanentAddress').should(be.blank).type(self.user.permanent_address).should(
                be.not_.blank).should(have.attribute("value").value(self.user.permanent_address))
        with allure.step("Click on #submit button"):
            browser.element('#submit').perform(command.js.scroll_into_view).click()
        return self

    @allure.step("Check that all values after submit")
    def should_all_values_after_submit(self) -> 'TextBoxPage':
        with allure.step("Check that all values after submit (Name, Email, Current Address, Permanent Address)"):
            browser.element('.border').perform(command.js.scroll_into_view).should(
                Condition.by_and(have.text(f'Name:{self.user.first_name} {self.user.last_name}'),
                                 have.text(f'Email:{self.user.user_email}'),
                                 have.text(f'Current Address :{self.user.current_address}'),
                                 have.text(f'Permananet Address :{self.user.permanent_address}'),
                                 )
            )
        return self
