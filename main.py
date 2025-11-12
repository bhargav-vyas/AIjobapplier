from ai_agent import interpret_command
from job_search import search_jobs
from cover_letter import generate_cover_letter
from auto_apply import auto_apply
import csv
import datetime
import csv
import datetime


def main():
    command = input("Enter your command: ")
    task = interpret_command(command)

    print("\n🧠 Interpreted Command:")
    print(task)  # ✅ Debug print

    job_title = task.get("job_title", "")
    location = task.get("location", "")

    print("\n🔍 Searching jobs...")
    jobs = search_jobs(job_title, location)

    print(f"✅ Found {len(jobs)} jobs")

    for job in jobs[:3]:
        print(f"\n💼 Applying: {job['title']} at {job['company']}")
        cover_letter = generate_cover_letter(job['title'], job['company'], ["Python", "AI", "Automation"])
        print("\n📝 Cover Letter:\n", cover_letter)

        auto_apply(job["link"], "C:/resume.pdf")

if __name__ == "__main__":
    main()
