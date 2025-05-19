from fastapi import APIRouter, Request
from schemas.chat import ChatRequest, ChatRequestResponse
# WelcomeRequest, WelcomeResponse,

chat_router = APIRouter()


# @chat_router.get("/welcome", response_model=WelcomeResponse)
# async def welcome(data: WelcomeRequest):
#     username = data.user_name
#
#     return {"greeting": f"Welcome {username}"}


# @chat_router.post("/user_message", response_model=UserMessageResponse)
# async def message(data: UserMessageRequest):
#     user_message = data.user_message
#
#     return UserMessageResponse(message=user_message)
#
#
# @chat_router.post("/bot_message", response_model=BotMessageResponse)
# async def chat(data: BotMessageRequest):
#     bot_message = "Here you are"
#     return BotMessageResponse(
#         response=bot_message
#     )

@chat_router.post("/chat", response_model=ChatRequestResponse)
async def chat(data: ChatRequest):
    message = data.message

    bot_message = f"Thanks for chatting. Your question is: {message}"

    return ChatRequestResponse(
            bot_message=bot_message
        )

