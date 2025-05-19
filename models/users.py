from sqlalchemy import create_engine, Column, Integer, Text, VARCHAR, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    user_name = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)


def init_db(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    return engine


def connect_db(db_url):
    engine = init_db(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


def create_user(session, first_name, last_name, user_name,password):
    new_user = Users(
        first_name=first_name,
        last_name=last_name,
        user_name=user_name,
        password=password
    )

    session.add(new_user)
    session.commit()

    return new_user


def get_user_by_credetials(session, user_name, password):
    user = session.query(Users).filter_by(user_name=user_name, password=password).first()

    if not user:
        raise Exception("Invalid credentials")
    return user


def update_password(session, user_name, current_password, new_password):
    user = session.query(Users).filter_by(user_name=user_name, password=current_password).first()

    if not user:
        raise Exception("Invalid credentials")

    user.password = new_password
    session.commit()
    return user


def delete(session, user_name, password):
    user = session.query(Users).filter_by(user_name=user_name, password=password).first()

    if not user:
        raise Exception("Invalid credentials")

    session.delete(user)
    session.commit()

    return user

