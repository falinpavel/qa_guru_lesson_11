import allure

from datetime import datetime
from selene import browser, be, have, command
from selene.core.condition import Condition

from const import Const
from helpers.config.links import Links
from helpers.data.user_info import PracticeFormUserGenerator


class PracticeFormPage:

    @property
    def practice_form_table(self):
        return browser.all('table.table-dark tbody tr')

    URL = Links.PRACTICE_FORM

    user = PracticeFormUserGenerator().get_random_user()

    @allure.step("Open Practice Form page")
    def open_page(self) -> 'PracticeFormPage':
        with allure.step(f"Open {self.URL}"):
            browser.open(self.URL)
        return self

    @allure.step("Filling form on Practice Form page and submit it")
    def registration_random_user_and_submit_form(self) -> 'PracticeFormPage':
        with allure.step("Filling #firstName field"):
            browser.element('#firstName').should(be.blank).type(self.user.first_name).should(be.not_.blank).should(
                have.attribute("value").value(self.user.first_name))
        with allure.step("Filling #lastName field"):
            browser.element('#lastName').should(be.blank).type(self.user.last_name).should(be.not_.blank).should(
                have.attribute("value").value(self.user.last_name))
        with allure.step("Filling #userEmail field"):
            browser.element('#userEmail').should(be.blank).type(self.user.user_email).should(be.not_.blank).should(
                have.attribute("value").value(self.user.user_email))
        with allure.step("Filling #gender field"):
            browser.all('[class="custom-control-label"]').element_by(
                have.text(self.user.gender)).click().should(be.enabled)
        with allure.step("Filling #userNumber field"):
            browser.element('#userNumber').should(be.blank).send_keys(self.user.user_number).should(
                be.not_.blank).should(have.attribute("value").value(self.user.user_number))
        with allure.step("Filling #dateOfBirth field and check that it is correct"):
            browser.element('#dateOfBirthInput').should(be.visible).click()
            browser.element('.react-datepicker__month-select').should(be.visible).click().all('[value]').element_by(
                have.text(self.user.birth_month)).click()
            browser.element('.react-datepicker__year-select').should(be.visible).click().all('[value]').element_by(
                have.attribute("value").value(self.user.birth_year)).click()
            browser.element('[class=react-datepicker__month][role="listbox"]').should(
                be.visible).all('div[role="option"]').element_by(have.text(self.user.birth_day)).click()
            browser.element('#dateOfBirthInput').should(Condition.by_and(have.attribute("value").value(
                f'{int(self.user.birth_day):02d} {self.user.birth_month[:3]} {self.user.birth_year}')))  # TODO!Optimize
        with allure.step("Filling #subjects field"):
            for subject in self.user.subjects:
                browser.element('#subjectsInput').should(be.visible).type(subject).press_enter()
        with allure.step("Filling #hobbies field"):
            for hobby in self.user.hobbies:
                browser.all('label[class="custom-control-label"]').element_by(
                    have.text(hobby)).should(be.visible).click().should(be.enabled)
        with allure.step("Filling #uploadPicture field"):
            browser.element('#uploadPicture').perform(command.js.scroll_into_view).send_keys(Const.UPLOADED_FILE)
        with allure.step("Filling #currentAddress field"):
            browser.element('#currentAddress').should(be.visible).should(
                be.blank).type(self.user.current_address).should(be.not_.blank).should(
                have.attribute("value").value(self.user.current_address))
        with allure.step("Filling #state field"):
            browser.element('#state').click().all('[tabindex="-1"]').element_by(have.text(self.user.state)).click()
        with allure.step("Filling #city field"):
            browser.element('#city').click().all('[tabindex="-1"]').element_by(have.text(self.user.city)).click()
        with allure.step("Click on #submit button"):
            browser.element('#submit').perform(command.js.scroll_into_view)
            browser.element('#submit').should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Check that all values after submit")
    def should_that_table_be_filled(self) -> 'PracticeFormPage':
        with allure.step("Check Student Name"):
            self.practice_form_table.element_by(have.text('Student Name')).all('td').second.should(
                have.text(f"{self.user.first_name} {self.user.last_name}"))
        with allure.step("Check Student Email"):
            self.practice_form_table.element_by(have.text('Student Email')).all('td').second.should(
                have.text(self.user.user_email))
        with allure.step("Check Gender"):
            self.practice_form_table.element_by(have.text('Gender')).all('td').second.should(
                have.text(self.user.gender))
        with allure.step("Check Mobile"):
            self.practice_form_table.element_by(have.text('Mobile')).all('td').second.should(
                have.text(self.user.user_number))
        with allure.step("Check Date of Birth"):
            self.practice_form_table.element_by(have.text('Date of Birth')).all('td').second.should(
                have.text(f'{self.user.birth_day} {self.user.birth_month},{self.user.birth_year}'))
        with allure.step("Check Subjects"):
            self.practice_form_table.element_by(have.text('Subjects')).all('td').second.should(
                have.text(', '.join(self.user.subjects)))
        with allure.step("Check Hobbies"):
            self.practice_form_table.element_by(have.text('Hobbies')).all('td').second.should(
                have.text(', '.join(self.user.hobbies)))
        with allure.step("Check Picture"):
            self.practice_form_table.element_by(have.text('Picture')).all('td').second.should(have.text("file.txt"))
        with allure.step("Check Address"):
            self.practice_form_table.element_by(have.text('Address')).all('td').second.should(
                have.text(self.user.current_address))
        with allure.step("Check State and City"):
            self.practice_form_table.element_by(have.text('State and City')).all('td').second.should(
                have.text(f"{self.user.state} {self.user.city}"))
        with allure.step("Click on #close button"):
            browser.element('#closeLargeModal').click()
        return self

    @allure.step("Check that all texts into form")
    def should_all_texts_into_form(self) -> 'PracticeFormPage':
        browser.element('.text-center').should(have.text('Practice Form'))
        browser.element('.practice-form-wrapper h5').should(have.text('Student Registration Form'))
        browser.element('#userName-wrapper').should(have.exact_text('Name'))
        browser.element('#firstName').should(have.attribute('placeholder').value('First Name'))
        browser.element('#lastName').should(have.attribute('placeholder').value('Last Name'))
        browser.element('#genterWrapper').should(have.text('Gender'))
        browser.all('.custom-radio').should(have.size(3)).should(have.exact_texts('Male', 'Female', 'Other'))
        browser.element('#userNumber-label').should(
            have.text('Mobile')).element('small').should(have.text('(10 Digits)'))
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

    @allure.step("Check that form not filled and not submitted")
    def form_not_filled_and_not_submitted(self) -> 'PracticeFormPage':
        with allure.step("Click on #submit button"):
            browser.element('#submit').perform(command.js.scroll_into_view)
            browser.element('#submit').should(be.visible).should(be.clickable).click()
        with allure.step("Check that form not filled and not submitted, elements not present"):
            browser.element('.modal-title').should(be.not_.present)
        return self
