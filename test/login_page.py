import logging
import pytest
from pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")


@pytest.mark.parametrize("app_url, username, password", [
    ("https://sim.verasity.ai/login", "sadmin@verasity.ai", "GTFgqX?k#bIS#;b7"),  # replace with env variables ideally
])
def test_login(driver, app_url, username, password):
    """
    Test only the login flow.
    """
    login_page = LoginPage(driver)

    logging.info("Starting login test...")
    login_page.login(app_url, username, password)

    # Add assertion to confirm login worked (example: check if brand element exists)
    assert "Campaign" in driver.page_source or "Dashboard" in driver.page_source
