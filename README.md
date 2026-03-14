# Background Job Queue System

A production-style background job processing system built with FastAPI, Redis, Celery, and PostgreSQL.

## Architecture

Client → FastAPI API → PostgreSQL → Redis Queue → Celery Worker → Background Processing → Database Update

## Tech Stack

- FastAPI
- PostgreSQL
- Redis
- Celery
- SQLAlchemy

## Features

- Create asynchronous jobs
- Track job status
- Background task processing
- Distributed worker architecture
- Persistent job storage

## API Endpoints

Create Job

POST /jobs

Check Job Status

GET /jobs/{job_id}

## Example Flow

1. Client creates job
2. Job stored in PostgreSQL
3. Task pushed to Redis queue
4. Celery worker processes task
5. Job status updated

## Run Locally

Start Redis

```
redis-server
```

Start API

```
uvicorn app.main:app --reload
```

Start Worker

```
celery -A workers.worker.celery worker --loglevel=info
```

## Example Response

```
{
  "job_id": 1,
  "status": "completed",
  "result": "Report generated successfully"
}
```

---

This project demonstrates real backend patterns used in scalable production systems.

