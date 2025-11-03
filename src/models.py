from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import BIGINT, SMALLINT, DateTime, MetaData, select, text

from datetime import datetime

import enum

metadata = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

class Gender(enum.Enum):
    default = 0
    male = 1
    female = 2

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    metadata=metadata
    id: Mapped[intpk]
    telegram_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    regisration_time: Mapped[datetime] = mapped_column(DateTime, server_default=text("TIMEZONE('utc', now())"))
    name: Mapped[str]
    email: Mapped[str]
    age: Mapped[int] = mapped_column(SMALLINT)
    gender: Mapped["Gender"] = mapped_column(default=Gender.default.name)

    