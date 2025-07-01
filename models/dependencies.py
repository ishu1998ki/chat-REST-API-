import datetime
import os
import jwt

from fastapi import Request
from datetime import datetime
from models.assistant import Session


def get_carbonhub_assistant_db():
    session = Session()

    try:
        yield session

    except Exception as e:
        session.rollback()

        raise e

    finally:
        session.close()


# def get_carbonhub_db():
#     session = CarbonHubSession()
#
#     try:
#         return session
#
#     except Exception as e:
#         session.rollback()
#
#         raise e
#
#     finally:
#         session.close()


def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return None

    token = auth_header.replace("Bearer ", "")

    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])

        # check if the token is expired
        if payload.get("exp") and datetime.utcnow().timestamp() > payload.get("exp"):
            return None

        return payload


    except jwt.InvalidTokenError as e:

        print(f"JWT Error: {str(e)}")

        return None

    except Exception as e:

        print(f"Error decoding token: {str(e)}")

        return None
