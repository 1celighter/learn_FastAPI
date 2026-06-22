from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    a = 3 
    b = 4 
    c = a + b 
    return {"hello guy", c}

if __name__ == "__main__":
    uvicorn.run("three:app", reload=True)