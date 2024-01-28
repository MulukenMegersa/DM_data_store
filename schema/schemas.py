def sure_name_serial(sure_name) -> dict:
    return {
       "id":str(sure_name["_id"]),
       "name":sure_name["name"]
    }

def list_sure_name_serial(sure_names) -> list:
    return [sure_name_serial(sure_name) for sure_name in sure_names]

def health_worker_serial(health_worker) -> dict:
    return {
       "id":str(health_worker["_id"]),
       "person_id":health_worker["person_id"],
       "prefix":health_worker["prefix"],
       "surname":health_worker["surname"],
       "first_name":health_worker["first_name"],
       "full_name":health_worker["full_name"],
       "date_of_birth":health_worker["date_of_birth"],
       "birth_place":health_worker["birth_place"],
       "province":health_worker["province"],
       "iscrizioni":health_worker["iscrizioni"],
       "lauree":health_worker["lauree"],
       "abilitazioni":health_worker["abilitazioni"],
       "last_update_date":health_worker["last_update_date"]
    }


def list_health_worker_serial(health_workers) -> list:
    return [health_worker_serial(health_worker) for health_worker in health_workers]
