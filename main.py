import threading
from time import time
from pages.login_page import login_simulation

from pages.phishing_page import phishing_simulation
from pages.smishing_page import smishing_simulation
from pages.vishing_page import vishing_simulation
from pages.quishing_page import quishing_simulation
from pages.deepfake_page import deepfake_simulation
from utils.browser_utils import get_driver

def run_simulations():
    driver = get_driver()

    try:
        # Run simulations one by one
        login_simulation(driver)
        phishing_simulation(driver)
        smishing_simulation(driver)
        vishing_simulation(driver)
        quishing_simulation(driver)
        deepfake_simulation(driver)

    finally:
        driver.quit()

if __name__ == '__main__':
    run_simulations()
