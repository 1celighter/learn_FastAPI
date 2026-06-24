from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

servers = [
    {
        "Server-ID": 1,
        "Location": "Germany",
        "City": "Hesse",
        "Avg-Ping": 80
    },
    {
        "Server-ID": 2,
        "Location": "Netherlands",
        "City": "Amsterdam",
        "Avg-ping": 60
    }
]

@app.get("/VPN_Info",
         tags=["VPN"],
         summary="Check info about our vpn servers")
def get_VPN_info():
    return {
        "message": "There all info what we can recive to our users",
        "Servers": servers,
        "FAQ": "All your data has been secure we dont use them and we dont give this data to third people",
        "Rules": "Do not use our VPN to download torrents. Do not use our VPN to doing some wired things"
    }

@app.get("/VPN_Status",
         tags=["VPN"],
         summary="Check status all servers")
def get_servers():
    return {
        "message": "There all status on all servers",
        "Servers": servers
    }
@app.get("/server_status/{ConnectServer}",
         tags=["VPN"],
         summary="check one vpn server before connect")
def check_vpn_status(ConnectServer: int):
    for connect_id in servers:
        if connect_id["Server-ID"] == ConnectServer:
            return{
                "Message": "There are server u was choice",
                "Server to Connect": ConnectServer 
            }
    raise HTTPException(status_code=404, detail="We cant give you server under this ID")
        

class NewServer(BaseModel):
    ServerLocation: str
    ServerCity: str
    ServerAvgPing: int

@app.post("/New_Server")
def CreateNewServer(NServer:NewServer):
    servers.append({
        "Server-ID": len(servers) + 1,
        "Location": NServer.ServerLocation,
        "City": NServer.ServerCity,
        "Avg-ping": NServer.ServerAvgPing
    })
    return{
        "Message": "Your new Server has been created",
        "VPNServerSettings": NServer
    }



if __name__ == "__main__":
    uvicorn.run("server:app",reload=True)
