import time

from workers.worker import celery
from app.database import SessionLocal
from app.models import Job


@celery.task
def process_job(job_id):

    db = SessionLocal()

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        print("Job not found")
        return

    job.status = "processing"
    db.commit()

    print(f"Processing job {job_id}")

    time.sleep(10)

    job.status = "completed"
    job.result = "Report generated successfully"

    db.commit()

    print(f"Finished job {job_id}")

    db.close()

