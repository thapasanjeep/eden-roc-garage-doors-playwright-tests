from playwright.sync_api import Page, expect


class HomePage:
    # URL of this page
    URL = "https://edenrocgaragedoors.com.au"

    def __init__(self, page: Page):
        # Store the page object — equivalent to self.driver in Selenium
        self.page = page

    # --- Navigation actions ---

    def navigate(self):
        """Open the homepage in the browser"""
        self.page.goto(self.URL)

    def go_to_contact(self):
        """Click the CONTACT button in the header"""
        self.page.get_by_role("link", name="CONTACT", exact=True).click()

    def go_to_doors(self):
        """Navigate to Garage Doors page"""
        self.page.goto(f"{self.URL}/garage-doors/")

    def go_to_openers(self):
        """Navigate to Openers page"""
        self.page.goto(f"{self.URL}/openers/")

    # --- Assertions ---

    def verify_page_loaded(self):
        """Assert the homepage loaded correctly"""
        expect(self.page).to_have_url(f"{self.URL}/")
        expect(self.page.get_by_text("YOUR NEW INSULATED DOOR")).to_be_visible()

    def verify_nav_links_visible(self):
        """Assert all main nav links are present"""
        expect(self.page.get_by_role("link", name="CONTACT", exact=True)).to_be_visible()