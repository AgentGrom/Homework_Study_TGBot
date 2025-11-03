from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import BIGINT, SMALLINT, DateTime, MetaData, select, text

from datetime import datetime

import enum

metadata = MetaData()