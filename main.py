from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/", summary="Main hand", tags=["main handlers"])
def home():
    return{"message": "hello world"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) # хорошая практика что бы код был читабелен и девопсу и бекендеру 