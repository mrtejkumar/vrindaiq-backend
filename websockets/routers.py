from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio
import random  # Placeholder for real data

router = APIRouter()

@router.websocket("/live-prices")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Simulate fetching live price (replace with real API call)
            price = random.uniform(100, 200)
            await websocket.send_text(f"Stock price: {price}")
            await asyncio.sleep(5)  # Update every 5 seconds
    except WebSocketDisconnect:
        pass