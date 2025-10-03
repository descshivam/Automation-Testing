
import time
import datetime
from utils.browser_utils import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.deepfake_page import deepfake_simulation



def quishing_simulation(driver):
    try:
        # time.sleep(5)  # small initial wait

        # Step 1: Click quishing button
        quishing_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[5]/h3/button/div"))
        )
        quishing_btn.click()
        time.sleep(10)

        # Step 2: Click Email campaign
        email_campaign = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[5]/div/div/ul/li[1]/a/button"))
        )
        email_campaign.click()
        time.sleep(10)

        # Step 3: Click create campaign
        create_campaign = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/nav/div/div[2]/button"))
        )
        create_campaign.click()

        # Step 4: Fill campaign name
        campaignname = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/input"))
        )
        random_campaign_name = "Quishing Campaign " + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        campaignname.clear()
        campaignname.send_keys(random_campaign_name)

        # Step 5: Select recipient
        recipient = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/div[1]/div/button"))
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

        # Step 7: Select email template
        email_template = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/div/button"))
        )
        email_template.click()
        template_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/button"))
        )
        template_option.click()
        close_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/div/button"))
        )
        close_btn.click()
        time.sleep(2)

        # Step 8: Next step
        next_btn2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/button[2]"))
        )
        next_btn2.click()

        # Step 9: Select landing page
        landingpage = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/button"))
        )
        landingpage.click()
        choose_page = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/span[2]"))
        )
        choose_page.click()

        # Step 10: Select schedule time
        schedule_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/div[1]/button"))
        )
        schedule_btn.click()
        pick_time = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]"))
        )
        pick_time.click()
        
        # click to next button 
        next_schedule_btn = WebDriverWait(driver, 20).until(    
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[6]/button[2]"))
        )
        next_schedule_btn.click()

        # form name
        form_name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div[1]/div/input"))
        )
        form_name.send_keys("test")
        
        # send domain
        click =WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/div/div/button"))
        )   
        click.click()
            
            
            
        send_domain = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]"))
        )
        send_domain.click()

        # Step 11: Accept privacy / confirm
        checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[6]/button"))
        )
        checkbox.click()

        # Step 12: Launch campaign
        launch_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[7]/button[2]"))
        )
        launch_btn.click()
        time.sleep(5)

        # Step 13: Suit campaign and refresh
        suit_campaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/span/div/div[3]/button"))
        )
        suit_campaign.click()
        time.sleep(10)
        driver.refresh()

        # Step 14: Call deepfake simulation
        try:
            print("✅ Quishing campaign created — calling deepfake_simulation...")
            deepfake_simulation(driver)
        except Exception as e:
            print(f"⚠️ deepfake_simulation or vishing_simulation not available or failed: {e}")

    except Exception as e:
        screenshot_path = "quishing_simulation_error.png"
        driver.save_screenshot(screenshot_path)
        print(f"❌ Error in quishing_simulation: {e}")
        print(f"Error captured at {screenshot_path}")
        raise
