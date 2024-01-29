from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from hashlib import md5 
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    email = Column(String(50), primary_key=True, nullable=False)
    username = Column(String(50), nullable=False)
    _password = Column('password', String(200), nullable=False)
    login_attempts = Column(Integer, default=0)
    locked_until = Column(DateTime, default=None)
    created_at = Column(DateTime, default=func.now())

    # Setter y Getter para encriptar y desencriptar la contraseña usando MD5
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        self._password = md5(plaintext_password.encode('utf-8')).hexdigest()
    
    def check_password(self, password):
        hashed_password = md5(password.encode()).hexdigest()
        return hashed_password == self._password
    
    def get_username(self):
        return self.username