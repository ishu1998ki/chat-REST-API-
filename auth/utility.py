import os
import jwt
from dotenv import load_dotenv
from datetime import timedelta, datetime
from typing import Optional


load_dotenv()


def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Creates a JSON Web Token (JWT) for a given payload and an optional expiration
    time. The resulting token is used for authentication purposes and includes
    encoded information about the user or entity to which it is assigned.

    :param data: Payload to include in the token. This is typically a dictionary
        containing user or entity identifiers and claims.
    :type data: dict
    :param expires_delta: Optional time duration for token expiration. If provided,
        the token will be valid for the specified duration from token creation.
        Otherwise, a default expiration time will be applied.
    :type expires_delta: Optional[timedelta]
    :return: Encoded JWT string including the input payload and expiration time
        when applicable.
    :rtype: str
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({"exp": expire.timestamp()})

    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise ValueError("SECRET_KEY environment variable not set")

    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm="HS256")
    print(f"Token created successfully: {encoded_jwt[:50]}...")

    return encoded_jwt
