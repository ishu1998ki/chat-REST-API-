from pydantic import BaseModel


class UserRegisterRequest(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    password: str


class UserRegisterResponse(BaseModel):
    status: bool
    message: str


class UserLoginRequest(BaseModel):
    user_name: str
    password: str


class UserLoginResponse(BaseModel):
    status: bool
    message: str


# class UpdatePasswordRequest(BaseModel):
#     user_name: str
#     current_password: str
#     new_password: str
#
#
# class UpdatePasswordResponse(BaseModel):
#     status: bool
#     message: str
#
#
# class DeleteRequest(BaseModel):
#     user_name: str
#     password: str
#
#
# class DeleteResponse(BaseModel):
#     status: bool
#     message: str
