import pytest
import requests
from selenium import webdriver
import helper
from data import Urls
from pages.personal_account_page import PersonalPage


@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    driver = None

    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1080")
        options.add_argument("--height=1920")
        driver = webdriver.Firefox(options=options)

    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def create_and_delete_user():
    body = helper.body
    response = requests.post(f'{Urls.CREATE_USER}', json=body)
    token = response.json().get('accessToken')

    yield helper.body, token

    requests.delete(f'{Urls.DELETE_USER}', headers={'Authorization': f'{token}'})


@pytest.fixture(scope='function')
def login(driver, create_and_delete_user):
    payload, token = create_and_delete_user
    email = payload["email"]
    password = payload["password"]
    page = PersonalPage(driver)
    page.open_page(Urls.LOGIN_URL)
    page.account(email, password)

    return driver
