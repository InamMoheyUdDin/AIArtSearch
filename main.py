from fastapi import FastAPI
from pydantic import BaseModel, Field
from ai_service.ai import filter_user_input
from function_call.retrieve_info import retrieve_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    input: str = Field(...)

@app.post("/submit")
def handle_input(request: UserInput):
    response = filter_user_input(request.input)
    data = retrieve_data(response)
    
    return data