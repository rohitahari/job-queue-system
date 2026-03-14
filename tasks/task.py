import time

from workers.worker import celery

from app.database import SessionLocal
from app.models import Job


@celery.task
def process_job(job_id):

    db = SessionLocal()

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return "Job not found"

    # mark job as processing
    job.status = "processing"
    db.commit()

    print(f"Processing job {job_id}")

    # simulate heavy work
    time.sleep(10)

    # mark job completed
    job.status = "completed"
    job.result = "Report generated successfully"

    db.commit()

    print(f"Finished job {job_id}")

    db.close()

    return "completed”
