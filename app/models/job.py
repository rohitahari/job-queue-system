from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    task_type = Column(String)
    status = Column(String, default="pending")
    result = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
