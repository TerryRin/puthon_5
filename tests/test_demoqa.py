from selene import browser, be, by, command

def test_form():
    browser.open('/automation-practice-form')
    #Заполнение формы
    browser.element('#firstName').should(be.blank).type('Gandalf')
    browser.element('#lastName').should(be.blank).type('Grey')
    browser.element('#userEmail').should(be.blank).type('gendalf@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('#89111111111')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('March')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2024')).click()
    browser.element('.react-datepicker__day--030').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    # browser.element('#uploadPicture').
    browser.element('#currentAddress').should(be.blank).type('adress')
    browser.element('#currentAddress').perform(command.js.scroll_into_view).click()
    browser.element('#state').click().element(by.text('Haryana')).click()
    browser.element('#city').click().element(by.text('Karnal')).click()
    browser.element('#"submit').click()
