from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import BIGINT, SMALLINT, DateTime, ForeignKeyConstraint, MetaData, ForeignKey, String, UniqueConstraint, select, text

from typing import List, Optional

from datetime import datetime

import enum

metadata = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True, nullable=False)]


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    metadata=metadata

    id: Mapped[intpk]
    telegram_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    regisration_time: Mapped[datetime] = mapped_column(DateTime, server_default=text("TIMEZONE('utc', now())"))
    username: Mapped[str] = mapped_column(String(20), nullable=True)

    group_permission: Mapped[List["User_StudGroup_associate"]] = relationship(
        "User_StudGroup_Permission_associate", 
        back_populates="user"
    )

class StudGroup(Base):
    __tablename__ = 'groups'
    metadata=metadata

    id: Mapped[intpk]
    groupname: Mapped[str] = mapped_column(String(20))

    user_permission: Mapped[List["User_StudGroup_associate"]] = relationship(
        "User_StudGroup_Permission_associate", 
        back_populates="group"
    )

class Permission(Base):
    __tablename__ = 'permissions'
    metadata=metadata

    id: Mapped[intpk]
    permname: Mapped[str] = mapped_column(String(30))

    user_group: Mapped[List["User_StudGroup_Permission_associate"]] = relationship(
        "User_StudGroup_Permission_associate", 
        back_populates="permission"
    )

class User_StudGroup_associate(Base):
    __tablename__ = "user_studgroup_associate"
    metadata=metadata
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), primary_key=True)

    user: Mapped["User"] = relationship(
        "User", 
        back_populates="group_permission"
    )
    group: Mapped["StudGroup"] = relationship(
        "StudGroup", 
        back_populates="user_permission"
    )

    permissions: Mapped[List["User_StudGroup_Permission_associate"]] = relationship(
        "User_StudGroup_Permission_associate", 
        back_populates="user_group"
    )
    

class User_StudGroup_Permission_associate(Base):
    __tablename__ = "user_studgroup_permission_associate"
    metadata=metadata
    
    id: Mapped[intpk]

    user_id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(primary_key=True)

    permission: Mapped[Permission] = relationship(
        "Permission", 
        back_populates="user_group"
    )
    
    user_group: Mapped["User_StudGroup_associate"] = relationship(
        "User_StudGroup_associate",
        back_populates="permissions",
        foreign_keys=[user_id, group_id]
    )

    __table_args__ = (
        ForeignKeyConstraint(
            ['user_id', 'group_id'], 
            ['user_studgroup_associate.user_id', 'user_studgroup_associate.group_id']
        ),
    )