from pydantic import BaseModel


# class WelcomeRequest(BaseModel):
#     user_name: str
#
#
# class WelcomeResponse(BaseModel):
#     greeting: str


# class UserMessageRequest(BaseModel):
#     user_message: str
#
#
# class UserMessageResponse(BaseModel):
#     message: str
#
#
# class BotMessageRequest(BaseModel):
#     bot_message: str
#
#
# class BotMessageResponse(BaseModel):
#     message: str


class ChatRequest(BaseModel):
    message: str


class ChatRequestResponse(BaseModel):
    bot_message: str
