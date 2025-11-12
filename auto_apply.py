from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import datetime


def auto_apply(job_link, resume_path):
    driver = webdriver.Chrome()
    driver.get(job_link)
    time.sleep(3)
    
    try:
        driver.find_element(By.NAME, "resume").send_keys(resume_path)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        print(f"✅ Applied to {job_link}")
    except Exception as e:
        print(f"⚠️ Failed to apply: {e}")

    driver.quit()
