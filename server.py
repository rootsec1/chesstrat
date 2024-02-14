from fastapi import FastAPI
# Local
from service import *

app = FastAPI()


@app.get("/")
async def root():
    return {"ping": "pong"}


# Function to accept lichess ID and get all their games and moves for each game
@app.get("/analyze/{lichess_id}")
async def analyze_games(lichess_id: str):
    games = get_user_games_and_moves(lichess_id)
    return {"games": games}
