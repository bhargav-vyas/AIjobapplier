import requests
import csv
import datetime

from bs4 import BeautifulSoup

def search_jobs(title, location):
    url = f"https://www.indeed.com/jobs?q={title}&l={location}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job_card in soup.select(".result"):
        title_el = job_card.select_one("h2")
        if title_el:
            link = "https://www.indeed.com" + title_el.find("a")["href"]
            company = job_card.select_one(".companyName")
            jobs.append({
                "title": title_el.text.strip(),
                "company": company.text.strip() if company else "Unknown",
                "link": link
            })
    return jobs
