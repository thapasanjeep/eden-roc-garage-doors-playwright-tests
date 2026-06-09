from playwright.sync_api import Page, expect


class ContactPage:
    URL = "https://edenrocgaragedoors.com.au/contact/"

    def __init__(self, page: Page):
        self.page = page

    # --- Navigation ---

    def navigate(self):
        """Go directly to the contact page"""
        self.page.goto(self.URL)

    # --- Form actions ---
    # Each method does ONE thing — fill a single field
    # This makes tests readable and easy to maintain

    def fill_name(self, name: str):
        self.page.get_by_role("textbox", name="Name").fill(name)

    def fill_email(self, email: str):
        self.page.get_by_role("textbox", name="Email").fill(email)

    def fill_phone(self, phone: str):
        self.page.get_by_role("textbox", name="Phone").fill(phone)

    def fill_message(self, message: str):
        self.page.get_by_role("textbox", name="Message").fill(message)

    def fill_address(self, address: str):
        # Note: the website has a typo — "Adresss" with 3 s's
        self.page.get_by_role("textbox", name="Adresss").fill(address)

    def fill_form(self, name: str, email: str, phone: str,
                  message: str, address: str):
        """Fill all form fields at once — convenience method"""
        self.fill_name(name)
        self.fill_email(email)
        self.fill_phone(phone)
        self.fill_message(message)
        self.fill_address(address)

    def click_submit(self):
        self.page.get_by_role("button", name="Submit").click()

    # --- Assertions ---

    def verify_page_loaded(self):
        """Assert contact page loaded correctly"""
        expect(self.page).to_have_url(self.URL)
        expect(self.page.get_by_role(
            "heading", name="Contact").first).to_be_visible()

    def verify_all_fields_visible(self):
        """Assert all form fields are present on the page"""
        expect(self.page.get_by_role("textbox", name="Name")).to_be_visible()
        expect(self.page.get_by_role("textbox", name="Email")).to_be_visible()
        expect(self.page.get_by_role("textbox", name="Phone")).to_be_visible()
        expect(self.page.get_by_role("textbox", name="Message")).to_be_visible()
        expect(self.page.get_by_role("textbox", name="Adresss")).to_be_visible()

    def verify_field_values(self, name: str, email: str,
                            phone: str, message: str):
        """Assert fields contain the expected values after filling"""
        expect(self.page.get_by_role(
            "textbox", name="Name")).to_have_value(name)
        expect(self.page.get_by_role(
            "textbox", name="Email")).to_have_value(email)
        expect(self.page.get_by_role(
            "textbox", name="Phone")).to_have_value(phone)
        expect(self.page.get_by_role(
            "textbox", name="Message")).to_have_value(message)