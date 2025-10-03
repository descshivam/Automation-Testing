import time
import json
import os
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.quishing_page import quishing_simulation

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Ensure folders exist
os.makedirs("screenshots", exist_ok=True)
os.makedirs("audit_logs", exist_ok=True)

AUDIT_LOG_PATH = "audit_logs/audit.log"

def write_audit_entry(entry: dict):
    try:
        with open(AUDIT_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        logging.error(f"Failed to write audit log: {e}")

def capture_screenshot(driver, test_name):
    try:
        timestamp = int(time.time())
        screenshot_name = f"screenshots/{test_name}_error_{timestamp}.png"
        for file in os.listdir("screenshots"):
            if file.startswith(test_name):
                os.remove(os.path.join("screenshots", file))
        driver.save_screenshot(screenshot_name)
        return screenshot_name
    except Exception as e:
        logging.error(f"Failed to capture screenshot: {str(e)}")
        return None

def run_step(driver, step_name, func, test_name="login_simulation"):
    start = time.time()
    try:
        result = func()
        duration = time.time() - start
        write_audit_entry({
            "test": test_name,
            "step": step_name,
            "success": True,
            "duration": duration,
            "message": "Step successful"
        })
        logging.info(f"[{step_name}] Success ({duration:.2f}s)")
        return True, result
    except Exception as e:
        duration = time.time() - start
        screenshot = capture_screenshot(driver, test_name)
        write_audit_entry({
            "test": test_name,
            "step": step_name,
            "success": False,
            "duration": duration,
            "error": str(e),
            "screenshot": screenshot
        })
        logging.error(f"[{step_name}] Failed: {e}")
        return False, e

def login_simulation(driver):
    test_name = "login_simulation"
    steps = []

    # Step 1: open page
    steps.append(run_step(driver, "open_page", lambda: driver.get("http://localhost:3000/"), test_name))

    # Step 2: Cognito button
    steps.append(run_step(driver, "click_cognito_button", lambda: WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[2]/form/div/div[2]/a/button"))
    ).click(), test_name))

    # Step 3: username
    steps.append(run_step(driver, "enter_username", lambda: WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="signInFormUsername"]'))
    ).send_keys("sadmin@verasity.ai"), test_name))

    # Step 4: password + sign in
    def enter_password():
        driver.find_element(By.XPATH, '//*[@id="signInFormPassword"]').send_keys("GTFgqX?k#bIS#;b7")
        driver.find_element(By.NAME, 'signInSubmitButton').click()
    steps.append(run_step(driver, "enter_password_and_signin", enter_password, test_name))

    # Step 5: maximize (unchanged)
    steps.append(run_step(driver, "maximize_window", lambda: driver.maximize_window(), test_name))

    # Step 6: brand element
    steps.append(run_step(driver, "click_brand_element", lambda: WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[1]/div/div[2]/div/nav/div[2]"))
    ).click(), test_name))
    time.sleep(10)
    # Step 7: brand button (YOUR ORIGINAL XPATH KEPT EXACTLY)
    steps.append(run_step(driver, "click_brand_button", lambda: WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div[2]/div/div/span/div/button[1]"))
    ).click(), test_name))

    # Step 8: final wait
    steps.append(run_step(driver, "final_wait", lambda: time.sleep(30), test_name))

    if any(not s[0] for s in steps):
        logging.error("Login simulation failed — running quishing_simulation")

        quishing_simulation(driver)
        
        write_audit_entry({"test": test_name, "overall_success": False})
    else:
        logging.info("Login simulation successful")
        write_audit_entry({"test": test_name, "overall_success": True})
