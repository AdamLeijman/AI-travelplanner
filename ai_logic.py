# ai_logic.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_itinerary(destination, start_date, end_date, interests, budget):
    prompt = f"""
    Create a day-by-day travel itinerary from {start_date} to {end_date} in {destination}.
    Interests: {', '.join(interests)}. Budget: {budget} :-.
    Include activities, restaurants, and sightseeing for each day. Be creative and specific.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
