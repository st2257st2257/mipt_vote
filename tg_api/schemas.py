from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class SStudentAdd(BaseModel):
    login: str
    email: str
    department: str
    year_name: str
    pref_array: str | None = None


class SStudent(SStudentAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SStudentId(BaseModel):
    id: int


class SPoolAdd(BaseModel):
    name: str
    description: str
    opt_values: str
    opt_names: str


class SPool(SPoolAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SPoolId(BaseModel):
    id: int


class SAnswerAdd(BaseModel):
    name: str
    value: str
    pool_name: str
    get_time: str


class SAnswer(SAnswerAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SAnswerId(BaseModel):
    id: int
