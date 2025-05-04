from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_logic import generate_itinerary
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (för frontend-anslutning)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TripRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str
    interests: list[str]
    budget: int

@app.post("/generate")
def create_trip_plan(trip: TripRequest):
    try:
        itinerary = generate_itinerary(
            trip.destination,
            trip.start_date,
            trip.end_date,
            trip.interests,
            trip.budget
        )
        return {"plan": itinerary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
