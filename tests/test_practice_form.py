from selene import browser, have, command
import os


def test_complete_practice_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('test')
    browser.element('#lastName').type('user')
    browser.element('#userEmail').type('test@user.com')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('79999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="11"]').click()
    browser.element('.react-datepicker__year-select').type('2000')
    browser.element('.react-datepicker__day.react-datepicker__day--025').click()
    browser.element('#subjectsInput').type('math').press_enter()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('//input[@type="file"]').send_keys(os.path.abspath("image.jpg"))
    browser.element('#currentAddress').type('Ростов-сити, Забугорная 3к1')
    browser.element('//*[@id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('//*[@id="react-select-4-input"]').type('Delhi').press_enter()
    browser.element('//footer').perform(command.js.remove)
    browser.all('#userForm > div').should(have.size(11))
    browser.element('#submit').click()
    browser.all('#todo-list>li').by(have.css_class('was-validated'))
    browser.element("//tbody/tr[1]").should(have.text("test user"))
    browser.element("//tbody/tr[2]").should(have.text("test@user.com"))
    browser.element("//tbody/tr[3]").should(have.text("Female"))
    browser.element("//tbody/tr[4]").should(have.text("Mobile 7999999999"))
    browser.element("//tbody/tr[5]").should(have.text("Date of Birth 25 December,2000"))
    browser.element("//tbody/tr[6]").should(have.text("Math"))
    browser.element("//tbody/tr[7]").should(have.text("Reading"))
    browser.element("//tbody/tr[8]").should(have.text("image.jpg"))
    browser.element("//tbody/tr[9]").should(have.text("Ростов-сити, Забугорная 3к1"))
    browser.element("//tbody/tr[10]").should(have.text("NCR Delhi"))










