import time
import datetime
from utils.browser_utils import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.vishing_page import vishing_simulation


def smishing_simulation(driver):
    try:
        time.sleep(50)  # small initial wait

        # Step 1: Click smishing button
        smishing_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[2]/h3/button/div"))
        )
        smishing_btn.click()
        time.sleep(5)
        # Step 2: Click SMS campaign
        sms_campaign = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[2]/div/div/ul/li[1]/a/button"))
        )
        sms_campaign.click()
        time.sleep(5)

        # Step 3: Click create campaign (more robust)
        create_campaign = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/nav/div/div[2]/button"))
        )
        create_campaign.click()

        # Step 4: Fill campaign name
        campaignname = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/input"))
        )
        random_campaign_name = "Phishing Campaign " + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        campaignname.send_keys(random_campaign_name)

        # Step 5: Select recipient
        recipient = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/div/div/button"))
        )
        recipient.click()

        dropdown_element = WebDriverWait(driver, 20).until(
            
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]"))
        )
        dropdown_element.click()

        # Step 6: Next button
        next_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[6]/button"))
        )
        next_btn.click()

        # Step 7: Select SMS template
        sms_template = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/div/button"))
        )
        sms_template.click()

        # Step 8: Choose first template
        template_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/button"))
        )
        template_option.click()

        # Step 9: Close template modal
        close_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/div/button"))
        )
        close_btn.click()

        # Step 10: Next step
        next_btn2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/button[2]"))
        )
        next_btn2.click()

        # Step 11: Select landing page
        landingpage = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/button"))
        )
        landingpage.click()

        choose_page = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/span[2]"))
        )
        choose_page.click()

        # Step 12: Select schedule time
        schedule_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/div[1]/button"))
        )
        schedule_btn.click()

        pick_time = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]"))
        )
        pick_time.click()

        # Step 13: Accept privacy / confirm
        checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[7]/button"))
        )
        checkbox.click()

        # Step 14: Launch campaign
        launch_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[8]/button[2]"))
        )
        launch_btn.click()
        
        # # suit campaign (unchanged)
        suit_campaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/span/div/div[3]/button"))
        )
        suit_campaign.click()
        
        time.sleep(10)
        driver.refresh()

        # # ===== Wait for toast =====
        # toast_xpaths = [
        #     "//*[contains(@class,'toast') and contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'success')]",
        #     "//*[@role='alert' and contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'success')]",
        #     "//*[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'launched')]"
        # ]
        # toast_found = False
        # for tx in toast_xpaths:
        #     try:
        #         WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, tx)))
        #         toast_found = True
        #         break
        #     except Exception:
        #         continue

        # if toast_found:
        #     print("✅ Smishing campaign launched successfully — moving to vishing_simulation...")
        vishing_simulation(driver)
        # else:
        #     print("⚠️ No success toast detected — skipping vishing_simulation.")

    except Exception as e:
        screenshot_path = "smishing_simulation_error.png"
        driver.save_screenshot(screenshot_path)
        print(f"❌ Error in smishing_simulation: {e}")
        print(f"Error captured at {screenshot_path}")
        raise
