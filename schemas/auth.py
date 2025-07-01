from pydantic import BaseModel


class AddNewUserRequest(BaseModel):
    user_name: str
    email: str
    password: str
    first_name: str
    last_name: str
    phone_number: str


class NewUserResponse(BaseModel):
    status: str
    message: str
    user_id: str


class LoginRequest(BaseModel):
    user_name: str
    password: str
    email: str


class LoginResponse(BaseModel):
    status: str
    message: str
    user_id: str


class RemoveUserRequest(BaseModel):
    email: str


class RemoveResponse(BaseModel):
    status: str
    message: str
    user_id: str
