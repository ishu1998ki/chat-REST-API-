import os
import uuid

from sqlalchemy.dialects.postgresql import UUID
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, Text, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

Base = declarative_base()

engine = create_engine(os.getenv("DB_URL"), echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base.metadata.create_all(engine)


class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, index=True)
    user_name = Column(VARCHAR, nullable=False, unique=True)
    email = Column(VARCHAR, nullable=False, unique=True)
    password = Column(VARCHAR(15), nullable=False)
    first_name = Column(VARCHAR, nullable=False)
    last_name = Column(VARCHAR, nullable=False)
    phone_number = Column(VARCHAR, nullable=False, unique=True)


try:
    print("Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")

except Exception as e:
    print(f"Error creating tables: {e}")


def create_new_user_(session, user: Users):
    session.add(user)
    session.commit()
    session.refresh(user)

    return user


def get_user_by_email_(session, email: str):
    return session.query(Users).filter(Users.email == email).first()


def remove_user_(session, user: Users):
    session.delete(user)
    session.commit()
