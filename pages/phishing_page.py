import time
import datetime
from utils.browser_utils import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.smishing_page import smishing_simulation

def phishing_simulation(driver):
    try:

        time.sleep(50)

        # Step 1: Click phishing button
        phishing = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div[2]/div/div[1]/h3/button"))
        )
        phishing.click()

        # Step 2: Click email campaign
        emailcampaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div[2]/div/div[1]/div/div/ul/li[1]/a/button"))
        )
        emailcampaign.click()

        # Step 3: Click create campaign
        createcampaign = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/nav/div/div[2]/button"))
        )
        createcampaign.click()

        # Step 4: Fill in campaign name (Only click if not filled)
        campaignname = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[4]/div/div/input"))
        )
        random_campaign_name = "Phishing Campaign " + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        campaignname.send_keys(random_campaign_name)

        # Step 5: Select recipient (Only click if not selected)
        recipient = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[5]/div/div/button"))
        )
        recipient.click()
        # time.sleep(5)
        dropdown_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[1]/div[1]"))
        )
        dropdown_element.click()
        # time.sleep(5)

        # Step 7:click next button
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[5]/div[2]/button"))
        )
        submit_button.click()

        # Step 8: Select email template (Only click if needed)
        email = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[4]/div/div/div/button"))
        )
        email.click()

        # Step 9: Ensure template selection only happens once
        driver.implicitly_wait(20)
        all_template_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/button"))
        )
        all_template_button.click()
        time.sleep(5)
        # Step 10: Close email page (Only if it's open)
        closepage_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[4]/div/div/div/button"))
        )
        closepage_button.click()

        # Step 11: click next button
        retry_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div[2]/button[2]"))
        )
        retry_button.click()
        # time.sleep(10)


        # slelect landing page 
        landingpage  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[4]/div/div/button"))
        )
        landingpage .click()
        # time.sleep(5)
        
        choose  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/span[2]"))
        )
        choose.click()
        # time.sleep(5)
        # select time on landing page
        driver.implicitly_wait(10)
        Timeoflandingpage = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[4]/div[2]/div[1]/button"))

        )
        Timeoflandingpage.click()

        # select time from dropdown 30 second
        next = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/span[2]"))
        )
        next.click()
        # time.sleep(5)

         #click multiple visit landing page
         
        multiplevisit  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[4]/div[2]/div[4]/button"))
        )
        # click on the next button
        retry_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/main/div/div[4]/div[3]/button[2]"))
        )
        retry_button.click()
        # time.sleep(10)
        
        
        # form name
        time_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section[2]/main/div/div[4]/div[1]/div/input'))
        )
        time_element.send_keys("test")
        # time.sleep(5)

        # select sending domain
        landingpage  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/section[2]/main/div/div[5]/div[1]/div/button'))
        )
        landingpage .click()
        # time.sleep(5)

        choose  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/span[2]'))
        )
        choose.click()
        # time.sleep(5)
        
        # privicy check box 
       
  
        checkbox  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[5]/div[2]/button"))
        )
        checkbox.click()
        # time.sleep(10)

        # click to cammpagin launch
        choose  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section[2]/main/div/div[5]/div[3]/button[2]'))
        )
        choose.click()
        # time.sleep(2)  # short pause to let UI create the toast

        # ===== wait for "campaign launched" toast then call smishing_simulation =====
        
        # click on suit campaign
        checkbox  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/span/div/button[3]"))
        )
        checkbox.click()
        time.sleep(5)
        
        # refresh the page 
        # refresh = WebDriverWait(driver, 20).until(  
        #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/main/div/nav/div/div[1]/button"))

        # )
        # refresh.click()
        driver.refresh()
        # time.sleep(10)
        
        
                # ===== wait for "campaign launched" toast then call smishing_simulation =====
        try:
            toast_xpaths = [
                # matches toast/alerts with "success" or "launched"
                "//*[contains(translate(@class,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'toast') "
                "and (contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'success') "
                "or contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'launched'))]",

                "//*[@role='alert' and (contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'success') "
                "or contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'launched'))]",

                "//*[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'launched') "
                "or contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'success')]"
            ]

            toast_element = None
            for tx in toast_xpaths:
                try:
                    toast_element = WebDriverWait(driver, 30).until(
                        EC.visibility_of_element_located((By.XPATH, tx))
                    )
                    if toast_element:
                        break
                except Exception:
                    continue

            if toast_element:
                print("✅ Campaign launch toast detected — calling smishing_simulation...")
                # driver.refresh()
                try:
                    smishing_simulation(driver)
                except Exception as e:
                    print("❌ smishing_simulation raised an error:", e)
            else:
                print("⚠️ No campaign-launch toast found within timeout; skipping smishing_simulation.")
        except Exception as e:
            print("⚠️ Toast detection error:", e)
        # ===== end toast detection + call =====


    except Exception as e:
        print(f"Error: {e}") 
        screenshot_path = "phishing_simulation_error.png"
        driver.save_screenshot(screenshot_path)
        print(f"Error captured at {screenshot_path}")
        raise e
