from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

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

    search_url = f"https://www.naukri.com/{job_keyword}-jobs-in-{location}"
    driver.get(search_url)
    time.sleep(5)

    jobs = driver.find_elements(By.XPATH, "//a[@class='title fw500 ellipsis']")
    print(f"Found {len(jobs)} jobs")

    for job in jobs[:5]:
        job_link = job.get_attribute("href")
        driver.execute_script("window.open(arguments[0]);", job_link)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)

        try:
            apply_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Apply')]"))
            )
            apply_btn.click()
            time.sleep(3)
        except:
            print("⚠️ No apply button")

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    driver.quit()

def run_job_application(job_title, location, resume_path):
    email = "YOUR_EMAIL"
    password = "YOUR_PASSWORD"
    naukri_auto_apply(email, password, resume_path, job_title, location)
