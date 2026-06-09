import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage

BASE_URL = "https://edenrocgaragedoors.com.au"


@pytest.fixture()
def home_page(page):
    """
    Returns a HomePage object ready to use in any test.
    'page' here is the Playwright page fixture injected by pytest-playwright.
    We wrap it in our HomePage class and return it.
    """
    return HomePage(page)


@pytest.fixture()
def contact_page(page):
    """Returns a ContactPage object ready to use in any test"""
    return ContactPage(page)