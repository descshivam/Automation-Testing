import time
import datetime
from utils.browser_utils import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.quishing_page import quishing_simulation   # ✅ import quishing

def vishing_simulation(driver):
    try:
        time.sleep(50)

        # Step 1: Click vishing button
        phishing = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[3]/h3/button/div"))
        )
        phishing.click()

        # Step 2: Click voice campaign
        emailcampaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[3]/div/div/ul/li[1]/a/button"))
        )
        emailcampaign.click()

        # Step 3: Create campaign
        createcampaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/nav/div/div[2]/button"))
        )
        createcampaign.click()

        # Step 4: Campaign name
        campaignname = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[4]/div/div/input"))
        )
        random_campaign_name = "Vishing Campaign " + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        campaignname.send_keys(random_campaign_name)

        # … [KEEP all your intermediate steps unchanged: recipients, template, landing page, domain, etc.] …

        # Step: Launch campaign
        launch_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section[2]/main/div/div[7]/button[2]'))
        )
        launch_btn.click()
        time.sleep(2)
        
        # suit campaign (unchanged)
        

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
            print("✅ Vishing campaign launched successfully — moving to quishing_simulation...")
            try:
                quishing_simulation(driver)   # ✅ call quishing here
            except Exception as e:
                print("quishing_simulation raised an error:", e)
        else:
            print("⚠️ No success toast detected — skipping quishing_simulation.")

        time.sleep(5)

        # suit campaign (unchanged)
        suit_campaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/span/div/div[3]/button"))
        )
        suit_campaign.click()
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")
        screenshot_path = "vishing_simulation_error.png"
        driver.save_screenshot(screenshot_path)
        print(f"Error captured at {screenshot_path}")
        raise e
