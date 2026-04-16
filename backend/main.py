from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from ai_service.ai import filter_user_input
from function_call.retrieve_info import retrieve_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    input: str = Field(...)

@app.post("/submit")
def handle_input(request: UserInput):
    try:
        response = filter_user_input(request.input)
        data = retrieve_data(response)

        if not data:
            raise HTTPException(status_code=404, detail="No artwork found")

        return data

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")
    