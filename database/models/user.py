from database import alchemy_db as db
import re
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
        # password_pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        # result = re.findall(password_pattern, password)

        if username[0].isdigit():
            print('username must start with a character')
        
        elif len(password) > 8:
            print('password must at list 8 character')

        else:
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

    def __repr__(self) -> str:
        return f"<User : {self.username}>"

    def register():
        pass

    @classmethod
    def login(cls, username, password):
        stmt = sql.select(cls).where(cls.username == username, cls.password == password)
        user = db.session.execute(stmt).one_or_none()

        print(user)

        return True if user is not None else False
        
    
