from selene import browser, have, command


def test_complete_practice_form():
    browser.open('/')
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
    browser.element('//*[@id="hobbiesWrapper"]/div[2]/div[2]/label').click()
    browser.element('//input[@type="file"]').send_keys('/home/user/Изображения/image.jpg')
    browser.element('#currentAddress').type('Ростов-сити, Забугорная 3к1')
    browser.element('//*[@id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('//*[@id="react-select-4-input"]').type('Delhi').press_enter()
    browser.element('//footer').perform(command.js.remove)
    browser.all('#userForm > div').should(have.size(11))
    browser.element('#submit').click()
    browser.all('#todo-list>li').by(have.css_class('was-validated'))
    browser.all('div.modal-body > div > table > tbody > tr').should(have.size(10))










