from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from src.email_notifier import send_daily_log
from dotenv import load_dotenv
import os
import time

load_dotenv()

def naukri_auto_apply(email, password, resume_path, job_keyword, location):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    print("🌐 Opening Naukri Login Page...")
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)

    driver.find_element(By.ID, "usernameField").send_keys(email)
    driver.find_element(By.ID, "passwordField").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)

    print("🔍 Searching for jobs...")
    search_url = f"https://www.naukri.com/{job_keyword}-jobs-in-{location}"
    driver.get(search_url)
    time.sleep(5)

    # Updated XPath — safer and more stable
    jobs = driver.find_elements(By.XPATH, "//a[contains(@class,'title')]")
    print(f"DEBUG: Found {len(jobs)} job links")

    applied_count = 0

    # ⭐ NEW LOOP STARTS HERE (OPTION D IMPLEMENTED)
    for i, job in enumerate(jobs[:5]):  # Process first 5 jobs
        try:
            job_link = job.get_attribute("href")

            # Open job in new tab
            driver.execute_script("window.open(arguments[0]);", job_link)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(4)

            try:
                # Try Apply button
                apply_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Apply')]"))
                )
                apply_btn.click()
                time.sleep(3)

                print(f"✅ Applied to job {i+1}: {job_link}")
                applied_count += 1

            except:
                print(f"⚠️ No direct apply button for job {i+1}")

            # Close job tab and return to search page
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        except Exception as e:
            print(f"❌ Error on job {i+1}: {e}")
            try:
                driver.switch_to.window(driver.window_handles[0])
            except:
                pass

    print("\n🎯 All job applications completed.")
    print(f"🟢 Successfully applied to {applied_count} jobs.")

    # Keep browser open for review
    print("⌛ Keeping browser open for 10 seconds...")
    time.sleep(10)

    # Clean close
    driver.quit()
    print("🧹 Browser closed cleanly.")


def run_job_application(job_title, location, resume_path):
    try:
        email = os.getenv("NAUKRI_EMAIL")
        password = os.getenv("NAUKRI_PASSWORD")

        naukri_auto_apply(email, password, resume_path, job_title, location)

    except Exception as e:
        print("🔥 FATAL ERROR:", e)
