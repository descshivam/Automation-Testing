# pages/vishing_page.py
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def vishing_simulation(driver):
    try:
        time.sleep(30)  # small initial wait

        # Step 1: Click vishing button
        vishing_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[3]/h3/button/div"))
        )
        vishing_btn.click()
        time.sleep(10)

        # Step 2: Click Voice campaign
        voice_campaign = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div[1]/div[2]/div/div[3]/div/div/ul/li[1]/a/button"))
        )
        voice_campaign.click()
        time.sleep(5)

        # Step 3: Click create campaign
        create_campaign = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div[1]/nav/div/div[2]/button"))
        )
        create_campaign.click()

        # Step 4: Fill campaign name
        campaignname = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/input"))
        )
        random_campaign_name = "Vishing Campaign " + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
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

        # Step 7: Select voice template
        voice_template = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/div/button"))
        )
        voice_template.click()
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
        
        # selecte voice
        voice_template_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div/div/button"))
        )
        voice_template_btn.click()

        select_voice = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[1]/div[1]"))
        )
        select_voice.click()
        
        # click next button 
        next_voice_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/button[2]"))
        )
        next_voice_btn.click()

       

        # Step 12: Fill form name
        form = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div[1]/div/input"))
        )
        form.send_keys("Vishing Form")

        # Step 13: Select domain
        domain_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/div/div/button"))
        )
        domain_btn.click()
        select_domain = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]"))
        )
        select_domain.click()
        
         # Step 11: Accept privacy / confirm
        checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[6]/button"))
        )
        checkbox.click()

        # Step 14: Launch campaign
        launch_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[7]/button[2]"))
        )
        launch_btn.click()
        time.sleep(5)

        # Step 15: Suit campaign and refresh
        suit_campaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/span/div/div[3]/button"))
        )
        suit_campaign.click()
        time.sleep(10)

        driver.refresh()

        # Step 16: Call phishing simulation
        try:
            from pages.phishing_page import phishing_simulation
            print("✅ Vishing campaign created — calling phishing_simulation...")
            phishing_simulation(driver)
        except Exception as e:
            print(f"⚠️ phishing_simulation not available or failed: {e}")

    except Exception as e:
        screenshot_path = "vishing_simulation_error.png"
        driver.save_screenshot(screenshot_path)
        print(f"❌ Error in vishing_simulation: {e}")
        print(f"Error captured at {screenshot_path}")
        raise
