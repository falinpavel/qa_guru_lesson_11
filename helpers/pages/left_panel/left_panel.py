from selene import browser, command

from helpers.config.links import Links


class LeftPanel:

    URL = Links.FORMS

    def open_page(self):
        browser.open(self.URL)
        return self

    def click_to_elements(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Elements")]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_forms(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Forms")]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_alerts_frames_windows(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Alerts, Frame & Windows")]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_widgets(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Widgets")]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_interactions(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Interactions")]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_book_store(self):
        browser.element('//*[contains(@class, "header-text")][contains(text(), "Book Store Application")]').perform(
            command.js.scroll_into_view).click()
        return self


class LeftPanelElements(LeftPanel):

    def click_to_text_box(self):
        browser.element('//span[normalize-space()="Text Box"]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_check_box(self):
        browser.element('//span[normalize-space()="Check Box"]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_radio_button(self):
        browser.element('//span[normalize-space()="Radio Button"]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_web_tables(self):
        browser.element('//span[normalize-space()="Web Tables"]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_buttons(self):
        browser.element('//span[normalize-space()="Buttons"]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_links(self):
        browser.element('//span[normalize-space()="Links"]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_broken_links_images(self):
        browser.element('//span[normalize-space()="Broken Links - Images"]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_upload_and_download(self):
        browser.element('//span[normalize-space()="Upload and Download"]').perform(
            command.js.scroll_into_view).click()
        return self

    def click_to_dynamic_properties(self):
        browser.element('//span[normalize-space()="Dynamic Properties"]').perform(
            command.js.scroll_into_view).click()
        return self


class LeftPanelForms(LeftPanel):

    def click_to_practice_form(self):
        browser.element('//span[normalize-space()="Practice Form"]').perform(
            command.js.scroll_into_view).click()
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