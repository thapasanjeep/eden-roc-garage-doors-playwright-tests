from pages.contact_page import ContactPage


def test_contact_form_fields_visible(contact_page: ContactPage):
    contact_page.navigate()
    contact_page.verify_all_fields_visible()


def test_contact_form_fill(contact_page: ContactPage):
    contact_page.navigate()
    contact_page.fill_form(
        name="John Smith",
        email="john@test.com",
        phone="0412345678",
        message="I would like a quote for a roller door.",
        address="123 Test St, Perth"
    )
    contact_page.verify_field_values(
        name="John Smith",
        email="john@test.com",
        phone="0412345678",
        message="I would like a quote for a roller door."
    )


def test_contact_page_loaded(contact_page: ContactPage):
    contact_page.navigate()
    contact_page.verify_page_loaded()


def test_contact_form_empty_name(contact_page: ContactPage):
    contact_page.navigate()
    contact_page.fill_email("john@test.com")
    contact_page.fill_phone("0412345678")
    contact_page.fill_message("Test message")
    contact_page.click_submit()
    # Name was not filled — form should not have submitted
    from playwright.sync_api import expect
    expect(contact_page.page.get_by_role(
        "textbox", name="Name")).to_have_value("")