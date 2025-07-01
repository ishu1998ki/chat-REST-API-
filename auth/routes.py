import uuid

from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse

from auth.utility import create_access_token
from models.dependencies import get_carbonhub_assistant_db, get_current_user
from models.assistant import Users, create_new_user_, get_user_by_email_, remove_user_
from schemas.auth import AddNewUserRequest, RemoveUserRequest, LoginRequest

router = APIRouter()


@router.post("/add")
def create_new_user(request: Request, data: AddNewUserRequest, db_session=Depends(get_carbonhub_assistant_db)):
    """
    Creates a new user in the system by processing the provided request and data.

    This function receives a request and user data, processes the data to add a
    new user to the system, and returns the relevant response. The function expects
    specific input data containing necessary details for adding a new user. Validation
    may be performed on the provided data before creating the user.
    """
    try:
        new_user = Users(
            id=uuid.uuid4(),
            user_name=data.user_name,
            email=data.email,
            password=data.password,
            first_name=data.first_name,
            last_name=data.last_name,
            phone_number=data.phone_number
        )

        result = create_new_user_(db_session, new_user)

        return JSONResponse(
            status_code=200,
            content={"status": "success",
                     "message": "User created successfully.",
                     "user_id": str(result.id),
                     "access_token": create_access_token(
                         data={
                             "sub": new_user.email,
                             "phone_number": new_user.phone_number,
                             "user_id": str(result.id),
                         }
                     )
                     }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "failed",
                     "message": f"Failed to create user. Error: {str(e)}"}
        )


@router.post("/login")
def login_user(request: Request, data: LoginRequest, db_session=Depends(get_carbonhub_assistant_db),
               current_user=Depends(get_current_user)):
    """
    Handles the login functionality for a user. This function authenticates a user
    based on the provided login credentials, establishes a session, and returns
    response details. It requires dependency-injected resources like the database
    session and the current user.

    :param request: Incoming HTTP request object.
    :type request: Request
    :param data: Data containing login credentials for the user.
    :type data: LoginRequest
    :param db_session: Database session dependency for performing database operations.
    :type db_session: Session
    :param current_user: The currently authenticated user, injected dependency.
                         May be None for unauthenticated users.
    :type current_user: User
    :return: The HTTP response object, typically indicating success or failure of the login operation.
    :rtype: Response
    """
    try:
        if current_user is None:
            user = get_user_by_email_(db_session, data.email)

            if user is None:
                print("user jwt not found")

                return JSONResponse(
                    status_code=404,
                    content={"status": "failed",
                             "message": "Invalid credintials."}
                )

            if user.password != data.password:
                return JSONResponse(
                    status_code=401,
                    content={"status": "failed",
                             "message": "Invalid credintials."}
                )

            access_token = create_access_token(
                data={
                    "sub": user.email,
                    "phone_number": user.phone_number,
                    "user_id": str(user.id),

                }
            )

            return JSONResponse(
                status_code=200,
                content={"status": "success",
                         "message": "Login successful.",
                         "user_id": str(user.id),
                         "access_token": access_token}
            )

        else:
            print("user jwt found")

            # check user is already in the system
            user = get_user_by_email_(db_session, current_user["sub"])

            if user is None:
                return JSONResponse(
                    status_code=404,
                    content={"status": "failed",
                             "message": "User not found."}
                )

            return JSONResponse(
                status_code=200,
                content={"status": "success",
                         "message": "User already logged in.",
                         "user_id": str(user.id)
                         }
            )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "failed",
                     "message": f"Failed to login user. Error: {str(e)}"}
        )


@router.delete("/delete")
def delete_user(request: Request, data: RemoveUserRequest, db_session=Depends(get_carbonhub_assistant_db)):
    """
    Deletes a user from the system based on the provided user ID.

    This endpoint is responsible for permanently removing a user
    record from the database. It requires a valid user ID to
    identify the user to be deleted and ensures that the respective
    entry is removed from the persistent storage.

    :param email:
    :param request: The HTTP request object provided by the application,
        which may include metadata about the request or other context.
    :type request: Request
    :param user_id: A universally unique identifier (UUID) that specifies
        the user to be deleted from the system.
    :param db_session: The database session dependency providing access
        to the application's persistent datastore.
    :return: None
    """
    try:
        user = get_user_by_email_(db_session, data.email)

        if user is None:
            return JSONResponse(
                status_code=404,
                content={"status": "failed",
                         "message": "User not found."}
            )

        remove_user_(db_session, user)

        return JSONResponse(
            status_code=200,
            content={"status": "success",
                     "message": "User deleted successfully."}
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "failed",
                     "message": f"Failed to delete user. Error: {str(e)}"}
        )
