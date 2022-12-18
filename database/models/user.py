from database import alchemy_db as db
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
        unique = True
    )

    password = Column(
        String(255),
    )
