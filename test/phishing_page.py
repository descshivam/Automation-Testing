import logging
import pytest
from pages.phishing_page import PhishingPage

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")


def test_phishing_flow(driver):
    """
    Test only the phishing flow (assumes user is already logged in).
    You may need to run test_login first, or configure login steps here if required.
    """
    phishing_page = PhishingPage(driver)

    logging.info("Starting phishing flow test...")
    phishing_page.run_full_phishing_flow()

    # Add assertion to confirm phishing campaign was created or progressed
    assert "Phishing" in driver.page_source or "Campaign" in driver.page_source
