from fastapi import FastAPI

app = FastAPI()

from home import home_router
app.include_router(home_router)