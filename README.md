# Distributed Job Queue System

A backend system for asynchronous job processing using FastAPI, Celery, and Redis.

This system allows long-running tasks to run in background workers without blocking the API.

---

## Features

• Submit jobs through API  
• Background task processing  
• Redis message broker  
• Celery worker execution  
• Job status tracking  

---

## Tech Stack

Python  
FastAPI  
Celery  
Redis  
SQLAlchemy  

---

## System Architecture

Client → FastAPI API → Redis Queue → Celery Workers → Database

Flow

1. Client submits job through API  
2. Job placed into Redis queue  
3. Celery worker picks task from queue  
4. Worker processes the job  
5. Job status updated in database  

---

## Project Structure

app/
- main.py
- routes/
- models/
- database/

workers/
- worker.py

tasks/
- tasks.py

requirements.txt  
README.md  

---

## Run Locally

Install dependencies

pip install -r requirements.txt

Start Redis

redis-server

Start Celery worker

celery -A workers.worker.celery worker --loglevel=info

Start FastAPI server

python -m uvicorn app.main:app --reload --port 8001

---

## Example API Usage

Create job

POST /jobs

{
"task_type": "generate_report"
}

Response

{
"job_id": 1,
"status": "pending"
}

Check job status

GET /jobs/1

Response

{
"job_id": 1,
"status": "completed",
"result": "Report generated successfully"
}

---

## Future Improvements

• task retries  
• scheduled jobs  
• distributed worker scaling  
• monitoring dashboard

