from fastapi import FastAPI
from routes.route import router

from pymongo.mongo_client import MongoClient

app = FastAPI(
    title="Italy Health Workers Data",
    summary="Summary Goes Heres"
)

app.include_router(router)
