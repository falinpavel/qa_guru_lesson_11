from datetime import datetime
from selene import browser, be, have, command
from selene.core.condition import Condition

from helpers.config.links import Links
from const import UPLOADED_FILE
from helpers.data.user_info import PracticeFormUserGenerator


class PracticeFormPage:

    @property
    def practice_form_table(self):
        return browser.all('table.table-dark tbody tr')

    URL = Links.PRACTICE_FORM

    user = PracticeFormUserGenerator().get_random_user()

    def open_page(self) -> 'PracticeFormPage':
        browser.open(self.URL)
        return self

    def registration_random_user_and_submit_form(self) -> 'PracticeFormPage':
        browser.element('#firstName').should(be.blank).type(self.user.first_name).should(be.not_.blank).should(
            have.attribute("value").value(self.user.first_name))
        browser.element('#lastName').should(be.blank).type(self.user.last_name).should(be.not_.blank).should(
            have.attribute("value").value(self.user.last_name))
        browser.element('#userEmail').should(be.blank).type(self.user.user_email).should(be.not_.blank).should(
            have.attribute("value").value(self.user.user_email))
        browser.all('[class="custom-control-label"]').element_by(
            have.text(self.user.gender)).click().should(be.enabled)
        browser.element('#userNumber').should(be.blank).send_keys(self.user.user_number).should(
            be.not_.blank).should(have.attribute("value").value(self.user.user_number))
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').should(be.visible).click().all('[value]').element_by(
            have.text(self.user.birth_month)).click()
        browser.element('.react-datepicker__year-select').should(be.visible).click().all('[value]').element_by(
            have.attribute("value").value(self.user.birth_year)).click()
        browser.element('[class=react-datepicker__month][role="listbox"]').should(
            be.visible).all('div[role="option"]').element_by(have.text(self.user.birth_day)).click()
        browser.element('#dateOfBirthInput').should(Condition.by_and(have.attribute("value").value(
            f'{int(self.user.birth_day):02d} {self.user.birth_month[:3]} {self.user.birth_year}')))# TODO! Optimize
        for subject in self.user.subjects:
            browser.element('#subjectsInput').should(be.visible).type(subject).press_enter()
        for hobby in self.user.hobbies:
            browser.all('label[class="custom-control-label"]').element_by(
                have.text(hobby)).should(be.visible).click().should(be.enabled)
        browser.element('#uploadPicture').perform(command.js.scroll_into_view).send_keys(UPLOADED_FILE)
        browser.element('#currentAddress').should(be.visible).should(be.blank).type(self.user.current_address).should(
            be.not_.blank).should(have.attribute("value").value(self.user.current_address))
        browser.element('#state').click().all('[tabindex="-1"]').element_by(have.text(self.user.state)).click()
        browser.element('#city').click().all('[tabindex="-1"]').element_by(have.text(self.user.city)).click()
        browser.element('#submit').perform(command.js.scroll_into_view).click()
        return self

    def should_that_table_be_filled(self) -> 'PracticeFormPage':
        self.practice_form_table.element_by(have.text('Student Name')).all('td').second.should(
            have.text(f"{self.user.first_name} {self.user.last_name}"))
        self.practice_form_table.element_by(have.text('Student Email')).all('td').second.should(
            have.text(self.user.user_email))
        self.practice_form_table.element_by(have.text('Gender')).all('td').second.should(have.text(self.user.gender))
        self.practice_form_table.element_by(have.text('Mobile')).all('td').second.should(have.text(self.user.user_number))
        self.practice_form_table.element_by(have.text('Date of Birth')).all('td').second.should(
            have.text(f'{self.user.birth_day} {self.user.birth_month},{self.user.birth_year}'))
        self.practice_form_table.element_by(have.text('Subjects')).all('td').second.should(
            have.text(', '.join(self.user.subjects)))
        self.practice_form_table.element_by(have.text('Hobbies')).all('td').second.should(
            have.text(', '.join(self.user.hobbies)))
        self.practice_form_table.element_by(have.text('Picture')).all('td').second.should(have.text("file.txt"))
        self.practice_form_table.element_by(have.text('Address')).all('td').second.should(
            have.text(self.user.current_address))
        self.practice_form_table.element_by(have.text('State and City')).all('td').second.should(
            have.text(f"{self.user.state} {self.user.city}"))
        browser.element('#closeLargeModal').click()
        return self

    def should_all_texts_into_form(self) -> 'PracticeFormPage':
        browser.element('.text-center').should(have.text('Practice Form'))
        browser.element('.practice-form-wrapper h5').should(have.text('Student Registration Form'))
        browser.element('#userName-wrapper').should(have.exact_text('Name'))
        browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
        browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
        browser.element('#genterWrapper').should(have.text('Gender'))
        browser.all('.custom-radio').should(have.size(3)).should(have.exact_texts('Male', 'Female', 'Other'))
        browser.element('#userNumber-label').should(have.text('Mobile')).element('small').should(
            have.text('(10 Digits)'))
        browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number'))
        browser.element('#dateOfBirth-label').should(have.text('Date of Birth'))
        browser.element('#dateOfBirthInput').should(have.attribute('value').value(datetime.now().strftime('%d %b %Y')))
        browser.element('#subjectsWrapper').should(have.text('Subjects'))
        browser.element('#hobbiesWrapper').should(have.text('Hobbies'))
        browser.all('.custom-checkbox').should(have.size(3)).should(have.exact_texts('Sports', 'Reading', 'Music'))
        browser.element('#currentAddress-wrapper').should(have.text('Current Address'))
        browser.element('#currentAddress').should(have.attribute('placeholder').value('Current Address'))
        browser.element('#stateCity-wrapper').should(have.text('State and City'))
        return self

    def form_not_filled_and_not_submitted(self) -> 'PracticeFormPage':
        browser.element('#submit').click()
        # browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
        browser.element('.modal-title').should(be.not_.present)
        return self