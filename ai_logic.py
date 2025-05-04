import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_itinerary(destination, start_date, end_date, interests, budget):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # eller "gpt-4" om du har tillgång
        messages=[
            {"role": "system", "content": "You are a helpful travel assistant."},
            {"role": "user", "content": f"""Plan a trip to {destination} from {start_date} to {end_date}.
            Interests: {', '.join(interests)}.
            Budget: {budget} USD.
            Provide a daily itinerary."""}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
