import allure
from selene import be, by, browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.config.window_width = 1500
        browser.config.window_height = 900
        browser.open('')


    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)
