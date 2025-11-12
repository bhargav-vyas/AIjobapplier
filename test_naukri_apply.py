import os
from dotenv import load_dotenv
from naukri_apply import naukri_auto_apply
import csv
import datetime

load_dotenv()

email = os.getenv("NAUKRI_EMAIL")
password = os.getenv("NAUKRI_PASSWORD")
resume = os.getenv("RESUME_PATH")

naukri_auto_apply(email, password, resume, "python-developer", "pune")
