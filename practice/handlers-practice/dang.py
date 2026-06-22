from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/home-handler")
def home_handler():
    return {"message": "something else", "ID": "1"}

if __name__ == "__main__":
    uvicorn.run("dang:app", reload=True)