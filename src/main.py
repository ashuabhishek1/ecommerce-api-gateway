from fastapi import FastAPI
import httpx

app = FastAPI()

# Service endpoints
SERVICE_URLS = {
    "user": "http://localhost:8002",
    "cart": "http://localhost:8003",
    "order": "http://localhost:8004",
    "payment": "http://localhost:8005"
}

# Proxy requests
@app.get("/customer")
async def get_customer(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{SERVICE_URLS['user']}/customer", params={"id": id})
        return response.json()

@app.post("/customer/address")
async def update_address(customer_id: str, new_address: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{SERVICE_URLS['user']}/customer/address", json={"customer_id": customer_id, "new_address": new_address})
        return response.json()

# WebSocket endpoint (placeholder)
@app.websocket("/ws")
async def websocket_endpoint(websocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Received: {data}")