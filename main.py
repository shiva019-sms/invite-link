from fastapi import FastAPI
from models import PersonRequest, PersonResponse
from aggregator import aggregate_person_info

app = FastAPI()

@app.post("/api/profile", response_model=PersonResponse)
async def get_profile(request: PersonRequest):
    return await aggregate_person_info(request)