from fastapi import FastAPI, HTTPException
from pydantic import EmailStr, Field, ConfigDict, BaseModel
import uvicorn 

app = FastAPI()

Servers = []

@app.get("/Servers",
         tags=["Servers"],
         summary="There a way to get all servers")
def GetServers() -> dict:
    return {
        "Message": "There all your servers",
        "Servers": Servers
    }

@app.get("/Servers/{Server_Id}",
         tags=["Servers"],
         summary="There a way to get a specific server by Server ID")
def GetServerById(ServerById: int):
    for Server in Servers:
        if Server["SID"] == ServerById:
            return {
                "Message": "There ur server by ur specific request",
                "Server": Server
            }
    raise HTTPException(status_code=404, detail=f"this server under this {ServerById} Id has not found")

class ServerSchema(BaseModel):
    SID: int = Field(ge=0)
    Server_Name: str = Field(min_length=2, max_length=15)
    Server_Owner_email: EmailStr
    Server_Ping: int = Field(ge=0, le=5000)
    
    model_config = ConfigDict(extra="forbid")

@app.post("/Create",
          tags=["Servers"],
          summary="There the way to create a server")
def CreateServers(CreateServer:ServerSchema) -> dict:
    Servers.append({
        "SID": len(Servers) + 1,
        "Server_Name": CreateServer.Server_Name,
        "Server_Owner_email": CreateServer.Server_Owner_email,
        "Server_Ping": CreateServer.Server_Ping
    })
    return {
        "Message": "Your new server has been created check it below and continue",
        "Server Stats": CreateServer,
        "Done": True,
        "after word message": "If u need edit some parameters u can do it in another put endpoint"
    }
@app.put("/UpdateServer/{Server_Id}",
         tags=["Servers"],
         summary="There a way to edit ur server")
def UpdateServer(Server_Id: int, EditedServer: ServerSchema) -> dict:
    index = Server_Id - 1
    Server_dict = EditedServer.model_dump()
    Server_dict["Server_Id"] = Server_Id
    Servers[index] = Server_dict
    return {
        "Message": f"Your server with {Server_Id} SID has been edited",
        "Edited Server": Servers[index]
    }

@app.delete("/DeleteServer/{Server_Id}",
            tags=["Servers"],
            summary="There the way to delete ur own server")
def DeleteServer(Server_Id: int) -> dict:
    Deleted_Server = Servers.pop(Server_Id - 1)
    return { 
        "Message": f"Server with {Server_Id} SID has been deleted",
        "Deleted content": Deleted_Server
    }


if __name__ == "__main__":
    uvicorn.run("servers:app", reload=True)