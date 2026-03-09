import datetime as dt
import logging
from pydantic import BaseModel
from enum import Enum


class CalendarSource(Enum):
    GOOGLE = "google"
    MICROSOFT = "microsoft"


class CalendarEvent(BaseModel):
    id: str
    title: str
    start_time: dt.datetime
    end_time: dt.datetime | None = None
    source: CalendarSource
