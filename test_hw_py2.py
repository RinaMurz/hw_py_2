from selene import browser, be, have


def test_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_text_not_found():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('hvbherfbvrrygsvyrslffrgtpoliedrfgthyujikolp45677899').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу -hvbherfbvrrygsvyrslffrgtpoliedrfgthyujikolp45677899 ничего не найдено.'))
