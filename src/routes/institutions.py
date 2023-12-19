from fastapi import APIRouter
from config.db import db
from schemas.institutions import institutions_entity

institution = APIRouter()


@institution.get("/all", tags=["institutions"])
def all_institutions():
    institutes = db.institutions.find({})
    list_of_institutes = institutions_entity(institutes)

    if list_of_institutes is not None:
        return {
            "institutions": list_of_institutes
        }
    else:
        return {
            "institutions": {
                "id": "",
                "AddressUniqueNeeds": "",
                "BehaviourOfStaff": "",
                "CollegeName": "",
                "Opportunities": "",
                "StaffTraining": "",
                "SupportService": ""
            }
        }
