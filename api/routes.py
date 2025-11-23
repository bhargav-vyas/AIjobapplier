from fastapi import APIRouter
from pydantic import BaseModel
from src.naukri_apply import run_job_application
from src.logger import logger
import os
import glob
import pandas as pd

router = APIRouter()

# ⭐ NEW MODEL with job_count + experience
class JobRequest(BaseModel):
    job_title: str
    location: str
    resume_path: str
    job_count: int
    experience: int


@router.post("/apply-job")
def apply_job(req: JobRequest):
    logger.info(
        f"API called — Applying for '{req.job_title}' in '{req.location}', "
        f"Experience: {req.experience} years, Jobs to apply: {req.job_count}"
    )

    try:
        run_job_application(
            req.job_title,
            req.location,
            req.resume_path,
            req.job_count,
            req.experience
        )
        return {
            "status": "success",
            "message": "JobPilot AI started applying to the jobs!"
        }

    except Exception as e:
        logger.error(f"Error applying job: {e}")
        return {"status": "error", "message": str(e)}


@router.get("/logs")
def get_logs():
    try:
        log_dir = os.path.join(os.getcwd(), "logs")

        if not os.path.exists(log_dir):
            return {"status": "no_logs"}

        files = sorted(glob.glob(os.path.join(log_dir, "*.log")), reverse=True)

        if not files:
            return {"status": "no_logs"}

        latest_file = files[0]

        with open(latest_file, "r", encoding="utf-8") as f:
            content = f.read()

        return {"status": "success", "log": content}

    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.get("/applied-jobs")
def applied_jobs():
    if not os.path.exists("applied_jobs.csv"):
        return {"status": "no_data"}

    df = pd.read_csv("applied_jobs.csv")
    return {"status": "success", "data": df.to_dict(orient="records")}
