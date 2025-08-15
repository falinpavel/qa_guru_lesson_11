from selene import browser, be, have, command
from selene.core.condition import Condition

from helpers.config.links import Links
from helpers.data.user_info import TextBoxUserGenerator


class TextBoxPage:
    URL = Links.TEXT_BOX

    user = TextBoxUserGenerator().get_random_user()

    def open_page(self):
        browser.open(self.URL)
        return self

    def registration_random_user_and_submit_form(self) -> 'TextBoxPage':
        browser.element('#userName').should(be.blank).type(f'{self.user.first_name} {self.user.last_name}').should(
            be.not_.blank).should(have.attribute("value").value(f'{self.user.first_name} {self.user.last_name}'))
        browser.element('#userEmail').should(be.blank).type(self.user.user_email).should(be.not_.blank).should(
            have.attribute("value").value(self.user.user_email))
        browser.element('#currentAddress').should(be.blank).type(self.user.current_address).should(
            be.not_.blank).should(
            have.attribute("value").value(self.user.current_address))
        browser.element('#permanentAddress').should(be.blank).type(self.user.permanent_address).should(
            be.not_.blank).should(have.attribute("value").value(self.user.permanent_address))
        browser.element('#submit').perform(command.js.scroll_into_view).click()
        return self

    def should_all_values_after_submit(self) -> 'TextBoxPage':
        browser.element('.border').perform(command.js.scroll_into_view).should(
            Condition.by_and(have.text(f'Name:{self.user.first_name} {self.user.last_name}'),
                             have.text(f'Email:{self.user.user_email}'),
                             have.text(f'Current Address :{self.user.current_address}'),
                             have.text(f'Permananet Address :{self.user.permanent_address}'),
                             )
        )
        return self