from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn 

app = FastAPI()
songs = [
    {
        "SongId": 1,
        "SongName": "Faint",
        "SongAuthor": "Linkin Park"
    },
    {
        "SongId": 2,
        "SongName": "Не все дома",
        "SongAuthor": "Noize MC"
    }
]
@app.get("/CheckSongs",
         tags=["Songs"],
         summary="get all songs here")
def CheckSongs():
    return{
        "Message": "There all your songs",
        "Songs": songs
    }
@app.get("/CheckSongs/{SongById}",
         tags=["Songs"],
         summary="get song by song id")
def GetSongById(SongById: int):
    for song in songs:
        if song["SongId"] == SongById:
            return{
                "message": "there ur song what did u want to get",
                "Choiced Song": song
            }
    raise HTTPException(status_code=404, detail="Sadly but we dont have a song by this ID")

class NewSong(BaseModel):
    NewSongName: str
    NewSongAuthor: str

@app.post("/CreateNewSong",
          tags=["Songs"],
          summary="Create ur song there")
def GetNewSong(NSong:NewSong):
    songs.append({
        "SongId": len(songs) + 1,
        "SongName": NSong.NewSongName,
        "SongAuthor": NSong.NewSongAuthor
    })
    return{
        "Message": "There your new created song check before public ur song",
        "Song": NSong,
    }
if __name__ == "__main__":
    uvicorn.run("songs:app",reload=True)