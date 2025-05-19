from fastapi import APIRouter
from schemas.auth import UserRegisterRequest, UserRegisterResponse, UserLoginRequest, UserLoginResponse
from models.users import connect_db, create_user, get_user_by_credetials

auth_router = APIRouter()
session = connect_db('sqlite:///./database/user.sqlite')


@auth_router.post("/register", response_model=UserRegisterResponse)
def new_user(data: UserRegisterRequest):
    try:
        result = create_user(session,
                             data.first_name,
                             data.last_name,
                             data.user_name,
                             data.password)
        return UserRegisterResponse(
            status=True,
            message="User registered successfully")

    except Exception as e:
        return UserRegisterResponse(
            status=False,
            message="User registration failed"
        )


@auth_router.post("/login", response_model=UserLoginResponse)
def user_login(data: UserLoginRequest):
    try:
        results = get_user_by_credetials(session,
                                         data.user_name,
                                         data.password)

        return UserLoginResponse(
            status=True,
            message="Login successful!"
        )

    except Exception as e:
        return UserLoginResponse(
            status=False,
            message="Invalid credentials!"
        )


# @auth_router.put("/user/update_password", response_model=UpdatePasswordResponse)
# def update_user_password(data: UpdatePasswordRequest):
#     try:
#         result = update_password(session,
#                                  data.user_name,
#                                  data.current_password,
#                                  data.new_password)
#
#         return UpdatePasswordResponse(
#             status=True,
#             message="Password update successful"
#         )
#     except Exception as e:
#         return UpdatePasswordResponse(
#             status=False,
#             message="Password update Failed!, {}".format(e)
#         )
#
#
# @auth_router.delete("/users/delete", response_model=DeleteResponse)
# def delete_user(data: DeleteRequest):
#     try:
#         result = delete(session,
#                         data.user_name,
#                         data.password)
#
#         return DeleteResponse(
#             status=True,
#             message="Account delete successful!"
#         )
#     except Exception as e:
#         return DeleteResponse(
#             status=False,
#             message="Account delete Failed!, {}".format(e)
#         )
