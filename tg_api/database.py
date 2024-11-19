from __future__ import annotations

from datetime import datetime
from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


engine = create_async_engine("sqlite+aiosqlite:///tasks.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class StudentOrm(Model):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    email: Mapped[str]
    department: Mapped[str]
    year_name: Mapped[str]
    pref_array: Mapped[str | None]


class PoolOrm(Model):
    __tablename__ = "pools"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    opt_values: Mapped[str | None]
    opt_names: Mapped[str | None]


class AnswerOrm(Model):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    value: Mapped[str]
    pool_name: Mapped[str | None]
    get_time: Mapped[datetime | None]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
