from fastapi import FastAPI
from fastapi.responses import FileResponse
from public.users import users_router
from public.orders import orders_router
import uvicorn


app = FastAPI()

app.include_router(users_router)
app.include_router(orders_router)

@app.get('/')
async def main():
    return FileResponse("files/index.html")