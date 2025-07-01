import uuid

from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse

from models.assistant import get_user_by_email_
from models.dependencies import get_carbonhub_assistant_db, get_current_user

router = APIRouter()


@router.get("history")
async def get_conversations(request: Request,
                            db_session=Depends(get_carbonhub_assistant_db),
                            current_user=Depends(get_current_user)):
    try:
        authed_user = current_user.get("sub")
        user = get_user_by_email_(db_session, authed_user)

        if user is None:
            return JSONResponse(
                status_code=401,
                content={"status": "Failed",
                         "message": "Unauthorized access"
                         }
            )

        return JSONResponse(
            status_code=200,
            content={"status": "Success",
                     "message": "Conversation retrieved successfully",
                     "data": [
                         {
                             "ID": 1,
                             "Title": "Conversation",
                             "created at": "2024.06.26",
                             "Updaed at": "2024.06.26"
                         },
                         {
                             "ID": 2,
                             "Title": "Conversation",
                             "created at": "2024.06.26",
                             "Updaed at": "2024.06.26"
                         }
                     ]}
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "Failed",
                     "message": "Unauthorized access"
                     }
        )
