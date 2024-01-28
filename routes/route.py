from fastapi import APIRouter
import ast

from models.sure_name import SureName
from models.health_worker import HealthWorker

from config.database import sure_name_collection,health_workers_collection

from schema.schemas import list_sure_name_serial,list_health_worker_serial

from bson import ObjectId
from bson.json_util import dumps
from typing import List

router = APIRouter()

@router.get("/api/surename")
async def get_sure_names():
    sure_names = list_sure_name_serial(sure_name_collection.find())
    return sure_names

@router.post("/api/surename")
async def post_sure_name(sure_name:SureName):
    sure_name_collection.insert_one(dict(sure_name))

@router.post("/api/surename/bulk")
async def post_bulk_sure_name(sure_names:List[SureName]):
    sure_name_collection.insert_many([{"name": sure_name.name} for sure_name in sure_names])

@router.put("/api/surename/{id}")
async def post_sure_name(id:str,sure_name:SureName):
    sure_name_collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(sure_name)})

@router.delete("/api/surename/{id}")
async def delete_sure_name(id:str):
    sure_name_collection.find_one_and_delete({"_id":ObjectId(id)})


@router.get("/api/health_worker")
async def get_health_workers():
    health_workers = list_health_worker_serial(health_workers_collection.find())
    return health_workers

@router.post("/api/health_worker")
async def post_sure_name(health_worker:HealthWorker):
    health_worker = dict(health_worker)
    health_worker['iscrizioni'] = [iscrizione.dict() for iscrizione in health_worker['iscrizioni']]
    health_worker['lauree'] = [laurea.dict() for laurea in health_worker['lauree']]
    health_worker['abilitazioni'] = [abilitazione.dict() for abilitazione in health_worker['abilitazioni']]
    health_workers_collection.insert_one(health_worker)

@router.post("/api/health_worker/bulk")
async def post_bulk_health_worker(health_workers:List[HealthWorker]):
    health_workers_collection.insert_many([health_worker.dict() for health_worker in health_workers])

@router.put("/api/health_worker/{id}")
async def post_health_work(id:str,health_worker:HealthWorker):
    health_worker = dict(health_worker)
    health_worker['iscrizioni'] = [iscrizione.dict() for iscrizione in health_worker['iscrizioni']]
    health_worker['lauree'] = [laurea.dict() for laurea in health_worker['lauree']]
    health_worker['abilitazioni'] = [abilitazione.dict() for abilitazione in health_worker['abilitazioni']]
    health_workers_collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(health_worker)})

@router.delete("/api/health_worker/{id}")
async def delete_health_worker(id:str):
    health_workers_collection.find_one_and_delete({"_id":ObjectId(id)})