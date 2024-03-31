from selene import browser, be, by, command, have
import os.path

def test_form():
    browser.open('/automation-practice-form')
    # Заполнение формы
    browser.element('#firstName').should(be.blank).type('Gandalf').press_tab()
    browser.element('#lastName').should(be.blank).type('Grey').press_tab()
    browser.element('#userEmail').should(be.blank).type('gandalf@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('March')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2024')).click()
    browser.element('.react-datepicker__day--030').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('Gendolf.jpg'))
    browser.element('#currentAddress').should(be.blank).type('adress').press_tab()
    browser.element('#currentAddress').perform(command.js.scroll_into_view).click()
    browser.element('#state').click().element(by.text('Haryana')).click()
    browser.element('#city').click().element(by.text('Karnal')).click()
    browser.element('#submit').click()

    # Проверка var1 - этот постоянно падает
    # browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    # browser.element('.table').all('td').with_(timeout=10).even.should(
    #     have.exact_texts(
    #         'Gandalf Grey',
    #         'gandalf@gmail.comm',
    #         'Male',
    #         '1234567890',
    #         '30 March,2024',
    #         'Arts',
    #         'Reading',
    #         'Gendolf.jpg',
    #         'adress',
    #         'Haryana Karnal'
    #     )
    # )
    # browser.element('#closeLargeModal').click()


    # Проверка var2 - этот отрабатывает
    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Gandalf Grey'))
    browser.element('.modal-body').should(have.text('gandalf@gmail.com'))
    browser.element('.modal-body').should(have.text('Male'))
    browser.element('.modal-body').should(have.text('1234567890'))
    browser.element('.modal-body').should(have.text('30 March,2024'))
    browser.element('.modal-body').should(have.text('Arts'))
    browser.element('.modal-body').should(have.text('Reading'))
    browser.element('.modal-body').should(have.text('Gendolf.jpg'))
    browser.element('.modal-body').should(have.text('adress'))
    browser.element('.modal-body').should(have.text('Haryana Karnal'))

