from database import alchemy_db as db
from sqlalchemy import sql
from sqlalchemy import (
    Column,
    Integer,
    String
)


class UserModel(db.Base):
    __tablename__ = 'account_user'

    def __init__(self,username, password):
        self.username = username
        self.password = password

    id = Column(
        Integer,
        primary_key = True
    )
    
    username = Column(
        String(255),
        nullable = False,
        unique = True
    )

    password = Column(
        String(255),
        nullable = False,
    )
    
    @classmethod
    def create(cls, username, password):
        stmt = sql.insert(cls).values(
            username = username, 
            password = password
            )
        db.session.execute(stmt)
        db.session.commit()

    @classmethod
    def update(cls, old_username, new_username):
        stmt = sql.update(cls).where(cls.username == old_username).values(
            old_username = new_username, 
            )
        db.session.execute(stmt)
        db.session.commit()

    
    @classmethod
    def read(cls, username):
        stmt = sql.select(cls).where(cls.username == username)
        user = db.session.execute(stmt).one_or_none()
        return user

    
    @classmethod
    def delete(cls, username):
        stmt = sql.delete(cls).where(cls.username == username)
        db.session.execute(stmt)
        db.session.commit()