from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Job
from tasks.tasks import process_job


router =APIRouter()


@router.post("/jobs")
def create_job(task_type: str, db: Session = Depends(get_db)):

    new_job = Job(
        task_type=task_type,
        status="pending"
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    # send job to background worker
    process_job.delay(new_job.id)

    return {
        "job_id": new_job.id,
        "status": new_job.status
    }








@router.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return {
        "job_id": job.id,
        "task_type": job.task_type,
        "status": job.status,
        "result": job.result
    }
