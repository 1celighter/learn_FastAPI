from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home_page():
    return("welcome back to ur home page")

if __name__ == "__main__":
    uvicorn.run("two:app", reload=True)