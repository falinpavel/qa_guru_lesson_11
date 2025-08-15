import allure
from selene import browser, command, be

from helpers.config.links import Links


class LeftPanel:

    URL = Links.FORMS

    @allure.step("Open Left Panel page")
    def open_page(self):
        with allure.step(f"Open {self.URL}"):
            browser.open(self.URL)
        return self

    @allure.step("Click to Elements group")
    def click_to_elements(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Elements")]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Forms group")
    def click_to_forms(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Forms")]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Alerts, Frame & Windows group")
    def click_to_alerts_frames_windows(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Alerts, Frame & Windows")]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Widgets group")
    def click_to_widgets(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Widgets")]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Interactions group")
    def click_to_interactions(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Interactions")]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Book Store Application group")
    def click_to_book_store(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Book Store Application")]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self


class LeftPanelElements(LeftPanel):

    @allure.step("Click to Text Box")
    def click_to_text_box(self):
        browser.element('//span[normalize-space()="Text Box"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Check Box")
    def click_to_check_box(self):
        browser.element('//span[normalize-space()="Check Box"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Radio Button")
    def click_to_radio_button(self):
        browser.element('//span[normalize-space()="Radio Button"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Web Tables")
    def click_to_web_tables(self):
        browser.element('//span[normalize-space()="Web Tables"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Buttons")
    def click_to_buttons(self):
        browser.element('//span[normalize-space()="Buttons"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Links")
    def click_to_links(self):
        browser.element('//span[normalize-space()="Links"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Broken Links - Images")
    def click_to_broken_links_images(self):
        browser.element('//span[normalize-space()="Broken Links - Images"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Upload and Download")
    def click_to_upload_and_download(self):
        browser.element('//span[normalize-space()="Upload and Download"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self

    @allure.step("Click to Dynamic Properties")
    def click_to_dynamic_properties(self):
        browser.element('//span[normalize-space()="Dynamic Properties"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self


class LeftPanelForms(LeftPanel):

    @allure.step("Click to Practice Form")
    def click_to_practice_form(self):
        browser.element('//span[normalize-space()="Practice Form"]').perform(
            command.js.scroll_into_view).should(be.visible).should(be.clickable).click()
        return self


# class LeftPanelAlertsFramesWindows(LeftPanel):
#     raise NotImplementedError
#
#
# class LeftPanelWidgets(LeftPanel):
#     raise NotImplementedError
#
#
# class LeftPanelInteractions(LeftPanel):
#     raise NotImplementedError
#
#
# class LeftPanelBookStore(LeftPanel):
#     raise NotImplementedError