from pages.home_page import HomePage


def test_doors_navigation(home_page: HomePage):
    home_page.navigate()
    home_page.go_to_doors()
    from playwright.sync_api import expect
    expect(home_page.page).to_have_url(
        "https://edenrocgaragedoors.com.au/garage-doors/")


def test_openers_navigation(home_page: HomePage):
    home_page.navigate()
    home_page.go_to_openers()
    from playwright.sync_api import expect
    expect(home_page.page).to_have_url(
        "https://edenrocgaragedoors.com.au/openers/")


def test_contact_navigation(home_page: HomePage):
    home_page.navigate()
    home_page.go_to_contact()
    from playwright.sync_api import expect
    expect(home_page.page).to_have_url(
        "https://edenrocgaragedoors.com.au/contact/")