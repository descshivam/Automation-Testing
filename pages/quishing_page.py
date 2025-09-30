import time
import datetime
from utils.browser_utils import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.deepfake_page import deepfake_simulation   # ✅ import deepfake


def quishing_simulation(driver):
    try:
        time.sleep(50)

        # Step 1: Click quishing button
        phishing = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[5]/h3/button/div"))
        )
        phishing.click()

        # Step 2: Click email campaign
        emailcampaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[5]/div/div/ul/li[1]/a/button"))
        )
        emailcampaign.click()

        # Step 3: Create campaign
        createcampaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div[1]/nav/div/div[2]/button"))
        )
        createcampaign.click()

        # Step 4: Campaign name
        campaignname = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[4]/div/div/input"))
        )
        random_campaign_name = "Quishing Campaign " + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        campaignname.send_keys(random_campaign_name)

        # … all your intermediate steps unchanged (recipients, template, landing page, domain, etc.) …

        # Step: Launch campaign
        launch_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section[2]/main/div/div[7]/button[2]'))
        )
        launch_btn.click()
        time.sleep(2)

        # ===== Toast detection =====
        toast_xpaths = [
            "//*[contains(translate(@class,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'toast') and contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'success')]",
            "//*[@role='alert' and contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'success')]",
            "//*[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'launched')]"
        ]
        toast_found = False
        for tx in toast_xpaths:
            try:
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, tx)))
                toast_found = True
                break
            except Exception:
                continue

        if toast_found:
            print("✅ Quishing campaign launched successfully — moving to deepfake_simulation...")
            try:
                deepfake_simulation(driver)   # ✅ call deepfake next
            except Exception as e:
                print("deepfake_simulation raised an error:", e)
        else:
            print("⚠️ No success toast detected — skipping deepfake_simulation.")

        time.sleep(5)

        # suit campaign button (unchanged)
        checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/span/div/button[3]"))
        )
        checkbox.click()
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")
        screenshot_path = "quishing_simulation_error.png"
        driver.save_screenshot(screenshot_path)
        print(f"Error captured at {screenshot_path}")
        raise e
