import csv, datetime


with open("applied_jobs.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(["Job Title", "Company", "Link", "Date", "Cover Letter"])
    writer.writerow(["Test Job", "Test Company", "https://example.com", datetime.date.today(), "Sample cover letter"])

print("✅ CSV file created successfully!")
