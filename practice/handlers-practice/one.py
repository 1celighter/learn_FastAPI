from fastapi import FastAPI
import uvicorn

apc = FastAPI()

@apc.get("/")
def home_page():
    return f"Hello world!"

if __name__ == "__main__":
    uvicorn.run("one:apc", reload=True)
