from fastapi import FastAPI
import os

app = FastAPI()

from home import home_router
app.include_router(home_router)
# from x import y - fazer as rotas aqui 