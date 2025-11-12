from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import datetime


def naukri_auto_apply(email, password, resume_path, job_keyword, location):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    print("🌐 Opening Naukri Login Page...")
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)

    # 🔐 Login
    driver.find_element(By.ID, "usernameField").send_keys(email)
    driver.find_element(By.ID, "passwordField").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)

    # 🔍 Search for jobs
    print("🔍 Searching for jobs...")
    search_url = f"https://www.naukri.com/{job_keyword}-jobs-in-{location}"
    driver.get(search_url)
    time.sleep(5)

    jobs = driver.find_elements(By.XPATH, "//a[@class='title fw500 ellipsis']")
    print(f"✅ Found {len(jobs)} jobs")

    applied_count = 0

    for i, job in enumerate(jobs[:5]):  # First 5 jobs for test ✅
        try:
            job_link = job.get_attribute("href")

            # Open job in new tab
            driver.execute_script("window.open(arguments[0]);", job_link)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(4)

            try:
                # Click Apply Button
                apply_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Apply')]"))
                )
                apply_btn.click()
                time.sleep(3)

                print(f"✅ Applied to job {i+1}: {job_link}")
                applied_count += 1

            except:
                print(f"⚠️ No direct apply button for job {i+1}")

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        except Exception as e:
            print("❌ Error:", e)

    print(f"\n🎯 Auto-applied to {applied_count} jobs ✅")
    driver.quit()
