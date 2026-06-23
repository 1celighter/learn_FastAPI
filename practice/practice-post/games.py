from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

games = [
    {
        "Game-ID": 1,
        "The game name": "Dota 2",
        "Genre of this game": "MOBA"
    },
    {
        "Game-ID": 2,
        "The game name": "Risk of Rain 2",
        "Genre of this game": "Looter-Shooter"
    }
]

@app.get("/games",
        tags=["Library"],
        summary="Get the all games in this library")
def get_games():
    return {f"there all games from library and they name's are{games}"}

@app.get("/get_game/{Game_id}",
         tags=["Library"],
         summary="get game by 'Game-ID'")
def get_game(Game_id: int):
    for game in games:
        if game["Game-ID"] == Game_id:
            return {f"there are your game searched by Game-ID - {game}"}
    raise HTTPException(status_code=404, detail="that game has been not found in your library try to add they")

class NewGame(BaseModel): # ниже описываем то что будет наследоваться в будущем что бы было проще добавлять
    The_game_name: str
    The_game_genre: str

@app.post("/New_game",
          tags=["Library"],
          summary="add your own game!")
def add_game(newgame:NewGame):
    games.append({
        "Game-ID": len(games) + 1,
        "The game name": newgame.The_game_name,
        "The game genre": newgame.The_game_genre
    })
    return{f"There are ur updated library {games}"}


if __name__ == "__main__":
    uvicorn.run("games:app", reload=True)
