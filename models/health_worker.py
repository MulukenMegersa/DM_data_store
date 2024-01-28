from pydantic import BaseModel
from typing import List

class IscrizioniItem(BaseModel):
    province: str
    year: str
    number: str


class LaureeItem(BaseModel):
    university_name: str
    name: str
    year: str


class AbilitazioniItem(BaseModel):
    university_name: str
    name: str
    year: str
    round: str

class HealthWorker(BaseModel):
    person_id:str
    prefix:str
    surname:str
    first_name:str
    full_name:str
    date_of_birth:str
    birth_place:str
    province:str
    iscrizioni: list[IscrizioniItem]
    lauree: list[LaureeItem]
    abilitazioni: list[AbilitazioniItem]
    last_update_date: str

