from fastapi import FastAPI

from src.app.infrastructure.controller.chat_controller import chat_router
    
app = FastAPI()
app.include_router(chat_router)